import json
from pykakasi import kakasi, wakati


kakasi = kakasi()
kakasi.setMode("J","H")
conv_j2h = kakasi.getConverter()
kakasi.setMode("K","H")
conv_k2h = kakasi.getConverter()


def hiraganafy(keyword):
    k = keyword.upper()
    k = conv_j2h.do(k)
    k = conv_k2h.do(k)
    return k


def add_word(emoji, keyword, l):
    word = ':' + keyword + '\t' + emoji + '\t' + '記号' + '\t'
    l.append(word)
    return l


if __name__ == "__main__":
    with open('/data/emoji_ja.json') as f:
        d = json.load(f)
    # print(d['🐶'])
    # for k in d['🐶']:
    #     print(k)

    l = []
    for emoji in d:
        for k in d[emoji]['keywords']:
            if k.isalpha() is False:
                continue
            k = hiraganafy(k)
            l = add_word(emoji, k, l)

        # 国旗の国名を short_name から抽出
        k = d[emoji]['short_name']
        if k.isalpha() is False:
            continue
        k = hiraganafy(k)
        l = add_word(emoji, k, l)

    l_uniq = list(set(l))
    l_uniq.sort()
    output = '\n'.join(l_uniq)
    # print(l)
    with open("emoji.txt", 'w') as f:
        f.write(str(output))
