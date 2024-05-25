# Scheduling Algorithms Simulation

This Flask application simulates various CPU scheduling algorithms including FIFO, SJF, Priority Scheduling, and Round Robin. It provides a web interface where users can input process details and visualize the scheduling outcomes.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)


## Features

- **FIFO (First In First Out) Scheduling**: Processes are scheduled in the order they arrive.
- **SJF (Shortest Job First) Scheduling**: Processes with the shortest burst time are scheduled first.
- **Priority Scheduling**: Processes with the lowest priority are scheduled first.
- **Round Robin Scheduling**: Processes are scheduled in a cyclic order with a fixed time quantum.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository:**

   ```sh
   git clone https://github.com/fe15de/OperatingSystems.git
2. **Create a virtual environment and activate it:**
   ``` sh 
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
3. **Install the dependencies:**
   ```
   pip install flask
4. **Run the application:**
   ```
   python app.py
## Usage

**Home Page:**

The home page allows you to navigate to different scheduling algorithm simulations.

**Scheduling Algorithms:**

- **FIFO (First In First Out):**
  - Enter the number of processes.
  - Input the arrival and burst times for each process.
  - Submit to see the scheduling results and the graph.

- **SJF (Shortest Job First):**
  - Enter the number of processes.
  - Input the arrival and burst times for each process.
  - Submit to see the scheduling results and the graph.

- **Priority Scheduling:**
  - Enter the number of processes.
  - Input the arrival time, burst time, and priority for each process.
  - Submit to see the scheduling results and the graph.

- **Round Robin:**
  - Enter the number of processes.
  - Input the time quantum.
  - Input the arrival and burst times for each process.
  - Submit to see the scheduling results and the graph.

## Endpoints

- **Home (`/`):**
  - GET and POST methods.
  - Renders the home page where users can select the scheduling algorithm.

- **FIFO (`/fifo`):**
  - GET and POST methods.
  - Input: Number of processes, arrival times, and burst times.
  - Output: Scheduling results, average waiting time, average turnaround time, and a graph.

- **SJF (`/sjf`):**
  - GET and POST methods.
  - Input: Number of processes, arrival times, and burst times.
  - Output: Scheduling results, average waiting time, average turnaround time, and a graph.

- **Priority (`/priority`):**
  - GET and POST methods.
  - Input: Number of processes, arrival times, burst times, and priorities.
  - Output: Scheduling results, average waiting time, average turnaround time, and a graph.

- **Round Robin (`/roundRobin`):**
  - GET and POST methods.
  - Input: Number of processes, time quantum, arrival times, and burst times.
  - Output: Scheduling results, average waiting time, average turnaround time, and a graph.
