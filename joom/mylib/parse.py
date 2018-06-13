from pyquery import PyQuery as pq
import re
import time 
# ebay解析类
class parse:
    def __init__(self,download):
        self.download=download
    # 解析总调度
    def parse(self,content):
        # joom 返回 商品列表字典
        if isinstance(content,dict):
            newUrls=self.parseDictUrls(content)
            nextUrl=self.parseDictNexturl(content)
        else:
            newUrls=self.parseUrl(content)
            nextUrl=self.parseNextUrl(content)
            # 返回数组，字典，字符串
        return newUrls,nextUrl

    # 解析商品列表所有网址
    def parseUrl(self,content):
        reStr=re.compile(r'class="_1ZooeOL8crIkGtZ5sFnN3F".+?href="(.*?)"')
        print(re.findall(reStr,content))

    def parseDictUrls(self,content):
        baseUrl='https://api.joom.com/1.1/products/'
        lastUrl='?language=en-US&currency=USD&_=jiabd0r5'
        urls=set()
        for v in content['contexts'][0]['value']:
            url=baseUrl+v['id']+lastUrl
            urls.add(url)
        return urls

    def parseDictNexturl(self,content):
        url='https://api.joom.com/1.1/search/products?language=en-US&currency=USD&_=jiabd0r5'
        
        return (url,content['payload']['nextPageToken'])

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
        size=self.parseSize(content)
        createTime=time.strftime('%Y-%m-%d',time.localtime())
        return {'title':title,'productId':productId,'storeName':storeName,'storeLink':storeLink,'imgList':imgList,'price':price,'size':size,'attr':attr,'description':description,'location':location,'ship':ship,'createTime':createTime}

    def parseNextUrl(self,content):
        reStr=re.compile(r'class="pagn-next".+?href="(.*?)"')
        urlList=re.findall(reStr,content)
        if len(urlList)!=0:
            return urlList[0]
        return  ''

    def parseTitle(self,content):
        return content['payload']['engName']

    def parseId(self,content):
        return content['payload']['id']

    def parseStoreName(self,content):
        return content['payload']['store']['name']

    def parseStoreLink(self,content):
        return ''

    def parseImg(self,content):
        imgs=set()
        for v in content['payload']['gallery']:
            imgs.add(v['payload']['images'][3]['url'])
        
        if len(imgs)!=0:
            imgStr=''
            for i in imgs:
                imgStr+='%s|'%i
            return imgStr[0:-1]
        return ''

    def parsePrice(self,content):
        pStr='%s-%s'%(content['payload']['prices']['min'],content['payload']['prices']['max'])
        return pStr

    def parseAttr(self,content):
        colors=set()
        size=set()
        try:
            if not content['payload']['variants']:
                return ''
            vStr=''

            for x in range(len(content['payload']['variants'])):
                v=content['payload']['variants'][x]
                color=v['colors'][0]['name']+'/'
                for i in range(10):
                    try:
                        c=v['colors']
                        if i==0:
                            pass
                        else:
                            color=color+c[i]['name']+'/'
                    except Exception as e:
                        pass
                color=color[0:-1]
                if color in colors:
                    continue
                colors.add(color)
                try:
                    vStr+=color+'^'+v['mainImage']['images'][3]['url']+'|'
                except:
                    vStr+=color+'|'
            vStr=vStr[0:-1]
            return vStr
            html=pq(content)
            return html('.itemAttr').text()
        except:
            return ''

    def parseSize(self,content):
        size=set()
        try:
            if not content['payload']['variants']:
                return ''
            vStr=''
            for v in content['payload']['variants']:
                size.add(v['size'])
            for v in size:
                vStr+=v+'|'
            vStr=vStr[0:-1]
            return vStr
        except Exception as e:
            return ''

    def parseDescription(self,content):
        return content['payload']['engDescription']

    def parseLocation(self,content):
        return ''
        # 发货地
        html=pq(content)
        return html('#itemLocation').find('span').text()
     
    def parseShip(self,content):
        pStr='%s-%s'%(content['payload']['shippingPrices']['min'],content['payload']['shippingPrices']['max'])
        return pStr



