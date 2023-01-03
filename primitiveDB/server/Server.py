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

from flask import Flask, request
import flask.cli
import logging
import os
from sys import platform
import cpuinfo
import time
import hashlib

__global_vars__ = {"db_file":"",
                   "db_ip":"0.0.0.0",
                   "db_port":"8080",
                   "db_acess_key":None,
                   "db_headers":{"col0",
                                 "col1"},
                   "Server_name":__name__}

class init():
    def __init__(self):
        """
        The __init__ function is called when the class is instantiated.
        It initializes the global variables and sets up logging.
        
        Param:
            self: Reference the object itself
        Return:
            A reference to the object that it creates
        """
        global __global_vars__
        self.__global_vars__ = __global_vars__
        
    def db(self,file) -> open:
        """
        The columns function is used to create a list of column names for the database.
        The first argument is a list of strings that are the column names.
        This function will return an empty list if no arguments are passed.
        
        Param(s):
            self: Access the class attributes
            headers: Set the headers of the columns in a database
        Return:
            A list of the headers in the database
        """    
        self.__global_vars__["db_file"] = file

    
    def auth(self,key) -> str:
        """
        The auth function is used to authenticate the user.
        It takes a key as an argument and returns a string.
        
        Param(s):
            self: Reference the class object
            key: Authenticate the user
        Return: 
            A hash of the key
        """
        
        self.__global_vars__["db_acess_key"] = hashlib.sha256(key.encode('utf-8')).hexdigest()
    
    def uri(self,ip,port) -> tuple:
        """
        The uri function is used to set the ip and port of the database.
        It takes two arguments, an ip address and a port number.
        
        
        Param(s):
            self: Access variables that belongs to the class
            ip: Set the ip address of the database
            port: Specify the port number to connect to
        Return: 
            A tuple containing the ip and port of the database
        """
        
        self.__global_vars__["db_ip"] = ip
        self.__global_vars__["db_port"] = port
    
    def columns(self,headers) -> list:
        """
        The columns function is used to create a list of column names for the database.
        The function takes in a list of headers and returns a list of column names.
        
        Param(s):
            self: Access the class attributes
            headers: Set the headers of the database
        Return:
            The list of headers
        """
        
        self.__global_vars__["db_headers"] = headers
            
    def id(self,id) -> id:
        """
        The id function is used to set the server name.
        It takes one argument, id, which is a string that will be used as the server name.
        
        Param(s):
                self: Refer to the object itself
                id: Set the server name
        Return: 
            The id of the server
        """
        
        self.__global_vars__["Server_name"] = id
    

class run():
    def __init__(self):
        """
        The __init__ function is called when the class is instantiated. It initializes all of the variables and sets up any
        default behavior that you want to happen automatically whenever a new instance of your class is created.
        
        
        Param: 
            self: Access variables that belongs to a class
        """
        global __global_vars__
        global __protcs__
        self.cpu = str(cpuinfo.get_cpu_info()["brand_raw"])
        self.ip = __global_vars__["db_ip"]
        self.port = __global_vars__["db_port"]
        self.database_file = __global_vars__["db_file"]
        self.acess_key = __global_vars__["db_acess_key"] if isinstance(__global_vars__["db_acess_key"],list) else [__global_vars__["db_acess_key"]]
        self.serv_name = __global_vars__["Server_name"] if __global_vars__["Server_name"]!=None else __name__ 
        self.headers = __global_vars__["db_headers"]
        self.index_HTML = '<html>\n    <body>\n    <p>\n        <form method="POST" action="/test"></form>\n        <form method="GET" action="/test"></form>\n    </p>\n    </body>\n</html>'
        self.last_synced = 0
        self.GMT = None
        self.__RUN__()
       
        
    def __RUN__(self):
        """
        The __RUN__ function is used to start the server. It takes no arguments and returns nothing.
        
        Param:
            self: Access variables that belongs to the class
        Return: 
            The output of the command &amp;quot;clear&amp;quot; on linux and windows
        """
        
        def _log():
            """
            The _log function is used to clear the terminal and print out a message
            indicating which server is running on which port. It takes no arguments.
            
            Return: 
                    The output of the command &quot;clear&quot; on linux and windows
            """
            
            OS = {"linux":"clear","linux2":"clear",
                  "win32":"cls","cygwin":"cls"}
            os.system(OS[platform])
            print(f"\033[92m* Running {self.serv_name} on {self.ip}:{self.port}\033[0m\n\n")

        def _update_GMT():
            """
            The _update_GMT function updates the GMT variable with the current time.
            The function is called by _update_time() and is not meant to be used on its own.

            Return: 
                The current time in gmt
            """
            gmt = time.gmtime(time.time())
            self.GMT = f"{gmt.tm_hour}:{gmt.tm_min}:{gmt.tm_sec}"
            return self.GMT
        
        database_serv = Flask(self.serv_name)
        logging.getLogger('werkzeug').disabled = True
        flask.cli.show_server_banner = lambda *args: None
        _log()
      
        fltr = filter(lambda line:(line!= ""), open(self.database_file,"r").read().split("\n"))
        if len([line for line in fltr])<=0:
            open(self.database_file,"w").write(",".join([j[1:-1] for j in str(self.headers)[1:-1].split(", ")])+"\n")
            
        @database_serv.route("/", methods=["POST","GET"])
        def main():
            """
            The main function of the server.
            
            Return: 
                Unsucessful: The index.html
                Sucessful: 
                          GET:
                                The database
                          POST:
                                The time the server last synced
            """
            if request.method == "GET":
                packet = request.args.to_dict()
                try:
                    auth_key = packet["auth"]
                    if auth_key in self.acess_key:
                        command = packet["command"]
                        if command == 'POST':
                            print(f"\033[0;33m* Server was changed @{_update_GMT()}\033[0m")
                            open(self.database_file,"w").write(packet["data"])
                            self.last_synced = self.GMT
                            return f"Server last synced @{self.last_synced}"
                            
                        elif command == 'GET':
                            print(f"\033[0;33m* Server was read @{_update_GMT()}\033[0m")
                            return open(self.database_file,"r").read()
                        else:
                            return f"Connected to `{self.serv_name}`"
                    else:
                        return f"<!> False authorization to acess `{self.serv_name}`"
                except KeyError:
                    return self.index_HTML
                    
            return self.index_HTML            
        
        """
        These functions are for future features that'll be added or to ping the server
        """
        @database_serv.route("/data", methods=["POST","GET"])
        def sys_data():
            if request.method == "GET":
                try:
                    if request.args.to_dict()["auth"]==self.acess_key:
                        required_data = {"Processor":self.cpu,
                                         "Server-name":self.serv_name,
                                         "Ip":self.ip,
                                         "Port":self.port,
                                         "Db size":os.path.getsize(self.database_file)}
                        
                        return "\n<br>\n".join([i+":"+str(required_data[i]) for i in required_data])
                    else:
                        return f"<!> False authorization to acess `{self.serv_name}`"        
                except:
                    return f"<!> False authorization to acess `{self.serv_name}`"
            else:
                return f"<!> False authorization to acess `{self.serv_name}`"

        @database_serv.route("/primitive_DB_check", methods=["POST","GET"])
        def check():
          return "True"
          
        database_serv.run(host=self.ip,port=int(self.port))

init = init()