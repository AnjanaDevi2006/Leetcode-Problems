from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

        queue = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        wordList = set(wordList)
        words=1

        while queue:

            length = len(queue)

            for i in range(length):

                curr_word = queue.popleft()

                if curr_word==endWord:

                    return words

                for j in range(len(beginWord)):

                    for char in alpha:

                        if curr_word[j]==char:
                            continue

                        next_word = list(curr_word)
                        next_word[j]=char
                        next_word = "".join(next_word)

                        if next_word in wordList and next_word not in visited:

                            visited.add(next_word)
                            queue.append(next_word)

            words+=1
        return 0