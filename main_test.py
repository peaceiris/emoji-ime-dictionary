import unittest
import main


class TestStringMethods(unittest.TestCase):

    def test_hiraganafy(self):
        katakana = 'カタカナ'
        self.assertEqual(main.hiraganafy(katakana), 'かたかな')
        kanji = '漢字'
        self.assertEqual(main.hiraganafy(kanji), 'かんじ')
        hiragana = 'ひらがな'
        self.assertEqual(main.hiraganafy(hiragana), 'ひらがな')

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
