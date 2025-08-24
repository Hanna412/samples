import numpy as np

def smape(y_true: np.array, y_pred: np.array) -> float: # type: ignore
    num = np.abs(y_true - y_pred)
    den = (np.abs(y_true) + np.abs(y_pred)) / 2
    ratio = num / np.where(den == 0, 1, den)
    return np.mean(ratio) 

