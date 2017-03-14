#!/usr/bin/python


def outlierCleaner(predictions, ages_train, net_worths_train):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    error = list()
    cd = list()
    
    i = 0
    while i < 90 :
        error.append(abs(net_worths_train[i] - predictions[i]))
        cd.append((ages_train[i], net_worths_train[i], error[i]))
        i = i + 1

    cleaned_data = sorted(cd, key = lambda x: x[2])
    
    return cleaned_data[:81]

