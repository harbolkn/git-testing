from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 1, 0])


model = LogisticRegression()
model.fit(X, y)
