class A:
    def __init__(self, headers=''):
        self.api_headers = headers
    @property
    def api_headers(self):
        return self.__headers
    
    @api_headers.setter
    def api_headers(self, val):
        self.__headers = val

class B(A):
    @property
    def api_headers(self):
        return super().api_headers
    
    @api_headers.setter
    def api_headers(self, x):
        headers = {
            "Content-Type": "application/json",
        }
        return super(B, type(self)).api_headers.fset(self, headers)

# class C(B):
#     @B.api_headers.setter
#     def api_headers(self):
#         headers = {
#             "Content-Type": "multipart/form-data",
#         }
#         return super().api_headers(headers)

aa = A()
print(aa.api_headers)

bb = B()
print(bb.api_headers)

# cc = C()
# print(cc.api_headers)