#Test Site https://www.scrapethissite.com/pages/
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited_urls = set()
stored_urls=[]


def spidering(user_input_url,keyword):
    
    try :
        respone = requests.get(user_input_url)
    except Exception as e:
        print(f"Request Failed {user_input_url} {e}")
    try:
# The tags "a" and "href" can be customized according to will.
        if respone.status_code == 200:
            soup = BeautifulSoup(respone.content, "html.parser")
            a_tag = soup.find_all("a")
            
            for tag in a_tag:
                href=tag.get("href")
                if href is not None and href!="":
                    stored_urls.append(href)
            #print(stored_urls)
#This is the recursion part               
        for i in stored_urls:
            if i not in visited_urls:
                visited_urls.add(i)
                url_formated=urljoin(user_input_url, i)
                if keyword in url_formated:
                    print(url_formated)
                    spidering(url_formated,keyword) 
                else:
                    pass
                        
    except Exception as e:
        print(e)
        
user_input_url = input("user_input_url : ")
keyword = input("Keyword : ") 
spidering(user_input_url,keyword)      
    

