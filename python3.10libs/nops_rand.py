import numpy as np
import time
import secrets
from typing import List
import random
import hou

#utility functions to generate random numbers

def GetRandomSeed(seed:int = 9, slow:int = 10) -> int:

    # increasing slow means slower change in seed value
    
    nanoseconds: int = time.monotonic_ns()
    
    now:int = nanoseconds % slow

    return secrets.randbits(now + random.randint(1,6) + seed)


def GetRandomList(size:int = 3) -> List:

    return np.random.default_rng(seed=GetRandomSeed()).random((size,)).tolist() 


def RandomTrigger(probability:float = 0.1,seed:int = 6) -> bool:

    seed: int = GetRandomSeed(seed)
    
    value: float = np.random.default_rng(seed=seed).random()

    return  value <  probability
            

def GetRandomPosition(seed: int = 6, scale: float = 25.0) -> hou.Vector2:

    seed: int = GetRandomSeed(seed)
    return hou.Vector2([(elem-.5) * scale for elem in GetRandomList(2)]) 


def ChooseFromStringArray(array: tuple, slow:int = 10) -> str:

    array_length: int = len(array)
    random.seed(GetRandomSeed(slow=slow))
    return random.randint(0,array_length-1)
