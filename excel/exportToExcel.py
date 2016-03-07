import sys
import xlwt

resultMap = dict()



def writeToExcel():
    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('My Worksheet')
    worksheet.write(0, 0, label = 'Row 0, Column 0 Value')
    workbook.save('Excel_Workbook.xls')


def convertTxtToMap(resultFile):
    file = open(resultFile)

    lines = file.readlines(100000)

    for i in xrange(0, len(lines)-1):
        firstLine = lines[i]
        secondLine = lines[i+1]

        if "read" in secondLine and "bw" in secondLine and "iops" in secondLine and "runt"  in secondLine:
            if "4k" in firstLine:
                resultMap['4k'] = dict()

                if "seq-read" in firstLine:
                    str = secondLine.split(',', 4)
                    rate = str[1].replace('bw=','').replace('KB/s','')
                    iops = str[2].replace('iops=','').strip()
                    resultMap['4k'][0] = rate
                    resultMap['4k'][4] = iops
                    print resultMap



    return resultMap


if __name__ == '__main__':
    if len(sys.argv) < 2:
        # print len(sys.argv)
        print 'usage: python exportToExcel.py result-ext4.txt result-xfs.txt ...'
        exit(1)

    for i in xrange(1, len(sys.argv)):
        print 'processing ' + sys.argv[i]
        resultMap = convertTxtToMap(sys.argv[i])
        print resultMap



