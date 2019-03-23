# coding: utf-8
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
digits = load_digits()
print(digits.target.shape)
plt.show(digits.images[0])
