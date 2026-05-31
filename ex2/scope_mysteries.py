from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(power: int) -> Callable[[int], int]:

    def accumulate(amount: int) -> int:
        nonlocal power
        power += amount
        return power
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    storage = {}

    def store(key: str, value: int) -> None:
        storage[key] = value

    def recall(key: str) -> Any:
        if key in storage:
            return storage[key]
        else:
            return "Memory not found"

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("Testing mage counter...")
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    base = 100
    result = spell_accumulator(base)
    print()
    print("Testing spell accumulator...")
    print(f"Base {base}, add 20: {result(20)}")
    print(f"Base {base}, add 30: {result(30)}")

    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print()
    print("Testing enchantment factory...")
    print(flaming("Sword"))
    print(frozen("Shield"))

    vault = memory_vault()
    vault['store']('secret', 42)
    print()
    print("Testing memory vault...")
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
