# Translate My Code v0.1

Did you know that EcmaScript languages(JavaScript and ActionScript for example)
support unicode variable, function and class names? Now nothing stops you
from writing all your variables names in Korean, function names in Chinese and Class names in Russian.

But what if you already have a huge project that you want to convert to different language?
Fear not my friend, as this Python script will let you translate your code using Google Translate
into any language or even multiple languages at once!

## Setup

Requires Python 3

Required modules:

* futures 2.1.6
* goslate 1.1.2
* regex 2014.02.19

Quick Setup

1. Get Python 3
2. (Optionally) Install `virtualenv` - http://www.virtualenv.org/
3. Install all required modules from `requirements.txt` using `pip install -r requirements.txt`

## Usage
* `py -3 translatemycode.py fileWithCode.as otherFileWithCode.js -l language`
* Don't specify `-l` to use random language for each word.

## Helping develop this script

Pull requests are welcomed, as long as variable names are not in English.