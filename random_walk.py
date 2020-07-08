# インポート
import random
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":


    # 粒子の数 item_number
    inum = 50

    # 粒子の位置 　初期値(5,5)を粒子（inum）の数だけ作る
    x = [[5] for i in range(inum)]
    y = [[5] for i in range(inum)]

    # 時刻
    t = [0]

    # 足跡　10行10列の配列（中身は0）
    count = np.zeros((10, 10))

    # 移動方向
    direction = 0

    # 粒子の個数（inum）回ループ
    for m in range(0, inum):

        # 最初に表示されるやつ
        # print("\n",m+1)
        # print('時刻t|サイコロの目r|位置(x,y)|移動方向')
        # print('0|-|[5, 5]|-')

        # ステップ数 ループ
        for n in range(1, 6):

            # count[5,5] += 1 #初期値を足跡に含む場合に使用

            # サイコロの目（ランダム）
            r = random.randint(1, 4)

            # rによってx, yが変化
            if r == 1:
                x[m].append(x[m][n - 1])  # xはそのまま
                y[m].append(y[m][n - 1] + 1)  # y方向に+1
                direction = "↑"
            elif r == 2:
                x[m].append(x[m][n - 1] + 1)  # x方向に+1
                y[m].append(y[m][n - 1])
                direction = "→"
            elif r == 3:
                x[m].append(x[m][n - 1])
                y[m].append(y[m][n - 1] - 1)  # y方向に-1
                direction = "↓"
            elif r == 4:
                x[m].append(x[m][n - 1] - 1)  # x方向に-1
                y[m].append(y[m][n - 1])
                direction = "←"

            # 時間、出た目、現在地、方向を表示
            z = [x[m][n], y[m][n]]
            # print('{}|{}|{}|{}'.format(n, r, z, direction))

            # 足跡記録
            if 1 <= r <= 4:
                count[x[m][n], y[m][n]] += 1

        # 時刻が＋１
        t.append(n)

    # 足跡の配列とグラフの方向調節
    count_T = count.T  # 転置
    count_TF = np.flipud(count_T)  # 上下反転

    # 足跡表示
    print("\n", count_TF)
    # print("  ↑原点(0,0)      ↑5行目(5,0)")

    # 確率
    new_count = np.round(count_TF / inum, 2)
    print("\n", new_count)

    # walkに値が入っていればその位置をプリント
    """for nn in range(10):
        for mm in range(10):
            if walk[nn][mm] != 0:
                print(nn,mm)
    """

    # グラフ作成
    # 一つ目のグラフ ax
    fig = plt.figure(figsize=(10, 14))
    ax = fig.add_subplot(211)

    # グラフ表示
    for a, b in zip(x, y):
        ax.plot(a, b, marker='o', ms=14, color='black')  # msはマーカーのサイズ
        ax.plot(a[0], b[0], marker='o', ms=14, color='green')  # スタート地点を緑
        ax.plot(a[n], b[n], marker='o', ms=14, color='red')  # ゴール地点を赤

    # ラベル
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # グリッド線
    ax.grid(b=True, which='major', axis='both')

    # 表示範囲
    plt.xticks(list(range(0, 11)))
    plt.yticks(list(range(0, 11)))

    # 二つ目のグラフ ax2
    from mpl_toolkits.mplot3d import Axes3D

    ax2 = fig.add_subplot(212, projection="3d")

    # X, Y, Zの定義
    X, Y = np.mgrid[0:10, 0:10]
    Y = np.flipud(Y)  # 配列や２次元グラフと方向を合わせるため
    Z = new_count

    # 3Dグラフ表示　edgecolorはマス目の色 「注意」x軸が縦、y軸が横
    surf = ax2.plot_surface(X, Y, Z, edgecolor="gray", cmap="bone_r")

    # カラーバー
    fig.colorbar(surf)

    # ラベル
    ax2.set_xlabel('y')
    ax2.set_ylabel('x')
    ax2.set_zlabel('z')

    # グラフの表示角度を調節 elevでz軸
    # ax2.view_init(elev=40)

    plt.show()

    # xとyの値
    # print('x:{} y:{}'.format(x,y))