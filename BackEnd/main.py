from ultralytics import YOLO
import cv2
import numpy as np
import torch

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

        cv2.imwrite('segmented_frame.jpg', segmented_frame)
        cv2.imwrite('segmented_mask_frame.jpg', segmented_mask_frame)
        frame = cv2.resize(frame, (640, 480))
        cv2.imwrite('frame.jpg', frame)

        break
        
    cap.release()


read_video(video_path, model)