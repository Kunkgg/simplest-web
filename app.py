"""
simple web app
only handle GET method and response the basical client, server and http headers info.
"""
from http.server import BaseHTTPRequestHandler
from urllib import parse
from host_info import get_host_info


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        server_info = get_host_info()
        message_parts = [
            'CLIENT VALUES:',
            'client_address={} ({})'.format(
                self.client_address,
                self.address_string()),
            'command={}'.format(self.command),
            'path={}'.format(self.path),
            'real path={}'.format(parsed_path.path),
            'query={}'.format(parsed_path.query),
            'request_version={}'.format(self.request_version),
            '',
            'SERVER VALUES:',
            'hostname={}'.format(server_info.get('hostname')),
            'server_version={}'.format(self.server_version),
            'sys_version={}'.format(self.sys_version),
            'protocol_version={}'.format(self.protocol_version),
            'ip_local={}'.format(server_info.get('ip_local')),
            'ip_LAN={}'.format(server_info.get('ip_LAN')),
            'ip_public={}'.format(server_info.get('ip_public')),
            '',
            'HEADERS RECEIVED:',
        ]
        for name, value in sorted(self.headers.items()):
            message_parts.append(
                '{}={}'.format(name, value.rstrip())
            )
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8000), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()

