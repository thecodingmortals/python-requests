# Standard Library
import json

# Third Party Stuff
import requests

from .base import BaseHTTPRequest

class FileBaseHTTPRequest(BaseHTTPRequest):
    def __init__(self, api_URL, data=dict(), api_headers=dict(), x_auth_token=None, x_auth_client=None, query_dict=None) -> None:
        """initialize method for the class"""
        if not api_headers: api_headers = {
            "Content-Type": "multipart/form-data",
        }
        super().__init__(api_URL, data, api_headers, x_auth_token, x_auth_client, query_dict)

    @property
    def files(self):
        """getter property for API data"""
        return self.__files

    @files.setter
    def files(self, val):
        """setter property for API data"""
        self.files = val if val else [
            (self.file_key, open(self.filename,'rb'))
        ]
    
    def send_http_POST_request(self):
        """method to send an HTTP POST request"""
        return requests.post(
            self.api_URL, data=json.dumps(self.data), files=self.files, headers=self.headers
        )
    
    def send_http_PUT_request(self):
        """method to send an HTTP PUT request"""
        return requests.put(
            self.api_URL, data=json.dumps(self.data), files=self.files, headers=self.headers
        )
