<h1 align="center">Primitive-Database (primitveDB)</h1>

<div align="center">

  ![logo](https://user-images.githubusercontent.com/79488582/183230798-31b73d18-3154-4928-b746-4e89ac9f486d.jpg)
  
</div>


# About PrimitiveDB
Primitive-Database is a lightweight databasing library written in Python3. It uses CSV(Comma Separated Values) file(s) to store data, making it easy to perform simple and minimalistic tasks with great and stable performance.


<br></br>

# Using PrimitiveDB

<h2>Server</h2>

<h3>Creating a simple vertical database</h3>

```python
from primitiveDB.server import Server

Server.init.db(<CSV FILE>)
Server.init.id(<SPEICAL ID FOR THE SERVER>)

Server.init.columns(["Name",       #Title for column 1
                     "Age",        #Title for column 2
                     "Address"])   #Title for column 3


Server.init.auth(<AUTHENTICATION KEY>)

#                  IP             PORT
Server.init.uri("0.0.0.0"    ,    8080) #Server IP is `http://localhost:8080` or `http://127.0.0.1:8080`

Server.run()
```

<br></br>

<h2>Client</h2>
<h3>Connecting to the database</h3>

```python
from primitiveDB.client import Client

DB = client.connect(<IP>)
DB.set_auth(<AUTHENTICATION KEY>)
```

<h3>Fetching data from the database</h3>

```python
from primitiveDB.client import Client

DB = client.connect(<IP>)
DB.set_auth(<AUTHENTICATION KEY>)


DB_data = DB.fetch() #returns a pandas.datafraem
print(DB_data)
```


<h3>Inserting data into the database</h3>

```python
from primitiveDB.client import Client

DB = client.connect(<IP>)
DB.set_auth(<AUTHENTICATION KEY>)


DB_data = DB.fetch()


DB_data["Name"] = ["Jack",           # Adding `Jack` to first row into Names
                   "James"]           # Adding `Jill` to second row into Names

DB_data["Age"] = [10,                 # Adding the age for `Jack` 
                  07]                 # Adding the age for  `James`
                  
DB_data["Adress"] = ["123 NAME ST",   # Adding the adress for `Jack`
                     "123 MAIN ST"]   # Adding the adress for `James`

DB.insert(DB_data)
```

