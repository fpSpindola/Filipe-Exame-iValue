__author__ = 'Filipe P. Spindola'

import requests


class Questao1:
    def __init__(self):
        self.foo = ['t', 's', 'w', 'l', 'h']
        self.raw_text1 = 'https://raw.github.com/I-Value/ExameIValue/master/textoA.txt'
        self.raw_text2 = 'https://raw.github.com/I-Value/ExameIValue/master/textoB.txt'
        self.prep_text_1 = []
        self.prep_text_2 = []

    def process_text_1(self, text):

        text1 = requests.get(text).content.decode().split()
        for word in text1:
            if len(word) == 3 and word[-1:] in self.foo and 'm' not in word:
                self.prep_text_1.append(word)
        return len(self.prep_text_1)

    def process_text_2(self, text):

        text2 = requests.get(text).content.decode().split()
        for word in text2:
            if len(word) == 3 and word[-1:] in self.foo and 'm' not in word:
                self.prep_text_2.append(word)
        return len(self.prep_text_2)

if __name__ == '__main__':
    cl = Questao1()
    ret_text_1 = cl.process_text_1(cl.raw_text1)
    ret_text_2 = cl.process_text_2(cl.raw_text2)
    print('The first text has {0}'.format(ret_text_1), 'prepositions')
    print('The second text has {0}'.format(ret_text_2), 'prepositions')