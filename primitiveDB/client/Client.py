"""
Copyright 2023 Fahim Ferdous

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import httpx
import pandas
import io
import hashlib

class connect():
    def __init__(self,host:str):
        """
        The __init__ function is called when the class is instantiated.
        It initializes the attributes of an object, like a unique ID or connection.
        
        Param(s):
                self: Refer to the object itself
                host(str): Set the url of the primitveDB Server
        Return:
                The object itself
        """
        global __global_vars__
        self.url = host
        self.connected = httpx.get(self.url).status_code == 200
        if not self.connected:
            raise ConnectionError(f"Can't connect to `{self.url}`")
 
         
    def set_auth(self,authorization:str) -> str:
        """
        The set_auth function is used to set the authorization hash for a connection.
        It takes one argument, which is the user's authorization key. It then uses that
        key to generate an SHA256 hash and sets it as self.auth
        
        Param(s):
                self: Access the attributes and methods of the class in python
                authorization(str): Passes the authorization key to the set_auth function
        Return: 
                The handshake message
        """
        
        handshake = httpx.get(self.url,params={"auth":str(hashlib.sha256(authorization.encode('utf-8')).hexdigest()),
                                              "command":"Handshake"}).text
        if handshake.split(" ",1)[0] == "<!>":
            error = handshake.split(" ",1)[1]
            raise ConnectionRefusedError(error)
        else:
            self.auth = str(hashlib.sha256(authorization.encode('utf-8')).hexdigest())
            return handshake
    
        
    def fetch(self) -> pandas.DataFrame:
        """
        The fetch function is used to fetch data from the server.
        It takes a url and an auth key as parameters, and returns a pandas DataFrame.
        
        Param: 
            self: Access the attributes of the class
        Return:
                A pandas dataframe
        """
        
        Get = httpx.get(self.url,params={"auth":self.auth,
                                         "command":"GET"}).text
        return pandas.read_csv(io.StringIO(Get), sep=",")

  
    def insert(self, dataframe:pandas.DataFrame) -> str:
        """
        The insert function inserts a dataframe into the database.
        It returns the response from the server as a string.
        
        Param(s): 
            self: Access the variables and methods in the class
            dataframe:pandas.DataFrame: Pass the dataframe that is to be inserted into the database
        Return:
                The response from the server
        """
        
        Post = httpx.get(self.url,params={"auth":self.auth,
                                          "data":dataframe.to_csv(index=False),
                                          "command":"POST"}).text
        return Post 