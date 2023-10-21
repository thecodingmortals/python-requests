# Standard Library
import json

# Third Party Stuff
import requests


class BaseHTTPRequest:
    def __init__(
        self, api_URL, data=dict(), api_headers=dict(), x_auth_token=None, x_auth_client=None, query_dict=None
    ) -> None:
        """initialize method for the class"""
        self.api_URL = api_URL
        if query_dict: self.set_query_parameters(query_dict)
        self.api_headers = api_headers
        self.set_x_auth_headers(x_auth_token, x_auth_client)
        self.data = data
        self.sendHTTPRequest()

    @property
    def api_URL(self):
        "getter property for API urls"
        return self.__api_url

    @api_URL.setter
    def api_URL(self, val):
        "setter property for api URLs"
        self.__api_url = val

    @property
    def api_headers(self):
        """getter property for API headers"""
        return self.__headers
    
    @api_headers.setter
    def api_headers(self, val):
        """setter for API headers"""
        self.__headers = val if val else {
            "Content-Type": "application/json",
        }

    def set_x_auth_headers(self, x_auth_token=None, x_auth_client=None):
        self.__headers["X-Auth-Token"] = x_auth_token
        if x_auth_client:
            self.__headers["X-Auth-Client"] = x_auth_client
    
    @property
    def data(self):
        """getter property for API data"""
        return self.__data

    @data.setter
    def data(self, data=dict()):
        """setter property for API data"""
        self.__data = data

    def send_http_GET_request(self):
        """method to send an HTTP GET request"""
        return requests.get(self.api_URL, headers=self.headers)

    def send_http_POST_request(self):
        """method to send an HTTP POST request"""
        return requests.post(
            self.api_URL, data=json.dumps(self.data), headers=self.headers
        )

    def send_http_PUT_request(self):
        """method to send an HTTP PUT request"""
        return requests.put(
            self.api_URL, data=json.dumps(self.data), headers=self.headers
        )

    def send_http_DELETE_request(self):
        """method to send an HTTP DELETE request"""
        pass

    def sendHTTPRequest(self):
        """method to send an HTTP request"""
        if self.__class__.__name__.startswith("Get"):
            response = self.send_http_GET_request()
        elif self.__class__.__name__.startswith("Create"):
            response = self.send_http_POST_request()
        elif self.__class__.__name__.startswith("Update"):
            response = self.send_http_PUT_request()
        elif self.__class__.__name__.startswith("Delete"):
            response = self.send_http_DELETE_request()
        self.json_response = response
    
    def get_json_response(self):
        print("RESPONSE", self.response.text)
        return self.response.text
    
    @property
    def json_response(self):
        """getter property for JSON response"""
        return self.__json_response

    @json_response.setter
    def json_response(self, response=dict()):
        """setter property for JSON response"""
        self.__json_response = response.text
    
    def set_query_parameters(self, query_dict):
        """setter for API URL query parameters"""
        self.api_URL += '?'
        for key, value in query_dict.items():
            self.api_URL += f'{key}={value}&'
        self.api_URL = self.api_URL[:-1]
