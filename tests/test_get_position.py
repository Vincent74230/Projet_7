"""module that tests if request from Get_position is ok"""
from grandpy.get_position import Get_position



def test_get_position_return_correct_datas(monkeypatch):
    """Test that mimics the request.get in Get_position class"""
    class MockRequestsGet:
        def __init__(self, url, params=None):
            self.status_code = 200
        def json(self):
            return {
                'results':[{'formatted_address':'Champs de mars, 5 Avenue Anatole France, 75007 Paris, France', 
                'geometry':{'location':{'lat': 48.85837009999999, 'lng': 2.2944813}}}]}

    test_get_position = Get_position()

    monkeypatch.setattr('grandpy.get_position.requests.get', MockRequestsGet)

    assert test_get_position.send_request('tour eiffel') == {'address':'Champs de mars, 5 Avenue Anatole France, 75007 Paris, France', 
                                                             'position':{'lat': 48.85837009999999, 'lng': 2.2944813}}
