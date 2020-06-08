import requests


url = "http://127.0.0.1:5001/event"

def create_event(data):
    try:
        idx, st, duration, tags = data['id'], data['start_time'], data['duration'], data['tags']
    except KeyError:
        return "failure"
    
    tags = [tag.lower() for tag in tags]

    params = {'id':idx, 'start_time':st, 'duration':duration, 'tags':tags}
    
    print(params)
    r = requests.post(url=url, json=params)
    return "success"

def get_all_events():
    r = requests.get(url=url)
    #print(r)
    return r.json()

def delete_event(event_id):
    url_del = url+"/"+event_id
    r = requests.delete(url=url_del)
    return "success"

def search_tags(tag):
    urltag = url+"tag/"+tag
    r = requests.get(urltag)
    print(urltag)
    return r.json()
