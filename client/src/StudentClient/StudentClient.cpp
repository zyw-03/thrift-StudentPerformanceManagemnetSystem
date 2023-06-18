#include <iostream>

#include <thrift/protocol/TBinaryProtocol.h>
#include <thrift/transport/TSocket.h>
#include <thrift/transport/TTransportUtils.h>

#include "ScoreServer/ScoreManagement.h"

using namespace std;
using namespace apache::thrift;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;
using namespace ::ScoreServer;

int main() {
	std::shared_ptr<TTransport> socket(new TSocket("127.0.0.1", 8200));
	std::shared_ptr<TTransport> transport(new TBufferedTransport(socket));
	std::shared_ptr<TProtocol> protocol(new TBinaryProtocol(transport));
	ScoreManagementClient client(protocol);

	try {
		transport->open();
		int id, score;
		string name, course;
		printf("请先绑定如下信息:\n");
		printf("学号:");
		cin >> id;
		
		printf("姓名:");
		cin >> name;

		while (true){
			printf("请输入你要查询的科目(输入exit退出):");
			cin >> course;
			if (course == "exit"){
				printf("Bye");
				break;
			}	
			else	score = client.get(id, name, course, "");
			if(score == -1)	printf("你该科目暂无分数\n");
			else	cout << "科目:" << course << " 成绩:" << score <<endl;
        	}		
		transport->close();
	} catch (TException& tx) {
		cout << "ERROR: " << tx.what() << endl;
	}
}
