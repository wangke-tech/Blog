<br>
##想看一下效果？[点我！点我！点我！](http://wangke.tech) :[http://wangke.tech/](http://wangke.tech/)
<br>
##部署方式
   ```Nginx <--> gunicorn <--> blog <--> sqlite```
###Nginx负责分发请求：
   ```
        Browser
           |
           |  url = /static/
         Nginx
           |  url = /
           |
        gunicore
   ```
###总结一下用到的服务有：

   ```
   Nginx：高性能Web服务器+负责反向代理；

   gunicorn：高性能WSGI服务器；

   gevent：把Python同步代码变成异步协程的库；

   Supervisor：监控服务进程的工具
   
   fabric: 自动化部署工具
   ```
