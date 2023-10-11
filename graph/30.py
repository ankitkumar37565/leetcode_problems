from collections import deque

class Solution:
    def findSequences(self, beginWord, endWord, wordList):
        # Push all values of wordList into a set
        # to make deletion from it easier and in less time complexity.
        word_set = set(wordList)
        
        # Creating a queue ds which stores the words in a sequence which is
        # required to reach the targetWord after successive transformations.
        q = deque([[beginWord]])

        # A vector defined to store the words being currently used
        # on a level during BFS.
        used_on_level = [beginWord]
        level = 0

        # A vector to store the resultant transformation sequence.
        ans = []

        while q:
            vec = q.popleft()

            # Now, erase all words that have been
            # used in the previous levels to transform
            if len(vec) > level:
                level += 1
                for word in used_on_level:
                    word_set.discard(word)

            word = vec[-1]

            # Store the answers if the end word matches with targetWord.
            if word == endWord:
                # The first sequence where we reached the end
                if not ans or len(ans[0]) == len(vec):
                    ans.append(vec)
                continue

            for i in range(len(word)):
                # Now, replace each character of 'word' with char
                # from 'a' to 'z' then check if 'word' exi
                for c in 'absts in wordList.
                original = word[i]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    word = word[:i] + c + word[i + 1:]
                    if word in word_set:
                        # Check if the word is present in the wordList and
                        # push the word along with the new sequence in the queue.
                        new_vec = vec.copy()
                        new_vec.append(word)
                        q.append(new_vec)
                        # Mark as visited on the level
                        used_on_level.append(word)
                    word = word[:i] + original + word[i + 1:]

        return ans

# A comparator function to sort the answer.
def comp(a, b):
    x = ''.join(a)
    y = ''.join(b)
    return x < y

if __name__ == "__main__":
    wordList = ["des", "der", "dfr", "dgt", "dfs"]
    startWord = "der"
    targetWord = "dfs"

    obj = Solution()
    ans = obj.findSequences(startWord, targetWord, wordList)

    # If no transformation sequence is possible.
    if not ans:
        print(-1)
    else:
        ans.sort(key=lambda x: ''.join(x))
        for seq in ans:
            print(' '.join(seq))
