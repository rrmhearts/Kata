
from collections import defaultdict

def boyer_moore_search(text, pattern):
    """
    Boyer-Moore string search algorithm implementation.
    
    Args:
        text (str): The text to search within.
        pattern (str): The pattern to search for.
        
    Returns:
        int: The starting index of the first occurrence of the pattern in the text, or -1 if not found.
    """
    m = len(pattern)
    n = len(text)

    if m == 0 or n == 0 or m > n:
        return -1

    # Preprocess the pattern to create the bad character table
    last = defaultdict(lambda: -1)
    for c in pattern:
        last[c] = pattern.rfind(c)

    i, j = m - 1, m - 1
    while i <= n - 1:
        if pattern[j] == text[i]:
            if j == 0:
                return i # Pattern found at index i
            i, j = i - 1, j - 1
        else:
            i = i + m - min(j, 1 + last[text[i]]) #.get(text[i], -1))
            j = m - 1

    return -1  # Pattern not found

if __name__ == "__main__":
    text = "ababcababcabc"
    pattern = "abc"
    result = boyer_moore_search(text, pattern)
    if result != -1:
        print(f"Pattern found at index {result}")
    else:
        print("Pattern not found")