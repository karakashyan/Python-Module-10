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


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} spell hits {target} for {power} damage"


if __name__ == "__main__":
    nums = [10, 20, 30, 40]
    print()
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(nums, 'add')}")
    print(f"Product: {spell_reducer(nums, 'multiply')}")
    print(f"Max: {spell_reducer(nums, 'max')}")
    print(f"Min: {spell_reducer(nums, 'min')}")
    try:
        spell_reducer(nums, "unknown")
    except ValueError as e:
        print(f"Error: {e}")

    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(memoized_fibonacci.cache_info())

    test_spell = spell_dispatcher()
    print()
    print("Testing spell dispatcher...")
    print(test_spell(42))
    print(test_spell("fireball"))
    print(test_spell([1, 2, 3]))
    print(test_spell(3.14))

    enchanters = partial_enchanter(base_enchantment)
    print()
    print("Testing partial enchanter...")
    print(enchanters['fire']('Dragon'))
    print(enchanters['water']('Golem'))
    print(enchanters['earth']('Troll'))
