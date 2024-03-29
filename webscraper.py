import requests
import time
import datetime
import smtplib
import anvil.server

#anvil stuff
pip install anvil-uplink
anvil.server.connect("server_OMUQTSB4R6YWHHN2AQBBW22P-AA7NC2TON2CLKDAF")

class ScrapedData:
    @anvil.server.callable
    def raw_data(url, topic):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept-Language": "en-US,en;q=0.9", 
            "Host": "httpbin.org", 
            "Referer": "https://www.youtube.com/", 
            "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"", 
            "Sec-Ch-Ua-Mobile": "?0", 
            "Sec-Ch-Ua-Platform": "\"macOS\"", 
            "Sec-Fetch-Dest": "document", 
            "Sec-Fetch-Mode": "navigate", 
            "Sec-Fetch-Site": "cross-site", 
            "Sec-Fetch-User": "?1", 
            "Upgrade-Insecure-Requests": "1", 
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", 
            "X-Amzn-Trace-Id": "Root=1-6568f7cc-1700f23442d59a687e8e741e"
        }
        page = requests.get(url, headers)

        word = topic 
        list_header = []
        soup1 = BeautifulSoup(page.content, "html.parser")
        soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

        for tag in soup1.find_all():
            list_header.append(BeautifulSoup(tag,'html.parser'))
            
        for header in list_header:
            for text in header.get_text():
                if word in text:
                    return text

        s = soup1.find(tag).get_text()
        price = title.find('priceblock_ourprice').get_text()
        title = title.strip()
        print(soup2)
        print(list_header)