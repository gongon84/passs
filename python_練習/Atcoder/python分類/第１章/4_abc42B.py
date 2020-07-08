if __name__ == "__main__":

    n, l = map(int, input().split()) #map()でintを適用させる。下のrange()でintが必要なため
    s = sorted([input() for i in range(n)]) #n個の要素が入ったリストを作成
    print(*s, sep='') #*sでリストを個々に分ける

    #別解
    n, l = map(int, input().split())
    s = sorted([input() for i in range(n)])
    print("".join(s)) #join()で文字列を統合させる

    #自分 →　空欄

    '''
    map()
    sorted()
    *s
    join()
    
    リンク　→　https://atcoder.jp/contests/abc042/tasks/abc042_b    
    '''