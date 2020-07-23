import urllib.request
import json

from pykakasi import kakasi, wakati


EMOJI_JSON_URL = 'https://raw.githubusercontent.com/yagays/emoji-ja/20190726/data/emoji_ja.json'
EMOJI_DICT_PATH = 'tsv/emoji.tsv'
kakasi = kakasi()


class EmojiDict():
    emoji_json = None
    emoji_dict = []

    def __init__(self, emoji_json_url: str, emoji_dict_path: str) -> None:
        self.emoji_json_url = emoji_json_url
        self.emoji_dict_path = emoji_dict_path

    def get_emoji_json(self) -> None:
        with urllib.request.urlopen(self.emoji_json_url) as f:
            self.emoji_json = json.loads(f.read().decode('utf-8'))

    def save_emoji_dict(self) -> None:
        with open(self.emoji_dict_path, 'w') as f:
            f.write(str(self.emoji_dict))

    def create_emoji_dict(self) -> None:
        for emoji in self.emoji_json:
            for k in self.emoji_json[emoji]['keywords']:
                if k.isalpha() is False:
                    continue
                k = k.upper()
                kakasi.setMode("J","H")
                conv = kakasi.getConverter()
                k = conv.do(k)
                kakasi.setMode("K","H")
                conv = kakasi.getConverter()
                k = conv.do(k)
                w = f':{k}\t{emoji}\t記号\t'
                self.emoji_dict.append(w)

            k = self.emoji_json[emoji]['short_name']
            if k.isalpha() is False:
                continue
            k = k.upper()
            kakasi.setMode("J","H")
            conv = kakasi.getConverter()
            k = conv.do(k)
            kakasi.setMode("K","H")
            conv = kakasi.getConverter()
            k = conv.do(k)
            w = f':{k}\t{emoji}\t記号\t'
            self.emoji_dict.append(w)

        self.emoji_dict.sort()
        self.emoji_dict = '\n'.join(self.emoji_dict)


if __name__ == "__main__":
    emoji_dict = EmojiDict(EMOJI_JSON_URL, EMOJI_DICT_PATH)
    emoji_dict.get_emoji_json()
    emoji_dict.create_emoji_dict()
    emoji_dict.save_emoji_dict()
