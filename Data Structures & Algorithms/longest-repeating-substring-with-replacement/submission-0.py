class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0

        mx = -1
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0) + 1

            max_letter_count = 0
            max_letter = ''

            for letter in freq:
                max_letter_count = max(freq[letter], max_letter_count)
            
            while (r-l) - max_letter_count >= k: 
                freq[s[l]] = freq.get(s[l],0) - 1
                l+=1
                mx = max(mx, r-l)
            mx = max(mx, r-l)

        return mx+1



        
            

            
                


            

               
            
                

            



            





        