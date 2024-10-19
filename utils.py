import numpy as np

def describe_np_array(arr : np.ndarray) -> None:
    print("-" * 20)
    print("arr type:",type(arr))
    print("No of dimensions:",arr.ndim)
    print("arr shape:", arr.shape)
    print("arr size:", arr.size)
    print("arr stores elements of type:", arr.dtype)

