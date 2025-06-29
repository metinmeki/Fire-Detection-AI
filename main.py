import cv2
from ultralytics import YOLO

model = YOLO('model/yolov8n.pt')  # Your custom fire detection model

class_names = ["Fire"]  # Update according to your model

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR (OpenCV) to RGB (Ultralytics expects RGB)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Run inference (pass list of images or numpy arrays)
    results = model.predict(source=[img_rgb], verbose=False)

    # 'results' is a list with one Result object for each image
    result = results[0]

    for box in result.boxes:
        cls = int(box.cls[0])
        conf = box.conf[0]
        if conf < 0.3:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        label = f"{class_names[cls]} {conf:.2f}"
        color = (0, 0, 255)

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Fire Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
