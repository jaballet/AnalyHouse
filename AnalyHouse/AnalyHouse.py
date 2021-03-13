
import requests
import xml.etree.ElementTree as ET  


## 공공데이터 포털 
URL = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'

##국토교통부_아파트매매 실거래자료
#서비스키
ServiceKey = "sEkWhWER%2Fsn%2FgRDrtuBW2BHO%2BE65ORsVQQuDOqMnvZOa%2Fh6Ir0L6ppED3VIkx%2BqSEFdkhygEpOHsOQfQqzq56w%3D%3D"
# 지역별 코드 Sample : 11110
LAWD_CD = "LAWD_CD"
# 월단위 신고 자료 Sample : 201512
DEAL_YMD = "DEAL_YMD"

strSetup = "?serviceKey={0}&{1}=11110&{2}=201512".format(ServiceKey, LAWD_CD, DEAL_YMD)
response = requests.get(URL + strSetup)
response.status_code
#print(response.text)

#https://118k.tistory.com/215
#xml 파싱
root = ET.fromstring(response.text)
print(root.tag, root.attrib) # root 가 <data> 엘리먼트를 가르키게 된다.

# root 태그로 for 문을 돌리면 자식 엘리먼트 전체가 추출 됨
for child in root:
	print(child.tag, child.attrib)
	for item in child.items :
		print(item)



# iter() 메소드를 이용하면 xml 문서 전체의 엘리먼트를 가지고 온다.
for neighbor in root.iter('neighbor'):
	print(neighbor.tag, neighbor.attrib)


# findall() 메소드를 이용하면 현재 태그의 자식중에서 지정한 태그를 반환한다. 
for neighbor in root.findall('neighbor'):
	print(neighbor.tag)




tree = ET.fromstring(response.text)
root = tree.getroot()

tree = elemTree(response.text)
root = tree.getroot()


a =  0


