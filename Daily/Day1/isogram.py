def isogram(word):
    return len(list(word)) == len(set(word))

if __name__ == '__main__':
    print(isogram("Bhanu"))