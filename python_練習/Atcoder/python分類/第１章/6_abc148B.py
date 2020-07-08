if __name__ == "__main__":

    N = input()
    S,T = input().split()
    print(*[s+t for s,t in zip(S,T)], sep="")

    #自分
    # N = input()
    # s,t = input().split()
    # lists = []
    # for a,b in zip(s,t):
    #     lists.append(a+b)
    # print(*lists,sep="")

    '''
    リンク　→　https://atcoder.jp/contests/abc148/tasks/abc148_b
    '''