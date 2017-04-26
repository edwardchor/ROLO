import os,cv2
import numpy as np


class PreProcessor:
    def __init__(self):
        pass

    def readVideo(self,fileName):
        # vfile=open(fileName,'r')
        cap = cv2.VideoCapture(fileName)

        while (cap.isOpened()):
            ret, frame = cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            cv2.imshow('frame',gray)
            cv2.imwrite()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


    def video_to_img(self,fileName,code):
        vidcap=cv2.VideoCapture(fileName)
        count=0
        while vidcap.isOpened():
            success, image = vidcap.read()
            if success:
                # cv2.imshow(image)
                print('!')
                cv2.imwrite('../benchmark/DATA/{}/{}.jpg'.format(code,count), image)
                count += 1
            else:
                break
        cv2.destroyAllWindows()
        vidcap.release()


if __name__ == '__main__':
    p=PreProcessor()
    p.video_to_img("../benchmark/DATA/tmp/car1.mov",'car1')