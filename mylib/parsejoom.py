from pyquery import PyQuery as pq
import re
import time 
# ebay解析类
class parse:
    def __init__(self,download):
        self.download=download
    # 解析总调度
    def parse(self,content):
        newUrls=self.parseUrl(content)
        nextUrl=self.parseNextUrl(content)
        if not newUrls:
            newData=self.parseData(content)
        else:
            newData=''
            # 返回数组，字典，字符串
        return newUrls,newData,nextUrl

    # 解析商品列表所有网址
    def parseUrl(self,content):
        reStr=re.compile(r'class="s-item__link".+?href="(.*?)"')
        return re.findall(reStr,content)

    # 解析商品具体数据
    def parseData(self,content):
        # 标题
        title=self.parseTitle(content)
        # 商品id
        productId=self.parseId(content)
        # 店铺名称
        storeName=self.parseStoreName(content)
        # 店铺地址
        storeLink=self.parseStoreLink(content)
        # 商品图片列表
        imgList=self.parseImg(content)
        # bigImg=imgList[0]
        # 价格
        price=self.parsePrice(content)
        # 属性
        attr=self.parseAttr(content)
        # 产品描述
        description=self.parseDescription(content)
        # 发货地
        location=self.parseLocation(content)
        # 物流
        ship=self.parseShip(content)
        createTime=time.strftime('%Y-%m-%d',time.localtime())
        return {'title':title,'productId':productId,'storeName':storeName,'storeLink':storeLink,'imgList':imgList,'price':price,'attr':attr,'description':description,'location':location,'ship':ship,'createTime':createTime}

    def parseNextUrl(self,content):
        reStr=re.compile(r'class="pagn-next".+?href="(.*?)"')
        urlList=re.findall(reStr,content)
        if len(urlList)!=0:
            return urlList[0]
        return  ''

    def parseTitle(self,content):
        html=pq(content)
        return html('.it-ttl').remove('span').text()

    def parseId(self,content):
        html=pq(content)
        return html('#descItemNumber').text()

    def parseStoreName(self,content):
        html=pq(content)
        name=html('#mbgLink')
        if len(name)>1:
            return name.eq(0).text()
        return name.text()

    def parseStoreLink(self,content):
        html=pq(content)
        link=html('#mbgLink')
        if len(link)>1:
            return link.eq(0).attr('href')
        return link.attr('href')

    def parseImg(self,content):
        html=pq(content)
        imgs=set()
        img=html('.tdThumb').find('img')
        if len(img)!=0:
            imgStr=''
            for i in range(len(img)):
                src=img.eq(i).attr('src').replace('s-l64.jpg','s-l640.jpg')
                imgs.add(src)
            for i in imgs:
                imgStr+='%s|'%i
            return imgStr[0:-1]
        else:
            bigImg=html('#icImg').attr('src')
            return bigImg
        return ''

    def parsePrice(self,content):
        html=pq(content)
        return html('.notranslate').text()

    def parseAttr(self,content):
        html=pq(content)
        return html('.itemAttr').text()

    def parseDescription(self,content):
        # 产品描述的iframe地址
        reStr=re.compile('id="desc_ifr".*?src="(.+?)"')
        srcList=re.findall(reStr,content)
        if len(srcList)!=0:
            src=srcList[0]
        else:
            # ebay产品描述有http协议时iframe地址
            src=pq(content)('#snippetdesc').attr('href')
        try:
            # 请求该地址
            info=self.download.download(src)
        except Exception as e:
            return ''
        html=pq(info)
        return html('#ds_div').html()

    def parseLocation(self,content):
        # 发货地
        html=pq(content)
        return html('#itemLocation').find('span').text()
     
    def parseShip(self,content):
        html=pq(content)
        return html('#shSummary').remove('#e2').find('span').text()



