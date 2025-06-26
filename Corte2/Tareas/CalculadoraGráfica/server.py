import http.server
import socketserver

PORT = 8000

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin']

with socketserver.TCPServer(('', PORT), handler) as httpd:
    print(f"Servidor corriendo en http://localhost:{PORT}")
    httpd.serve_forever()
