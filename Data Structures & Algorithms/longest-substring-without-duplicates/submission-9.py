class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst_of_substr = []
        for i in range(len(s)):
            left = i
            right = i

            while right <= len(s):

                if left == right:
                    right += 1
                    continue
                sub_str = s[left:right]
                right += 1
                lst_of_substr.append(sub_str)
        result = 0
        for lst in lst_of_substr:
            for i, s in enumerate(lst):
                if lst.count(s) > 1:
                    break
                if i == len(lst)-1:
                    result = max(result, len(lst))

        return result


                
        