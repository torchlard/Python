import sys as Sys
# Print iterations progress
def printProgress (iteration, total, prefix = 'Progress:', suffix = '', decimals = 2, barLength = 70):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : number of decimals in percent complete (Int) 
        barLength   - Optional  : character length of bar (Int) 
    """
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '#' * filledLength + '-' * (barLength - filledLength)
    Sys.stdout.write('%s [%s] %s%s\r' % (prefix, bar, percents, '%')),
    Sys.stdout.flush()
    if iteration == total:
        print("\n")
        print("Complete!!")

# # items = ["a", "b", "c", "d", "e"]
# items=range(200000)
# i     = 0
# l     = len(items)

# # Initial call to print 0% progress
# printProgress(i, l, prefix = 'Progress:', barLength = 100)
# for item in items:
#     i += 1
#     printProgress(i, l, prefix = 'Progress:', barLength = 100)



