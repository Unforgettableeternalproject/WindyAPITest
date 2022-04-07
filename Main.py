import openpyxl
import Functions.Windy as Windy
import Functions.Electicity as Electicity
import time

files = []
#每小時行程
init = int(time.strftime('%H', time.localtime())-1)
runtime = 0
#初始化

while runtime != init:
    file = []
    runtime = int(time.strftime('%H', time.localtime()))
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
    time.sleep(3600)

wb = openpyxl.Workbook()
sheet = wb.create_sheet("第十組觀測資料", 0)
    
titles = ("紀錄時間", "淨發電量", "發電量比", "風速", "風向")
sheet.append(titles)
 
for file in files:
	sheet.append(file)
 
#輸出
wb.save("第十組觀測資料.xlsx")
