from pandas import DataFrame, Series
import numpy


#def avg_medal_count():
'''
    Compute the average number of bronze medals earned by countries who
    earned at least one gold medal.

    Save this to a variable named avg_bronze_at_least_one_gold. You do not
    need to call the function in your code when running it in the browser -
    the grader will do that automatically when you submit or test it.

    HINT-1:
    You can retrieve all of the values of a Pandas column from a
    data frame, "df", as follows:
    df['column_name']

    HINT-2:
    The numpy.mean function can accept as an argument a single
    Pandas column.

    For example, numpy.mean(df["col_name"]) would return the
    mean of the values located in "col_name" of a dataframe df.

    '''

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
             'Netherlands', 'Germany', 'Switzerland', 'Belarus',
             'Austria', 'France', 'Poland', 'China', 'Korea',
             'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
             'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
             'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

olympic_medal_counts = {'country_name': Series(countries),
                        'gold': Series(gold),
                        'silver': Series(silver),
                        'bronze': Series(bronze)}
df = DataFrame(olympic_medal_counts)

#print numpy.mean(df["bronze"])
'''Solution 1'''
#bronze_at_least_one_gold = df[(df.gold >= 1)]                                      # create df with all columns and without (countries without gold medals)
#avg_bronze_at_least_one_gold = numpy.mean(bronze_at_least_one_gold["bronze"])      # calc. average of all bronze medals
#print avg_bronze_at_least_one_gold

'''Solution 2'''
bronze_at_least_one_gold = df['bronze'][df['gold'] >= 1]       # create df only with bronze column and without (countries without gold medals)
print bronze_at_least_one_gold
avg_bronze_at_least_one_gold = numpy.mean(bronze_at_least_one_gold)
print avg_bronze_at_least_one_gold

'''df.apply(numpy.mean)     does not work here cause gives mean of all columns and 1 column here is string type'''

#print df['gold'].map(lambda x: x >= 1) # returns df with True/False for 'gold' column dependent on how many medals are won (equal or more than 1)
#print df.applymap(lambda x: x >= 1)    # returns df with True/False for each column dependent on how many medals are won (equal or more than 1)

'''As a refresher on lambda, lambda functions are small
    inline functions that are defined on-the-fly in Python.

    lambda x: x>= 1 will take an input x and return x>=1,
    or a boolean that equals True or False.

    In this example,
    map() and applymap() create a new Series or DataFrame by
    applying the lambda function to each element. Note that map()
    can only be used on a Series to return a new Series and applymap()
    can only be used on a DataFrame to return a new DataFrame.

    For further reference, please refer to the official documentation on lambda'''

# return avg_bronze_at_least_one_gold


