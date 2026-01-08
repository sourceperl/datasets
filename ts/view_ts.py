#!/usr/bin/env python3

import argparse
import lzma
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# configuration du parser
parser = argparse.ArgumentParser(description='load time series data')
parser.add_argument('path', type=str, help='path to the .txt or .xz file')
args = parser.parse_args()

# load and process data with type auto-detection
file_path = Path(args.path)

if file_path.suffix == '.xz':
    with lzma.open(file_path, 'rt') as f:
        data = np.genfromtxt(f, dtype=float)
else:
    data = np.genfromtxt(file_path, dtype=float)

plt.plot(data)
plt.grid()
plt.show()
