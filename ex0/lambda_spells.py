from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    powers = list(map(lambda x: x['power'], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
    ]

    sorted_artifacts = artifact_sorter(artifacts)
    first = sorted_artifacts[0]
    second = sorted_artifacts[1]

    print()
    print("Testing artifact sorter...")
    print(f"{first['name']} ({first['power']} power) comes before "
          f"{second['name']} ({second['power']} power)")

    spells = ['fireball', 'heal', 'shield']
    print()
    print("Testing spell transformer...")
    print(' '.join(spell_transformer(spells)))

    mages = [
        {'name': 'Alex', 'power': 92, 'element': 'fire'},
        {'name': 'Jordan', 'power': 45, 'element': 'water'},
        {'name': 'Riley', 'power': 78, 'element': 'earth'},
    ]
    min_power = 70
    filtered = power_filter(mages, min_power)
    names = ', '.join(map(lambda x: x['name'], filtered))
    print()
    print("Testing power filter...")
    print(f"Mages with power >= {min_power}: {names}")

    result = mage_stats(mages)

    print()
    print("Testing mage stats...")
    print(f"Max: {result['max_power']}, Min: {result['min_power']}, "
          f"Avg: {result['avg_power']}")
