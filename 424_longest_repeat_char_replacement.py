class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 2 and k > 0:
            return 2

        start = 0
        end = 1
        freqmax = 0
        lenmax = 1
        counter = {}

        while (end <= len(s)) and start<end:
            
            if s[end-1] in counter:
                counter[s[end-1]] = counter[s[end-1]] + 1
            else:
                counter[s[end-1]] = 1

            freqmax = self.maxcount(counter)
            print(counter)
            
            print( len(s[start:end]), freqmax)
            if len(s[start:end]) - freqmax > k:
                counter[s[start]]-=1
                start += 1
                counter[s[end-1]] -=1
            else:
                
                lenmax = max(lenmax,   len( s[start:end]   ))
                end = end + 1

            

        return lenmax

    def maxcount(self, d: dict) -> int:
        if not d:
            return 0
        return max(list(d.values()))





sol = Solution()

print( sol.characterReplacement("AABABBA", 1))		