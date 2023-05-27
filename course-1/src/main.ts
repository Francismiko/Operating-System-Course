import { Student, generateStudents, generateScore } from './app/studentSort';
import { quickSort } from './utils/quickSort';

let students: Student[] = generateStudents();
generateScore(students);

// 计算总分和平均分
students.forEach(s => {
  let sum = 0;
  sum += s.Chinese;
  sum += s.Math;
  sum += s.English;
  sum += s.Physics;
  sum += s.Chemistry;
  sum += s.Biology;
  s.total = sum;
  s.avg = sum / 6;
});

// 使用快速排序算法对学生进行排序
students = quickSort(students);

// 打印成绩单表格
console.log('成绩单:');
console.table(students); 
