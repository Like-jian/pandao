import requests,json

class download:
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0',
        'content-type':'application/json',
        'cookie':'''_bl_uid=sRjOIh7qzR8mav7Ln9FbgR9ntqp5; cookietest=1; gpv_pn=category%3A; s_vnum=1559613152692%26vn%3D1; s_invisit=true; _tsm=m%3DDirect%2520%252F%2520Brand%2520Aware%253A%2520Typed%2520%252F%2520Bookmarked%2520%252F%2520etc%7Cs%3D%28none%29; lzd_cid=2941935b-c5e0-4812-954f-e56bd8f243af; t_uid=2941935b-c5e0-4812-954f-e56bd8f243af; hng=MY|en-MY|MYR|458; userLanguageML=en; t_fv=1528077265416; t_sid=xAOouzrgOJghRk5cCh6NIW4E9WUjtqLa; __utma=93748224.1238778493.1528077265.1528077265.1528077265.1; __utmc=93748224; __utmz=93748224.1528077265.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); s_cc=true; lzd_sid=165c9dc0c4608151334fc842b1cadbb9; _tb_token_=77e6be8316613; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1506950487%7CMCMID%7C47234438059396422387790881948205328067%7CMCAID%7CNONE%7CMCAAMLH-1528682066%7C11%7CMCAAMB-1528682066%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; cna=1YmbExHn0BMCAcYNK9KHBXdI; cto_lwid=d7843ea9-028f-4181-8004-f143574ac3c9; ki_r=; __utmt=1; s_ppvl=D%253Dch%2B%2522%253A%2522%2C100%2C100%2C769%2C1440%2C769%2C1440%2C900%2C1%2CP; _uetsid=_uet53ac0400; ki_t=1528077272781%3B1528077272781%3B1528078024215%3B1%3B10; JSESSIONID=0CE0268E6A614B426BDA33F0D30A6218; __utmb=93748224.11.10.1528077265; s_ppv=D%253Dch%2B%2522%253A%2522%2C100%2C15%2C5569%2C1139%2C769%2C1440%2C900%2C1%2CP; s_sq=lazwebmy%3D%2526pid%253DD%25253Dch%25252B%252522%25253A%252522%2526pidt%253D1%2526oid%253Dfunction%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DLI; isg=BOHh3zggHqRxSLLDEmaGhNzt8K07JlVJWRxYeEO3GOgcqgN8i92IUd-sCN4sYu24''',
        'referer':'https://www.lazada.com.my/shop-food-supplements-weight-management/?page=102&spm=a2o4k.searchlistcategory.cate_4.1.7d532ea1THDAOI'}
        self.proxie={}
    def download(self,url):
        try:
            
            content=requests.get(url,headers=self.headers)
            if content.status_code==200:
                text=content.content.decode('utf-8')
                return text
        except Exception as e:
            raise e
    def post(self,url):
        url
        # itemsId="1473502936226769818-70-2-118-2760164976"
        headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'content-type':'application/json',
        'origin':'https://www.joom.com',
        'authorization':'Bearer SEV0001MTUyODA5Njg1MXxLRy02MkRtRDhucnpHYS13QldtX2o3Nm9URnU3dXhQUi1QQkxwLXhoMU1pbWZfdTZYbW1sTE1tN0FFLXRHaXB4cGljMjVMd0tIUklwVjdyUU42UkdsQ3FrMzdEYW1IVGIweUd6UGM2RFZ2ODNWalV5a28za0ZGUTI5aGNmRmpMdmUwNW0xLUFmNk1BQnBpd3FBcUdteHExTXVuQzRCUjk2QTdiT3BTZlFZTVVhaVhJPXynsDsuLyanQx3JAuJWcEmTvmQVvZjWum7bdKi6eEgEag=='
        }
        data={ 
            'category':'d56a7d49-2721-471b-b236-9472d7893325',
            'page':'1',
            'sort':'',
            'priceFrom':'',
            'priceTo':'',
            'qid':'88426d5c296806c1',
            'seed':'146285',
            'ga_from':'category/krasota-i-zdorove',
            'ga_cat':'Товары для красоты и здоровья из Китая — косметика, парфюмерия, средства гигиены недорого с бесплатной доставкой!'
            }

        try:
            content=requests.post(url,headers=headers,data=json.dumps(data),proxies=self.proxie)
            # print(json.loads(content.content)['contes'])
            if content.status_code==200:
                text=json.loads(content.content)
                return text
            else:
                time.sleep(60)
                content=requests.post(url,headers=headers,data=json.dumps(data),proxies=self.proxie)
                # print(json.loads(content.content)['contes'])
                if content.status_code==200:
                    text=json.loads(content.content)
                    return text
        except Exception as e:
            raise e


    # 设置代理
    def setProxie(self,proxie):
        self.proxie=proxie





url='https://pandao.ru/ajax/catalog'
d=download()
print(d.post(url))
