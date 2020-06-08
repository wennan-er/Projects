from flask import Flask
from flask import render_template, request, jsonify
import json
import sql_interface as sql_int
import sys
import mongo_interface as mon_int

# OS = 1

app = Flask(__name__)

@app.route('/')
def home():
    # return render_template('index.html', opsys=OS)
    return render_template('index.html')

@app.route('/create.html')
def create_html():
    return render_template('create.html')

@app.route('/login.html')
def login_html():
    return render_template('login.html')

@app.route('/search.html')
def search_html():
    return render_template('search.html')

@app.route('/settings.html')
def settings_html():
    return render_template('settings.html')

@app.route('/events.html')
def events_html():
    return render_template('events.html')

@app.route('/MyEvents.html')
def my_events_html():
    return render_template('MyEvents.html')

@app.route('/create_event', methods=['POST'])
def make_event():
    print("endpoint")
    data = json.loads(request.data)
    print(data)
    value = mon_int.create_event(data)
    return jsonify({"value": value})

@app.route('/delete_event', methods=['POST'])
def del_event():
    data = json.loads(request.data)
    print(data)
    value = mon_int.delete_event(data["id"])
    return jsonify({"value": value})

@app.route('/search_event', methods=['POST'])
def search_event():
    data = json.loads(request.data)
    results = mon_int.search_tags(data["query"])
    return results

@app.route('/get_all_events')
def get_all_events():
    results = mon_int.get_all_events()
    return results


@app.route('/create', methods=['POST'])
def create():
    data = json.loads(request.data)
    username = data['username'] + "_name"
    password = data['password']
    return jsonify({
        "username": username
    })

# create user with username and password
@app.route('/create_user', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    email = data['email']
    password = data['password']
    value = sql_int.create_user(email, password)
    return jsonify({
        "value": value
    })

@app.route('/get_all_users')
def get_all_users():
    results = sql_int.get_all_users()
    return results

# login
@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    email = data['email']
    password = data['password']

    value = sql_int.login(email, password)

    return jsonify({
        "value": value
    })

# get contact info
@app.route('/contact', methods = ['POST'])
def contact():
    data = json.loads(request.data)
    email = data['email']
    contact_info = sql_int.contact_info(email)

    return jsonify({
        "contacts": contact_info
    })

# add contact info
# delete contact info
# edit contact info
@app.route('/edit_contact', methods=['POST'])
def edit_contact():
    data = json.loads(request.data)
    email = data['email']
    edit = data['edit'] # either "add", "edit", "delete"
    oldval = data['oldval'] # if add, ""
    newval = data['newval'] # if delete, ""

    if edit == "add":
        value = sql_int.add_contact_info(email, newval)
    elif edit == "delete":
        value = sql_int.delete_contact_info(email, oldval)
    elif edit == "edit":
        value = sql_int.update_contact_info(email, oldval, newval)

    return jsonify({
        "value": value
    })


if __name__ == '__main__':
    # add code to startup the sql and nosql databases
    # if sys.platform == "linux":
    #    OS = 2
    app.run(debug=True)
