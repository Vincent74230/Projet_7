from grandpy.parser import parser

class Test_parser:
    """this class tests the parser that 'cleans' user's question"""

    def test_correct_one_word_response(self):#it must return a single word in a string
        magic_word = ''
        magic_word = parser("Grandpy what is the address of openclassrooms ?")
        assert magic_word == "openclassrooms"

    def test_correct_two_words_response(self):#the same but must return 3 words
        magic_words=''
        magic_words=parser("Tell me about the arc de triomphe GrandPy please")
        assert magic_words == "arc de triomphe"
"""
    def test_no_special_characters(self):
        magic_words=''
        magic_words=parser("'&-()$^ù%*!;,:")
"""