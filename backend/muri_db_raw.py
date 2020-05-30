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
            self.logger.info('--- Writing Data to Raw database ---')
            conn = await asyncpg.connect(user=USER, password=PW, database=DATABASE, host=HOST)
            query = '''
                    INSERT INTO 0xd2a8_raw VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15,
                    $16, $17, $18, $19, $20, $21, $22, $23, $24, $25, $26, $27, $28, $29, $30,
                    $31, $32, $33, $34, $35, $36, $37, $38, $39, $40, $41, $42, $43)
                    '''
            values = self.stat_update_0xd2a8()

            await conn.execute(query, *values)

            await conn.close()

        except Exception as e:
            self.logger.log_app("Exception in Database (0xd2a8) Connection Script: %s" % e)

    async def run_0xd2a8(self):
        try: 
            self.logger.log_app('--- Writing Data to Raw database ---')
            conn = await asyncpg.connect(user=USER, password=PW, database=DATABASE, host=HOST)
            query = '''
                    INSERT INTO 0xd2a8_raw VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15,
                    $16, $17, $18, $19, $20, $21, $22, $23, $24, $25, $26, $27, $28, $29, $30,
                    $31, $32, $33, $34, $35, $36, $37, $38, $39, $40, $41, $42, $43, $44, $45)
                    '''
            values = self.stat_update_0xC109()

            await conn.execute(query, *values)

            await conn.close()

        except Exception as e:
            self.logger.log_app("Exception in Database (0xd2a8) Connection Script: %s" % e)

    def msg_in(self, payload):
        self.current_message = payload


    def stat_update_0xC109(self):
        msg_obj = {
            self.station:  self.current_message['station'],
            self.receiver:  self.current_message['receiver'],
            self.timestamp: self.current_message['data']['TIMESTAMP'],
            self.address:  self.current_message['data']['ADDR_FROM'],
            self.rssi: self.current_message['data']['RSSI_RX'],
            self.frame_type: self.current_message['data']['FRAME_TYPE'],
            self.frame_cnt: self.current_message['data']['FRAME_CNT'],
            self.frame: self.current_message['data']['FRAME'],
            self.packet_id: self.current_message['data']['frame_data']['packet_id'],
            self.packet_num: self.current_message['data']['frame_data']['packet_num'],
            self.epoch_index: self.current_message['data']['frame_data']['epoch index'],
            self.interval_index: self.current_message['data']['frame_data']['interval index'],
            self.gps_lat: self.current_message['data']['frame_data']['gps_lat'],
            self.gps_lon: self.current_message['data']['frame_data']['gps_lon'],
            self.gps_alt: self.current_message['data']['frame_data']['gps_alt'],
            self.gps_tow: self.current_message['data']['frame_data']['gps_tow'],
            self.gps_fix: self.current_message['data']['frame_data']['gps_fix'],
            self.gps_numsats: self.current_message['data']['frame_data']['gps_numsats'],
            self.cw_sa_0: self.current_message['data']['frame_data']['CW SA 0'],
            self.cw_sa_1: self.current_message['data']['frame_data']['CW SA 1'],
            self.cw_sa_2: self.current_message['data']['frame_data']['CW SA 2'],
            self.cw_sa_3: self.current_message['data']['frame_data']['CW SA 3'],
            self.cw_sa_4: self.current_message['data']['frame_data']['CW SA 4'],
            self.cw_sa_5: self.current_message['data']['frame_data']['CW SA 5'],
            self.cw_sa_6: self.current_message['data']['frame_data']['CW SA 6'],
            self.cw_sa_7: self.current_message['data']['frame_data']['CW SA 7'],
            self.cw_sa_8: self.current_message['data']['frame_data']['CW SA 8'],
            self.hw_sa_0: self.current_message['data']['frame_data']['HW SA 0'],
            self.hw_sa_1: self.current_message['data']['frame_data']['HW SA 1'],
            self.hw_sa_2: self.current_message['data']['frame_data']['HW SA 2'],
            self.hw_sa_3: self.current_message['data']['frame_data']['HW SA 3'],
            self.hw_sa_4: self.current_message['data']['frame_data']['HW SA 4'],
            self.hw_sa_5: self.current_message['data']['frame_data']['HW SA 5'],
            self.hw_sa_6: self.current_message['data']['frame_data']['HW SA 6'],
            self.hw_sa_7: self.current_message['data']['frame_data']['HW SA 7'],
            self.hw_sa_8: self.current_message['data']['frame_data']['HW SA 8'],
            self.cw_meas_vr1: self.current_message['data']['frame_data']['CW Meas Vr1'],
            self.cw_meas_vr2: self.current_message['data']['frame_data']['CWMeas Vr2'],
            self.cw_meas_vo1: self.current_message['data']['frame_data']['CW Meas Vo1'],
            self.cw_meas_vo2: self.current_message['data']['frame_data']['CWMeas Vo2'],
            self.cw_meas_cpot: self.current_message['data']['frame_data']['CW Meas Cpot'],
            self.cw_meas_gpot: self.current_message['data']['frame_data']['CW Meas Gpot'],
            self.hw_meas_vr1: self.current_message['data']['frame_data']['HW Meas Vr1'],
            self.hw_meas_vr2: self.current_message['data']['frame_data']['HW Meas Vr2'],
            self.hw_meas_vo1: self.current_message['data']['frame_data']['HW Meas Vo1'],
            self.hw_meas_vo2: self.current_message['data']['frame_data']['HW Meas Vo2']
        }
        return msg_obj


    def stat_update_0xd2a8(self):
        msg_obj = {
        self.station: self.current_message['station'],
        self.receiver: self.current_message['receiver'],
        self.timestamp: self.current_message['data']['TIMESTAMP'],
        self.address: self.current_message['data']['ADDR_FROM'],
        self.rssi: self.current_message['data']['RSSI_RX'],
        self.frame_type: self.current_message['data']['FRAME_TYPE'],
        self.frame_cnt: self.current_message['data']['FRAME_CNT'],
        self.frame: self.current_message['data']['FRAME'],
        self.packet_id: self.current_message['data']['frame_data']['packet_id'],
        self.packet_num: self.current_message['data']['frame_data']['packet_num'],
        self.epoch_index: self.current_message['data']['frame_data']['epoch index'],
        self.gps_lat: self.current_message['data']['frame_data']['gps_lat'],
        self.gps_lon: self.current_message['data']['frame_data']['gps_lon'],
        self.gps_alt: self.current_message['data']['frame_data']['gps_alt'],
        self.gps_tow: self.current_message['data']['frame_data']['gps_tow'],
        self.gps_fix: self.current_message['data']['frame_data']['gps_fix'],
        self.gps_numsats: self.current_message['data']['frame_data']['gps_numsats'],
        self.batt: self.current_message['data']['frame_data']['Batt Mon'],
        self.gondola: self.current_message['data']['frame_data']['Gondola Statu'],
        self.rs41_temp: self.current_message['data']['frame_data']['RS41 Temp'],
        self.rs41_hum: self.current_message['data']['frame_data']['RS41 Hum'],
        self.rs41_pres: self.current_message['data']['frame_data']['RS41 Pres'],
        self.ta1: self.current_message['data']['frame_data']['temp Ta1 (amb)'],
        self.ti1: self.current_message['data']['frame_data']['temp Ti1 (int)'],
        self.ta2: self.current_message['data']['frame_data']['temp Ta2 (amb)'],
        self.ti2: self.current_message['data']['frame_data']['temp Ti2 (int)'],
        self.cw_chop_vr1: self.current_message['data']['frame_data']['CW Chop Vr1'],
        self.cw_chop_vr2: self.current_message['data']['frame_data']['CW Chop Vr2'],
        self.cw_chop_vo1: self.current_message['data']['frame_data']['CW Chop Vo1'],
        self.cw_chop_vo2: self.current_message['data']['frame_data']['CW Chop Vo2'],
        self.cw_chop_cpot: self.current_message['data']['frame_data']['CW Chop Cpot'],
        self.cw_chop_gpot: self.current_message['data']['frame_data']['CW Chop Gpot'],
        self.gps_veln: self.current_message['data']['frame_data']['gps_veln'],
        self.gps_vele: self.current_message['data']['frame_data']['gps_vele'],
        self.gps_vel_d: self.current_message['data']['frame_data']['gps_vel_d'],
        self.hw_chop_vr1: self.current_message['data']['frame_data']['HW Chop Vr1'],
        self.hw_chop_vr2: self.current_message['data']['frame_data']['HW Chop Vr2'],
        self.hw_chop_vo1: self.current_message['data']['frame_data']['HW Chop Vo1'],
        self.hw_chop_vo2: self.current_message['data']['frame_data']['HW Chop Vo2'],
        self.hw_chop_cpot: self.current_message['data']['frame_data']['HW Chop Cpot'],
        self.hw_chop_gpot: self.current_message['data']['frame_data']['HW Chop Gpot'],
        self.rms_hor_vel: self.current_message['data']['frame_data']['RMS Hor Vel'],
        self.rms_ver_vel: self.current_message['data']['frame_data']['RMS Ver Vel'],
        self.var_35: self.current_message['data']['frame_data']['var_35']
        }

    async def main_loop(self):
        last_time = time.time()
        self.logger.log_app('--- Raw database service started succesfully ---')
        try:
            while(True):
                if (time.time() - last_time > 5): 
                    last_time = time.time()
                    key = self.current_message.get('0xd2a8', None)

                    if key != None:
                        self.stat_update_0xd2a8()
                        # run_0xd2a8
                        await self.run_0xd2a8()

                    elif key == None:
                        key = self.current_message.get('0xC109', None)
                        if key != None:
                            self.stat_update_0xC109()
                            # run_0xC109
                            await self.run()

                    elif key == None:
                        pass

                await asyncio.sleep(0.1)

        except Exception as e:
            self.logger.log_app.log_app("Exception in raw database service: %s" % e)


if __name__ == "__main__":
    db_conn =  muri_db_raw()

    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.ensure_future(db_conn.main_loop()))