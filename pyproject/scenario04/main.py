import ccircle
import connection
from math import*

con = connection.create()
d = {
    aa: 10,
    bb: -50000000000000000
}

while True:
    con.send('set_name', {'name': 'undefined'})
    #con.send('get_player_id_by_name': {'qwertyuiop'})
    con.send('send_money', d)

# Write code to make money and kill the evil cat!
# See readme.txt !