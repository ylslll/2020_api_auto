# 导入mysql驱动
# import mysql.connector
import pymysql

class MysqlCon():

    def select(self, sql, database):
        # 创建连接
        db = pymysql.connect(host='test.db.yelopack.com', user='dev', password='123456',
                             database=database, charset='utf8mb4')
        # 创建游标对象
        db_cursor = db.cursor()
        mysql_result = ()
        # sql='SELECT * FROM t_tray_customer_company WHERE id=5'
        try:
            # 执行sql
            db_cursor.execute(sql)
            mysql_result = db_cursor.fetchall()
        except Exception as e:
            print(e)
            # 数据库回滚
            db.rollback()
        finally:
            # 提交事务
            db.commit()
            # 断开连接
            db.close()
            return mysql_result

if __name__ == '__main__':
    a = MysqlCon().select('SELECT verification_code FROM t_verification_code WHERE created_by="10123456789" ORDER BY id DESC LIMIT 1','test_yelo_basicdata')
    print(a)
    print(type(a), type(a[0][0]), len(a))

