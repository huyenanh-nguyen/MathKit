import numpy as np

class Statistics:
    """
    Some common used statistical measures for an array-like data.
    It contains a few function like:

        std_mean() : calculate the mean of the data
        std_dev() : calculate the standard deviation of all the data without keeping the degree of freedom in count
        std_dev_mean() : is something that was asked in the task -> shows how random the errors are(?)
                       ∆x_Stat = s_m (s_m: standard deviation of the mean)
    """

    def __init__(self, valueset):
        """
        Args:
            valueset (list or array): list or array-like data
        """
        self.value_set = valueset


    def std_mean(self):
        """
        Args:
            value_set (list or array): one dimensional set of values

        Returns:
            int: sum of the values divided by the number of the values. 
        """
        
        value = self.value_set
        return sum(value) / len(value)  # sum is a function, that sums up all the elements in the list


    def std_dev(self):
        """calculate the standard deviation of the data. (how disperse are the data in relation to the mean)
        Args:
            value_set (list or array): one dimensional set of values

        Returns:
            int: return a single integer 
        """
        value = self.value_set

        mean = self.std_mean()
        difference = []

        for i in range(len(value)):

            difference.append(value[i] - mean)   # appending the difference of the value from mean
        
        std_dev = np.sqrt(sum(np.square(difference))/ (len(value) - 1))

        return std_dev


    def confidence_interval(self):
        """well... they call it "standard deviation of the mean" but I guess they meant confidence interval..
        But I am not quite sure..

        Args:
            value_set (list or array): one dimensional set of values

        Returns:
            int: return how random the errors are. 
        """
        value = self.value_set
        
        std_dev = self.std_dev()    # standard deviation

        return std_dev / np.sqrt(len(value))
    

    def total_uncertainty_value(self, systematic):
        """getting the total Error of my measured variable of the experiment.
        Like the total error for the length or the time or whatever.
        -> the systematic error for the time is mostly the last digit from the timer
        

        Args:
            systematic (int): uncertainty due to measurement limitation

        Returns:
            total error: the total uncertainty of my measured value (include random and systematic erros)
        """

        
        value = self.value_set
        std_dev = self.std_dev()

        random_err = (1 / np.sqrt(len(value))) * std_dev    # calculate random error

        total_err = np.sqrt( random_err ** 2 + systematic ** 2) # total error -> combined random and systematic errors

        return total_err
    


