# a=2,b=10,求3的b次幂：
# 3^10=(3^2)^5=9^5=9*9^4=9*[(9^2)^2]=9*[18^2]
def fast_pow(a, b):
    ans=1
    while b:
        if b%2==0:
            a=a*a
            b//=2
        else:
            ans*=a
            a=a*a
            b//=2
    return ans
a=2
b=3
print(fast_pow(a,b))
# 2^3=2*[2^2]