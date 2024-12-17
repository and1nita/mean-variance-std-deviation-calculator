import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    conv_arr = np.array(list)
    conv_arr = conv_arr.reshape((3,3))

    calculations = {
        'mean' : [conv_arr.mean(axis=0).tolist(), conv_arr.mean(axis=1).tolist(), conv_arr.mean()],
        'variance' : [conv_arr.var(axis=0).tolist(), conv_arr.var(axis=1).tolist(), conv_arr.var()],
        'standard deviation' : [conv_arr.std(axis=0).tolist(), conv_arr.std(axis=1).tolist(), conv_arr.std()],
        'max' : [conv_arr.max(axis=0).tolist(), conv_arr.max(axis=1).tolist(), conv_arr.max()],
        'min' : [conv_arr.min(axis=0).tolist(), conv_arr.min(axis=1).tolist(), conv_arr.min()],
        'sum' : [conv_arr.sum(axis=0).tolist(), conv_arr.sum(axis=1).tolist(), conv_arr.sum()]
    }

    return calculations