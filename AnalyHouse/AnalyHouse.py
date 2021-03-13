
import requests
import xml.etree.ElementTree as elemTree


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
print(response.text)


#xml 파싱
tree = elemTree(response.text)
root = tree.getroot()


a =  0


