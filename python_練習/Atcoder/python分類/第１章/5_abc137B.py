if __name__ == "__main__":

    K,X = map(int, input().split())
    print(*[x for x in range(X-K+1,X+K)])

    #別解
    # K,X = map(int, input().split())
    # print(*list(range(X-K+1,X+K)))

    # 別解２
    # K,X = map(int, input().split())
    # print(*range(X-K+1,X+K))

    #自分
    # k, x = map(int, input().split())
    # t = x - k + 1
    # lists =[]
    # for i in range(2*k - 1):
    #     lists.append(t)
    #     t += 1
    # print(*lists)

    '''
    リンク　→　https://atcoder.jp/contests/abc137/tasks/abc137_b
    '''