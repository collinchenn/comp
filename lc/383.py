class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counts, magazine_counts = [0] * 26, [0] * 26

        for letter in ransomNote:
            ransom_counts[ord(letter)-97] += 1
        
        for letter in magazine:
            magazine_counts[ord(letter)-97] += 1

        for i in range(len(ransom_counts)):
            if ransom_counts[i] > magazine_counts[i]:
                return False
        
        return True