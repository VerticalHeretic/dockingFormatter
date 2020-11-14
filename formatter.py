import csv 
import openpyxl

class DockingFormatter:

    def findAffinityForCompound(self, fileName):
        #Creation of the intersting proccessedCompounds list
        affinity_list = []
        f = open(fileName)
        i = 0
        modeIterator = 0
        proccessedCompound = ""
        affinitCount = ""
        for x in f:
            if "Processing compound" in x:
                proccessedCompound += x[-14:-8]
            if "mode" in x:
                modeIterator = i
            if i == (modeIterator + 3):
                affinitCount += x[13:17]
                affinity_list.append([proccessedCompound,x[3:4],x[13:17]])
            if i == (modeIterator + 4) and x[13:17] == affinitCount:
                affinity_list.append([proccessedCompound,x[3:4], x[13:17]])
            else:
                affinitCount = ""
                proccessedCompound = ""
                break
            if i == (modeIterator + 5) and x[13:17] == affinitCount:
                affinity_list.append([proccessedCompound,x[3:4], x[13:17]])
            else:
                affinitCount = ""
                proccessedCompound = ""
            if i == (modeIterator + 6) and x[13:17] == affinitCount:
                affinity_list.append([proccessedCompound,x[3:4], x[13:17]])
                affinitCount = ""
                proccessedCompound = ""
                
            i += 1
        affinity_list.pop(0)
        affinity_list.pop(1)
        f.close()
        # with open(fileName + ".csv", 'w') as csv_file:
        #     writer = csv.writer(csv_file)
        #     writer.writerows(affinity_list)
        
        # Parsing data to excel workbook section
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet["A1"] = "Processing compound"
        sheet["B1"] = "Mode"
        sheet["C1"] = "Affinity"
        for row in affinity_list:
            sheet.append(row)
        workbook.save("./results/dockingResults.xlsx")
        



