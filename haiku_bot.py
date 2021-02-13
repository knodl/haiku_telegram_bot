from collections import deque


def split_sentence(msg: str) -> list:
    splitted = msg.split('.')
    result = [sentence.strip() for sentence in splitted]
    return result


def split_words(msg: str) -> list:
    splitted = msg.split(' ')
    result = [''.join(e for e in word.strip() if e.isalnum()) for word in splitted]
    return result


def count_syllables(word: str) -> int:
    en_vowels = "aeiouy"
    ru_vowels = "аеёиоыуэюя"

    cnt = 0

    for s in word:
        if s in en_vowels or s in ru_vowels:
            cnt += 1
    if word[-1] == 'e':
        cnt -= 1
    if cnt == 0:
        cnt = 1

    return cnt


def is_n_syllables(word: str, n_syllables: int) -> bool:
    word_syllables = count_syllables(word)
    return word_syllables == n_syllables


def compose_haiku(words: list) -> str:
    first_row = {'syllables': 0, 'words': []}
    second_row = {'syllables': 0, 'words': []}
    third_row = {'syllables': 0, 'words': []}

    d = deque(words)

    while first_row['syllables'] < 5:
        w = d.popleft()
        first_row['syllables'] += count_syllables(w)
        first_row['words'].append(w)
    if first_row['syllables'] > 5:
        raise ValueError('Impossible to create first row.')
    
    while second_row['syllables'] < 7:
        w = d.popleft()
        second_row['syllables'] += count_syllables(w)
        second_row['words'].append(w)
    if second_row['syllables'] > 7:
        raise ValueError('Impossible to create second row.')

    while third_row['syllables'] < 5:
        w = d.popleft()
        third_row['syllables'] += count_syllables(w)
        third_row['words'].append(w)
    if third_row['syllables'] > 5:
        raise ValueError('Impossible to create third row.')

    result = ' '.join(first_row['words']) + '\n'
    result += ' '.join(second_row['words']) + '\n'
    result += ' '.join(third_row['words'])

    return result


def get_haiku(msg: str) -> str:
    words = split_words(msg)
    n_syllables = [count_syllables(word) for word in words]
    if sum(n_syllables) == 17:
        result = compose_haiku(words)
        return result
    return ''

