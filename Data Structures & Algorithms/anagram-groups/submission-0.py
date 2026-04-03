class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we take this type of dict for making appending the world with the 
        # same set of letters: res[(0,0,1...)].append("word")

        res = defaultdict(list)

        for s in strs:
            # make the alphabet list [0, 0, 0...0]
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # Here you have filled alphavet code and you can create the list
            res[tuple(count)].append(s)
        
        return list(res.values())