from ultralytics import YOLO
import serial
import time
import winsound

# arduino = serial.Serial('COM7', 9600)

frequency = 500
duration = 1000

model = YOLO('best.pt')

# results = model.predict(source='test_video.mp4', stream=True, imgsz=512, show=True)
results = model.predict(source=0, stream=True, imgsz=512, show=True)
# results = model.predict(source='test.jpg', stream=True, imgsz=512, show=True, conf=0.4)

names = model.names
# print(names)
for r in results:
    for c in r.boxes.cls:
        # print(names[int(c)])
        if names[int(c)] == '0':
            print("Yes it is Monkey\n")
            winsound.Beep(frequency, duration)
            # arduino.write(b'Y')
        else:
            print("Human")
# arduino.close()





















#
# from ultralytics import YOLO
# import serial
# import time
# import winsound
# import threading
# import cv2
# def stream_video():
#     cap = cv2.VideoCapture('test_video.mp4')
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         cv2.imshow('Video Stream', frame)
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#
# def perform_object_detection():
#     model = YOLO('best.pt')
#     names = model.names
#
#     for r in model.predict(source='test_video.mp4', stream=True, imgsz=512, show=False):
#         for c in r.boxes.cls:
#             if names[int(c)] == '0':
#                 print("Yes it is Monkey\n")
#                 winsound.Beep(frequency, duration)
#                 arduino.write(b'Y')
#             else:
#                 print("Human")
#
# if __name__ == "__main__":
#     arduino = serial.Serial('COM7', 9600)
#     frequency = 500
#     duration = 1000
#
#     video_thread = threading.Thread(target=stream_video)
#     detection_thread = threading.Thread(target=perform_object_detection)
#
#     video_thread.start()
#     detection_thread.start()
#
#     video_thread.join()
#     detection_thread.join()
#
#     arduino.close()
