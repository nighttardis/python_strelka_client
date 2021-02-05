#Python Strelka Client

This is a simple Python library created to integrate [Strelka](https://target.github.io/strelka) created by Target. 
This code is based off Target's oneshot code written in Golang.

## Example Usage
```python
from python_strelka_client import python_strelka_client

strelkaclient = python_strelka_client.PythonStrelkaClient(
    url='192.168.73.128:57314'
)

responses = strelkaclient.scanfile(filename='/home/nighttardis/dc932c886dbf8fdef4417bf34fddc08c89203f31f70a4e0049deca801fae4f67.exe')

for response in responses:
    print(response.id)
    print(response.event)
```

## Library Information

### PythonStrelkaClient

Parameter | Description | Default Value | Required
----------|-------------|---------------|---------
url|Host and Port of Strelka Frontent| | Yes
clientname|Client Name that will show up in Strelka Logs|python-client|No
hostname|Hostname of machine|socket.gethostname()|No

### scanfile

#### Returns: gRPC response

Parameter | Description | Default Value | Required
----------|-------------|---------------|---------
filename|File to send to strelka including full path| |Yes
delay|Delay between sending `chunk`s| 0 | No
chuck|Size of data (in bytes) to send per request| 32768 | No
timeout|How long to wait for response from Strelka (in seconds)| 60 |No