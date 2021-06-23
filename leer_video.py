import cv2

def run():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read() # si o si va el ret
        cv2.imshow('Video',frame)

        if cv2.waitKey(1) == ord('x'):
            break
    cap.release()
    cv2.destroyAllWindows

if __name__ == '__main__':
    run()