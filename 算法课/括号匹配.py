# 给一个括号字符串，求至少需要添加几个括号，使得括号变匹配

# 先考虑如果判断括号字符串是否匹配：
#   设定一个变量count，初始为0，遍历字符串，遇到左括号count加1，遇到右括号count减1
#   如果匹配，则遍历完成后count=0【前提：不出现诸如')('的样例,这种需要判断下就好】
# 据此解题：
#   用ans记录需要添加的括号数，依然设定一个变量count，
#   遍历字符串，遇到左括号count加1，遇到右括号count减1，
#   1)在遍历过程中，当遇到右括号时，如果count=0，说明此时当前右括号是多出来的，需要添加一个左括号才能够匹配，因此ans加1，(count从0变成-1，然后再人工改成0，所以这一步可以省略，反正结果都是让count为0)
#   然后继续遍历
#   2)在遍历过程中，当遇到右括号时，如果count!=0，那么count一定是1（应该说一定不是0），此时直接让count减1
#   在整个遍历完成后，count的取值就是多出来的左括号个数，此时需要再添加同样个数的右括号
def needParentheses(s):
    count=0
    ans=0
    for i in range(len(s)):
        if s[i]=='(':
            count+=1
        else:# s[i]==')'
            if count==0:# 保证了count始终不会小于0
                ans+=1
            else:# 此时count不一定是1哦
                count-=1
    # print(ans,count)
    return ans+count

s=')('
print('最少需要添加的括号数：',needParentheses(s))

    

