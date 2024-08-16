# k_means
## k-meansのアルゴリズム
目的関数

$$J=\sum_{n=1}^N\sum_{k=1}^Kr_{n,k}\lVert\boldsymbol{x}_n-\boldsymbol{\mu}_k\rVert^2$$

の最小化を行う．ただし，

$$r_{n,k}=
\begin{cases}
1 & k=k'(k'\in\{ 1,2,\ldots,K\} ) \\
0 & otherwise
\end{cases}
$$
### $r_{n,k}$について最適化

$$
J = \sum_{n=1}^N\sum_{k=1}^Kr_{n,k}\lVert\boldsymbol{x}_n-\boldsymbol{\mu}_k\rVert^2
$$

$$
= \sum_{k=1}^Kr_{1,k}\lVert x_1-\mu_k\rVert^2+\sum_{k=1}^Kr_{2,k}\lVert x_2-\mu_k\rVert^2+\ldots+\sum_{k=1}^Kr_{N,k}\lVert x_N-\mu_k\rVert^2
$$

$r_{n,k}$の制約から，最適化を行うと，

$$r_{n,k}=
\begin{cases}
1 & k=\arg\min_j \lVert x_n-\mu_j\rVert^2\\
0 & otherwise
\end{cases}
$$

### $\mu_k$について最適化

$$
\frac{\partial J}{\partial\mu_k} = \sum_{n=1}^N\frac{\partial}{\partial\mu_k}\sum_{k=1}^Kr_{n,k}\lVert x_n-\mu_k\rVert^2=2\sum_{n=1}^Nr_{n,k}(x_n-\mu_k)
$$

となるので
$\frac{\partial J}{\partial\mu_k} = 0$
とすると，

$$
\mu_k = \frac{\sum_{n=1}^Nr_{n,k}x_n}{\sum_{n=1}^Nr_{n,k}}
$$

となる．つまり
$\mu_k$
はクラス
$k$
に含まれるデータの平均とすれば良い．

上記の二つの最適化を交互に行うことでk-meansを実装できる．
またk-meansでは代表点の初期値に依存性があるが，有限回でクラスタリングが行えることがわかっている．
