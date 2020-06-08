import sqlite3
import sql_interface as sq
import sqlite3_database as sqldb

# What Has been Tests:
# create_user(email, password)
# login(email, password)
# add_contact_info(email, value)
# contact_info(email)
# delete_contact_info(email, info)
# update_contact_info(email, oldval, newval)


def main():
    # sp.create_user("test@illinois.edu", "password")
    # print(sp.login("test@illinois.edu", "password"))
    # sp.add_contact_info("test@illinois.edu", "Twitter", "@test")
    #
    #

    # Testing for create_user(email, password)
    # sqldb.create_database('sql_database.db')
    # print(sq.create_user("test@illinois.edu", "password"))
    # print(sq.create_user("test2@illinois.edu", "password2"))

    # Testing for login(email, password)
    # print(sq.login("test@illinois.edu", "password"))
    # print(sq.login("test2@illinois.edu", "password2"))

    # connection = sq.create_connection()
    # cursor = connection.cursor()
    # contact_method = ''' CREATE TABLE ContactMethod(User_username text NOT NULL, info text,
    #                      FOREIGN KEY(User_username) REFERENCES User(email) ON DELETE CASCADE);'''
    # cursor.execute(contact_method)
    # connection.commit()
    # connection.close()

    # Testing for contact_info(email)
    # print(sq.delete_contact_info("test@illinois.edu", "IG:@test"))
    # print(sq.contact_info("test@illinois.edu"))
    #print(sq.contact_info("test2@illinois.edu"))

    # Testing for update_contact_info
    # print(sq.update_contact_info("test@illinois.edu", "Twitter:@test", "IG:@test"))
    # print(sq.contact_info("test@illinois.edu"))

    # print(sq.add_contact_info("test@illinois.edu", "IG:@test"))

    # sql = "SELECT * FROM ContactMethod"
    # sql_funct(sql)

    # sq.get_all_users()
    # user_list = ['demo1test@demo.org', 't1000estuser1000', 'testuser10', 'testuser1000']

    # sql = "DELETE FROM ContactMethod WHERE User_username = 'demo1test@demo.org'"

    sql = "SELECT * FROM User"
    sql = "SELECT * FROM ContactMethod"
    print (sql_funct(sql))

    # print(sq.get_all_users())

    # for user in user_list:
    #     print(sq.contact_info(user))

def sql_funct(sql):
    connection = sq.create_connection()
    cursor = connection.cursor()
    result = cursor.execute(sql).fetchall()
    print(result)
    connection.close()

if __name__ == "__main__":
    main()
