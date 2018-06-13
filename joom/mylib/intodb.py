import pymysql
class intoDb():
    def __init__(self):
        self.table=''

    def createTable(self,table):
        self.table=table
        sql='drop table if exists %s'%table
        sql2='''
            CREATE TABLE `%s` (
          `id`          int(11)      NOT NULL AUTO_INCREMENT COMMENT 'id',
          `link`        varchar(255) NOT NULL COMMENT '地址',
          `title`       varchar(250) NOT NULL COMMENT '标题',
          `productId`   varchar(200) NOT NULL COMMENT '产品id',
          `storeName`   varchar(200) NOT NULL COMMENT '店铺名称',
          `storeLink`   varchar(200) NOT NULL COMMENT '店铺地址',
          `imgList`     text         NOT NULL COMMENT '图片地址串',
          `price`       varchar(200) NOT NULL COMMENT '价格',
          `size`        varchar(200) NOT NULL COMMENT '尺寸',
          `attr`        text         NOT NULL COMMENT '变体',
          `description` text         NOT NULL COMMENT '产品描述',
          `location`    varchar(200) NOT NULL COMMENT '发货地',
          `ship`        varchar(200) NOT NULL COMMENT '物流',
          `createTime`  date         NOT NULL COMMENT '爬取时间',
                                     PRIMARY KEY (`id`)
            ) ENGINE=MyISAM  DEFAULT CHARSET=utf8;
            '''%table
        conn=pymysql.connect('127.0.0.1','root','123','pytest',charset='utf8')
        cursor=conn.cursor()
        try:
            cursor.execute(sql)
            cursor.execute(sql2)
            conn.commit()
        except:
            conn.rollback()

        cursor.close()
        conn.close()


    def collect(self,data,link):
        if not data:
            return
        sql='insert into '+self.table+' (link ,title,productId,storeName,storeLink,imgList,price,size,attr,description,location,ship,createTime) values(\''+self.changeStr(link)+'\','
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

        