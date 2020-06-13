#coding utf-8
from grandpy.get_wiki_summary import Get_wiki_summary

def test_get_wiki_summary_return_correct_datas(monkeypatch):
    class MockRequestsGet:
        def __init__(self, url, params=None):
            self.status_code = 200

        def json (self):
            return {'query':{'pages':{777:{'extract': "The Eiffel Tower ( EYE-fəl; French: tour Eiffel [tuʁ‿ɛfɛl] (listen)) is a wrought-iron lattice tower on the Champ de Mars in Paris, France."}}}}
    
    test_wiki_summary = Get_wiki_summary()

    monkeypatch.setattr('grandpy.get_wiki_summary.requests.get', MockRequestsGet)
    assert test_wiki_summary.send_request('eiffel tower') == "The Eiffel Tower ( EYE-fəl; French: tour Eiffel [tuʁ‿ɛfɛl] (listen)) is a wrought-iron lattice tower on the Champ de Mars in Paris, France."
