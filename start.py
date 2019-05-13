import http.server
import socketserver

HOST = "localhost"
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print("Stating at", HOST, "with port", PORT)
    try:
	    httpd.serve_forever()
    except KeyboardInterrupt: 
	    pass

http.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))