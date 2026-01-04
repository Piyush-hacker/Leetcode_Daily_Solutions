class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        external=[]
        
        for num in nums:
            internal=[]
            
            for i in range(1,int(num**0.5)+1):
                if num%i==0:
                    
                    internal.append(i)
                    if i != num // i:     
                        internal.append(num // i)
                    if len(internal)>4:
                        break
            if len(internal)==4:
                external+=internal
        return sum(external)
                    


            


        
        