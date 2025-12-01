## Transformation Functions


# Create function to convert column
def average_usage (x):
    '''
    Convert average daily usage from float to categorical
    '''
    if x >= 8:
        return 8
    elif x >= 7:
        return 7
    elif x >= 6:
        return 6
    elif x >= 5:
        return 5
    elif x >= 4:
        return 4
    elif x >= 3:
        return 3
    else:
        return 2