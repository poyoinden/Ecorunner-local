import serial
import time
from datetime import datetime

try:
	ser = serial.Serial(baudrate = 38400, port = '/dev/FuelCell', timeout = 0.1)
	print(ser.isOpen())
	print("port opened")
except:
	print("Does not open.")

def Toggle(tog):
	return tog
def State(s):
	return s
def Error(err):
	return err
def Temperature(High_T, Low_T):
	return (High_T * 256 + Low_T)/100.
def Voltage(High_U, Low_U):
	return (High_U * 256 + Low_U)/100.
def Current(High_I, Low_I):
	return (High_I * 256 + Low_I)/100.
def Power(voltage, current):
	return voltage*current
def CurrentBOP(current):
	return current-5
def PowerBOP(voltage, currentBOP):
	return voltage*currentBOP
def Time(High_high_high_t, High_high_t, High_t, Low_t):
	return 256 * 256 * 256 * High_high_high_t + 256 * 256 * High_high_t + 256 * High_t + Low_t

with open("Output_raw.txt", "a") as text_file:
	with open("Output_filtered.txt", "a") as text_file2:
		while(True):
			try:
				incoming = []
				incoming2 = []
				lines = ser.readline()
				if len(lines) == 26:
					for line in lines:
						incoming.append(line)

					ctime = datetime.utcnow().strftime('%H-%M-%S.%f')
					incoming.append(ctime)

					stdout = str(incoming) + '               \t'
					text_file.write(str(incoming) + '\n')

					incoming2.append(Toggle(incoming[5]))
					incoming2.append(State(incoming[6]))
					incoming2.append(Error(incoming[7]))
					temperature = Temperature(incoming[10],incoming[11])
					incoming2.append(temperature)
					voltage = Voltage(incoming[12],incoming[13])
					incoming2.append(voltage)
					current = Current(incoming[14],incoming[15])
					incoming2.append(current)
					incoming2.append(round(Power(voltage, current),4))
#					incoming2.append(CurrentBOP(current))
#					incoming2.append(PowerBOP(voltage, CurrentBOP(current)))
					incoming2.append(datetime.utcnow().strftime('%H-%M-%S.%f'))
#					incoming2.append(Time(incoming[20],incoming[21],incoming[22],incoming[23]))

					stdout = stdout + str(incoming2)
					print(stdout)

					text_file2.write(str(incoming2) + '\n')
			except KeyboardInterrupt:
				break


