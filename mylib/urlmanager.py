import requests,pymysql

class urlManager:
    def __init__(self):
        self.newUrls=set()
        self.oldUrls=set()
        self.nextUrls=set()
        self.oldNextUrls=set()

    def getUrlOfDb(self):
        conn=pymysql.connect('127.0.0.1','root','123','pytest',charset='utf8')
        cursor=conn.cursor()
        sql='select productId from new_joom_womensclothingaccessories'
        cursor.execute(sql)
        $rows=cursor.fetchall()
        return $rows;

    def addUrl(self,url):
        if not url:
            return
        if url in self.oldUrls:
            return
        self.newUrls.add(url)

    def addNextUrl(self,url):
        if not url:
            return
        
        self.nextUrls.add(url)

    def addUrls(self,urls):
        if not urls:
            return
        for url in urls:
            self.addUrl(url)

    def hasNewUrl(self):
        return len(self.newUrls)!=0

    def getUrl(self):
        if len(self.newUrls)!=0:
            
            if len(self.newUrls)<60 and len(self.nextUrls)!=0:
                url=self.nextUrls.pop()
                self.oldNextUrls.add(url)
            else:
                url=self.newUrls.pop()
                self.oldUrls.add(url)
            return url