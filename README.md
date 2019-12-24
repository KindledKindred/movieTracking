
## 作業開始まで

このリポジトリをクローンします．

```
~ user@ mkdir Develop
~ user@ cd Develop
Develop user@ git clone 
```

もし GitHub のアカウントを所持していないなら，
代わりに zip 等でダウンロードしたあと，作業用フォルダに展開します．

```
~ user@ cd Develop/plainTensorDocker
```

次に Docker という仮想コンテナを扱えるサービスを入れます．

URL：https://www.docker.com

`Get started` からアカウンティング登録をお願いします．
非常に巨大かつ有名なサービスなので，信頼できるアカウントで登録しても大丈夫だと思います．

今回は，とりあえずコピペで動くようになっていますが，
より高度な操作や仮想コンテナの概念の把握を求める場合，以下の記事を参考にしてください．

[Docker入門（さくらインターネット）](https://knowledge.sakura.ad.jp/13265/)

[いまさらだけどDockerに入門したのでわかりやすくまとめてみた（Qiita）](https://qiita.com/gold-kou/items/44860fbda1a34a001fc1)

次にDocker にログインします．

```
plainTensorDocker user@ docker login
```

作業用ディレクトリの中から doker コマンドを叩きます．

```terminal01
plainTensorDocker user$ docker run --rm -v `pwd`:/home/tensor-docker -it tensor-docker:0.1 /bin/bash
```

を入力すると

```
root@123456789:/home/tensor-docker#
```

のように，コンテナに入って作業することができます．
コンテナの内外どちらで作業しても，起動時のディレクトリと同期されますが，
後述の VScodeRemote 上で作業するのが設定を持ち運べるので便利だと思います．

また同期させる必要がない場合，たとえばすべてコンテナ内で解決する場合は

```
plainTensorDocker user$ docker run --rm -it tensor-docker:0.1 /bin/bash
```

で同期せず潜り込むこともできます．

仮想コンテナから抜け出す場合は

```
root@123456789:/home/tensor-docker# exit
```

を行ってください．

その他，コピーや削除等は上記記事を参照してください．

## VScode Remote

エディタ左側の Extension（拡張機能）から Remote - container をインストールします．
その後，左下の `><` のようなマークをクリックし，

`Reopen...` > `Refer Dockerfile...` （一例です，状況に応じて変更してください）

のように提示された選択肢をクリックしていくと，VScode が仮想コンテナ内で開きます．

拡張機能は Extension タブからローカルにあるものを一括インストールできますし，
`.devcontainer/devcontainer.json` を編集することで，
任意の環境に整えることも可能です．

そこからは自由に組み立てて操作することができます．

```
root@123456789:/workspaces/plainTensorDocker# touch src/main.py
```
