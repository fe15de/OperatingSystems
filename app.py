from flask import Flask , render_template, request

app = Flask(__name__)

@app.route("/" ,methods = ['POST', 'GET'])
def home():
    return render_template("home.html") 

@app.route("/fifo",methods = ['POST', 'GET'])
def fifo():
    if request.method == 'GET':
        n = 0
    if request.method == 'POST':
        n = int(request.form['n'])
        if n != 0:
            data = request.form
            last_data = list(data.items())[-1]
            if last_data[0] == 'start':
                arrival_time = [] * n
                burst_time = [] * n
                CPU = 0
                for i in range(n):
                    arrival_time.append(int(request.form.get('at' + str(i))))
                    burst_time.append(int(request.form.get('bt' + str(i))))
                ATt = [0] * n
                NoP = n  # number of Processes
                waiting_time = [0] * n
                turnaround_time = [0] * n

                for i in range(n):
                    ATt[i] = arrival_time[i]


                while NoP > 0 and CPU <= 1000:
                    for i in range(n):
                        if ATt[i] <= CPU:
                            
                            waiting_time[i] = CPU - arrival_time[i]
                            CPU += burst_time[i]
                            turnaround_time[i] = CPU - arrival_time[i]
                            ATt[i] = float('inf')  # Set arrival time to infinity so that this process won't be selected again
                            NoP -= 1
                            
                            break
                    else:
                        CPU += 1  # If no process is eligible to run, just increment CPU time

                return render_template("program.html", n = n,bt = burst_time, at= arrival_time, wt = waiting_time, tat = turnaround_time,AvgWT = sum(waiting_time) /n ,AVGTaT = sum(turnaround_time) / n, table = True, name = 'FIFO')
                                                
    return render_template("program.html", n = n, table = False, name = 'FIFO') 

@app.route("/sjf",methods = ['POST', 'GET'])
def sjf():
    if request.method == 'GET':
        n = 0
    if request.method == 'POST':
        n = int(request.form['n'])
        if n != 0:
            data = request.form
            last_data = list(data.items())[-1]
            if last_data[0] == 'start':
                arrival_time = [] * n
                burst_time = [] * n
                CPU = 0
                for i in range(n):
                    arrival_time.append(int(request.form.get('at' + str(i))))
                    burst_time.append(int(request.form.get('bt' + str(i))))
                ATt = [0] * n
                NoP = n  # number of Processes
                waiting_time = [0] * n
                turnaround_time = [0] * n
                processed = [False] * n

                for i in range(n):
                    ATt[i] = arrival_time[i]

                print("\nProcess execution sequence:")
                while NoP > 0 and CPU <= 1000:
                    min_burst = float('inf')
                    min_index = -1
                    for i in range(n):
                        if ATt[i] <= CPU and not processed[i] and burst_time[i] < min_burst:
                            min_burst = burst_time[i]
                            min_index = i

                    if min_index == -1:
                        CPU += 1
                    else:
                        print("At CPU time {}: Process P{} is running".format(CPU, min_index + 1))
                        waiting_time[min_index] = CPU - arrival_time[min_index]
                        CPU += burst_time[min_index]
                        turnaround_time[min_index] = CPU - arrival_time[min_index]
                        processed[min_index] = True
                        NoP -= 1

                return render_template("program.html", n = n,bt = burst_time, at= arrival_time, wt = waiting_time, tat = turnaround_time,AvgWT = sum(waiting_time) /n ,AVGTaT = sum(turnaround_time) / n, table = True, name = 'SJF')
    return render_template("program.html", n = n, table = False,name = 'SJF') 

@app.route("/priority",methods = ['POST', 'GET'])
def priority():
    if request.method == 'GET':
        n = 0
    if request.method == 'POST':
        n = int(request.form['n'])
        if n != 0:
            data = request.form
            last_data = list(data.items())[-1]
            if last_data[0] == 'start':
                arrival_time = [] * n
                burst_time = [] * n
                priority = [] * n
                CPU = 0
                for i in range(n):
                    arrival_time.append(int(request.form.get('at' + str(i))))
                    burst_time.append(int(request.form.get('bt' + str(i))))
                    priority.append(int(request.form.get('priority' + str(i))))
                ATt = [0] * n
                NoP = n  # number of Processes
                PPt = [0] * n
                waiting_time = [0] * n
                turnaround_time = [0] * n

                for i in range(n):
                    PPt[i] = priority[i]
                    ATt[i] = arrival_time[i]

                LAT = max(arrival_time)
                for i in range(n):
                    if arrival_time[i] > LAT:
                        LAT = arrival_time[i]

                print("\nProcess execution sequence:")
                while NoP > 0 and CPU <= 1000:
                    min_priority = float('inf')  # Initialize with positive infinity
                    min_priority_index = -1
                    for i in range(n):
                        if ATt[i] <= CPU and PPt[i] != (LAT + 10) and PPt[i] < min_priority:
                            min_priority = PPt[i]
                            min_priority_index = i
                            
                    if min_priority_index == -1:
                        CPU += 1
                    else:
                        print("P{} is running at CPU time {}".format(min_priority_index + 1, CPU))
                        waiting_time[min_priority_index] = CPU - arrival_time[min_priority_index]
                        CPU += burst_time[min_priority_index]
                        turnaround_time[min_priority_index] = CPU - arrival_time[min_priority_index]
                        ATt[min_priority_index] = LAT + 10
                        PPt[min_priority_index] = LAT + 10
                        NoP -= 1
                return render_template("program.html", prio = priority ,n = n,bt = burst_time, at= arrival_time, wt = waiting_time, tat = turnaround_time,AvgWT = sum(waiting_time) /n ,AVGTaT = sum(turnaround_time) / n, table = True, name = 'PRIORITY')
    return render_template("program.html", n = n, table = False,name = 'PRIORITY') 


@app.route("/roundRobin",methods = ['POST', 'GET'])
def roundRobin():
    return render_template("roundRobin.html") 


if __name__ == "__main__":
    app.run(debug=True)