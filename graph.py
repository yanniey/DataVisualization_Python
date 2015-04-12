from collections import Counter
from parse import MY_FILE

import csv
import matplotlib.pyplot as plt 
import numpy as np
import parse

def visualize_days():
    #Visualize data by day of week

    # 1. grab our parsed data that we parsed earlier
    data_file = parse.parse(MY_FILE,",")

    # 2. make a new variable, 'counter', from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen on each day of the week

    counter = Counter(item["DayOfWeek"] for item in data_file)

    # 3. separate the x-axis data (the days of the week) from the
    # 'counter' variable from the y-axis data (the number of
    # incidents for each day)
    data_list = [
                counter["Monday"],
                counter["Tuesday"],
                counter["Wednesday"],
                counter["Thursday"],
                counter["Friday"],
                counter["Saturday"],
                counter["Sunday"]
    ]

    day_tuple = tuple(["Mon","Tues","Wed","Thur","Fri","Sat","Sun"])
    # 4. with that y-axis data, assign it to a matplotlib plot instance
    
    plt.plot(data_list)
    
    # 5. create the amount of ticks needed for our x-axis, and assign
    # the labels
    plt.xticks(range(len(day_tuple)),day_tuple)

    """parameter 1 = [0, 1, 2, 3, 4, 5, 6] The first parameter is so matplotlib knows how many ticks it needs to place."""
    """parameter 2 = ("Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun")"""
    
    # save the plot!
    plt.savefig("Days.png")

    # close plot file
    plt.clf()

def visualize_type():
    # grab our parsed data
    data_file = parse.parse(MY_FILE,",")
    # make a new variable, 'counter', from iterating through each line
    # of data in the parsed data, and count how many incidents happen
    # by category
    counter = Counter(item["Category"]for item in data_file)
    # Set the labels which are based on the keys of our counter.
    # Since order doesn't matter, we can just used counter.keys()
    labels = tuple(counter.keys())
    # Set exactly where the labels hit the x-axis
    # numpy.arange() creates evenly spaced numbers
    xlocations = np.arange(len(labels)) + 0.5
    # Width of each bar that will be plotted
    width = 0.5
    # Assign data to a bar plot (similar to plt.plot()!)
    plt.bar(xlocations, counter.values(),width=width)
    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width /2, labels, rotation = 90)
    # Give some more room so the x-axis labels aren't cut off in the
    # graph
    plt.subplots_adjust(bottom=0.5)
    # Make the overall graph/figure is larger
    plt.rcParams['figure.figsize'] = 12,12
    # Save the graph!
    plt.savefig("Type.png")
    # Close plot figure
    plt.clf()

def main():
    visualize_days()
    visualize_type()

if __name__ == "__main__":
    main()