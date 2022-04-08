import openpyxl
import Functions.Windy as Windy
import Functions.Electicity as Electicity
import os
import time

#初始化
files = []
index = 0
print("Program initiating...\nEnter arguments:\n\nFilename(Leave blank for default): ", end="")
filename = input()
if(filename == ""): 
    filename = "第十組觀測資料"
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
    gap = 13
    print("Must be integer input! Used default settings instead.")
    
copyright = ["windyAPI designed by Bernie.", f"Runned cycles:{cycle}", f"Time gaps:{gap}"]
if(gap > 12): gap -= 12
elif(gap <= 12): gap = 0
print("\n\nArgument accepted, running program...\n")


while True:
    
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
    print("Current Time: " + time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()) + f"\nFetching Operation Had Done {index} Time(s).\n\n")
    if(cycle == 0): break

    #等待
    time.sleep(gap)

basepath = os.path.dirname(os.path.realpath(__file__))

jpgimagepath = os.path.join(
        basepath, '../Instance', filename + ".xlsx")

wb = openpyxl.Workbook()
sheet = wb.create_sheet(filename, 0)
    
titles = ("紀錄時間                             ", "淨發電量        ", "發電量比     ", "風速", "風向")
sheet.append(titles)
 
for file in files:
	sheet.append(file)

sheet.append(copyright)

#輸出
print("Attempting to save the data as .xlsx file...")
excelpath = os.path.join(basepath, 'Instance', filename + ".xlsx")

try:
    wb.save(excelpath)
    print("Saving process compeleted.")
except Exception as e:
    excelpath = os.path.join(basepath, 'Instance', f"{time.strftime('%m_%d-%H_%M', time.localtime())}.xlsx")
    wb.save(excelpath)
    print(f"Error occured when saving, backup saved into {excelpath} instead.")

print("\n\nProgram closing...")

