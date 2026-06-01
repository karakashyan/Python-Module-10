from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable[..., object]) -> Callable[..., object]:
    @wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper
