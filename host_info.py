"""
Write host info in file index.html.
Include the following host infos:
    1. hostname
    2. local ip
    3. LAN ip
    4. public ip
"""
import socket
import urllib.request


def get_host_info():
    """get host infos, return dict"""
    hostname = socket.gethostname()
    ip_local = socket.gethostbyname(socket.gethostname())

    return {
            'hostname': hostname,
            'ip_local': ip_local,
            'ip_LAN': get_ip_lan(),
            'ip_public': get_ip_public()
            }

def make_html(info, tag='h3'):
    """write infos in simple html tag, return string"""
    html = ''
    for key, value in info.items():
        line = f"<{tag}>{key} : {value}</{tag}>\n"
        html += line
    return html

def get_ip_lan():
    """get LAN ip by socket connect to google DNS server(8.8.8.8), return string"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 53))
        result = s.getsockname()[0]
    except:
        result = "Can't get LAN IP"
    finally:
        return result

def get_ip_public():
    """get public ip by request(ident.me), return string"""
    try:
        result = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    except:
        result = "Can't get Public IP"
    finally:
        return result

def write_web_page(filepath, content):
    """write content in the special file"""
    with open(filepath, 'w') as f:
        f.writelines(content)

if(__name__ == '__main__'):
    filepath = 'index.html'
    write_web_page(filepath, make_html(get_host_info()))
    

