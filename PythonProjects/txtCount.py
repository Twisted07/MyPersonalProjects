
counts = dict()
with open("sample3.txt", encoding="utf-8") as newFile:
    txt = newFile.read()
    word = txt.split()
    #print("Words: ", word)

    print("Now counting...")
    for words in word:
        counts[words] = counts.get(words, 0) + 1
    maxiV = max(counts.values())
    for a,b in counts.items():
        if b == maxiV:
            c = (a,b)
        else:
            continue
    print(f"Here's the word statistics: {counts}\n\nMost repeated word is: {c}")