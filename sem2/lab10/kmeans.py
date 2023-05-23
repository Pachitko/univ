import numpy as np
import matplotlib
from PIL import Image
import time


def kmeans(Input, K, Max_iters):
    N, D = np.shape(Input)
    R = np.random.permutation(N)
    Kvec = Input[R[0:K], :]
    Distance = np.zeros((N, K))

    for nn in range(0, Max_iters):
        F = np.zeros((N, K))
        for kk in range(0, K):
            Distance[:, kk] = np.sum(
                np.square(Input - np.tile(Kvec[kk, :], (N, 1)), dtype=np.float64), axis=1)
            Dmin = Distance.argmin(axis=1) % Distance.shape[1]
            for mm in range(0, K):
                if np.size(Dmin[mm == Dmin]) > 0:
                    Kvec[mm, :] = np.mean(Input[mm == Dmin], axis=0)
            for ii in range(0, N):
                F[ii, Dmin[ii]] = 1
            error = sum(sum((F * Distance) / N))
            print('Error = ' + str(error))
        return Kvec, Dmin


Datain = np.asarray(Image.open('./spartak.jpg'), dtype=np.float64)
ReshapedData = np.reshape(
    Datain, (np.size(Datain, 0) * np.size(Datain, 1), np.size(Datain, 2)))

Max_iters = 10
for K in [64, 128, 256]:
    start_time = time.time()
    Kvec, Dmin = kmeans(ReshapedData, K, Max_iters)
    Dvec = np.zeros((len(Dmin), len(Kvec[0, :])))
    for jj in range(0, K):
        Dvec[jj == Dmin, :] = Kvec[jj, :]

    imout = np.reshape(np.uint8(Dvec), (np.size(Datain, 0),
                       np.size(Datain, 1), len(Kvec[0, :])))
    im = Image.fromarray(imout, 'RGB')

    im.show()
    im.save(f'spartak_{K}_{Max_iters}_{elapsed_time}.jpeg',
            "JPEG", optimize=True)

    elapsed_time = time.time() - start_time
    print(f'elapsed_time: {elapsed_time}')
