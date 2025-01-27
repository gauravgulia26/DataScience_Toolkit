import numpy as np
cimport numpy as cnp
from cython.parallel import prange

# Function to calculate bins in parallel
def calculate_bins(cnp.ndarray[double, ndim=1] data, cnp.ndarray[double, ndim=1] bins):
    """
    Calculate histogram bins for a dataset using bin edges.
    Parameters:
        data: 1D NumPy array of data points
        bins: 1D NumPy array of bin edges
    Returns:
        1D NumPy array with the index of the bin each data point belongs to
    """
    cdef:
        Py_ssize_t n = data.shape[0]
        Py_ssize_t m = bins.shape[0]
        cnp.ndarray[int, ndim=1] histogram = np.zeros(n, dtype=np.int32)
        Py_ssize_t i, j

    # Iterate over the dataset in parallel
    for i in prange(n, nogil=True):
        for j in range(m):
            if data[i] <= bins[j]:
                histogram[i] = j
                break

    return histogram
