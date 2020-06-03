from grandpy.parser import parser

class Test_parser:
    """this class tests the parser that 'cleans' user's question"""

    def test_one_word_response(self):#it must return a single word in a string
        magic_word = parser("Grandpy what is the address of openclassrooms ?")
        assert magic_word == "openclassrooms"

    def test_tree_words_response(self):#must return 3 words
        magic_words=parser("Tell me about the arc de triomphe GrandPy please")
        assert magic_words == "arc de triomphe"
"""
    def test_no_special_characters(self):#must return a 'clean' sentence with no punctuation
        magic_words=parser("Hello GrandPy, can you tell me about the gizah pyramids? `,~,!,@,#,$,%,^,&,*,(,),_,-,+,=,{,[,},},|,:,;,',<>,.,?,/#")
        assert magic_words == "gizah pyramids"

    def test_no_unuseful_spaces(self):#tests if parser returns a sentence with no unuseful spaces
        magic_words=parser("Hello Grandpy, where is the san       Francisco              golden gate    ? ")
        assert magic_words == "san francisco golden gate"

    def test_empty_sentence(self):#tests if parser returns None if user's question is empty
        magic_words=parser("")
        assert magic_words==None

    def test_no_numbers(self):#obvious purpuse : numbers not allowed in user's question..
        magic_words=parser("Hi grandpy, who lives on the 3223 columbia street in V5J 1A1 Vancouver, CA ?")
        assert magic_words == "vancouver"

    def test_no_single_letter(self):#single letters : destroy them with lasers!!
        magic_words=parser("Hi grandpy, a b  c  d  e  A Z O    P washington")
        assert magic_words == "washington"
"""