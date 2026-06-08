import sys
import os

# Add home dir to path to find core.so
sys.path.append("/data/data/com.termux/files/home/")

import core

# Entry point
if __name__ == "__main__":
    core.run(sys.argv[1:])
