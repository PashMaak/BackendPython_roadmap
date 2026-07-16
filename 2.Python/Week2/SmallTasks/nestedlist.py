def flatten_list(nested_list):
# takes one list form the nested list
# takes values form list above
# and returns all values as a single list 
# in retrun it should be backward order (like recur)

    return [value for listbek in nested_list for value in listbek]

nested_list = [[1,2,3,4,5], [6,7,8,9,10],[111,123,134,12432]]

print(flatten_list(nested_list), '\n')