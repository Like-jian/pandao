import pymysql
class intoDb():
    def __init__(self):
        pass
    def collect(self,data,link,myType):
        if not data:
            return
        sql='insert into  `lazada` (link ,type,title,productId,storeName,storeLink,imgList,price,attr,description,location,ship,createTime) values(\'%s\',\'%s\','%(self.changeStr(link),myType)
        # 组装sql
        for k in data:
            s=self.changeStr(data[k])
            sql+="'%s',"%s
        sql=sql[0:-1]
        sql+=')'
        # print(sql)
        conn=pymysql.connect('127.0.0.1','root','123','pytest',charset='utf8')
        cursor=conn.cursor()
        try:
            cursor.execute(sql)
            print('insert ok')
        except Exception as e:
            conn.rollback()
            print('insert no')
            print(e)
        conn.commit()
        cursor.close()
        conn.close()

    # 转义字符串的\ ' "等
    def changeStr(self,cStr):
        if cStr is None:
            return
        retStr=''
        for c in cStr:
            if c =='"':
                c='\\\"'
            if c =="'":
                c="\\\'"
            if c=='\\':
                c='\\\\'
            retStr+=c
        return retStr

        