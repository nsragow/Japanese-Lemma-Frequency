Used to get a lemma frequency on a specific text instead of the whole language.
My goal is to use this to prepare myself for specific episodes of anime by studying their most frequent words.

Steps:
1. Run try_fugashi.py (which reads the text from episode1.txt)
2. Run translate.py to add translation to each line

```
pip install 'fugashi[unidic]' 
python -m unidic download     
pip install -U deep-translator
```
