import sqlite3

conn = sqlite3.connect("CMS.db")
c = conn.cursor()
c.execute("""
        CREATE TABLE cms_login(
            ID INT PRIMARY KEY NOT NULL,
            USERNAME       TEXT  NOT NULL,
            PASSWORD       TEXT  NOT NULL,
            CASENAME       TEXT
        )

""")
# c.execute("""
#             create table
#         """)
conn.commit()
conn.close()