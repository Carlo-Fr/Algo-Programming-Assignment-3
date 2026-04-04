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

def get_optimal_subsequence(dp, string_a, string_b):
    i = len(string_a)
    j = len(string_b)
    subsequence = []

    while i > 0 and j > 0:
        if string_a[i-1] == string_b[j-1]:
            # characters match, so part of the subsequence
            subsequence.append(string_a[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            # larger value came from i side
            i -= 1
        else:
            # larger value came j side
            j -= 1

    # need to reverse and join
    return "".join(reversed(subsequence))

def main():
    alphabet_values, string_a, string_b = read_input()
    
    if not alphabet_values:
        return

    #Building the table
    dp_table = build_dp_table(alphabet_values, string_a, string_b)
    #Get Max Value
    max_value = dp_table[-1][-1]

    # Get optimal string
    optimal_string = get_optimal_subsequence(dp_table, string_a, string_b)

    # print output (max value followed by optimal string)
    print(max_value)
    print(optimal_string)

if __name__ == "__main__":
    main()