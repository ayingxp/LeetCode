# 数字拆分问题
# 给定一个数字，求所有可能的分解组合

res = []

def num_div(n):
    if n == 0:
        print(res)
    else:
        for i in range(1, n + 1):
            res.append(i)
            num_div(n-i)
            res.pop()



if __name__ == "__main__":
    num = 7
    num_div(num)
    print(res)