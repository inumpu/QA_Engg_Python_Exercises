import datetime

def jmeter_logs_test():
    with open("Jmeter_log1.jtl", 'r') as f:
        logs = f.readlines()
        for i, log in enumerate(logs):
            row_data = log.split(",")
            if i != 0 and '200' not in row_data:
                d_time = datetime.datetime.fromtimestamp(int(row_data[0])//1000)
                print("Label: ", row_data[2])
                print("Response code: ", row_data[3])
                print("Response message: ", row_data[4])
                print("Failure message: ", row_data[8])
                print("Time stame: ", d_time, " PST")
                print("\n")
    
jmeter_logs_test()
