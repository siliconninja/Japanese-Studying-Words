# Japanese-Studying-Words
Make random word combinations! Useful for Japanese Hiragana and Katakana practice!

## How to use

Install romkan: `pip install romkan`

(If using Windows, in a Command Prompt with admin permissions, type `set PYTHONUTF8=1` first,
then type `pip install romkan`. See https://github.com/soimort/python-romkan/issues/10#issuecomment-614783904 for more details on this issue)

Then run the program using the following command: `python japanese_words.py <r/h/k> <up_to (the last kana in Rōmaji)> <num_letters_per_word> <num_words>`

For example: `python japanese_words.py k ho 4 10`

This prints 10 random Katakana word combinations from a-ho with 4 letters (kana) in each word.

On Windows, you can only do Romaji word generation (but the above may work in Command Prompt). To do Romaji word generation, type `python japanese_words.py r ho 4 10`.

## Troubleshooting

### `UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-3: character maps to <undefined>`

~~Run the command `set PYTHONUTF8=1` then run the `japanese_words.py` program again.~~

Apparently Katakana/Hiragana generation does not work in Windows, at least not in Git Bash. :(

This fix may work in Command Prompt though.

## Tests

Coming soon!

[ ] Correct combo is generated

[ ] Zero words results in failure

[ ] `up_to` generates the correct katakana
