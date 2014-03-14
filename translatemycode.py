#!python
# -*- coding: utf-8 -*-

import regex
import goslate
import random
import codecs
import argparse

__автор__ = 'Женя'

языки = (
'af', 'sq', 'ar', 'az', 'eu', 'bn', 'be', 'bg', 'ca', 'zh-CN', 'zh-TW', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl',
'fi', 'fr', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'iw', 'hi', 'hu', 'is', 'id', 'ga', 'it', 'ja', 'kn', 'ko', 'la', 'lv',
'lt', 'mk', 'ms', 'mt', 'no', 'fa', 'pl', 'pt', 'ro', 'ru', 'sr', 'sk', 'sl', 'es', 'sw', 'sv', 'ta', 'te', 'th', 'tr',
'uk', 'ur', 'vi', 'cy', 'yi')


def найти_названия(текст):
	переменые = regex.findall('var (\w+)', текст)
	константы = regex.findall('const (\w+)', текст)
	функции = regex.findall('function (\w+)', текст)
	классы = regex.findall('class (\w+)', текст)
	return переменые + функции + классы + константы


def перевести_название(название, язык):
	gs = goslate.Goslate()
	слова = regex.split('(?V1)(?<=[a-z])(?=[A-Z])|(_)', название)
	слова = [слово for слово in слова if isinstance(слово, str)]
	try:
		перевод = gs.translate(' '.join(слова), язык if язык != '' else random.choice(языки))
		переводы = перевод.split(' ')
		переводы = [перевод.capitalize() for перевод in переводы]
	except:
		return название
	return ''.join(переводы)


def перевести_текст(текст, язык):
	названия = найти_названия(текст)
	for название in названия:
		перевод = перевести_название(название, язык)
		if название != перевод:
			текст = текст.replace(название, перевод)
	return текст


def переведимойкод(путь, язык):
	файл = codecs.open(путь, 'r+', 'utf-8')
	текст = файл.read()
	перевод = перевести_текст(текст, язык)
	файл.seek(0)
	файл.write(перевод)
	файл.truncate()
	файл.close()


def main():
	парсер = argparse.ArgumentParser(description='Translate your code v0.1')
	парсер.add_argument('files', metavar='files', type=str, nargs='+', help='files to parse')
	парсер.add_argument('-l', dest='language', default='', type=str,
	                    help='language to translate to. Omit to use random language per word.')

	аргументы = парсер.parse_args()
	if len(аргументы.files) < 1:
		парсер.print_usage()
		return

	for файл in аргументы.files:
		переведимойкод(файл, аргументы.language)


if __name__ == '__main__':
	main()