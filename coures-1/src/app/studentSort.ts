export class Student {
  name: string;       
  Chinese: number;     
  Math: number;        
  English: number;   
  Physics: number;       
  Chemistry: number;     
  Biology: number;    
  total?: number;      
  avg?: number;  
  
  constructor(
    name: string,
    Chinese: number, 
    Math: number,
    English: number,
    Physics: number,
    Chemistry: number,
    Biology: number
  ) {
    this.name = name;
    this.Chinese = Chinese;
    this.Math = Math;
    this.English = English;
    this.Physics = Physics;
    this.Chemistry = Chemistry;
    this.Biology = Biology;
  }
}

// 生成随机学生信息
export function generateStudents(): Student[] {
  let students: Student[] = [];
  for (let i = 0; i < 45; i++) {
    students.push({
      name: `Student${i}`,
      Chinese: 0,
      Math: 0,
      English: 0,      
      Physics: 0,  
      Chemistry: 0,   
      Biology: 0
    });
  }
  return students;
}  

// 生成随机成绩
export function generateScore(students: Student[]) {
  for (let i = 0; i < students.length; i++) {
    students[i].Chinese = Math.floor(Math.random() * 101);
    students[i].Math = Math.floor(Math.random() * 101);
    students[i].English = Math.floor(Math.random() * 101);
    students[i].Physics  = Math.floor(Math.random() * 101);
    students[i].Chemistry = Math.floor(Math.random() * 101);
    students[i].Biology = Math.floor(Math.random() * 101);
  }
}

