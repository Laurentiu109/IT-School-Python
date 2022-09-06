
def create_todo_table(con):

    cur = con.cursor()
    cur.execute("""
    INSERT INTO todos (title, body):
    """)