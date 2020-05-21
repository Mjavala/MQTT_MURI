import asyncio
import asyncpg
import time

#TODO: need to set up pw / env variables
# USER = '!--config--!'
# PW = '!--config--!'
DATABASE = 'muri'
HOST = "64.227.104.52"

class muri_db():
    def __init__(self):
        self.current_message = {}
                
        self.last_time = time.time()
        self.id = str
        self.alt = float
        self.rssi = int
        self.temp = float
        self.hum = float 

    async def run(self):
        try: 
            conn = await asyncpg.connect(user=USER, password=PW, database=DATABASE, host=HOST)
            await conn.execute(
                '''
                    INSERT INTO muri_data VALUES (NOW(), $1, $2, $3, $4, $5)
                ''', self.id, self.alt, self.rssi, self.temp, self.hum)
            await conn.close()

        except Exception as e:
            print('error error!')
            print(e)

    def msg_in(self, payload):
        self.current_message = payload


    def stat_update(self):
        self.id = self.current_message['mqtt']['device_id']
        self.alt = self.current_message['mqtt']['altitude']
        self.rssi = self.current_message['mqtt']['rssi']
        self.temp = self.current_message['mqtt']['temperature']
        self.hum = self.current_message['mqtt']['humidity']

    async def main_loop(self):
        last_time = time.time()

        while(True):
            if (time.time() - last_time > 5): 
                last_time = time.time()
                if self.current_message['mqtt'] != {}:
                    self.stat_update()
                    await self.run()

            await asyncio.sleep(0.1)

if __name__ == "__main__":
    db_conn =  muri_db()

    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.ensure_future(db_conn.main_loop()))