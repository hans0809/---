# 小美和小团合作开发了一款新游戏！他们相信这款游戏一定可以大火。
# 游戏规则是这样的，现在有一个方格地图，你控制一个机器人位于初始位置(x, y)，然后你可以向上下左右的地块移动。
# 其中一些地块上会有得分点，经过这些点可以获得分数。
# 当然，路上还会有一些陷阱点，如果想要通过陷阱点，就需要付出一定的分数来清除这个陷阱点。
# 注意陷阱点付出分数清除后就会变成普通的地块。即反复经过陷阱点只需付出一次代价。同样的，得分点也只能获得一次分数。
# 小美想到了一个策划案来让这个游戏变得难一些。小美把地图和机器人的初始位置给了小团，并且告诉了小团他操控机器人的行进路线。
# 小美想试试小团能不能算出来他的最终得分。
# 小团完美地完成了这个任务。现在，小美和小团想找一些测试人员看看这款游戏的难度如何。他们找到了你，希望你帮他们测试一下这个游戏。而你能否挑战成功呢？
# 注意分数允许为负。初始分数为0.

# 输入描述:
# 第一行四个整数N，M，P，Q，表示这张地图是N行M列的，得分点的得分是P，陷阱点清除的代价是Q。
# 接下来N行，每行M个字符，表示这张地图。其中，字符S表示初始机器人位置。字符#表示墙壁，字符O代表得分点。字符X代表陷阱点。字符+代表普通的地块。
# 接下来一行一个连续的字符串表示机器人的移动路线，只由大写字母WASD构成，W向上，A向左，S向下，D向右。
# 机器人可以上下左右移动。不能超出地图边界。也不能走到墙壁之上。试图走出边界和走到墙壁的行动会停留在原来的位置不动。

# 输出描述:
# 一个整数，表示小团的机器人最终获得了多少分

# 输入例子1:
# 6 6 20 10
# S#++O#
# OXX#X#
# ++++++
# ###XX#
# ++#O#+
# OXO++X
# SSDDDDDAWWSSSAWSSSADDD

# 输出例子1:
# 40


def gamer(grid, path, p, q):
    n,m=len(grid),len(grid[0])#nxm
    score=0

    # 定位机器人所在初始位置
    def find_init_loc():
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='S':
                    return [i,j]

    # 根据当前位置的地标执行相应操作
    def check(grid,i,j):
        cur_score=0
        if grid[i][j]=='O':# 奖励
            cur_score+=p# 吃了奖励
            grid[i][j]='+'
        elif grid[i][j]=='X':# 障碍
            cur_score-=q# 破除障碍
            grid[i][j]='+'
        elif grid[i][j]=='+':# 普通地块
            cur_score+=0# 原地踏步
        return cur_score

    # 机器人开始移动
    def run(score):
        init_loc=find_init_loc()
        i,j=init_loc[0],init_loc[1]# 初始位置所在的行数i和列数j

        for move in path:
            # 向上
            if move=='W':
                if i-1<0 or grid[i-1][j]=='#':
                    continue
                else:
                    i-=1
                    score+=check(grid,i,j)
            # 向下
            elif move=='S':
                # 如果当前已经处于最后一行，或者往下走是墙壁，那么就不能往下走了，执行S将原地踏步
                if i+1>=n or grid[i+1][j]=='#':
                    continue
                # 否则就向下走一步
                else:
                    i+=1
                    score+=check(grid,i,j)

            # 向左
            elif move=='A':
                if j-1<0 or grid[i][j-1]=='#':
                    continue
                else:
                    j-=1
                    score+=check(grid,i,j)
            # 向右
            elif move=='D':
                if j+1>=m or grid[i][j+1]=='#':
                    continue
                else:
                    j+=1
                    score+=check(grid,i,j)
        return score
    final_score=run(score)
    return final_score


N, M, P, Q = map(int, input().split(' '))
grid = [[0 for _ in range(M)] for _ in range(N)]  # NxM
for row in range(N):
    s=input()
    for col in range(M):
        grid[row][col] = s[col]
path = input()
final_score = gamer(grid, path, P, Q)
print(final_score)
