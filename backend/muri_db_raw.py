import asyncio
import asyncpg
import time
import logging
import os
from os.path import join, dirname
from dotenv import load_dotenv
import muri_app_log as muri_app_log

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USER = os.getenv('DB_USER')
PW = os.getenv('DB_PASSWORD')
DATABASE = os.getenv('DB_NAME')
#   Note diff host from muri_db
HOST = os.getenv('DB_HOST_RAW')

class muri_db_raw():
    def __init__(self):
        self.current_message = {}

        self.app_log_setup = muri_app_log.main_app_logs()
        self.logger = logging.getLogger('app')

    async def run_0xd2a8(self):
        try: 
            self.logger.info('--- Writing Data to Raw database (0xd2a8) ---')
            conn = await asyncpg.connect(user=USER, password=PW, database=DATABASE, host=HOST)
            query = '''
                        INSERT INTO "0xd2a8_raw" VALUES ($1, $2)
                    '''
            values = self.stat_update_0xd2a8()
            print('0xd2a8 %s' % values)

            await conn.execute(query, *values)

            await conn.close()

        except Exception as e:
            self.logger.log_app("Exception in Database (0xd2a8) Connection Script: %s" % e)

    async def run_0xc109(self):
        try: 
            self.logger.log_app('--- Writing Data to Raw database (0xc109) ---')
            conn = await asyncpg.connect(user=USER, password=PW, database=DATABASE, host=HOST)
            query = '''
                        INSERT INTO "0xC109_raw" VALUES ($1, $2)
                    '''
            values = self.stat_update_0xc109()
            print('0xc109 %s' % values)
            print(*values)

            await conn.execute(query, *values)

            await conn.close()

        except Exception as e:
            self.logger.log_app("Exception in Database (0xc109) Connection Script: %s" % e)

    def msg_in(self, payload):
        self.current_message = payload
        self.message_type = payload['data']['FRAME_TYPE']


    def stat_update_0xc109(self):
        try:
            msg_obj = [
                self.current_message['station'],
                self.current_message['receiver']
            ]
        except Exception as e:
            self.logger.log_app("Exception in parsing 0xc109 message field: %s" % e)

        return msg_obj


    def stat_update_0xd2a8(self):
        try:
            msg_obj = [
                self.current_message['station'],
                self.current_message['receiver']
            ]
        except Exception as e:
            self.logger.log_app("Exception in parsing 0xc109 message field: %s" % e)

        return msg_obj

    async def main_loop(self):
        last_time = time.time()
        self.logger.log_app('--- Raw database service started succesfully ---')
        try:
            while(True):
                if (time.time() - last_time > 5): 
                    last_time = time.time()

                    if self.message_type == '0xd2a8':
                        self.stat_update_0xd2a8()

                        await self.run_0xd2a8()
                        continue

                    if self.message_type == '0xc109':
                        self.stat_update_0xc109()

                        await self.run_0xc109()
                        continue
                    else:
                        pass


                await asyncio.sleep(0.1)

        except Exception as e:
            self.logger.log_app("Exception in raw database service: %s" % e)


if __name__ == "__main__":
    db_conn =  muri_db_raw()

    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.ensure_future(db_conn.main_loop()))