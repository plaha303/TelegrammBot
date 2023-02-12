import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('fuelBot.db')
    cur = base.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS user_info('
        'user_id INTEGER PRIMARY KEY,'
        'user_name TEXT,'
        'car TEXT,'
        'fuel TEXT,'
        'money TEXT)')
    base.commit()

async def sql_add_command(state, user_id):
    async with state.proxy() as data:
        cur.execute(f'SELECT user_id FROM user_info WHERE user_id = {user_id}')
        exam = cur.fetchone()
        if exam is None:
            cur.execute('INSERT INTO user_info VALUES (?, ?, ?, ?, ?)', tuple(data.values()))
            base.commit()
