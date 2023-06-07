import numpy as np

def is_safe_state(max_resources, allocated_resources, need_resources, available_resources):
    num_processes, num_resources = max_resources.shape

    work = available_resources.copy()
    finish = np.zeros(num_processes, dtype=bool)
    need = need_resources.copy()
    allocation = allocated_resources.copy()

    while True:
        found = False
        for i in range(num_processes):
            if not finish[i] and np.all(need[i] <= work):
                work += allocation[i]
                finish[i] = True
                found = True

        if not found:
            break

    return np.all(finish)


def resource_allocation(max_resources, allocated_resources, need_resources, available_resources, process_index, request):
    len(max_resources[0])

    if np.all(request <= need_resources[process_index]) and np.all(request <= available_resources):
        available_resources -= request
        allocated_resources[process_index] += request
        need_resources[process_index] -= request

        if is_safe_state(max_resources, allocated_resources, need_resources, available_resources):
            return True, allocated_resources, need_resources, available_resources
        else:
            # 回滚操作，将资源分配还原
            available_resources += request
            allocated_resources[process_index] -= request
            need_resources[process_index] += request
            return False, allocated_resources, need_resources, available_resources
    else:
        return False, allocated_resources, need_resources, available_resources


def print_resource_state(resource_state, title):
    print(f"{title}:")
    print("   A  B  C")
    for i, row in enumerate(resource_state):
        print(f"P{i}  {row[0]}  {row[1]}  {row[2]}")


def main():
    # 资源情况
    max_resources = np.array([[7, 5, 3],
                              [3, 2, 2],
                              [9, 0, 2],
                              [2, 2, 2],
                              [4, 3, 3]])
    allocated_resources = np.array([[0, 1, 0],
                                    [2, 0, 0],
                                    [3, 0, 2],
                                    [2, 1, 1],
                                    [0, 0, 2]])
    need_resources = max_resources - allocated_resources
    available_resources = np.array([10, 5, 7])

    # 1. 检测T0时刻系统是否处于安全状态
    safe_state = is_safe_state(max_resources, allocated_resources, need_resources, available_resources)
    if safe_state:
        print("The system is in a safe state at time T0")
    else:
        print("The system is not in a safe state at time T0")

    # 2. P1发出请求向量Request1(1, 0, 2)，系统能否将资源分配给它
    request = np.array([1, 0, 2])
    process_index = 1  # P1的索引为1

    success, new_allocated, new_need, new_available = resource_allocation(max_resources, allocated_resources,
                                                                         need_resources, available_resources,
                                                                         process_index, request)
    if success:
        print("The system can allocate resources to P1")
        print_resource_state(new_allocated, "Allocated")
        print_resource_state(new_need, "Need")
        print_resource_state(new_available.reshape(1, -1), "Available")
    else:
        print("The system cannot allocate resources to P1")
        print("The resource allocation remains unchanged")


if __name__ == "__main__":
    main()
