import cv2
import numpy as np
import glob
from pathlib import Path

def hist_mean(image):
    img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    return img

def hist_mean2(image):
    img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    img = cv2.cvtColor(img_yuv, cv2.COLOR_HSV2BGR)
    return img

def sigmoid(a):
    return 1 / (1 + np.exp(-a))

def transrate(src,style):
    # 入力画像を読み込み
    img = cv2.imread(style)
    img = hist_mean(img)
    img2 = cv2.imread(src)

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 方法3
    gray_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    gray_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    edge = np.sqrt(gray_x ** 2 + gray_y ** 2) 
    # print(dst)
    # edge = edge / 255
    # dst = cv2.resize(img,tuple(img2.shape[:2][::-1]))
    dst = cv2.resize(edge,tuple(img2.shape[:2][::-1]))
    
    dst = (1 + dst / dst.max())
    # dst = sigmoid(dst)
    # dst = np.sqrt(dst) 
    # dst = dst / dst.var()
    dst = dst[:,:,None]

    # print(dst.max())
    # dst[dst > 0.01] += 1
    dst[dst <= dst.var()] = 1
    img_tmp = img2.astype(np.float64) * dst
    img_tmp = (img_tmp / img_tmp.max() * 255).astype(np.uint8)
    # img_tmp = hist_mean(img_tmp)
    return img_tmp


files = glob.glob("bg/*")
src = 'test.jpg'

for f in files:
    out = Path(f)
    out = Path('test') / (out.stem + '.jpg')
    styled_img = transrate(src,f)
    cv2.imwrite(str(out),styled_img)