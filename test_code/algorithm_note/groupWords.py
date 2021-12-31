from collections import defaultdict

def groupWords(words):
    grouper = defaultdict(list)
    for word in words:
        length = len(word)
        grouper[length].append(word)
    return grouper


if __name__ == "__main__":
    words = ["classic", "pop", "classic", "classic", "pop"]
    print(groupWords(words))