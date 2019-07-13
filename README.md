# simplest-web
Simplest python http server for test, bind with dockerhub, auto build docker

### Function
Write host info in file `index.html`, include the following host infos:
    1. hostname
    2. local ip
    3. LAN ip
    4. public ip

### Run by docker

`docker run -d -p 8000:8000 --name simple-web kunka/simplest-web:v0.1`

### Run by manully

`python host_info.py && python -m http.server`

