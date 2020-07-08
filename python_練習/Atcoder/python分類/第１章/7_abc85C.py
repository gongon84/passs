if __name__ == "__main__":

    N,Y = map(int, input().split()) #z=N-x-yとして２変数の問題にする
    answer = -1,-1,-1
    for x in range(N+1):
        for y in range(N+1-x):
            z = N-x-y
            if 0 <= z <= 2000 and 10000 * x + 5000 * y + 1000 * z == Y:
                answer = x, y, z
                break
        else:
            continue
        break
    print(answer)

    #自分

    '''
    整数問題
    リンク　→　https://atcoder.jp/contests/abc085/tasks/abc085_c
    '''