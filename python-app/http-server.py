# -*- coding: utf-8 -*-
#
# ------------------------------------------------------------
#  Copyright (c) 2023 AIS Servis, s.r.o.
#  This software is the proprietary information of AIS Servis, s.r.o.
#  All Right Reserved.
#  ------------------------------------------------------------
#
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("\n".join([
            f'Host: {socket.gethostname()}',
            f'Time: {datetime.now()}',
            f'Version: v1',
        ]) + '\n', 'utf-8'))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")