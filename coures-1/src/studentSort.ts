interface Student {
  name: string;
  score: number[];  // 6 个学科的成绩
  total: number;     // 总分
  avg: number;    // 平均分
}

// 生成随机成绩  
function generateScore() {
  let students: Student[] = [];
  
  for (let i = 0; i < 45; i++) {
    students.push({
      name: '学生' + i,
      score: [],
      total: 0,
      avg: 0
    });
  }
  
  for (let i = 0; i < 45; i++) {
    for (let j = 0; j < 6; j++) {
      students[i].score.push(Math.floor(Math.random() * 101));  // 0-100 的随机成绩
      students[i].total += students[i].score[j];
    }
    students[i].avg = students[i].total / 6;
  }
  
  return students;
}

// 对学生成绩进行排序(冒泡排序)
function sortScore(students: Student[]) {
  for (let i = 0; i < 44; i++) {
    for (let j = 0; j < 44 - i; j++) {
      if (students[j].total < students[j+1].total) {
        let temp = students[j];
        students[j] = students[j+1];
        students[j+1] = temp;
      }
    }
  }
}

// 打印所有学生信息  
function printScore(students: Student[]) {
  for (let i = 0; i < 45; i++) {
    console.log(`${students[i].name}: `);
    for (let j = 0; j < 6; j++) {
      console.log(`${students[i].score[j]}  `);
    }
    console.log(`总分: ${students[i].total} 平均分: ${students[i].avg}`);
  }
}

let students = generateScore();   // 生成随机成绩
sortScore(students);             // 按总分排序  
printScore(students);           // 打印所有学生成绩
