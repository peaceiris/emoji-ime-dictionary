import urllib.request
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


def add_word_to_dict(emoji, keyword, emoji_dict):
    valid_keyword = keyword.replace('ゔ', 'う゛')
    word = f':{valid_keyword}\t{emoji}\t記号\t'
    emoji_dict.append(word)


class EmojiDict():
    emoji_json = None
    emoji_dict = []

    def __init__(self, emoji_json_path: str, emoji_dict_path: str) -> None:
        self.emoji_json_path = emoji_json_path
        self.emoji_dict_path = emoji_dict_path

    def get_emoji_json(self) -> None:
        with open(self.emoji_json_path, 'r') as f:
            self.emoji_json = json.load(f)

    def save_emoji_dict(self) -> None:
        with open(self.emoji_dict_path, 'w') as f:
            f.write(str(self.emoji_dict))
            f.write('\n')

    def create_emoji_dict(self) -> None:
        for emoji in self.emoji_json:
            for k in self.emoji_json[emoji]['keywords']:
                if k.isalpha() is False:
                    continue
                k = hiraganafy(k)
                add_word_to_dict(emoji, k, self.emoji_dict)

            k = self.emoji_json[emoji]['short_name']
            if k.isalpha() is False:
                continue
            k = hiraganafy(k)
            add_word_to_dict(emoji, k, self.emoji_dict)

        self.emoji_dict.sort()
        self.emoji_dict = '\n'.join(self.emoji_dict)


if __name__ == "__main__":
    EMOJI_JSON_PATH = '/root/emoji_ja.json'
    EMOJI_DICT_PATH = 'tsv/emoji.tsv'
    emoji_dict = EmojiDict(EMOJI_JSON_PATH, EMOJI_DICT_PATH)
    emoji_dict.get_emoji_json()
    emoji_dict.create_emoji_dict()
    emoji_dict.save_emoji_dict()
