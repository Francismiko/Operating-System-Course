import * as readlineSync from 'readline-sync';

let bootTime = new Date();
console.log("开机时间: ", bootTime.toLocaleString());

let count = 0;
let timer = 0;
let timeAlarm = readlineSync.question("请输入定时闹钟（毫秒）：");
let timeAlarmNumber = parseInt(timeAlarm, 10);

while (timeAlarmNumber > 0) {
  console.log("时钟中断，保存现场");

  timer++;
  timeAlarmNumber;

  console.log("处理器调度");

  console.log("开机时间: ", bootTime.toLocaleString(), " 定时闹钟: ", timeAlarm);

  if (++count % 10 == 0) {
    readlineSync.question("按任意键继续...");
    console.clear();
  }
}

let endTime = new Date(bootTime.getTime() + timer * 20000);
console.log("结束时间: ", endTime.toLocaleString());
