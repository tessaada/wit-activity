with open("./challenges/words.txt") as f:
    lines = f.read().splitlines()
    print(lines)

with open("./challenges/wordlist.txt", "a") as f:
    f.write(str(lines))