def function_with_uncommon_error(data):
    try:
        result = data['key'] + 1  # KeyError if 'key' is missing
        return result
except KeyError:
    # This handles the KeyError, but what about other exceptions?
    return 0

data1 = {'key': 10}
data2 = {'other_key': 20}
print(function_with_uncommon_error(data1))
print(function_with_uncommon_error(data2))