# OpenCV
import cv2 as cv
# Numpy
import numpy as np

# 画像のパス
img_path = "line.jpg"
# BGR画像読み込み
img = cv.imread(img_path)

# imgと同じサイズのノイズ生成
# img.shape -> (y, x, channel_num)
noise = np.random.normal(0, 3, img.shape)

# ノイズを付与して型をunsigned intに変換
#img += noise.astype(np.uint8)
#cv.imwrite("noise.jpg", img)

# バイラテラルフィルタ処理(カーネルサイズ，畳み込みフィルタサイズ，画素分散，座標分散)
dst_5 = cv.bilateralFilter(img, 5, 75, 75)
dst_25= cv.bilateralFilter(img, 25, 75, 75)
dst_125= cv.bilateralFilter(img, 125, 75, 75)

# 保存
cv.imwrite("bilateral_5.jpg", dst_5)
cv.imwrite("bilateral_25.jpg", dst_25)
cv.imwrite("bilateral_125.jpg", dst_125)

# 比較用ガウシアンフィルタ結果
dst_5 = cv.GaussianBlur(img, (5, 5), 0)
dst_15 = cv.GaussianBlur(img,(15,15),0)
cv.imwrite("gaussian_5.jpg", dst_5)
cv.imwrite("gaussian_15.jpg",dst_15)

