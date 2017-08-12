import sqlite3

sqlite_file = 'timeline_db.sqlite'
table_name = 'my_table'  # name of the table to be created
new_field = 'my_1st_column' # name of the column
field_type = 'REAL'  # column data type

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('CREATE TABLE {tn} ({nf} {ft})'\
            .format(tn = table_name, nf = new_field, ft = field_type))

conn.commit()
conn.close()
