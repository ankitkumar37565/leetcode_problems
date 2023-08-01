# 126. Word Ladder II
from collections import deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        # Push all values of wordList into a set
        # to make deletion from it easier and in less time complexity.
        wordSet = set(wordList)

        # Creating a queue ds which stores the words in a sequence
        # that is required to reach the targetWord after successive transformations.
        q = deque([[beginWord]])

        # A vector defined to store the words being currently used
        # on a level during BFS.
        usedOnLevel = [beginWord]
        level = 0

        # A vector to store the resultant transformation sequences.
        ans = []
        while q:
            vec = q.popleft()

            # Now, erase all words that have been
            # used in the previous levels to transform
            if len(vec) > level:
                level += 1
                for it in usedOnLevel:
                    wordSet.discard(it)

            word = vec[-1]

            # Store the answers if the end word matches with targetWord.
            if word == endWord:
                # The first sequence where we reached the end
                if not ans:
                    ans.append(vec)
                elif len(ans[0]) == len(vec):
                    ans.append(vec)

            for i in range(len(word)):
                # Now, replace each character of ‘word’ with char
                # from a-z then check if ‘word’ exists in wordSet.
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordSet:
                        # Check if the word is present in the wordSet
                        # and push the word along with the new sequence in the queue.
                        q.append(vec + [newWord])
                        # Mark as visited on the level
                        usedOnLevel.append(newWord)

        return ans
