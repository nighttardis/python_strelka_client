import grpc
import socket
import os
import time

import python_strelka_client.protocals.strelka_pb2 as strelka_pb2
import python_strelka_client.protocals.strelka_pb2_grpc as strelka_pb2_grpc


class PythonStrelkaClient:
    def __init__(self, url: str, clientname: str = "python-client", hostname: str = ""):
        """

        :param url: Host:Port for gRPC Connection
        :param clientname: Client name to pass to Strelka
        :param hostname: Hostname to pass to Strelka (will default to socket.gethostname() if not provided)
        """
        self.url = url
        self.channel = grpc.insecure_channel(self.url)
        self.stub = strelka_pb2_grpc.FrontendStub(self.channel)
        self.clientname = clientname
        if hostname != "":
            self.hostname = hostname
        else:
            self.hostname = socket.gethostname()

    def __readfile(self, filename: str, chunk: int) -> bytes:
        """
        Read file a chunk at the time, prevents having to load the entire file in memory if the file is large but can
        still read the entire file by continued calls to the function.

        :param filename: full path to the file to read
        :param chunk: Size of the chuck (in bytes) to read per call
        :return: chuck size of file
        """
        with open(filename, 'rb') as binary_file:
            while True:
                data = binary_file.read(chunk)
                if not data:
                    break
                yield data

    def __scanfile(self, filename: str, file: bytes, delay: int = 0) -> strelka_pb2.ScanResponse:
        """
        Create the request and send the file in chucks to Strelka

        :param filename: Name of the file to include in request to Strelka. If full path to file will split on '/' and take the last element.
        :param file: Binary data of file to loop through and send
        :param delay: Amount of time to wait between sending chunks of data
        :return: Strelka gRPC Scan Response
        """
        request = strelka_pb2.Request(
                client=self.clientname,
                source=self.hostname,
                gatekeeper=False
            )
        attributes = strelka_pb2.Attributes(
            filename=filename.split('/')[-1]
        )
        for data in file:
            yield strelka_pb2.ScanFileRequest(request=request, attributes=attributes, data=data)
            time.sleep(delay)

    def scanfile(self, filename: str, delay: int = 0, chunk: int = 32768, timeout: int = 60):
        """
        Creates stream to Strelka use gRPC to submit the file to be scanned

        :param filename: Full path to file to be sent to Strelka
        :param delay: Ammount of time to wait between sending chunks of data
        :param chunk: Size (in btyes) to break up the file
        :param timeout: How long to wait for response from Strelka
        :return: Strelka gRPC Scan Response
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Unable to find {filename}")
        return self.stub.ScanFile(self.__scanfile(filename=filename,
                                                  file=self.__readfile(filename=filename, chunk=chunk), delay=delay),
                                  timeout=timeout)
