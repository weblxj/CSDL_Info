#!/usr/bin/env python

#import C_Python
import requests
from requests.auth import HTTPBasicAuth
import re

class CSDLInfo:
    # url_1 = "https://wwwin-si.cisco.com/projects/20814/?tab=PSB+Compliance" 
    # url_2 = "https://wwwin-si.cisco.com/api/v1/project-summary/csdl?csdl_project_id=20814" -H "Content-Type: application/json"  -u "ronling:weblxjhuQ~4" 
    # url_3 = "https://wwwin-si.cisco.com/api/v1/project-summary/psb?csdl_project_id=20814" -H "Content-Type: application/json"  -u "ronling:weblxjhuQ~4" 
    # url_4 = "https://wwwin-si.cisco.com/api/v1/project-summary/svs?csdl_project_id=20814" -H "Content-Type: application/json"  -u "ronling:weblxjhuQ~4" 

    def __init__(self, username, password):
        self.username = username
        self.password = password
        return

    def PSB_Compliance(self):
        #url = '''https://wwwin-si.cisco.com/api/v1/project-summary/csdl?csdl_project_id=20814 -H "Authorization: Token c1650b7731df92b9476d543eb22c0db33bae06f0" -H "Content-Type: application/json"  -u "ronling:weblxjhuQ~4"'''
        url = "https://wwwin-si.cisco.com/api/v1/project-summary/psb?csdl_project_id=20814"

        requests.adapters.DEFAULT_RETRIES = 3
        requests.Timeout = 10
        requests.allow_redirects = True
        headers={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36','Content-Type':'application/json'}
        print ("URL is:%s" % url)
        #response = requests.get(url, user_agent)
        response = requests.get(url, headers, auth=HTTPBasicAuth(self.username, self.password ))
        #exp_str = r'(\d{6},\d{4},PHONE,'+self.branch_name+',)'ls

        #pattern_all = re.compile(exp_str,re.DOTALL)
        # print re.search(pattern_all,response.content).string
        #count_overall = len(re.findall(pattern_all,self.content))


        # response = requests.get("https://wwwin-si.cisco.com/api/v1/project-summary/csdl?csdl_project_id=20814",
        #     headers={
        #         "Accept": "application/json, text/javascript, */*; q=0.01",
        #         "Accept-Encoding": "gzip, deflate, br",
        #         "Accept-Language": "en-US,en;q=0.9",
        #         "Connection": "keep-alive",
        #         "Referer": "https://wwwin-si.cisco.com/projects/20814/?tab=PSB+Compliance",
        #         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        #         "X-Requested-With": "XMLHttpRequest"
        #     },
        #     cookies={
        #         "AMCVS_B8D07FF4520E94C10A490D4C%40AdobeOrg": "1",
        #         "AMCV_B8D07FF4520E94C10A490D4C%40AdobeOrg": "-227196251%7CMCIDTS%7C17711%7CMCMID%7C69334761282393279937625048571810906706%7CMCAID%7CNONE%7CMCAAMLH-1530777893%7C9%7CMCAAMB-1530777898%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCOPTOUT-1530180298s%7CNONE",
        #         "CONSENTMGR": "ts:1530173098964%7Cconsent:true",
        #         "CP_GUTC": "72.163.4.169.1530173088422893",
        #         "ObSSOCookie": "znDmqr44G31JqS%2BJoLlheRWGK5YvYihpigw%2F8Ha0jrpLBYCJOE1DVlJgyg9eRNzd%2Fv1L%2Fv4jwRJ8qnXDuawubX%2F7%2FS79KwZtx57VIO3tGi8BDi%2BOXC%2Fqmu3noE2IwWZjX%2B4HAHdQTYx6ys6R6GdUn562TJN58D1PCZrNJ1UzT0p9do9fUrm5tyodhDU%2F7Uzj%2BKAOv%2FqMEctvbcjIlnf%2FqN9Q8ZcBljcaXDCQNVsiSactOzv3Fkp7mfDQBPaKt8J9bH0MVLKyynxVjlkMW5AuLEPDW1MhlzPgTNnirkjCiMvYLIqpFb4sNGIeylicjcLh1mG479tv217Ud0EXwEwPqana6eUwqMTEDSmrUH%2Fima9BH1lv2L7c3qTvUMbXQYWdB%2FRtETs%2BaboSbqrzY86SNKEKSKsl%2B8iE3veU8JbEVN3rGLE9sq1MRq7gV4kN4Sr9XEdEPljsd34%2FI4Z%2Ba4bhG6c12XfEZOjXbs3kdj5EZDJRyGZX6HwHHfpedYd0QqPA",
        #         "authorization": "loggedIn",
        #         "cdcUniqueKey": "5cf5bhfhd9h67",
        #         "hbx_lid": "no_id",
        #         "loginPageRef": "",
        #         "loginPageReferrer": "",
        #         "s_cc": "true",
        #         "s_fid": "7230E5230F2632EB-012F6C14BAA36A1A",
        #         "s_ppv": "cloudsso.cisco.com%2Fsp%2Fstartsso.ping%2C100%2C100%2C899%2C1200%2C899%2C1920%2C1080%2C1%2CP",
        #         "s_ppvl": "%5B%5BB%5D%5D",
        #         "s_ptc": "%5B%5BB%5D%5D",
        #         "s_sq": "%5B%5BB%5D%5D",
        #         "utag_main": "v_id:0164456c8bb3009a8e2b5aae374003078008e07000bd0:1:0:1530174934664:1530173098933%3Bexp-session:1%3Bexp-session:cisco.com",
        #         "wamsessiontracker": "bGFzdGxvZ2luPTA3LzAyLzIwMTggMDY6Mjc6NDQ=",
        #         "wasOnLoginPage": "true"
        #     },
        # )
        print ('The response content  is: %s' % response.content)
        return response.content


    def CSDL_Process(self):
        #url = '''https://wwwin-si.cisco.com/api/v1/project-summary/csdl?csdl_project_id=20814 -H "Content-Type: application/json"  -u "ronling:weblxjhuQ~4" '''
        url = "https://wwwin-si.cisco.com/api/v1/project-summary/csdl?csdl_project_id=20814 "
        headers={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36','Content-Type':'application/json'}

        requests.adapters.DEFAULT_RETRIES = 3
        requests.Timeout = 10
        requests.allow_redirects = True
        print ("URL is:%s" % url)
        response = requests.get(url, headers, auth=HTTPBasicAuth(self.username, self.password ))

        #exp_str = r'(\d{6},\d{4},PHONE,'+self.branch_name+',)'
        #pattern_all = re.compile(exp_str,re.DOTALL)
       # print re.search(pattern_all,response.content).string      
        #count_overall = len(re.findall(pattern_all,self.content))
        print ('The response content  is: %s' % response.content)
        response.content


    def Vital_Signs(self):
        #url = '''https://wwwin-si.cisco.com/api/v1/project-summary/svs?csdl_project_id=20814 -H "Content-Type: application/json"  -u "ronling:weblxjhuQ~4" '''
        url = "https://wwwin-si.cisco.com/api/v1/project-summary/svs?csdl_project_id=20814"
        headers={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36','Content-Type':'application/json'}
    
        requests.adapters.DEFAULT_RETRIES = 3
        requests.Timeout = 10
        requests.allow_redirects = True
        print ("URL is:%s" % url)
        response = requests.get(url, headers, auth=HTTPBasicAuth(self.username, self.password ))

        #exp_str = r'(\d{6},\d{4},PHONE,'+self.branch_name+',)'
        #pattern_all = re.compile(exp_str,re.DOTALL)
       # print re.search(pattern_all,response.content).string     
        #count_overall = len(re.findall(pattern_all,self.content))
        print ('The response content  is: %s' % response.content)
        response.content



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
class PythonOrgSearch():
 
    def __init__(self):
        self.driver = webdriver.Chrome()
 
    def test_search_in_python_org(self):
        driver = self.driver
        #url = '''https://wwwin-si.cisco.com/projects/20814/?tab=PSB+Compliance -H "Authorization: Token c1650b7731df92b9476d543eb22c0db33bae06f0" -H "Content-Type: application/json" -H "Cookie: CP_GUTC=173.37.145.94.1495691556920061; OPTOUTMULTI=0:0%7Cc2:0%7Cc1:0; Apache=173.36.27.7.1525408804354666; AMCVS_B8D07FF4520E94C10A490D4C%40AdobeOrg=1; wasOnLoginPage=true; loginPageReferrer=; cdcUniqueKey=20j8fi3c8c12h; loginPageRef=; hbx_lid=no_id; CONSENTMGR=ts:1530152788010%7Cconsent:true; AMCV_B8D07FF4520E94C10A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C17711%7CMCMID%7C91593192566811968257887690656718648124%7CMCAID%7CNONE%7CMCOPTOUT-1530159988s%7CNONE%7CMCAAMLH-1530757588%7C9%7CMCAAMB-1530757588%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; s_fid=1CC5A38128270DBB-18A3E4D14488EE40; gpv_v9=cloudsso.cisco.com%2Fsp%2Fstartsso.ping; s_ptc=%5B%5BB%5D%5D; s_cc=true; s_ppvl=%5B%5BB%5D%5D; s_ppv=cloudsso.cisco.com%2Fsp%2Fstartsso.ping%2C89%2C34%2C821%2C1920%2C530%2C1920%2C1080%2C1%2CP; s_sq=%5B%5BB%5D%5D; utag_main=v_id:015c3e29fe9c0022684159ceac4004079003007100838$_sn:7$_ss:0$_st:1530154800773$vapi_domain:cisco.com$ses_id:1530152787972%3Bexp-session$_pn:1%3Bexp-session; wamsessiontracker=bGFzdGxvZ2luPTA2LzI4LzIwMTggMDI6MzA6Mjc=; authorization=loggedIn; ObSSOCookie=Vr6386w7xVfOBkcU1cEnRh3fyADEzCX2lguYB8TxTY3Yz6N6Ad%2B31vfpIq8tAmYG8zQN9RZ%2F5yOkTl7JenEnEPQwSXxvaFck%2BdiGtKK8a%2BItBm4KHRZRQ1qNMcVMLdRxA07REDfnR2RPe7gUs8Sm5ZE4zFDjFWyBsLr%2F6efR9RpedsfWcPs0xoyp%2B%2F500%2B%2BGC3vimOq%2FehXl%2BZfmslF%2F4V6XR7rGKxcGAbiWXcbrLINez2p90caY%2FJvZZ4hK3UdAQ4C07EeODp33gnIGdMUn0gF7WaqyfkaSGk6VSEBafq4GafpBjD9vWPb377K3HVuxOPE2M82MYplkg7uyCR5IhUnxKDEEBGnmO16SL2w0JQCetoTcD%2FppEKBaueRiBw0qWBZsGm6%2Bty0CBeiqQPs9Nj0qsZnK%2FgIwaF5%2BTVg3OvhzPvFjEXHPFoc4UrQoYN%2FnOBI3XSEjcNmpqC6Joo6nDtFXx%2FSXmkQMKUIC%2FaiLimnzNyZ4gf69M0PIC2qZni2c" -H "Content-Type: application/json"
#''' 
        url = '''"https://wwwin-si.cisco.com/api/v1/project-summary/csdl?csdl_project_id=20814"  -u "ronling:weblxjhuQ~4"'''

        driver.get(url) #"http://www.python.org")
        # self.assertIn("Python", driver.title)
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source


        print(driver.page_source)
        #elem = driver.find_element_by_name("Project")
        #print(elem)
 
    def __del__(self):
        self.driver.close()
 


if __name__ == '__main__':
    # csdl_info = CSDLInfo('ronling','weblxjhuQ~4')
    # csdl_info.PSB_Compliance()
    # csdl_info.CSDL_Process()
    # csdl_info.Vital_Signs()

    info = PythonOrgSearch()
    info.test_search_in_python_org()






    
