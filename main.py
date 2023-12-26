import tkinter as tk
import threading
import time

class PetersonMutex:
    def __init__(self, num_processes):
        self.flag = [False] * num_processes
        self.turn = 0

    def lock(self, process_id):
        other_process = 1 - process_id
        self.flag[process_id] = True
        self.turn = process_id
        while self.flag[other_process] and self.turn == process_id:
            pass

    def unlock(self, process_id):
        self.flag[process_id] = False

class SharedResource:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

def shared_resource_access(process_id, peterson_mutex, shared_resource, text_widget):
    start_time = time.time()

    for _ in range(5):
        peterson_mutex.lock(process_id)
        with shared_resource.lock:
            shared_resource.value += 1
            text_widget.insert(tk.END, f"Process {process_id} accessed the shared resource. Value: {shared_resource.value}\n")
            text_widget.see(tk.END)  
        peterson_mutex.unlock(process_id)
        time.sleep(0.1)

    end_time = time.time()
    text_widget.insert(tk.END, f"Process {process_id} finished in {end_time - start_time:.2f} seconds\n")
    text_widget.see(tk.END)

def start_threads(num_processes, text_widget, shared_resource):
    peterson_mutex = PetersonMutex(num_processes)
    threads = [threading.Thread(target=shared_resource_access, args=(i, peterson_mutex, shared_resource, text_widget)) for i in range(num_processes)]
    
    for thread in threads:
        thread.start()

def start_simulation(num_processes, text_widget, shared_resource):
    start_threads(num_processes, text_widget, shared_resource)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Peterson Algorithm with GUI")

    text_widget = tk.Text(root, height=10, width=50)
    text_widget.pack()

    num_processes = int(input("Enter the number of processes: "))
    
    shared_resource = SharedResource()

    start_button = tk.Button(root, text="Start Simulation", command=lambda: start_simulation(num_processes, text_widget,
                                                                                               shared_resource))
    start_button.pack()
    stop_button = tk.Button(root,text="Stop Simulation", command=root.destroy)
    stop_button.pack()
    root.mainloop()
