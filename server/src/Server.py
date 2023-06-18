
from ScoreServer import ScoreManagement
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from ServerHandler import ServiceHandler


def main():
    handler = ServiceHandler()
    processor = ScoreManagement.Processor(handler)
    transport = TSocket.TServerSocket(port=8200)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
    print("Starting the server...")
    server.serve()


if __name__ == '__main__':
    main()
