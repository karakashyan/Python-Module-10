from collections.abc import Callable


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]
                   ) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:
    def casted(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return casted


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        return list(map(lambda x: x(target, power), spells))
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} for {power} turns"


def has_enough_power(target: str, power: int) -> bool:
    return power >= 20


if __name__ == "__main__":
    target = "Dragon"
    power = 10
    combined = spell_combiner(fireball, heal)
    result = combined(target, power)
    print()
    print("Testing spell combiner...")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    multiplier = 3
    power_amp = power_amplifier(fireball, multiplier)
    print()
    print("Testing power amplifier...")
    print(f"Original: {fireball(target, power)}")
    print(f"Amplified: {power_amp(target, power)}")

    cond_cast = conditional_caster(has_enough_power, fireball)
    print()
    print("Testing conditional caster...")
    print(cond_cast(target, 10))
    print(cond_cast(target, 50))

    seq = spell_sequence([fireball, heal, shield])
    print()
    print("Testing spell sequence...")
    print(seq(target, power))

    print()
    print("Testing callable()...")
    print(callable(fireball))
    print(callable(target))
