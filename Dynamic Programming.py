# Dynamic programming is the division of a large task into small subtasks.
# elements must be independent of each other
elements = {}
elements["water"] = (10, 3)
elements["book"] = (3, 1)
elements["food"] = (9, 2)
elements["jacket"] = (5, 2)
elements["camera"] = (6, 1)

l = ["water", "book", "food", "jacket", "camera"]

max_weight = 6
table = [[0] * (max_weight + 1) for _ in range(len(elements.keys()) + 1)]
for i in range(1, len(elements.keys()) + 1):
    for j in range(1, max_weight + 1):
        if j >= elements[l[i - 1]][1]:
            table[i][j] = max(table[i - 1][j], elements[l[i - 1]][0] + table[i - 1][j - elements[l[i - 1]][1]])
        else:
            table[i][j] = table[i - 1][j]
# for i in table:
#   print(*i)

# The longest common substring.
current_word = "fosh"
words = ["fish", "fort"]
results = []
for word in words:
    table = [[0] * (len(current_word) + 1) for _ in range(len(word) + 1)]
    for i in range(1, len(word) + 1):
        for j in range(1, len(current_word) + 1):
            if current_word[j - 1] == word[i - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
    tempmax = 0
    for i in table:
        if max(i) > tempmax:
            tempmax = max(i)
    results.append(tempmax)
print(results, words[results.index(max(results))])

# The longest common subsequence.
current_word = "fosh"
words = ["fish", "fort"]
results = []
for word in words:
    table = [[0] * (len(current_word) + 1) for _ in range(len(word) + 1)]
    for i in range(1, len(word) + 1):
        for j in range(1, len(current_word) + 1):
            if current_word[j - 1] == word[i - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    tempmax = 0
    for i in table:
        if max(i) > tempmax:
            tempmax = max(i)
    results.append(tempmax)
print(results, words[results.index(max(results))])

# 9.3
word1 = "blue"
word2 = "clues"
table = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
for i in range(1, len(word2) + 1):
    for j in range(1, len(word1) + 1):
        if word2[i - 1] == word1[j - 1]:
            table[i][j] = table[i - 1][j - 1] + 1
for w in table:
    print(*w)
