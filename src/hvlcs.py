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

def build_dp_table(alphabet_values, string_a, string_b):
    n = len(string_a)
    m = len(string_b)

    dp = [[0] * (m + 1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1, m+1):
            if string_a[i-1] == string_b[j-1]:
                #Characters Match
                char_val = alphabet_values[string_a[i - 1]]
                dp[i][j] = dp[i-1][j-1] + char_val
            else:
                #Mismatch
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp

def main():
    alphabet_values, string_a, string_b = read_input()
    
    if not alphabet_values:
        return

    


    # test statements to check parsing
    print(f"Alphabet Values: {alphabet_values}")
    print(f"String A: {string_a}")
    print(f"String B: {string_b}")

    # todo - implement DP table using variables

    #Building the table
    dp_table = build_dp_table(alphabet_values, string_a, string_b)
    #Get Max Value
    max_value = dp_table[-1][-1]
    print(f"Maximum Value: {max_value}")

if __name__ == "__main__":
    main()