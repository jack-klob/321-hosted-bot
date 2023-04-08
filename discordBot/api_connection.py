import requests

class APIConnection():
    '''
    a small API wrapper to mimic commands from the
    testing bot server. needed to aquire id's of tasks
    created through the BDD tests
    '''

    # the server id of the testing server
    _guild_id = 1094137227484856360

    # url where backend is hosted
    _baseurl =  'http://127.0.0.1:8000'

    @classmethod
    def create_task(cls, title):
        url = cls._baseurl + "/task"
        return requests.post(url=url, data={"title": title, 'guild' : cls._guild_id})
    
    @classmethod
    def get_list(cls):
        url = f'{cls._baseurl}/task?guild={cls._guild_id}'
        return requests.get(url=url) 
    
    @classmethod
    def get_task(cls, id):
        url = f'{cls._baseurl}/task/{id}'
        return requests.get(url=url)
        