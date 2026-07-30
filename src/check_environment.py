import sys

import matplotlib
import numpy as np
import pandas as pd
import sklearn


def main() -> None:
    print("Python executable:", sys.executable)
    print("Python version:", sys.version)
    print("NumPy:", np.__version__)
    print("pandas:", pd.__version__)
    print("matplotlib:", matplotlib.__version__)
    print("scikit-learn:", sklearn.__version__)


if __name__ == "__main__":
    main()