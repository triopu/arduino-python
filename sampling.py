import signal
import time
import sys
import datetime as dt
import pandas as pd
import serial

csv_data = []

def main_program():
    try:
        start_time = float(time.perf_counter())
        # Pengaturan Serial: '/dev/ttyACM1','COM3'
        arduino = serial.Serial('/dev/ttyACM1', 115200)
        
    except:
        print("Periksa pengaturan Serial di Python")
        sys.exit(1)
    
    while True:
        # Timer
        t_p = float(time.perf_counter())
        t = t_p - start_time               
                
        try:
            data = arduino.readline()[:-2]                  # Membaca Serial
            string = str(data, 'utf-8', errors='replace')   # Merubah Serial menjadi String
            if len(string) == 4:                            # Identifikasi jika String 4 huruf
                if 0 < int(string) < 1024:                  # Nilai String Sesui pemnacaan Analog
                    signal = int(string)                    # Merubah String ke Integer
                    csv_data.append([t,signal])             # Menyimpan data t dan signal di Array
                    print("{:.4f} - {:d}".format(t,signal)) # Menampilkan data di Terminal
        except Exception as e:
            print(e)
            break

def exit_program(signum, frame):    # Jika User tekan ctrl+c
    signal.signal(signal.SIGINT, original_sigint)
    try:
        if input("\nBerhenti merekam? (y/n)> ").lower().startswith('y'):
            # Proses Penyimpanan Data
            df = pd.DataFrame(csv_data)
            time = dt.datetime.now()
            df.to_csv('Logger'+time.strftime('_%H_%M')+'.csv',index = False, header= False)
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("Ok ok, berhenti")
        sys.exit(1)
        
    signal.signal(signal.SIGINT, exit_program)

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_program)
    main_program()
