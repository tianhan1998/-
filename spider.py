import requests
from bs4 import BeautifulSoup
url="https://www.baidu.com/home/pcweb/data/mancardwater?id=2&offset="
url1="5&sessionId=15553920744740&crids=&version=&pos="
url2="&newsNum="
url3="&blacklist_timestamp=1555331335&indextype=manht&_req_seqid=0xd20705670004b4e3&asyn=1&t=1555392315369&sid=1424_21122_28769_28720_28557_28839_28584_26350_28603"
data={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
      "Accept":"text/plain, */*; q=0.01",
      "Cookie":"BIDUPSID=09966FC9813AB11C5CB49E4D3D11A5F3; BAIDUID=FAE167E1AEEDA589370C2C5BA1B8F313:FG=1; PSTM=1545052794; BD_UPN=12314353; pgv_pvi=1885779968; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; PSINO=1; delPer=0; H_PS_PSSID=1424_21122_28769_28720_28557_28839_28584_26350_28603; BDUSS=XhLUjNOZ1U4cX5Ib1pkSEZhRWRaVDA4bGZ-ZU5aWWZGN2hIWEZ2TFdjZXA3TnhjRVFBQUFBJCQAAAAAAAAAAAEAAACoAQkFZGFidTExMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKlftVypX7VcY; BD_HOME=1; H_WISE_SIDS=124612_100807_129630_128065_131176_120143_118884_118864_118839_118829_118789_130763_129564_107311_129945_129748_130157_130128_130222_117331_130347_130569_129648_131022_124638_130690_129009_130320_128968_131035_129620_129835_130988_129901_129481_129646_124030_110085_127969_123289_131003_130481_127316_131163_127416_131037; FEED_SIDS=152041_0416_12; plus_lsv=393c3756be30db54; plus_cv=1::m:49a3f4a6; Hm_lvt_12423ecbc0e2ca965d84259063d35238=1555391076; SE_LAUNCH=5%3A25923184_0%3A25923184; rsv_i=c64fO2Q%2FBuUUOCGOcZHota%2BzO4oh44ew4sM6UiVUKSDctVZC2k7I8PGI4fWcU2faToe65%2BqSY0dd3%2F7t2fJ7aEdxQrCr66Q; Hm_lpvt_12423ecbc0e2ca965d84259063d35238=1555391530; H_PS_645EC=e9a7mKhKBsgxGsJCUlILGR7bE4oO4Fq%2FTWPAYSjwXRBeewsBExcGjf6Vth29%2BVqPNhod; sug=3; sugstore=0; ORIGIN=0; bdime=0"
      }
for i in range(1,20):
    rsp=requests.get(url+str(i)+url1+str(i)+url2+str(i)+url3,headers=data)
    soup = BeautifulSoup(rsp.text,"lxml")
    print(soup.find("h2").next.text+"\n")
    imgurl = soup.find("img").get('src').encode('utf-8').decode('unicode_escape').replace("\\","").replace("\"",'')
    imgreq=requests.get(imgurl)
    with open("./img/"+str(i)+".jpg",'wb') as f:
        f.write(imgreq.content)
    
