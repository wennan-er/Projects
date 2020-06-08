from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_restful import Resource, Api
import sys

app = Flask(__name__)
api = Api(app)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

app.url_map.strict_slashes = False # Disable redirecting on POST method from /event to /event/

mongo = PyMongo(app)

# find event by id
class Event(Resource):
     def get(self, _id):
        myevent = mongo.db.events
        e = myevent.find_one({'id' : _id})
        if e:
            output = {'id' : e['id'], 'start_time' : e['start_time'], 'duration':e['duration'], 'tags':e['tags']}
        else:
            output = "No such event"
        return jsonify({'id' : e['id'], 'start_time' : e['start_time'], 'duration':e['duration'], 'tags':e['tags']})
    
     def delete(self,_id):
        events = mongo.db.events
        e = events.find_one({'id' : _id})
        if e:
            events.remove({'id' : _id})
            return jsonify({'result' : "Delete successfully"})
        else:
            return jsonify({'result' : "Nothing to delete"})


# advanced function find by tag
class Eventtag(Resource):
    def get(self, _tag):
        events = mongo.db.events
        output = []
        # make lowercase 
        _tag = _tag.lower()
        for e in events.find({'tags' : _tag}):
            output.append({'id' : e['id'], 'start_time' : e['start_time'], 'duration':e['duration'], 'tags':e['tags']})
        return jsonify({'result' : output})
    
   
class EventList(Resource):
    
    def get(self):
        events = mongo.db.events
        output = []
        for e in events.find():
            output.append ({'id' : e['id'], 'start_time' : e['start_time'], 'duration':e['duration'], 'tags':e['tags']})
        return jsonify({'result' : output})

    

    def post(self):
        events = mongo.db.events
        _id = request.json['id']
        _start_time = request.json['start_time']
        _duration = request.json['duration']
        _tags = request.json['tags']
        
        # if the id exist, do not add that event
        e = events.find_one({'id' : _id})
        if e:
            return jsonify({'result' : "The id exists, could not be added!"})
        output = {'id' : _id, 'start_time' : _start_time, 'duration':_duration, 'tags':_tags}
        event_id = events.insert(output)

        return jsonify({'id' : _id, 'start_time' : _start_time, 'duration':_duration, 'tags':_tags})


api.add_resource(EventList, '/event')
api.add_resource(Event, '/event/<string:_id>')
api.add_resource(Eventtag, '/eventtag/<string:_tag>')


if __name__ == '__main__':
    port = 5000
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    app.run(debug=True, port=port)
