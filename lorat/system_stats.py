import psutil
import time
import platform as pfm
from threading import Thread, Lock
import matplotlib.pyplot as plt
import threading
import ctypes
import time
import timeit
import statistics
class thread_with_exception(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        total_ram = psutil.virtual_memory().total/10**9
        total_ram = str(round(total_ram, 2)) + " GB"
        self.platform_data = '\n'.join(["Python version: " + pfm.python_version(),
            "Python build: " + pfm.python_build()[1],
            "System: " + pfm.system(),
            "Platform: " + pfm.platform(),
            "Processor: " + pfm.processor(),
            "Total RAM: " + total_ram])
        self.process = psutil.Process()
        self.stop_recording = False
        self.lock = Lock()
        self.start_time = None
        self.time_record = None
        self.resources_record = None
        self.el_time = None
        self.start_time = None

    
    def _get_current_usage(self):
        RAM = psutil.virtual_memory()[2]
        CPU = psutil.cpu_percent()
        p_RAM = self.process.memory_percent()
        p_CPU = self.process.cpu_percent()
        return CPU, RAM, p_CPU, p_RAM
             
    def run(self):
        print('WTF')
        self.start_time = timeit.default_timer()
        time_record = []
        resources = []
        # target function of the thread class
        try:
            while True:
                time_record.append(timeit.default_timer())
                resources.append(self._get_current_usage())
                time.sleep(0.0001)
            
        finally:
            time_record.append(timeit.default_timer())
            resources.append(self._get_current_usage())
            self.el_time = time_record[len(time_record)-1] - self.start_time
            self.lock.acquire()
            self.time_record = time_record.copy()
            self.resources_record = resources.copy()
            self.lock.release()
            print('time stopped here')
            print('ended')
          
    def get_id(self):
 
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
  
    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')

        
    def get_elapsed_time(self):
        return self.el_time

    def plot_stats(self):
        print(len(self.time_record))
        CPU = []
        CPU_p = []
        time_r = []
        MEM = []
        MEM_p = []
        for (record, time_stamp) in zip(self.resources_record, self.time_record):
            CPU.append(record[0])
            CPU_p.append(record[2])
            MEM.append(record[1])
            MEM_p.append(record[3])
            time_r.append(time_stamp-self.start_time)

        plt.plot(time_r, CPU)
        print("CPU  ", statistics.mean(CPU))
        plt.show()
        plt.plot(time_r, CPU_p)
        print("CPU_p  ", statistics.mean(CPU_p))
        plt.show()
        plt.plot(time_r, MEM)
        plt.show()
        plt.plot(time_r, MEM_p)
        plt.show()

# class SystemStats:
#     def __init__(self):
#         total_ram = psutil.virtual_memory().total/10**9
#         total_ram = str(round(total_ram, 2)) + " GB"
#         self.platform_data = '\n'.join(["Python version: " + pfm.python_version(),
#             "Python build: " + pfm.python_build()[1],
#             "System: " + pfm.system(),
#             "Platform: " + pfm.platform(),
#             "Processor: " + pfm.processor(),
#             "Total RAM: " + total_ram])
#         self.process = psutil.Process()
#         self.stop_recording = False
#         self.lock = Lock()
#         self.start_time = None
#         self.time_record = None
#         self.resources_record = None
#         self.el_time = None

        
#     def _get_current_usage(self):
#         RAM = psutil.virtual_memory()[2]
#         CPU = psutil.cpu_percent()
#         p_RAM = self.process.memory_percent()
#         p_CPU = self.process.cpu_percent()
#         return CPU, RAM, p_RAM, p_CPU

#     def start(self):
#         t = Thread(target=self.record)
#         t.start()

#     def stop(self):
#         self.lock.acquire()
#         self.stop_recording = True
#         print("Will stop")
#         self.lock.release()

#     def record(self):
#         print('WTF')
#         self.start_time = time.time()
#         time_record = []
#         resources = []
#         while True:
#             time_record.append(time.time())
#             resources.append(self._get_current_usage())
#             self.lock.acquire()
#             stop = self.stop_recording
#             self.lock.release()
#             if stop:
#                 break
#             time.sleep(0.0001)
#         time_record.append(time.time())
#         resources.append(self._get_current_usage())
#         self.el_time = self.time_record[len(self.time_record)-1] - self.start_time
#         self.lock.acquire()
#         self.time_record = time_record.copy()
#         self.resources_record = resources.copy()
#         self.lock.release()
#         print('time stopped here')

#     def get_elapsed_time(self):
#         return self.el_time

#     def plot_stats(self):
#         print(len(self.time_record))
#         CPU = []
#         CPU_p = []
#         time_r = []
#         for (record, time_stamp) in zip(self.resources_record, self.time_record):
#             CPU.append(record[0])
#             CPU_p.append(record[2])
#             time_r.append(time_stamp-self.start_time)

#         plt.plot(time_r, CPU)
        
#         plt.show()
#         plt.plot(time_r, CPU_p)
#         plt.show()

    

    


# p = thread_with_exception("Holla")

# p.start()
# time.sleep(2)
# p.raise_exception()
# p.join()
# p.plot_stats()