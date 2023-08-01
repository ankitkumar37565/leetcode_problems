# 127. Word Ladder
from collections import deque
class Solution(object):
    def ladderLength(self, startWord, targetWord, wordList):
        # Creating a queue ds of type {word, transitions to reach ‘word’}.
        q = deque([(startWord, 1)])

        # Push all values of wordList into a set
        # to make deletion from it easier and in less time complexity.
        wordSet = set(wordList)
        if startWord in wordSet:
            wordSet.remove(startWord)

        while q:
            word, steps = q.popleft()

            # We return the steps as soon as the first occurrence of targetWord is found.
            if word == targetWord:
                return steps

            for i in range(len(word)):
                # Now, replace each character of ‘word’ with a character from a-z
                # then check if ‘word’ exists in the set and push it into the queue.
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + ch + word[i + 1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        q.append((newWord, steps + 1))

        # If there is no transformation sequence possible
        return 0