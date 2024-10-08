import requests
from pprint import pprint
from requests import Response
from requests import ConnectionError,TooManyRedirects,Timeout,HTTPError
def connect_youbike():
    youbike_url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=1000'
    try:
        response = requests.get(youbike_url)
        response.raise_for_status()
    except ConnectionError:
        return('連線主機出問題')
    except TooManyRedirects:
        return("太多轉址")
    except Timeout:
        return("主機正在忙")
    except HTTPError:
        return("status_不是200")
    except:
        return("不明錯誤")
    else:
        return response
def search_area(response:Response,district:str)->list[dict]:
    data = response.json()
    

    district_stations = [station for station in dataif station['sarea'] == district ]
    
    return district_stations
def main():
    response=connect_youbike()
    if not isinstance(response,Response):
        print(response)  
        return 

    district = input("請輸入新北市行政區: ")
    district = district + "區"

    district_stations=search_area(response,district)
    


    if district_stations:
            pprint(district_stations)
    else:
            print(f"沒有找到 {district} 行政區的站點資訊。請再輸入一次")
        
        
if __name__=='main':
    main()

