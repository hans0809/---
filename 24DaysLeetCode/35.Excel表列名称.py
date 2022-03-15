class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=[]
        while columnNumber:
            columnNumber-=1
            r=columnNumber%26
            columnNumber//=26
            res.append(r)
        final_res=''
        for i in res[::-1]:
            final_res+=chr(i+65)
        return final_res
        
        