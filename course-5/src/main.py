class PageTableEntry:
    def __init__(self, frame_number=None, valid=False):
        self.frame_number = frame_number
        self.valid = valid


class PageTable:
    def __init__(self, page_table_size, frame_count):
        self.page_table_size = page_table_size
        self.page_table = [PageTableEntry() for _ in range(page_table_size)]

    def update_entry(self, page_number, frame_number, valid=True):
        self.page_table[page_number] = PageTableEntry(frame_number, valid)

    def get_entry(self, page_number):
        return self.page_table[page_number]


class Memory:
    def __init__(self, frame_count):
        self.frames = [None] * frame_count

    def read(self, frame_number):
        return self.frames[frame_number]

    def write(self, frame_number, data):
        self.frames[frame_number] = data


class PageFault(Exception):
    pass


class PageFaultHandler:
    def handle_page_fault(self, page_number):
        raise NotImplementedError("Page fault handling not implemented")


class SimplePageFaultHandler(PageFaultHandler):
    def __init__(self, memory):
        self.memory = memory

    def handle_page_fault(self, page_number):
        print("Page fault occurred for page", page_number)
        frame_number = page_number
        data = "Data for page " + str(page_number)
        self.memory.write(frame_number, data)
        return frame_number


class MMU:
    def __init__(self, page_table, memory, page_fault_handler):
        self.page_table = page_table
        self.memory = memory
        self.page_fault_handler = page_fault_handler

    def translate(self, logical_address):
        page_number, offset = divmod(logical_address, self.page_table.page_table_size)
        page_table_entry = self.page_table.get_entry(page_number)

        if page_table_entry.valid:
            frame_number = page_table_entry.frame_number
        else:
            frame_number = self.page_fault_handler.handle_page_fault(page_number)
            self.page_table.update_entry(page_number, frame_number, valid=True)

        physical_address = (frame_number * self.page_table.page_table_size) + offset
        return physical_address


# 模拟页表大小为16，物理内存有8个帧
page_table_size = 8
frame_count = 8

# 创建页表、内存和页错误处理器
page_table = PageTable(page_table_size, frame_count)
memory = Memory(frame_count)
page_fault_handler = SimplePageFaultHandler(memory)

# 创建MMU
mmu = MMU(page_table, memory, page_fault_handler)

# 示例用法
logical_address = 25
physical_address = mmu.translate(logical_address)
print("Logical address:", logical_address)
print("Physical address:", physical_address)
print("Data at physical address:", memory.read(physical_address))
