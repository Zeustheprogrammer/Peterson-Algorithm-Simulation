# Peterson Algorithm Simulation

This project simulates the use of the Peterson algorithm for mutual exclusion in a multi-process environment. The simulation involves a specified number of processes concurrently accessing a shared resource, with the Peterson algorithm ensuring that only one process can enter its critical section at a time.

## Features

- **Dynamic Process Count:** User can input the number of processes involved in the simulation.
- **Real-time Updates:** Tkinter GUI displays real-time updates as processes access the shared resource.
- **Start and Stop Controls:** User can initiate and halt the simulation dynamically.

## Dependencies

- Python 3
- Tkinter (included in most Python installations)

## Usage

1. Run the script.
2. Input the number of processes when prompted.
3. Click "Start Simulation" to initiate the simulation.
4. Click "Stop Simulation" to halt the simulation.

## Example

```bash
python main.py
