import requests
from bs4 import BeautifulSoup
import csv

url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade"

encoding = "O9YLfGdeRwmJITv50o9b2%2BVvgzNxJ%2FHL4C33nn3%2BO59eXlvNm%2BsqAC3UY%2BF1UmTvhc%2FA1LgkfOtYRMT%2BF1i9zQ%3D%3D"
decoding = "O9YLfGdeRwmJITv50o9b2+VvgzNxJ/HL4C33nn3+O59eXlvNm+sqAC3UY+F1UmTvhc/A1LgkfOtYRMT+F1i9zQ=="

api_key_decode = requests.utils.unquote(encoding)


params ={'serviceKey' : api_key_decode, 'LAWD_CD' : '11110', 'DEAL_YMD' : '201912' }

response = requests.get(url, params=params)
#print(response.content)

soup = BeautifulSoup(response.text, 'xml')
csv_filename = "transaction_data.csv"

with open(csv_filename, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["거래금액", "년도", "법정동", "아파트", "월", "전용면적", "층"])

    items = soup.find_all("item")
    for item in items:
        거래금액 = getattr(item.find("거래금액"), 'text', None)
        년도 = getattr(item.find("년"), 'text', None)
        법정동 = getattr(item.find("법정동"), 'text', None)
        아파트 = getattr(item.find("아파트"), 'text', None)
        월 = getattr(item.find("월"), 'text', None)
        전용면적 = getattr(item.find("전용면적"), 'text', None)
        층 = getattr(item.find("층"), 'text', None)

        csv_writer.writerow([거래금액, 년도, 법정동, 아파트, 월, 전용면적, 층])

print(f"CSV 파일 '{csv_filename}'이 생성되었습니다.")