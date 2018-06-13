import pymysql
import time

class ips:
    # def __init__(self):
    #     pass
    def getIps(self):
        sql='select * from ip where used=1 and (to_days(lasttime)<to_days(now()) or lasttime=\'0000-00-00\')'
        conn=pymysql.connect('127.0.0.1','root','123','pytest')
        cursor=conn.cursor()
        cursor.execute(sql)
        rows=cursor.fetchall()
       
        cursor.close()
        conn.close()
        return rows
        
    def setLastTime(self,id):
        conn=pymysql.connect('127.0.0.1','root','123','pytest')
        cursor=conn.cursor()
        sql='update ip set lasttime= "%s" where id =%s'%(time.strftime('%Y-%m-%d',time.localtime()),id)
        cursor.execute(sql)
        conn.commit()
