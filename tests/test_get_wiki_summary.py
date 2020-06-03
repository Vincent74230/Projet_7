#coding utf-8
from grandpy.get_wiki_summary import get_wiki_summary

def test_get_wiki_summary_return_correct_datas(monkeypatch):
    class MockRequestsGet:
        def __init__(self, url, params=None):
            self.status_code = 200

        def json (self):
            return {'query':{'pages':{777:{'extract': "The Eiffel Tower ( EYE-fəl; French: tour Eiffel [tuʁ‿ɛfɛl] (listen)) is a wrought-iron lattice tower on the Champ de Mars in Paris, France."}}}}

    monkeypatch.setattr('grandpy.get_wiki_summary.requests.get', MockRequestsGet)
    assert get_wiki_summary('eiffel tower') == "The Eiffel Tower ( EYE-fəl; French: tour Eiffel [tuʁ‿ɛfɛl] (listen)) is a wrought-iron lattice tower on the Champ de Mars in Paris, France."