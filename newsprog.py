from collections import defaultdict
import json
import xml.etree.ElementTree as ET


def get_description_json(json_file):
    description_news = ''
    for item in json.load(json_file)['rss']['channel']['items']:
        description_news += item['description']
    return description_news


def get_description_xml(xml_file):
    description_news = ''
    for item in ET.parse(xml_file).getroot().findall("channel/item/description"):
        description_news += item.text
    return description_news


def get_words_list(description_news):
    return list(description_news.split())


def get_long_words_list(words_list):
    long_words_list = [word for word in words_list if len(word) >= 6]
    return long_words_list


def get_word_count(long_words_list):
    words_dict = {}
    for word in long_words_list:
        words_dict.setdefault(word, 0)
        words_dict[word] += 1
    return words_dict


def get_top_ten(words_dict):
    sorted_words = sorted(words_dict.items(), key=lambda item: -item[1])
    for count, word in enumerate(sorted_words):
        if count > 9:
            break
        print(f'Слово "{word[0]}" встречается в тексте {word[1]} раза')


if __name__ == '__main__':
    print('1___Расчёт для JSON-файла:')
    with open('newsafr.json', encoding='utf8') as json_file:
        get_top_ten(get_word_count(get_long_words_list(get_words_list(get_description_json(json_file)))))
    print(' ')
    print('2___Расчёт для XML-файла:')
    get_top_ten(get_word_count(get_long_words_list(get_words_list(get_description_xml('newsafr.xml')))))