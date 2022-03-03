import pickle
from typing import Tuple

import numpy as np
from numpy import array


def most_similar(mat: array, idx: int, k: int) -> Tuple[array, array]:
    vec = mat[idx]
    dists = mat.dot(vec) / (np.linalg.norm(mat, axis=1) * np.linalg.norm(vec))
    top_idxs = np.argpartition(dists, k)[-k:]
    dist_sort_args = dists[top_idxs].argsort()[::-1]
    return top_idxs[dist_sort_args], dists[top_idxs][dist_sort_args]


if __name__ == '__main__':
    with open('data/valid_nearest.dat', 'rb') as f:
        words, mat = pickle.load(f)
    word = 'ewig'
    word_idx = words.index(word)
    sim_idxs, sim_dists = most_similar(mat, word_idx, 1001)