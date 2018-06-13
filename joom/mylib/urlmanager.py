import requests
import pymysql 

class urlManager:
    def __init__(self):
        self.newUrls=set()
        self.oldUrls=set()
        self.nextUrls=set()
        self.oldNextUrls=set()

        # self.newUrls=self.getUrlOfDb()


    def getUrlOfDb(self):
        conn=pymysql.connect('127.0.0.1','root','123','pytest',charset='utf8')
        cursor=conn.cursor()
        sql='select productId from new_joom_womensclothingaccessories limit 0,2800'
        cursor.execute(sql)
        rows=cursor.fetchall()
        print(rows)
        return list(rows);

    def addUrl(self,url):
        if not url:
            return
        if url in self.oldUrls:
            return
        self.newUrls.add(url)

    def addNextUrl(self,url):
        if not url:
            return
        if url in self.oldNextUrls:
            return
        self.nextUrls.add(url)

    def addUrls(self,urls):
        if not urls:
            return
        for url in urls:
            self.addUrl(url)

    def hasNewUrl(self):
        return len(self.newUrls)!=0 or len(self.nextUrls)!=0

    def getUrl(self):
        if len(self.newUrls)!=0 or len(self.nextUrls)!=0:
            
            if len(self.newUrls)<60 and len(self.nextUrls)!=0:
                print(len(self.oldNextUrls),'业')
                url=self.nextUrls.pop()
                urlType='next'
                self.oldNextUrls.add(url)
                print(len(self.oldNextUrls),'页',url)
            else:
                url=self.newUrls.pop()
                # url='https://api.joom.com/1.1/products/'+url+'?language=en-US&currency=USD&_=jiabd0r5'
                urlType='product'
                self.oldUrls.add(url)
            return {'url':url,'type':urlType}