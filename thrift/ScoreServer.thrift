namespace cpp ScoreServer

struct Student{
	1: i32 id;
	2: string name;
	3: string course;
	4: i32 score;

}

service ScoreManagement{

	i32 add(1: Student student, 2: string info),

	i32 remove(1: Student student, 2: string info),
	
	i32 get(1: i32 id, 2: string name, 3: string course, 4: string info),
}
