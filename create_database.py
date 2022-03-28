import sqlite3

conn = sqlite3.connect('new.db')


#create table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_stuff( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        fileName TEXT \
        )")
    conn.commit()


#tuple of files
fileList = ('informaton.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


conn = sqlite3.connect('new.db')

#goes through 'fileList' and prints items that end with '.txt'
for item in fileList:
    if item.endswith(".txt"):
        with conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO tbl_stuff (fileName) VALUES(?)',(item,))
            print(item)

conn.close()
        
