import numpy as np
import time
import secrets
from typing import List
import random

def GetRandomList(size:int = 3) -> List:

    return np.random.default_rng(seed=secret.randbits(random.randint(1,666)+time.time())).random((size,)).tolist() 





