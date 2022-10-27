import os
import natsort
import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import xlwt


def files_extract():
    unsorted_files = os.listdir()
    sorted_files = natsort.natsorted(unsorted_files)
    # extract the name of the parkings
    parkings = []
    with open(sorted_files[0][:],'r') as file2:
        csvreader = csv.DictReader(file2)
        for row in csvreader:
            parkings.append(row['nombre'])
    return parkings,sorted_files
# extract the data of parking slots occupation
def data_extract(parkings,sorted_files):
    data = [0]*len(parkings)
    for file in sorted_files:
        if (file != 'data_format.py') and (file != 'statistics.xls'):
            rows = []
            with open(file,'r') as file2:
                csvreader = csv.DictReader(file2)
                for row in csvreader:
                    rows.append(float(row['libres']))
        data = np.vstack((data,rows))
    data = np.delete(data,0,0)
    return data;


# plot the evolution of the occupency for each location
def visualisation(parkings,data):
    x = list(range(len(data[:,0])))
    for i in range (len(parkings)):
        y = data[:,i]
        plt.plot(x,y)
    plt.legend(parkings)
    plt.xlabel('Time step . 15 minutes')
    plt.ylabel('Parking Availability')
    #plt.show() # uncomment to display
    img_name = 'parking_avilability'+str((datetime.now()))
    plt.savefig(img_name,format="pdf",bbox_inches='tight')

# compute the amplitude of the changes
def amplitude(parkings,data):
    book = xlwt.Workbook()
    sheet = book.add_sheet("stats")
    sheet.write(0, 0, "parking")
    sheet.write(0, 1, "15 min.")
    sheet.write(0, 2, "30 min.")
    sheet.write(0, 3, "45 min.")
    sheet.write(0, 4, "60 min.")
    for indx in range(len(parkings)):
        sheet.write(indx+1,0,parkings[indx])
        data_parking = data[:,indx]
        count_hour = 0
        count_threequartes = 0
        count_half = 0
        count_quarter = 0

        # test every quarter hour
        prev_val = data_parking[0]
        for ind in range(0,len(data_parking),1):
            if ind != 0:
                if prev_val != data_parking[ind]:
                    count_quarter += 1
                    prev_val = data_parking[ind]
        sheet.write(indx+1,1,count_quarter)

        # test every half hour
        prev_val = data_parking[0]
        for ind in range(0, len(data_parking), 2):
            if ind != 0:
                if prev_val != data_parking[ind]:
                    count_half += 1
                    prev_val = data_parking[ind]
        sheet.write(indx+1,2,count_half)

        # test every three quarters
        prev_val = data_parking[0]
        for ind in range(0, len(data_parking), 4):
            if ind != 0:
                if prev_val != data_parking[ind]:
                    count_threequartes += 1
                    prev_val = data_parking[ind]
        sheet.write(indx+1,3,count_threequartes)

        # test every hour
        prev_val = data_parking[0]
        for ind in range(0, len(data_parking), 4):
            if ind != 0:
                if prev_val != data_parking[ind]:
                    count_hour += 1
                    prev_val = data_parking[ind]
        sheet.write(indx+1,4,count_hour)
        book.save('statistics.xls')
    return;

def main():
    # rank the CSV files and extract parkings
    data1 = files_extract()
    # extract the parking availability
    data2 =  data_extract(data1[0],data1[1])
    # create visualisation
    visualisation(data1[0],data2)
    # calculate the amplitude of changes
    amplitude(data1[0],data2)

if __name__ == "__main__":
    main()



