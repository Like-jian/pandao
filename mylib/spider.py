import urlmanager,download,parse,intodb,ips
import time
import threading
class spider:
    def __init__(self):
        self.urlManager=urlmanager.urlManager()
        self.download=download.download()
        self.parse=parse.parse(self.download)
        self.intoDb=intodb.intoDb()
        self.ips=ips.ips()

    # 爬虫调度程序
    def main(self,root_url):
        self.urlManager.addUrl(root_url)
        count=1
        # ipList=self.ips.getIps()
        while self.urlManager.hasNewUrl():
            try:
                # ip=ipList[count-1]
                # self.ips.setLastTime(ip[0])
                newUrl=self.urlManager.getUrl()
                # 线程数量控制在10个以下
                th=threading.active_count()
                if th>10:
                    time.sleep(1)
                    continue
                # 代理ip
                # proxie={
                # 'http':'http://111.121.193.214:3218'
                # }
                # 设置代理ip
                # self.download.setProxie(proxie)
                # 多线程
                threading.Thread(target=self.theadAction,args=(newUrl,count)).start()
                
            except Exception as e:
                print('nonono')
                print(e)
            
            count +=1
            time.sleep(5)
            # 网址管理器没有网址时，并且运行线程不为0，休眠10秒等待线程可能取出地址
            if not self.urlManager.hasNewUrl() and threading.active_count()!=0:
                time.sleep(10)
            
            

    def theadAction(self,newUrl,count):
        content=self.download.download(newUrl)
        newUrls,newData,nextUrl=self.parse.parse(content,self.baseUrl)
        self.urlManager.addUrls(newUrls)
        self.urlManager.addNextUrl(nextUrl)
        self.intoDb.collect(newData,newUrl,self.myType)
        print(nextUrl)
        print(newUrls)
        print('%s success'%count)


urlList=[
('shop-hair-care','spm=a2o4k.searchlistcategory.cate_4.8.38d4106dfe2Ljb'),
('shop-hb-health-personal-care','spm=a2o4k.searchlistcategory.cate_4.9.6a234f43CsZUew'),
('shop-fragrances','spm=a2o4k.searchlistcategory.cate_4.10.8b7c3b6bL1fkS9')
]

root_url='https://www.lazada.com.my/'
spiderList=[spider(),spider(),spider(),spider()]


for i in range(len(urlList)):
    v=urlList[i]
    spider=spiderList[i]
    baseUrl=root_url+'%s/?%s&ajax=true&page='%v
    root_url=baseUrl+'1'
    myType=v[0]

    # 数据类型
    spider.myType=myType
    # 下一页的网址的baseurl
    spider.baseUrl=baseUrl
    spider.main(root_url)