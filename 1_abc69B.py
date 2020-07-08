if __name__ == "__main__":

    S = input()
    print(S[0]+str(len(S)-2)+S[-1])

    #別解
    a,*b,c=input()
    print(a+str(len(b))+c)

    #https://atcoder.jp/contests/abc069/tasks/abc069_b