if __name__ == "__main__":

    input()
    S = input()
    K = int(input())
    for s in S:print(s if s == S[K-1] else "*", end="")

    #自分
    # N = int(input())
    # S = input()
    # K = int(input())
    # moji = []
    # for i in S:
    #     if i != S[K-1]:
    #         i = "*"
    #     moji.append(i)
    # print(*moji,sep="")

    '''
    リンク　→　https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_b
    '''