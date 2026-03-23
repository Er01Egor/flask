if False:
    name_db = 'db/mars_explorer.db'
else:
    name_db = input()
global_init(name_db)
db_sess = create_session()
for user in db_sess.query(User).all():
    if user.address == 'module_1':
        if user.speciality != 'engineer' or user.position != 'engineer':
            print(user.id)
