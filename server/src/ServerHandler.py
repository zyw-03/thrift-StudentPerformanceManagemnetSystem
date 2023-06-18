from ScoreServer import ScoreManagement
from ScoreServer.ttypes import Student
import mysql.connector


class ServiceHandler(ScoreManagement.Iface):

    def add(self, student, info):
        try:
            cnx = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='zyw030303',
                database='myData'
            )

            i = f"insert into student values ({student.id}, '{student.name}', '{student.course}', {student.score}) "
            cursor = cnx.cursor()

            cursor.execute(i)
            cnx.commit()
            print(f"添加了学号为{student.id}, 姓名为{student.name}的{student.course}课程分数{student.score}")
            cursor.close()
            cnx.close()
            return 0

        except mysql.connector.Error:
            return 1

    def remove(self, student, info):
        try:
            cnx = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='zyw030303',
                database='myData'
            )

            cursor = cnx.cursor()
            i = f"delete from student where id={student.id} and name='{student.name}' and course='{student.course}' "

            cursor.execute(i)
            cnx.commit()
            print(f"删除了学号为{student.id},姓名为{student.name}的{student.course}的成绩")
            cursor.close()
            cnx.close()
            return 0
        except mysql.connector.Error:
            print(mysql.connector.Error)

    def get(self, id, name, course, info):
        try:
            cnx = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='zyw030303',
                database='myData'
            )

            cursor = cnx.cursor()

            q = f"select score from student where id={id} and name='{name}' and course='{course}'"
            cursor.execute(q)

            result = cursor.fetchall()

            cursor.close()
            cnx.close()
            print(f"学号为{id}的{name}同学查询了{course}的成绩")
            if len(result) == 0:
                return -1
            else:
                return result[0][0]
        except mysql.connector.Error:
            print(mysql.connector.Error)



