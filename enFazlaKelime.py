"""
30.12.2021

Tek bir cümlede görünen en fazla sözcük sayısını döndürün.

Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation:
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
"""
class Solution:
    def mostWordsFound(self, sentences):
        counter = 0
        counterList = []
        for i in range(len(sentences)):
            for j in range(len(sentences[i])):
                if sentences[i][j] == " ":
                    counter += 1
            counterList.append(counter)
            counter = 0
        return max(counterList)+1

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
st = Solution()
print(st.mostWordsFound(sentences))