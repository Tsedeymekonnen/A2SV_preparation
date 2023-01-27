class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        place = [0] * (len(word) + 1)
        for i, c in enumerate(word):
            place[i + 1] = place[i] + (c in 'aeiou') * (i + 1)  
        return sum(place)
