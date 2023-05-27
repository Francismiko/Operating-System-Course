import fs from 'fs';

// 读取文件
const fileContent = fs.readFileSync('./coures-1/src/app/test.txt', 'utf8');

// 将文件内容转换为字符串
let text = fileContent.toString();

// 替换非单词字符为空格
text = text.replace(/[^a-zA-Z ]/g, ' ');

// 将字符串转换为单词数组 
let words = text.split(' ');  

// 过滤空数组项
words = words.filter((word: string) => word != '');

// 统计单词总数
const wordCount = words.length;

// 输出结果到控制台
console.log(`The text contains ${wordCount} words.`);

// 将结果写入文件
fs.writeFileSync('./coures-1/src/app/wordCount.txt', `${wordCount}`);
