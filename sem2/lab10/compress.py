import numpy as np
from sklearn.cluster import KMeans
import cv2
import imutils
import time

for n_clusters in [2, 3, 4, 8, 16, 32, 64, 128, 256]:
    start_time = time.time()
    img = cv2.imread('./spartak.jpg')
    img_r = (img / 255.0).reshape(-1, 3)
    print(img)
    print("New shape (img_r): ", img_r.shape)
    k_colors = KMeans(n_clusters=n_clusters).fit(img_r)
    imgC = k_colors.cluster_centers_[k_colors.labels_]

    imgC = (np.reshape(imgC, (img.shape))*255).astype(np.uint8)
    print("Compressed image's shape: ", imgC.shape)

    elapsed_time = time.time() - start_time
    print(f'elapsed_time: {elapsed_time}')

    cv2.imwrite(f'spartak_{n_clusters}_{elapsed_time}.jpg', imgC)

    # cv2.imshow("Original image", imutils.resize(img, width=800))
    # cv2.imshow("Compressed image", imutils.resize(imgC, width=800))
    # cv2.waitKey(0)
