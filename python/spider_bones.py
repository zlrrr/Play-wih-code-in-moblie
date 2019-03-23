# coding: utf-8
import requests
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error happend"
        
if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))
    
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'spider_bones 21-33')
