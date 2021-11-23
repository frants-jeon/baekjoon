import sys

N = int(sys.stdin.readline())
words = set()
for _ in range(N):
    words.add(sys.stdin.readline().strip())
words = sorted(list(words),key= lambda x: (len(x), x))

for word in words:
    print(word)