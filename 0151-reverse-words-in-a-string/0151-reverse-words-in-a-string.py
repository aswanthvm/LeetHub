class Solution:
    def reverseWords(self, s: str) -> str:
        new_sentence = s.split()
        reversed_list = new_sentence[::-1]
        result = ' '.join(reversed_list)
        return result
        
        