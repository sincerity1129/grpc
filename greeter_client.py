from __future__ import print_function

import logging

import grpc
from pb2file import testProcess_pb2
from pb2file import testProcess_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:4000") as channel:
        stub = testProcess_pb2_grpc.TestProcessStub(channel)
        response = stub.TestHello(testProcess_pb2.TESTRequest(feature="start"))
    print("Greeter client received: " + response.name)


if __name__ == "__main__":
    logging.basicConfig()
    run()
