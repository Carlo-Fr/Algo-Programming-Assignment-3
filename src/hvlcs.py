import sys

def read_input():
    # Read values/strings from input
    lines = sys.stdin.read().splitlines()
    if not lines:
        return None, None, None

    # read number of characters in the alphabet
    k = int(lines[0].strip())

    # map each character to its value
    alphabet_values = {}
    for i in range(1, k + 1):
        char, val = lines[i].split()
        alphabet_values[char] = int(val)

    # read the two input strings
    string_a = lines[k + 1].strip()
    string_b = lines[k + 2].strip()

    return alphabet_values, string_a, string_b

def main():
    alphabet_values, string_a, string_b = read_input()
    
    if not alphabet_values:
        return

    # test statements to check parsing
    print(f"Alphabet Values: {alphabet_values}")
    print(f"String A: {string_a}")
    print(f"String B: {string_b}")

    # todo - implement DP table using variables

if __name__ == "__main__":
    main()