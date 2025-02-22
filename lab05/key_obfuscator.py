import random

key = "010A56FBD319D727"

bits_missing_list: list[int] = [4, 8, 12, 16, 20, 24, 32, 48]


def obfuscate_key(key: str, bits_missing: int) -> list[str]:
    hex_chars_missing: int = bits_missing // 4
    key_length: int = len(key)

    # beginning
    key_beginning: str = '*' * hex_chars_missing + key[hex_chars_missing:]

    # middle
    middle_start: int = (key_length - hex_chars_missing) // 2
    key_middle: str = key[:middle_start] + '*' * \
        hex_chars_missing + key[middle_start + hex_chars_missing:]

    # end
    key_end: str = key[:-hex_chars_missing] + '*' * hex_chars_missing

    # random
    key_random: str = key
    changes_left: int = hex_chars_missing
    while changes_left > 0:
        random_index: int = random.randint(0, key_length - 1)
        if key_random[random_index] != '*':
            changes_left -= 1
        else:
            continue
        key_random = key_random[:random_index] + \
            '*' + key_random[random_index + 1:]

    return [key_beginning, key_middle, key_end, key_random]


for bits_missing in bits_missing_list:
    obfuscated_keys: list[str] = obfuscate_key(key, bits_missing)
    print(f"Bits missing: {bits_missing}")
    for obfuscated_key in obfuscated_keys:
        print(obfuscated_key)
    print()
