# -*- coding: utf-8 -*-
#
# ------------------------------------------------------------
#  Copyright (c) 2023 AIS Servis, s.r.o.
#  This software is the proprietary information of AIS Servis, s.r.o.
#  All Right Reserved.
#  ------------------------------------------------------------
#
import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime

host_name = os.getenv('SERVER_HOST', '0.0.0.0')
server_port = os.getenv('SERVER_PORT', 8080)

class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        print('xxxx')
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytes("\n".join([
            f'Host: {socket.gethostname()}',
            f'Time: {datetime.now()}',
            f'Docker image: {os.getenv("DOCKER_IMAGE", default="")}',
        ]) + '\n', 'utf-8'))

if __name__ == '__main__':
    web_server = HTTPServer((host_name, server_port), MyServer)
    print('Server started http://%s:%s' % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print('Server stopped.')