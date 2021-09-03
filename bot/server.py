#!/usr/bin/env python3
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from cgi import FieldStorage

from .arguments import args
from .logger import logger
from . import forms
from . import redirection


class ReCaptchaRequestHandler(BaseHTTPRequestHandler):
  success_count = 0
  failure_count = 0

  def log_request(self, code):
    pass  # Disables built-in logging

  def _serve_captcha(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    try:
      with open(os.path.join(os.path.dirname(__file__), './static/captcha.html'), 'r') as html_file:
        self.wfile.write(bytes(html_file.read(), 'utf-8'))
    except IOError as error:
      logger.error('Unable to open ./static/captcha.html for reading.')
      logger.debug(error)

  def do_GET(self):
    logger.debug('GET request received.')
    self._serve_captcha()

  def do_POST(self):
    logger.debug('POST request received.')
    # Parse the form data posted
    form = FieldStorage(
      fp=self.rfile, headers=self.headers, environ={
        'REQUEST_METHOD': 'POST',
        'CONTENT_TYPE': self.headers['Content-Type'],
      }
    )

    # Utilize the reCaptcha token against the target
    token = form.getvalue('g-recaptcha-response')
    if token:
      logger.debug('g-recaptcha-response received: {}'.format(token))

      success = forms.anonymous_form(token)
      if success:
        print('Form successfully submitted!')
        self.success_count += 1

        if args.count != None and self.success_count >= args.count:
          print(
            'Shutting dowin with {} success{}, {} failure{}.'.format(
              self.success_count, '' if self.success_count == 1 else 'es', self.failure_count, '' if self.failure_count == 1 else 's'
            )
          )
          shutdown_thread = threading.Thread(target=self.server.shutdown)
          shutdown_thread.daemon = True
          shutdown_thread.start()
          return
      else:
        print('Form failed to submit.')
        self.failure_count += 1

      logger.info(
        '{} success{}, {} failure{}'.format(
          self.success_count, '' if self.success_count == 1 else 'es', self.failure_count, '' if self.failure_count == 1 else 's'
        )
      )
    else:
      logger.warning('No g-recaptcha-response received.')

    # Send the user back to the reCaptcha page to solve the challenge again
    self._serve_captcha()


def serve():
  redirection.redirect()

  server_address = ('', 8000)
  httpd = HTTPServer(server_address, ReCaptchaRequestHandler)
  print('Starting the web server at http://prolifewhistleblower.com:8000/')
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    print()
    print('Ctrl+C received, shutting down the web server.')
  finally:
    httpd.socket.close()
    redirection.end_redirect()


if __name__ == '__main__':
  serve()
