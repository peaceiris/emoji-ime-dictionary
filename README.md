# emoji-ime-dictionary

😃 絵文字入力を日本語 🇯🇵 でするための IME 追加辞書 📙



## 目次 - Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [概要 - Overview](#%E6%A6%82%E8%A6%81---overview)
- [変換例 - Examples](#%E5%A4%89%E6%8F%9B%E4%BE%8B---examples)
- [辞書の導入方法 - Installation](#%E8%BE%9E%E6%9B%B8%E3%81%AE%E5%B0%8E%E5%85%A5%E6%96%B9%E6%B3%95---installation)
  - [Google 日本語入力](#google-%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%85%A5%E5%8A%9B)
  - [Microsoft IME](#microsoft-ime)
  - [ATOK](#atok)
- [関連プロジェクト - Related project](#%E9%96%A2%E9%80%A3%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88---related-project)
- [作者 - Author](#%E4%BD%9C%E8%80%85---author)
- [謝辞 - Acknowledgement](#%E8%AC%9D%E8%BE%9E---acknowledgement)
- [ライセンス - License](#%E3%83%A9%E3%82%A4%E3%82%BB%E3%83%B3%E3%82%B9---license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->



## 概要 - Overview

この辞書を IME に導入することで、
GitHub, Slack のようにコロン `:` をトリガーとして IME でも絵文字を入力することができるようになります。
「**GitHub, Slack 以外のアプリケーションでも GitHub, Slack のように絵文字を入力したい**」
という要望に応えるための IME 追加辞書です。

現在 6610 ペアの絵文字とその読みが収録されています。
[GitHub 上から辞書の中身を閲覧・検索できます。](https://github.com/peaceiris/emoji-ime-dictionary/blob/master/emoji.tsv)



## 変換例 - Examples

- `:にっぽん` を 🇯🇵 に変換することができるようになります。
- 🐶 を入力するには以下の方法があります。
    - `:いぬ`, `:いぬのかお`, `:かお`, `:どうぶつ`, `:ぺっと`
- `:ぺっと` は以下の変換候補を持ちます。
    - 🐇・🐈・🐕・🐩・🐰・🐱・🐶・🐹



## 辞書の導入方法 - Installation

| macOS を利用されている方へ |
|:---|
| macOS は `control + command + space` で「文字ビュアー(Character Viewer)」を呼び出すことができるので、この辞書を導入する前にそちらの利用を検討してください。一方で、「**システム言語が英語だけど日本語で絵文字を検索したい**」という方にはこの辞書がおすすめです。 |

### Google 日本語入力

1. 最新の [辞書ファイル](https://github.com/peaceiris/emoji-ime-dictionary/raw/master/emoji.txt) をダウンロード
1. Google日本語入力の `辞書ツール` を開く
1. `管理` をクリック
1. `新規辞書にインポート` をクリック
1. `ファイルを選択` からダウンロードしたファイルを選択
1. お好きな `辞書名` をつける
1. `インポート` をクリック

### Microsoft IME

- [複数の単語を一括で登録するには](https://support.microsoft.com/ja-jp/help/881925)

作者が Windows を持っていないため検証できていません。どなたか検証をお願いします。
[Issue #4](https://github.com/peaceiris/emoji-ime-dictionary/issues/4)

### ATOK

- [テキストファイルから単語登録した内容を取り込みたい](http://support.justsystems.com/faq/1032/app/servlet/qadoc?QID=017975)

作者が ATOK を持っていないため検証できていません。どなたか検証をお願いします。
[Issue #5](https://github.com/peaceiris/emoji-ime-dictionary/issues/5)



## 関連プロジェクト - Related project

- [日英変換・英語略語展開のためのIME追加辞書📙](https://github.com/peaceiris/google-ime-dictionary)



## 作者 - Author

- peaceiris
    - [GitHub](https://github.com/peaceiris)
    - [Twitter](https://twitter.com/piris314)

何かあれば [Issue] を立ててください。



## 謝辞 - Acknowledgement

- [yagays/emoji-ja: UNICODE絵文字の日本語読み/キーワード/分類辞書](https://github.com/yagays/emoji-ja)
    - [project's site](https://yag-ays.github.io/project/emoji-ja/)
- [miurahr/pykakasi](https://github.com/miurahr/pykakasi)



## ライセンス - License

- [MIT License](./LICENSE)
    - `emoji.txt` と `emoji.tsv` は [MIT License - yagays/emoji-ja] を継承しています。



<!-- Internal References -->
[Issue]: https://github.com/peaceiris/emoji-ime-dictionary/issues
<!-- External References -->
[MIT License - yagays/emoji-ja]: https://github.com/yagays/emoji-ja/blob/master/LICENSE.md
