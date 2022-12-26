from datetime import datetime
import logging
from django.utils.deprecation import MiddlewareMixin

import socket
import time
import json

request_logger = logging.getLogger("django.request")

class RequestLogMiddleware(MiddlewareMixin):
    """Request Logging Middleware."""

    def __init__(self, *args, **kwargs):
            """Constructor method."""
            super().__init__(*args, **kwargs)

    def process_request(self, request):
        """Set Request Start Time to measure time taken to service request."""
        if request.method in ['POST', 'PUT', 'PATCH']:
            request.req_body = request.body
        if str(request.get_full_path()).startswith('/'):
            request.start_time = time.time()

    def extract_log_info(self, request, response=None, exception=None):
        """Extract appropriate log info from requests/responses/exceptions."""
        try:
            log_data = {
                'remote_address': request.META['REMOTE_ADDR'],
                'server_hostname': socket.gethostname(),
                'request_method': request.method,
                'request_path': request.get_full_path(),
                'ip_address': request.META.get('REMOTE_ADDR'),
                'run_time': time.time() - request.start_time,
            }
            if request.method in ['PUT', 'POST', 'PATCH']:
                log_data['request_body'] = json.loads(
                    str(request.req_body))
                if response:
                    response_body = response.content
                    log_data['response_body'] = response_body

            with open("log_data.txt", 'a') as f:
                for key in log_data.keys():
                    f.write(f"{key}: {log_data[key]}" + "\n")
                f.write("Time: " + f"{datetime.now()}" + "\n" + "-"*50 + "\n")
            
            return log_data
        except json.JSONDecodeError:
            return None

    def process_response(self, request, response):
        """Log data using logger."""
        if str(request.get_full_path()).startswith('/'):
                log_data = self.extract_log_info(request=request,
                                                 response=response)
                request_logger.debug(msg='', extra=log_data)
        return response

    def process_exception(self, request, exception):
        """Log Exceptions."""
        try:
            raise exception
        except Exception:
            request_logger.exception(msg="Unhandled Exception")
        return exception
