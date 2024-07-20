class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        merged_string = []
        i, j = 0, 0
        len1, len2 = len(word1), len(word2)

        while i < len1 and j < len2:
            merged_string.append(word1[i])
            merged_string.append(word2[j])
            i += 1
            j += 1
 
        while i < len1:
            merged_string.append(word1[i])
            i += 1
            
        while j < len2:
            merged_string.append(word2[j])
            j += 1
        
        return ''.join(merged_string)

solution = Solution()
word1 = "abc"
word2 = "pqr"
print(solution.mergeAlternately(word1, word2))  

word1 = "ab"
word2 = "pqrs"
print(solution.mergeAlternately(word1, word2))  

word1 = "abcd"
word2 = "pq"
print(solution.mergeAlternately(word1, word2)) 