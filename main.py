# -*- coding: utf-8 -*-
#Created on 2022年10月24日
#@author: One

# -*- coding: utf-8 -*-
#Created on 2021年10月28日
#@author: One


from tools import get_soup
import re
from tools import mail,send_wechat_message
import time


html = get_soup('https://newstock.cfi.cn/#table_kzzfx')
#html2 = get_soup('https://api.ghser.com/qinghua/')
html2 = get_soup('https://v1.hitokoto.cn/?c=a&c=b&c=c&c=d&c=h&c=i&c=k&encode=text')
print(type(html2))
print('html2')
#print(html2.html.body.p.text)
#print(html.find_all("table",class_="t_content",style=False)[1])
jijing_html = html.find_all("table",class_="t_content",style=False)[1]
#print(jijing_html.find_all('tr'))
body='''<!DOCTYPE html>
<html>
<head>
  <title>Bootstrap5 实例</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.staticfile.org/twitter-bootstrap/5.1.1/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.staticfile.org/twitter-bootstrap/5.1.1/js/bootstrap.bundle.min.js"></script>
</head>

<body>
<div class="container mt-3">
  <h2>今日可打新基金提醒</h2>
  <p>Good Luck !</p>            
  <table class="table">

    <thead>
      <tr>
        <th>基金名称</th>
        <th>中签率</th>
        <th>发行金额</th>
      </tr>
    </thead>
       
    <tbody>'''
run_or_not = 'not'
for i in jijing_html.find_all('tr'):
    if i.find_all('font',color="red"):
    #if 1 ==1:
        #print(i.find_all('td'))
        run_or_not = 'run'
        j = i.find_all('td')
        print('j')
        print(j)
        
        #for k in j:
            #print(k)
            
        body = body+"""
                    
                      <tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                      </tr>
                     """ %(j[0].text,j[6].text,j[4].text)
                        

body =   body +""" </tbody>
  </table>
</div>

</body>
</html>"""       
##################################################################################
title = '有今日新债券，记得打新哦！'
html =  body

try:
    print(run_or_not)
    time.sleep(2)
    if run_or_not=='run':
        send_wechat_message(title,html)
    else:
        print('今天没有发行新债券')
        pass
except:
    pass     
        
        
        
        
        
        
        
        
