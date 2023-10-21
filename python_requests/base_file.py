# Standard Library
import json

# Third Party Stuff
import requests

# python_requests Stuff
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
        """
        getter property for API files to be sent in HTTP request
        
            Returns
            -------
                self.__files (list): returns a class attribute storing a list of files to upload.
        """
        return self.__files

    @files.setter
    def files(self, val):
        """
        setter property for API files to be sent in HTTP request
        
            Parameters
            ----------
                val (list): a list of files to be uploaded.
        """
        self.files = val if val else [
            (self.file_key, open(self.filename,'rb'))
        ]
    
    def send_http_POST_request(self):
        """
        method to send an HTTP POST request

            Returns
            -------
                response (object): returns response of an HTTP POST request.
        
        """
        return requests.post(
            self.api_URL, data=json.dumps(self.data), files=self.files, headers=self.headers
        )
    
    def send_http_PUT_request(self):
        """
        method to send an HTTP PUT request

            Returns
            -------
                response (object): returns response of an HTTP PUT request.
        """
        return requests.put(
            self.api_URL, data=json.dumps(self.data), files=self.files, headers=self.headers
        )
