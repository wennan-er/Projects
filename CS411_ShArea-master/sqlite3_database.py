import sqlite3

def create_database(db_file):

    connection = create_connection(db_file)
    cursor = connection.cursor()

    event = '''CREATE TABLE Event(id text PRIMARY KEY, startTime time, duration text, tags text);'''
    cursor.execute(event)

    user = '''  CREATE TABLE User(email text NOT NULL, password text NOT NULL, Event_id text,
                PRIMARY KEY(email),
                FOREIGN KEY (Event_id) REFERENCES Event(id) ON DELETE CASCADE);'''
    cursor.execute(user)

    location = "CREATE TABLE Location(address text PRIMARY KEY, name text, type text);"
    cursor.execute(location)

    contact_method = ''' CREATE TABLE ContactMethod(User_username text NOT NULL, info text,
                         FOREIGN KEY(User_username) REFERENCES User(email) ON DELETE CASCADE);'''
    cursor.execute(contact_method)


    event_has_a_location = ''' CREATE TABLE EventHasALocation(Event_id text, Location_id text,
                               PRIMARY KEY(Event_id, Location_id),
                               FOREIGN KEY(Event_id) REFERENCES Event(id) ON DELETE CASCADE,
                               FOREIGN KEY(Location_id) REFERENCES Location(id) ON DELETE CASCADE);'''
    cursor.execute(event_has_a_location)

    connection.commit()
    connection.close()


def create_connection(db_file):

    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as error:
        print(error)
    return connection
