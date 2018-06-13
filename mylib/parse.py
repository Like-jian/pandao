from pyquery import PyQuery as pq
import re,json
import time 
# ebay解析类
class parse:
    def __init__(self,download):
        self.download=download
    # 解析总调度
    def parse(self,content,baseUrl):
        self.baseUrl=baseUrl
        newUrls,nextUrl=self.parseUrl(content)
        if not newUrls:
            newData=self.parseData(content)
        else:
            newData=''
            # 返回数组，字典，字符串
        return newUrls,newData,nextUrl

    # 解析商品列表所有网址
    def parseUrl(self,content):
        urls=set()
        nextUrl=self.baseUrl
        try:
            content= json.loads(content)
            for v in content['mods']['listItems']:
                urls.add('https:'+v['productUrl'])
            if len(urls)>1:
                page=content['mainInfo']['page']
                page=int(page)+1
                nextUrl+=str(page)
            return urls,nextUrl
        except:
            return '',''

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
        # 变体
        variant=self.parseVariant(content)
        createTime=time.strftime('%Y-%m-%d',time.localtime())
        return {'title':title,'productId':productId,'storeName':storeName,'storeLink':storeLink,'imgList':imgList,'price':price,'attr':attr,'description':description,'location':location,'ship':ship,'createTime':createTime}

    def parseNextUrl(self,content):
        html=pq(content)
        print( html('.c16H9d').find('a'))
        exit()
        return html('.c16H9d').find('a')

        if len(urlList)!=0:
            return urlList[0]
        return  ''

    def parseTitle(self,content):
        html=pq(content)
        return html('.pdp-product-title').text()

    def parseId(self,content):
        html=pq(content)
        return html('#descItemNumber').text()

    def parseStoreName(self,content):
        html=pq(content)
        return html('.seller-name__detail-name').text()

    def parseStoreLink(self,content):
        html=pq(content)
        return html('.seller-name__detail-name').attr('href')

    def parseImg(self,content):
        html=pq(content)
        imgs=set()
        img=html('.item-gallery__thumbnail-image')
        if len(img)!=0:
            imgStr=''
            for i in range(len(img)):
                src='https:'+img.eq(i).attr('src')
                imgs.add(src)
            for i in imgs:
                imgStr+='%s|'%i
            return imgStr[0:-1]
        return ''

    def parsePrice(self,content):
        html=pq(content)
        return html('.pdp-price_color_orange').text()

    def parseAttr(self,content):
        html=pq(content)
        return html('.pdp-product-highlights').text()

    def parseDescription(self,content):
        html=pq(content)
        return html('.detail-content').html()

    def parseLocation(self,content):
        # 发货地
        html=pq(content)
        return html('#itemLocation').find('span').text()
     
    def parseShip(self,content):
        html=pq(content)
        return html('#shSummary').remove('#e2').find('span').text()

    def parseVariant(self,content):
        html=pq(content)
        options=html('#msku-sel-1').find('option')
        variantStr=''
        if len(options)!=0:
            for v in range(len(options)):
                variantStr+=options.eq(v).text()+'|'
            variantStr=variantStr[0:-1]
        return variantStr


