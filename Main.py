import openpyxl
import Functions.Windy as Windy
import Functions.Electicity as Electicity
import os.path
from os import path
import time

#初始化
files = []
index = 0
print("Program initiating...\nEnter arguments:\n\nFilename(Leave blank for default): ", end="")
filename = input()
if(filename == ""): 
    filename = "\b第十組觀測資料"
    print(filename, end="")

print("\nAssumed run cycle count: ", end="")
try:
    cycle = int(input())
except ValueError:
    cycle = 10
    print("Must be integer input! Used default settings instead.")

print("\nAssumed run gap(seconds): ", end="")
try:
    gap = int(input())
except ValueError:
    gap = 10
    print("Must be integer input! Used default settings instead.")

print("\n\nArgument accepted, running program...\n")

while cycle != 0:
    
    #迴圈每小時執行一次
    file = []
    
    #時間
    date = time.strftime('%m/%d %H:%M', time.localtime())
    file.append(date)

    #發電量
    ele = Electicity.electricity()
    e_final = ele.fetch()
    file.extend(e_final)

    #風速與風向
    wind = Windy.wind()
    temp = wind.optimize(wind.fetch())
    w_final = wind.calculate(temp[0], temp[1])
    file.extend(w_final)

    #整合
    files.append(file)
    
    #告知主控端
    runtime = int(time.strftime('%H', time.localtime()))
    cycle -= 1
    index += 1
    print("Current Time: " + time.strftime('%Y/%m/%d %H:%M', time.localtime()) + f"\nFetching Operation Had Done {index} Time(s).\n\n")
    
    #等待
    time.sleep(gap)

wb = openpyxl.Workbook()
sheet = wb.create_sheet(filename, 0)
    
titles = ("紀錄時間", "淨發電量", "發電量比", "風速", "風向")
sheet.append(titles)
 
for file in files:
	sheet.append(file)

copyright = ["windyAPI designed by Bernie."]
sheet.append(copyright)
#輸出
print("Attempting to save the data as .xlsx file...")

try:
    wb.save(filename + ".xlsx")
    print("Saving process compeleted.")
except Exception as e:
    wb.save(f"{time.strftime('%m_%d-%H_%M', time.localtime())}.xlsx")
    print(f"Error occured when saving, backup saved into {time.strftime('%m_%d-%H_%M', time.localtime())}.xlsx instead.")

print("\n\nProgram closing...")

