import sqlite3


class Conndb:

    def __int__(self, db_path="database.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        #self.exec_schema()


    # def get_db(self):
    #     db = getattr(g, '_database', None)
    #     if db is None:
    #         db = g._database = sqlite3.connect(self.db_path)
    #     return db


    #
    # @g.teardown_appcontext
    # def close_connection(exception):
    #     db = getattr(g, '_database', None)
    #     if db is not None:
    #         db.close()
    #
    # def exec_schema(self):
    #     db = self.get_db()
    #     with g.open_resource('schema.sql') as f:
    #         db.executescript(f.read().decode('utf8'))

    # def init_servce(g):
    #     g.teardown_appcontext(close_db)
    #     g.cli.add_command(init_db_command)
    #

    # '''executa SQL'''
    # def executSQL(self, stringSQL, args):
    #     con = self.get_db()
    #     cur = con.cursor()
    #     cur.execute(stringSQL, args)
    #     con.commit()
