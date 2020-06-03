class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        
        digs = list(num)
        stack_least = []

        while digs and k:
            if not stack_least:
                stack_least.append(digs.pop(0))
            else:
                msd = digs.pop(0)
                while k and stack_least and stack_least[-1] > msd:
                        stack_least.pop()
                        k -= 1
                stack_least.append(msd)
            
        while k:
            # digits is empty
            stack_least.pop()
            k-=1
        
        digs = stack_least + digs
        # remove leading 0s
        while digs and digs[0] == "0":
            digs.pop(0)
        
        return "0" if not digs else ''.join(digs)
    