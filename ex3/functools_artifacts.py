from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return reduce(add, spells)
    if operation == "multiply":
        return reduce(mul, spells)
    if operation == "max":
        return reduce(lambda x, y: x if x > y else y, spells)
    if operation == "min":
        return reduce(lambda x, y: x if x < y else y, spells)

    raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]
                      ) -> dict[str, Callable[[str], str]]:
    fire = partial(base_enchantment, 50, "fire")
    water = partial(base_enchantment, 50, "water")
    earth = partial(base_enchantment, 50, "earth")
    return {'fire': fire, 'water': water, 'earth': earth}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(arg: Any) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @spell.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @spell.register(list)
    def _(arg: list[Any]) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return spell


