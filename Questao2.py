__author__ = 'Filipe P. Spindola'

import requests

class Questao2:
    def __init__(self):
        self.foo = ['t', 's', 'w', 'l', 'h']
        self.raw_text1 = 'https://raw.github.com/I-Value/ExameIValue/master/textoA.txt'
        self.raw_text2 = 'https://raw.github.com/I-Value/ExameIValue/master/textoB.txt'

    def process_text_1(self, text):

        verbs = []
        first_person_verbs = []
        text1 = requests.get(text).content.decode().split()

        for word in text1:
            if len(word) >= 8 and word[-1:] in self.foo:
                verbs.append(word)
                if word[:1] in self.foo:
                    first_person_verbs.append(word)
        return len(verbs), len(first_person_verbs)

    def process_text_2(self, text):

        verbs = []
        first_person_verbs = []
        text2 = requests.get(text).content.decode().split()

        for word in text2:
            if len(word) >= 8 and word[-1:] in self.foo:
                verbs.append(word)
                if word[:1] in self.foo:
                    first_person_verbs.append(word)
        return len(verbs), len(first_person_verbs)


if __name__ == '__main__':
    cl = Questao2()
    ret_text_1 = cl.process_text_1(cl.raw_text1)
    ret_text_2 = cl.process_text_2(cl.raw_text2)
    print('The first text has {0} verbs and {1} first person verbs'.format(ret_text_1[0], ret_text_1[1]))
    print('The second text has {0} verbs and {1} first person verbs'.format(ret_text_2[0], ret_text_2[1]))







