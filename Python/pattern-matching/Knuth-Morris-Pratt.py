
def LPS_table(pattern):
    plen = len(pattern)
    # for each index i in the pattern, the length
    # of the longest proper prefix of pattern[0...i] 
    # that is also a suffix of pattern[0...i].
    table = [0]* plen

    # length of previous longest prefix suffix
    length = 0
    # Compare the next value at start
    j = 1

    while j < plen:
        if pattern[j] == pattern[length]:
            length += 1
            table[j] = length
            j += 1
        else: # if there is a mismatch
            if length != 0:
                length = table[length - 1]
                # don't update j
            else:
                table[j] = 0
                j += 1
    return tuple(table)

def KMP(text, pattern):
    n, m = len(text), len(pattern)
    lps, result = LPS_table(pattern), []
    # traversing text and pattern
    i, j = 0, 0

    while i < n: # iterate over text
        if text[i] == pattern[j]:
            i += 1
            j += 1

            # if entire pattern is matched,
            # store the start index in result
            if j == m:
                result.append(i-m) # beginning index

                # use LPS of previous index to skip
                # unnecessary comparisons
                j = lps[j-1]
        else: # if mismatch
            # use LPS of previous index to skip
            # unnecessary comparisons
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return result

if __name__ == "__main__":
    test_pattern = "testingthiste"
    print(test_pattern)
    print(LPS_table(test_pattern))

    test_pattern = "test"
    test_string = "testingthistest case for me"

    print(KMP(test_string, test_pattern))