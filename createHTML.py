
import webbrowser

f = open('1.html','w')

message = """

<html>
    <head>
        <title>
            Gotcha!
        </title>
    </head>
    <body>
        <h1>
            Stay tuned for our amazing summer sale!
        </h1>
    </body>    
</html>
"""

f.write(message)
f.close()
webbrowser.open_new_tab('1.html')
