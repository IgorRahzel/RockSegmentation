from flask import Flask, Response
from ultralytics import YOLO
import numpy as np
import cv2
import torch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Paths
model_path = 'BackEnd/model/best_segment.pt'
video_path = 'BackEnd/IMG_8443.MOV'

# Initialize YOLO model
model = YOLO(model_path,task='segment')
print(model.model.task)

def get_mask(frame,model):
    #frame = cv2.resize(frame,(640,480))
    results = model(frame)  # No resizing

    if results[0].masks is None:
        print("No masks detected (results[0].masks is None)")
        return np.zeros((frame.shape[0], frame.shape[1]), dtype=np.uint8)

    masks = results[0].masks.data if results[0].masks is not None else None

    if masks is None or masks.shape[0] == 0:
        print("No masks found in results (masks.shape[0] == 0)")
        return np.zeros((frame.shape[0], frame.shape[1]), dtype=np.uint8)

    print(f"Detected {masks.shape[0]} masks with shape {masks.shape}")

    # Combine masks into a single binary image
    combined_mask = torch.any(masks, dim=0).int().cpu().numpy()
    
    return combined_mask.astype(np.uint8)


def segmented_frames(frame, model):
    
    bin_mask = get_mask(frame,model)
    print(f'bin_mask.shape: {bin_mask.shape}')
    bin_mask = cv2.resize(bin_mask,(640,480))
    frame = cv2.resize(frame, (640, 480))
    
    #colored frame
    colored_frame = np.zeros_like(frame)
    colored_frame[:,:] = (255,0,255)
    alpha = 0.5
    bin_mask = bin_mask.astype(bool)
    frame[bin_mask] = cv2.addWeighted(frame,alpha,colored_frame,1-alpha,0.0)[bin_mask]

    return frame

def segmented_mask(frame, model):
    
    combined_mask = get_mask(frame,model)
    combined_mask *= 255
    combined_mask = cv2.resize(combined_mask,(480,320))
    #Area
    area = np.sum(combined_mask > 0)


    return combined_mask.astype(np.uint8),area  # Ensure uint8 format

def read_video(video_path, model):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        segmented_frame = segmented_frames(frame, model)
        segmented_mask_frame,area = segmented_mask(frame, model)

        # Encode frames to JPEG
        _, segmented_frame_jpg = cv2.imencode('.jpg', segmented_frame)
        _, segmented_mask_jpg = cv2.imencode('.jpg', segmented_mask_frame)

        yield segmented_frame_jpg.tobytes(), segmented_mask_jpg.tobytes(),area

    cap.release()

# Streaming segmented frames
def generate_segmented_frames():
    for segmented_frame, _, _ in read_video(video_path, model):
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + segmented_frame + b'\r\n')

# Streaming segmentation masks
def generate_segmented_masks():
    for _, segmented_mask,_ in read_video(video_path, model):
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + segmented_mask + b'\r\n')

def generate_area():
    for _,_,area in read_video(video_path,model):
      yield f"data: {area}\n\n"


# Flask Routes
@app.route('/video/segmented')
def video_segmented():
    return Response(generate_segmented_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video/mask')
def video_mask():
    return Response(generate_segmented_masks(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video/area')
def video_area():
    return Response(generate_area(), mimetype='text/event-stream')


if __name__ == "__main__":
    app.run(debug=True)
