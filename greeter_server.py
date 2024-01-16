from concurrent import futures
import logging

import grpc
import testProcess_pb2
import testProcess_pb2_grpc


class TestProcess(testProcess_pb2_grpc.TestProcessServicer):
    def TestHello(self, request, context):
        return testProcess_pb2.TESTReply(name="Hello, %s!" % request.feature)


def serve():
    port = "4000"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    testProcess_pb2_grpc.add_TestProcessServicer_to_server(TestProcess(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
