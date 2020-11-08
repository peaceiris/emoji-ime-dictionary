import unittest
import main


class TestStringMethods(unittest.TestCase):

    def test_hiraganafy(self):
        test_cases = [
            {'in': 'カタカナ', 'out': 'かたかな'},
            {'in': '漢字', 'out': 'かんじ'},
            {'in': 'ひらがな', 'out': 'ひらがな'},
            {'in': '哺乳瓶', 'out': 'ほにゅうびん'},
            {'in': '長距離走', 'out': 'ちょうきょりそう'},
            {'in': '営', 'out': 'えい'},
            {'in': '営マーク', 'out': 'えいまーく'},
            {'in': '営業中', 'out': 'えいぎょうちゅう'},
            {'in': '営業日', 'out': 'えいぎょうび'},
            {'in': 'バルカン人', 'out': 'ばるかんじん'},
            {'in': '水球をする人', 'out': 'すいきゅうをするひと'},
            {'in': '人のシルエット', 'out': 'ひとのしるえっと'},
            {'in': '話す人のシルエット', 'out': 'はなすひとのしるえっと'},
            {'in': '2人のシルエット', 'out': 'ふたりのしるえっと'},
            {'in': '六芒星', 'out': 'ろくぼうせい'},
            {'in': '波乗り', 'out': 'なみのり'},
            {'in': 'きらきら星', 'out': 'きらきらぼし'},
            {'in': 'くす玉', 'out': 'くすだま'},
            {'in': 'ソロモン諸島', 'out': 'そろもんしょとう'},
            {'in': 'クリッパートン島', 'out': 'くりっぱーとんとう'},
            {'in': '白杖', 'out': 'はくじょう'},
            {'in': '介助犬', 'out': 'かいじょけん'},
            {'in': '筋トレ', 'out': 'きんとれ'},
        ]
        for t in test_cases:
            self.assertEqual(main.hiraganafy(t['in']), t['out'])

    def test_hiraganafy_todo(self):
        test_cases = [
            {'in': 'しかめ面', 'out': 'しかめっつら'},
            {'in': 'しかめ面の人', 'out': 'しかめつらのひと'},
            {'in': 'フェイスマッサージ中の人', 'out': 'ふぇいすまっさーじちゅうのひと'},
            {'in': '六角星', 'out': 'ろっかくせい'},
        ]
        for t in test_cases:
            self.assertNotEqual(main.hiraganafy(t['in']), t['out'])

    def test_add_word_to_dict(self):
        emoji_dict = []
        main.add_word_to_dict('🇯🇵', 'にっぽん', emoji_dict)
        expected_row = f':にっぽん\t🇯🇵\t記号\t'
        self.assertEqual(expected_row, emoji_dict[0])
        main.add_word_to_dict('🆚', 'ゔぁーさす', emoji_dict)
        valid_row = f':う゛ぁーさす\t🆚\t記号\t'
        self.assertEqual(valid_row, emoji_dict[1])


if __name__ == '__main__':
    unittest.main(verbosity=2)
