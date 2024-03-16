from ultralytics import YOLO
import serial
import time
import winsound
import cv2

# arduino = serial.Serial('COM7', 9600)

frequency = 500
duration = 1000

model = YOLO('best.pt')

# results = model.predict(source='test_video.mp4', imgsz=512, stream=True, show=True, stream_buffer=False, conf=0.6,
#                         vid_stride=5, show_labels=True, show_conf=False)
# results = model.predict(source=0, stream=True, imgsz=512, show=True)
# results = model.predict(source='test.jpg', stream=True, imgsz=512, show=True, conf=0.6)
# names = model.names
# for r in results:
#     for c in r.boxes.cls:
#         # print(names[int(c)])
#         if names[int(c)] == '0':
#             print("Yes it is Monkey\n")
#             winsound.Beep(frequency, duration)
#             # arduino.write(b'Y')
#         else:
#             print("Human")
# arduino.close()

video_path = "test_video_2.mp4"
# video_path = 0
cap = cv2.VideoCapture(video_path)
# arduino = serial.Serial('COM7', 9600)
while cap.isOpened():
    success, frame = cap.read()

    if success:
        results = model.predict(frame)
        names = model.names

        for c in results[0].boxes.cls:
            if names[int(c)] == '0':
                print("Yes, it is a Monkey\n")
                # winsound.Beep(frequency, duration)
                # arduino.write(b'Y')
                break
            else:
                print("No Monkey detected\n")
        annotated_frame = results[0].plot()
        annotated_frame = cv2.resize(annotated_frame, (640, 640))
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
# arduino.close()