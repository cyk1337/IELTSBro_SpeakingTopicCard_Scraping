import urllib2,os
from bs4 import BeautifulSoup
import requests

def download_img(url):
   
    headers={
        'Cookie':'_yasi_website_session=NE5pZU1zdEwySVlzUzRaOVl3eUNTTitQNE05eTcwdjUvNHBXbUJiNGt6QVVpOEV1UTlhMWR6aGZKVzlYVm10VTdWd2ZKOUtDTVhLeEIrOEd3ZUlocWhtLzcyb05TaHp1dVlCak11bW5wby9aWVBQSzZvNCtraHZ6ZGkzRTI4cUxtbTN5cXpqWlp2dXNVRytTZDhXRUU1QkhFSFpWTjdkNmY3UlpOZkw4VUdGb2lmVnJoUTBxa0RSV3ZlWHBjbGY4bUF6TzdwZVVyNnZKSUdvNklFbkkzYXAvdFl3TGNTUFluYWtsUEEzWjZRbExwZ3FORXV1QnNOYlpNVzRWNmpIUDdJR2tjUTVxVG9xTGdUZVhOWVBpdklDUXRhamNqOEJzWlAzblJkUDVsMThieDdueTEwbHhhMHNGcUo2dnBHREhVcm9mcld5OU9EOG03MTlMUG9FWXp3PT0tLXVJTHVvcmVrSk9VendEOVBtaGxKWGc9PQ%3D%3D--9462f8c529da941685976ccf6235f2bceda22298; CNZZDATA1260900061=1970134767-1488189272-%7C1488194905',
        'Host':'ieltsbro.com',
        'If-Modified-Since':'Mon, 09 Jan 2017 10:00:42 GMT',
        'If-None-Match':"58735f4a-14d73",
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36d73'
    }
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    bsObj=BeautifulSoup(response.read(),"lxml")
    imgList=bsObj.findAll('img',{"class":"ielts_image"})
    return imgList
    
   
    
def saveImg(imgName,imgUrl):
    if not os.path.exists("IELTS"): 
        os.mkdir("IELTS")

    
    try:
        print '-'*20
        #print imgUrl,imgName
        img=requests.get(imgUrl)
        imgFile=open('IELTS\\'+imgName+'.jpg','wb')
        imgFile.write(img.content)
        imgFile.close()
        print imgUrl,"was saved sucessfully!"
    except Exception,e:
        print e
        print imgName,"failed to save!"
    
        
def start():
    url='http://ieltsbro.com'
    imgList=download_img(url+'/article/view/54')
    
    imgInfo={}
    for imgData in imgList:
        imgInfo[imgData.attrs['alt']]=imgData.attrs['src']
    for k,v in imgInfo.items():
        print k,v
        saveImg(k, url+v)

if __name__=="__main__":
    start()
    