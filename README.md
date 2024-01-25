Used to get a lemma frequency on a specific text instead of the whole language.
My goal is to use this to prepare myself for specific episodes of anime by studying their most frequent words.

I got the transcript to anime episodes from here: https://github.com/Matchoo95/JP-Subtitles/tree/master

I translated the .ass file to txt here: https://subtitletools.com/convert-subtitles-to-plain-text-online

Steps:
1. Run try_fugashi.py (which reads the text from episode1.txt)
2. Run translate.py to add translation to each line

```
pip install 'fugashi[unidic]' 
python -m unidic download     
pip install -U deep-translator
```

todo: make it so I can reference where each original lemma came from.
Like each entry should have a list of translated sources to compare