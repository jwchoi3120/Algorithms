import unittest


class TestApplication(unittest.TestCase):

    def test_1(self):
        from hashtable import HashTable, HashNode, word_frequency

        string = "chefallfall"
        dictionary = ['chef', 'all', 'fall', 'a']

        table = HashTable()
        table = word_frequency(string, dictionary, table)
        solution = [None, HashNode('all', 1), None, None, None, None, None, None, HashNode('a', 0), None, None, None,
                    None, None, HashNode('chef', 1), HashNode('fall', 1)]

        print(solution)
        assert (solution == table.table)
        print(table)



    def test_2(self):
        from hashtable import HashTable, HashNode, word_frequency

        # Frank Ocean - Thinking bout you
        string = """atornadoflewaroundmyroombeforeyoucame"""
        dictionary = {'a': 1, 'tornado': 1, 'flew': 1, 'around': 1, 'my': 1, 'room': 1, 'before': 1, 'you': 1,
                      'came': 1}
        table = HashTable()
        table = word_frequency(string, dictionary.keys(), table)

        for word, count in dictionary.items():
            assert (table[word].value == count)
        print(table)

    def test_3(self):
        from hashtable import HashTable, HashNode, word_frequency

        # Isaac Asimov - The last question
        # https://www.multivax.com/last_question.html
        string = """thelastquestionwasaskedforthefirsttimehalfinjestonmay212061atatimewhenhumanityfirststeppedintothelightthequestioncameaboutasaresultofafivedollarbetoverhighballsandithappenedthiswayalexanderadellandbertramlupovweretwoofthefaithfulattendantsofmultivacaswellasanyhumanbeingscouldtheyknewwhatlaybehindthecoldclickingflashingfacemilesandmilesoffaceofthatgiantcomputertheyhadatleastavaguenotionofthegeneralplanofrelaysandcircuitsthathadlongsincegrownpastthepointwhereanysinglehumancouldpossiblyhaveafirmgraspofthewholemultivacwasselfadjustingandselfcorrecting"""
        dictionary = {'the': 9, 'last': 1, 'question': 2, 'was': 2, 'asked': 1, 'for': 1, 'first': 2, 'time': 2, 'half': 1, 'in': 1, 'jest': 1, 'on': 1, 'may': 1, '21': 1, '2061': 1, 'at': 2, 'a': 5, 'when': 1, 'humanity': 1, 'stepped': 1, 'into': 1, 'light': 1, 'came': 1, 'about': 1, 'as': 3, 'result': 1, 'of': 8, 'five': 1, 'dollar': 1, 'bet': 1, 'over': 1, 'highballs': 1, 'and': 5, 'it': 1, 'happened': 1, 'this': 1, 'wayalexander': 1, 'adell': 1, 'bertram': 1, 'lupov': 1, 'were': 1, 'two': 1, 'faithful': 1, 'attendants': 1, 'multivac': 1, 'well': 1, 'any': 2, 'human': 2, 'beings': 1, 'could': 2, 'they': 2, 'knew': 1, 'what': 1, 'lay': 1, 'behind': 1, 'cold': 1, 'clicking': 1, 'flashing': 1, 'face': 2, 'miles': 2, 'that': 2, 'giant': 1, 'computer': 1, 'had': 2, 'least': 1, 'vague': 1, 'notion': 1, 'general': 1, 'plan': 1, 'relays': 1, 'circuits': 1, 'long': 1, 'since': 1, 'grown': 1, 'past': 1, 'point': 1, 'where': 1, 'single': 1, 'possibly': 1, 'have': 1, 'firm': 1, 'grasp': 1, 'wholemultivac': 1, 'selfadjusting': 1, 'selfcorrecting': 1}

        table = HashTable()
        table = word_frequency(string, dictionary.keys(), table)

        for word, count in dictionary.items():
            assert (table[word].value == count)
        print(table)

if __name__ == "__main__":
    unittest.main()