from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='ja', target='en')

lines = open("episode1clean.txt", "r").readlines()
episode_translated = open('episode_translated.txt', 'a')
for line in lines:
    english = translator.translate(line)
    together = f'{line.strip()}   |   {english}\n'
    episode_translated.write(together)