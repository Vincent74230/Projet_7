from grandpy.parser import parser

class Test_parser:
    """this class tests the parser that 'cleans' user's question"""
    def test_single_word_response(self):
        magic_word = []
        magic_word.append(parser("Grandpy tell me about paris"))
        assert len(magic_word) == 1

    def test_correct_word_response(self):
        magic_word = ''
        magic_word = parser("Grandpy what is the address of openclassrooms ?")
        assert magic_word == "openclassrooms"