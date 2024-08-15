# -*- coding: shift_jis -*-
from scipy import stats
from sklearn.datasets import load_wine
import numpy as np
import random

def dis(x,y):
    ans = 0
    for i in range(len(x)):
        ans += (x[i] - y[i])**2
    return ans

# ワインデータセットのロード
wine = load_wine()

# データとターゲットの取得
X = wine.data  # 特徴量データ
y = wine.target  # ラベルデータ
n,m = X.shape

mu = np.mean(X,axis=0)
var = np.var(X,axis=0)

for i in range(n):
    for j in range(m):
        X[i][j] = (X[i][j] - mu[j]) / var[j]

r = []
for i in range(3):
    r.append([random.uniform(-1,1) for j in range(m)])

old_label = n * [0]
new_label = n * [1]

while(old_label != new_label):
    old_label = new_label.copy()
    sum_data = [m * [0.0] for _ in range(3)]
    count = 3 * [0]
    for i in range(n):
        d = [dis(X[i],r[j]) for j in range(3)]
        new_label[i] = int(np.argmin(d))
        count[new_label[i]] += 1
        for j in range(m):
            sum_data[new_label[i]][j] += X[i][j]
    for i in range(3):
        for j in range(m):
            r[i][j] = sum_data[i][j] / count[i]

f = 0
f += stats.mode(new_label[0:58]).count
f += stats.mode(new_label[59:129]).count
f += stats.mode(new_label[130:177]).count
print("クラスタリング成功率：{:.3f}".format(f/178))
