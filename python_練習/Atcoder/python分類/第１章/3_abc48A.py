if __name__ == "__main__":

    print("A{}C".format(input()[8]))


    #別解
    print("A" + input()[8] + "C")


    #自分の解答
    S = input()
    a,b,c = S.split()
    print(a[0]+b[0]+c[0])

    #https://atcoder.jp/contests/abc048/tasks/abc048_a