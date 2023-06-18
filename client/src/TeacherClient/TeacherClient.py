from ScoreServer import ScoreManagement
from ScoreServer.ttypes import Student

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from sys import stdin


def operate():

    transport = TSocket.TSocket('127.0.0.1', 8200)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = ScoreManagement.Client(protocol)

    # Connect!
    transport.open()

    for line in stdin:
        op, student_id, student_name, course, score = line.strip().split(' ')
        student = Student(int(student_id), student_name, course, int(score))

        if op == 'add':
            x = client.add(student, '')
            if x == 0:
                print(f"学号:{student.id} 姓名:{student.name} 课程:{student.course} 成绩:{student.score}")
            else:
                print(f"学号为{student.name}的同学的{student.course}已有成绩")
                print("若需要修改，请先删除再重新添加")

        elif op == 'remove':
            x = client.remove(student, '')

            if x == 0:
                print(f"已删除学号为{student.id},名字为{student.name}的{student.course}的成绩")

        elif op == 'get':
            x = client.get(int(student_id), student_name, course, '')
            print(x)
        else:
            print("输入有误,请重新输入")

    transport.close()


if __name__ == '__main__':

    operate()
