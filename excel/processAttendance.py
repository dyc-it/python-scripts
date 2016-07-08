import sys
import xlwt
import xlrd

attendance = range(0)


class record(object):
    def __init__(self, id, name, date, time_list):
        self.id = id
        self.name = name
        self.date = date
        self.time_list = time_list


def readLineFromExcel(inputExcelPath):
    data = xlrd.open_workbook(filename=inputExcelPath, encoding_override='gb2312')
    table = data.sheets()[0]
    nrows = table.nrows

    lastID = table.row_values(1)[0]
    lastName = table.row_values(1)[2]
    lastDate = table.row_values(1)[3].split(' ')[0]
    lastTime = table.row_values(1)[3].split(' ')[1]

    latestDate = ''
    time_list = range(0)
    time_list.append(lastTime)

    for rownum in range(2, nrows):
        row = table.row_values(rownum)
        currentID = row[0]
        currentDateTime = row[3]
        currentDate = row[3].split(' ')[0]
        currentTime = row[3].split(' ')[1]
        currentName = row[2]

        if currentID == lastID and currentDate == lastDate:
            time_list.append(currentTime)
        else:
            print lastID + '  ' + lastName + ' '+ lastDate + ' ' +  str(time_list)
            attendance.append(record(lastID, lastName, lastDate, time_list))

            # clear last time array, if last time is null, no operation
            time_list = range(0)
            time_list.append(currentTime)
            lastID = currentID
            lastDate = currentDate
            lastName = currentName

    time_list = range(0)
    # for the last date ,eg, 6.30
    for rownum in range(nrows - 1, 2, -1):
        row = table.row_values(rownum)
        currentID = row[0]
        currentDateTime = row[3]
        currentDate = row[3].split(' ')[0]
        currentTime = row[3].split(' ')[1]
        currentName = row[2]

        if currentID == lastID and currentDate == lastDate:
            time_list.append(currentTime)
        else:
            time_list.reverse()
            print lastID + '  ' + lastName + ' '+ lastDate + ' ' +  str(time_list)
            attendance.append(record(lastID, lastName, lastDate, time_list))
            break


def writeLineToExcel(attendance, outputPath):
    workbook = xlwt.Workbook(encoding = 'gb2312')
    worksheet = workbook.add_sheet('My Worksheet')
    worksheet.write(0, 0, label='id')
    worksheet.write(0, 1, label='name')
    worksheet.write(0, 2, label='date')

    rowNum = 1
    for obj in attendance:
        worksheet.write(rowNum, 0, label=obj.id)
        worksheet.write(rowNum, 1, label=obj.name)
        worksheet.write(rowNum, 2, label=obj.date)
        time_list_order = 0
        for str in obj.time_list:
            worksheet.write(rowNum, 3 + time_list_order, label=str)
            time_list_order += 1

        rowNum += 1

    workbook.save(outputPath)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print len(sys.argv)
        print 'usage: python processAttendance.py inputExcelPath.xls outputExcelPath.xls'
        exit(1)
    readLineFromExcel(sys.argv[1])
    writeLineToExcel(attendance, sys.argv[2])



