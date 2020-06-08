# CS411_ShArea

# Requirements
python3 
Flask
mongodb

# Running
[1] start mongodb

$ mkdir ./mongodata

$ mongod --dbpath ./mongodata

[2] start mongo server

$ python3 events.py 5001

[3] start server

$ python3 server.py



## Sql Database info
The following is the Code for the Databases. This was done through sqlite3

CREATE TABLE Location(address text PRIMARY KEY, name text, type text);

CREATE TABLE Event(id text PRIMARY KEY, startTime time, duration text, tags text);

CREATE TABLE EventHasALocation(Event_id text, Location_id text, 
  PRIMARY KEY(Event_id, Location_id),
  FOREIGN KEY(Event_id)
    REFERENCES Event(id)
    ON DELETE CASCADE,
  FOREIGN KEY(Location_id)
    REFERENCES Location(id)
    ON DELETE CASCADE);
    
CREATE TABLE User(email text NOT NULL, password text NOT NULL, Event_id text,
  PRIMARY KEY(email),
  FOREIGN KEY (Event_id)
    REFERENCES Event(id)
    ON DELETE CASCADE);
    
CREATE TABLE ContactMethod(User_username text, type text, info text,
  PRIMARY KEY(User_username),
  FOREIGN KEY(User_username) 
    REFERENCES User(email) 
    ON DELETE CASCADE);
