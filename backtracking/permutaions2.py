# 全排列问题

data = list("ABCDEF")

res = list()

def permutate(data):
    if not data:
        # res.append(None)
        return None
    if len(data) == 1:
        # res.append(data)
        return data[0]
    else:
        for i in range(len(data)):
            # res.append([data[i]] + data[0:i] + data[i+1:])
            return permutate(data[:i]) + [data[i]] + permutate(data[i+1:])

    return res

def permutate2(data, step):
    if step == len(data):
        res.append(data[:])  # 切片会进行深度拷贝
    else:
        for i in range(step, len(data)):
            data[i], data[step] = data[step], data[i]
            permutate2(data, step + 1)
            data[i], data[step] = data[step], data[i]



if __name__ == "__main__":
    from pprint import pprint
    # print(permutate(data[:3]))
    permutate2(data[:3], 0)
    pprint(res)