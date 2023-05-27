#include <iostream>
#include <iomanip>
#include <ctime>

int main() {
    time_t bootTime = time(0);
    char* s_bootTime = ctime(&bootTime);

    int count = 0;
    int timer = 0;
    int timeAlarm;

    std::cout << "请输入定时闹钟（毫秒）：";
    std::cin >> timeAlarm;

    while (timeAlarm > 0) {
        std::cout << "时钟中断，保存现场" << std::endl;

        timer++;
        timeAlarm--;

        std::cout << "处理器调度" << std::endl;

        std::cout << std::left << std::setw(16) << "开机时间: " << s_bootTime;
        std::cout << std::left << std::setw(16) << "定时闹钟: " << timeAlarm << std::endl;

        if (++count % 10 == 0) {
            std::cout << "按任意键继续..." << std::endl;
            std::cin.ignore();
            std::cin.get();
            system("clear");
        }
    }

    std::cout << std::left << std::setw(16) << "结束时间: ";
    time_t endTime = bootTime + timer * 20;
    char* s_endTime = ctime(&endTime);
    std::cout << s_endTime;

    return 0;
}
