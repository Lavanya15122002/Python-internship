from collections import defaultdict
try:
    with open("D:\ct\Level2\Text.txt") as file:
        word_counts = defaultdict(int)
        for i in file:
            words = i.split()
        for i in words:
            word_counts[i] += 1
        sorted_words = sorted(word_counts.items())
        for i, c in sorted_words:
            print(f"{i}: {c}")
except FileNotFoundError:
    print("That file was not found!")