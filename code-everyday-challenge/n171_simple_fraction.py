
# https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51187/Python-easy-to-understand-solution

# https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51110/Do-not-use-python-as-cpp-here's-a-short-version-python-code



def fractionToDecimal( numerator, denominator):
    if numerator % denominator == 0:
        return str(numerator//denominator)
    sign = '' if numerator * denominator >= 0 else '-'
    numerator, denominator = abs(numerator), abs(denominator)
    res = sign + str(numerator//denominator) + '.'
    numerator %= denominator
    i, part = 0, ''
    m = {numerator:i}
    print(res, numerator, denominator)
    while numerator % denominator:
        numerator *= 10
        i += 1
        rem = numerator % denominator
        part += str(numerator // denominator)
        print(part, rem, m, numerator, denominator)
        if rem in m:
            print(part[:m[rem]], '  hj', part[m[rem]:])

            part = part[:m[rem]]+'('+part[m[rem]:]+')'
            return res + part
        m[rem] = i
        numerator = rem
    return res + part




# Idea is to put every remainder into the hash table as a key,
#  and the current length of the result string as the value. 
# When the same remainder shows again, it's circulating from 
# the index of the value in the table.

# Approach: The idea is to first calculate the integral quotient (absolute part before decimal point) and then calculate the fractional part. To check if the fractional part is repeating, insert the remainder (numerator % denominator) in a map with key as remainder and value as the index position at which this remainder occurs. If at any point of time, the remainder becomes zero, then there doesn’t exist a repeating fraction otherwise if the remainder is already found in the map, then there exists a repeating fraction.


numerator = 4 
denominator = 333
print(fractionToDecimal(16,13))

