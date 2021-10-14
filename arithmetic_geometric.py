#Determine if a sequnce is Arithmetic or Geometric

def geo_art_seq(x,nth):
    if len(x) == 1:
        return x
    #Find the Ratio and Common Difference within the sequence
    ratio = x[1] / float(x[0])
    common_diff = x[1]-x[0]
    geometric = False
    arithmetic = False
    #Iterate through the list to see if the ratio or common difference is consistent
    for i in range(1, len(x)):
        if x[i]/float(x[i-1]) != ratio:
            geometric = False
        else:
            geometric = True
        if x[i] - x[i - 1] != common_diff:
            arithmetic = False
        else:
            arithmetic = True
    #If the ratio or common difference is consistent find the nth term based on the type of sequence it is
    if geometric:
        a = x[0]
        nth_term = a * (ratio ** nth - 1)
        return 'The sequence is geometric and the nth term is  {}'.format(nth_term)
    elif arithmetic:
        a = x[0]
        nth_term = a + (common_diff * (nth - 1))
        return 'The sequence is arithmetic and the nth term is {}'.format(nth_term)
    else:
        return 'It is neither a geometric sequence or an arithmetic sequence'


test = input('Enter a list of numbers:')
test = test.split(',')
nth_term = int(input('Enter the nth term you would like to find:'))
list = []
for x in test:
    list.append(int(x))
print(geo_art_seq(list,nth_term))