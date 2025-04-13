class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ns = 0  
        for i in range(low, high + 1):
            s = str(i)
            if len(s) % 2 == 0:  
                ind = len(s) // 2
                n1 = s[:ind]
                n2 = s[ind:]
                soma1 = sum(int(d) for d in n1)  
                soma2 = sum(int(d) for d in n2)  
                if soma1 == soma2:  
                    ns += 1
        return ns
