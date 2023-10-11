from collections import deque

class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        # Creating a queue ds of type (word, transitions to reach 'word').
        q = deque([(startWord, 1)])

        # BFS traversal with pushing values in queue
        # when after a transformation, a word is found in wordList.
        word_set = set(wordList)
        word_set.discard(startWord)
        while q:
            word, steps = q.popleft()

            # We return the steps as soon as
            # the first occurrence of targetWord is found.
            if word == targetWord:
                return steps

            for i in range(len(word)):
                # Now, replace each character of 'word' with char
                # from 'a' to 'z' then check if 'word' exists in wordList.
                original_char = word[i]
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + ch + word[i + 1:]
                    if new_word in word_set:
                        word_set.remove(new_word)
                        q.append((new_word, steps + 1))
                word = word[:i] + original_char + word[i + 1:]

        # If there is no transformation sequence possible
        return 0

if __name__ == "__main__":
    wordList = ["des", "der", "dfr", "dgt", "dfs"]
    startWord = "der"
    targetWord = "dfs"

    obj = Solution()

    ans = obj.wordLadderLength(startWord, targetWord, wordList)

    print(ans)
