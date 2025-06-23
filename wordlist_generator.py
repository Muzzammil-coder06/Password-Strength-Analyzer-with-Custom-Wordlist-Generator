from itertools import product
from patterns import keyboard_walks, repeat_patterns

def leetspeak(word):
    subs = {'a': ['a', '@', '4'], 'e': ['e', '3'], 'i': ['i', '1', '!'], 'o': ['o', '0'], 's': ['s', '$', '5']}
    results = ['']
    for char in word.lower():
        new_results = []
        if char in subs:
            for prefix in results:
                for sub in subs[char]:
                    new_results.append(prefix + sub)
        else:
            for prefix in results:
                new_results.append(prefix + char)
        results = new_results
    return results

def generate_wordlist(base_words, years=[2023, 2024]):
    wordlist = set()
    for word in base_words:
        for variant in leetspeak(word):
            wordlist.add(variant)
            for year in years:
                wordlist.update([f"{variant}{year}", f"{year}{variant}"])
    wordlist.update(keyboard_walks(base_words))
    wordlist.update(repeat_patterns(base_words))
    return sorted(wordlist)

def export_wordlist(words, filename='wordlists/custom_wordlist.txt'):
    import os
    os.makedirs("wordlists", exist_ok=True)
    with open(filename, 'w') as f:
        for word in words:
            f.write(word + "\n")
    print(f"[+] Wordlist saved to {filename}")
