import cv2
from ultralytics import YOLO
import numpy as np
import torch

# Paths
model_path = 'BackEnd/model/best_segment.pt'
video_path = 'BackEnd/IMG_8443.MOV'
output_video_path = 'output_video_with_mask.mp4'

# Load YOLO model
model = YOLO(model_path)
print(model.model.task)

# Open video file
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)  # Obtém a taxa de quadros por segundo do vídeo
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Número total de frames no vídeo
duration_seconds = 15  # Duração do vídeo de saída em segundos
frames_to_capture = int(fps * duration_seconds)  # Número de frames que correspondem a 15 segundos

# Verifique se o vídeo é grande o suficiente para gerar 15 segundos de vídeo
if frame_count < frames_to_capture:
    print("O vídeo não tem frames suficientes para gerar 15 segundos de vídeo.")
    exit()

# Cria um vídeo de saída
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec de vídeo
out = cv2.VideoWriter(output_video_path, fourcc, fps, (640, 480))  # Define as configurações do vídeo de saída

count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Stop if no frames left

    print(f'Frame Shape: {frame.shape}')

    # Run segmentation
    results = model(frame)

    # Extract masks
    masks = results[0].masks.data  # Shape: (N, H, W)

    if masks.shape[0] > 0:  # Ensure at least one detection exists
        # Combinar todas as máscaras em uma única binária
        combined_mask = torch.any(masks, dim=0).int().cpu().numpy()  # Convert para NumPy
        print(f'Combined Mask Shape: {combined_mask.shape}')

        # Converter frame para GrayScale
        frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.resize(frame_gray,(640,384))
        print(f'Frame Gray Shape: {frame_gray.shape}')
        print(np.unique(combined_mask))
        combined_mask = combined_mask.astype(np.uint8)
        imageInMask = combined_mask * frame_gray
        cv2.imwrite(f'output_image_in_mask_{count}.png',imageInMask)
        # Adiciona o frame processado ao vídeo de saída
        #out.write(frame)

        #print(f'Processed Frame {count}')

        break  # Stop after capturing 15 seconds of frames

# Cleanup
cap.release()
out.release()
cv2.destroyAllWindows()
