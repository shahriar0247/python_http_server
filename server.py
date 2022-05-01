import socket
from urllib import response
from wsgiref.handlers import format_date_time
import time
from datetime import datetime


def __init_socket():
    port = 8080
    server = socket.socket()
    server.bind(('', port))
    server.listen(5)
    print("Listening: http://localhost:" + str(port))
    return server


def send_response(html):
    now = datetime.now()
    date = str(format_date_time(time.mktime(now.timetuple())))
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nDate: "+date+"\r\nContent-Length: " + str(
        len(html)) + "\r\n\r\n" + html
    return response


def render_html(filename):
  file_ = open(filename, "r")
  data = file_.read()
  file_.close()
  return data

def main():
  server = __init_socket()
  while True:
      client, addr = server.accept()
      response = send_response(render_html("hello.html"))
      client.send(response.encode())

try:
  main()
except KeyboardInterrupt:
  print("Exiting")