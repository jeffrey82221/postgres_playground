import psycopg2
from config import config
from contextlib import closing
import pandas as pd

class SQLTool:
    def get_conn(self):
        params = config()
        conn = psycopg2.connect(**params)
        return conn
    def execute_sql(self, sql):
        with closing(self.get_conn()) as conn:
            cur = conn.cursor()
            try:
                cur.execute(sql)
                print('[execute_sql] DONE')
            except Exception as e:
                conn.rollback()
                print('[execute_sql] Rollback')
                raise e
            finally:                
                conn.commit()
                cur.close()
    def select_table(self, sql):
        with closing(self.get_conn()) as conn:
            try:
                table = pd.read_sql(sql, con=conn)
            except Exception as e:
                raise e
        return table