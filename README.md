#部署方式
##Nginx <--> gunicorn <--> blog <--> sqlite
##Nginx负责分发请求：
      ###Browser
           |
           |  url = /static/
      ### Nginx
           |  url = /
           |
      ###gunicore

#http://wangke.tech
