# https://www.nowcoder.com/practice/b929be9dbbaa489a91afa3fec195c228?tpId=101&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D101&difficulty=&judgeStatus=&tags=&title=
def solve(mt,k):
    max_rows=len(mt)-1
    max_cols=len(mt[0])-1
    row,col=0,max_cols-1# init num,右上角
    num=mt[row][col]
    
    while row<=max_rows and col>=0:
        num=mt[row][col]
        if num==k:
            print('Yes')
            return 
        if k>num:
            row+=1
        else:
            col-=1
    print('No')
            
            
n, m, k = list(map(int, input().split()))
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
solve(matrix,k)