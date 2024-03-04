from quickchart import QuickChart

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
        print(request.form)
        if n != 0:
            data = request.form
            last_data = list(data.items())[-1]
            print(last_data)
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

                print("\nProcess_Number\tBurst_Time\tArrival_Time\tWaiting_Time\tTurnaround_Time\n")
                for i in range(n):
                    print("P{}\t\t{}\t\t{}\t\t{}\t\t{}".format(i + 1, burst_time[i], arrival_time[i], waiting_time[i], turnaround_time[i]))

                AvgWT = sum(waiting_time) / n  # Average waiting time
                AVGTaT = sum(turnaround_time) / n  # Average Turnaround time

                print("Average waiting time =", AvgWT)
                print("Average turnaround time =", AVGTaT)
            
                            
                            

    return render_template("fifo.html", n = n) 

@app.route("/sjf",methods = ['POST', 'GET'])
def sjf():
    return render_template("sjf.html") 

@app.route("/priority",methods = ['POST', 'GET'])
def priority():
    return render_template("priority.html") 


@app.route("/roundRobin",methods = ['POST', 'GET'])
def roundRobin():
    return render_template("roundRobin.html") 


if __name__ == "__main__":
    app.run(debug=True)