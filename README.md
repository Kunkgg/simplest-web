# simplest-web
Simplest python http server for test, bind with dockerhub, auto build docker

### Function

Only handle GET method and response the basical client, server and http headers info.

```
# Result demo
CLIENT VALUES:
client_address=('127.0.0.1', 55574) (127.0.0.1)
command=GET
path=/
real path=/
query=
request_version=HTTP/1.1

SERVER VALUES:
hostname=****                    # hostname of server
server_version=BaseHTTP/0.6
sys_version=Python/3.7.3
protocol_version=HTTP/1.0
ip_local=127.0.1.1               # local IP
ip_LAN=192.168.100.15            # LAN IP
ip_public=123.123.123.123        # public IP

HEADERS RECEIVED:
Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding=gzip, deflate, br
Accept-Language=en,zh-CN;q=0.9,zh;q=0.8
Connection=keep-alive
Host=localhost:8000
Upgrade-Insecure-Requests=1
User-Agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/75.0.3770.90 Chrome/75.0.3770.90 Safari/537.36
```

### Run by docker

`docker run -d -p 8000:8000 --name simple-web kunka/simplest-web:latest`

### Run by manully

`python app.py`

