
# https://leetcode.com/problems/validate-ip-address/discuss/690025/Python-beats-100-12-ms
# https://practice.geeksforgeeks.org/problems/validate-an-ip-address-1587115621/1/?track=md-string&batchId=144#




# def is_integer(n):
#     try:
#         # float(n)
#         int(n)
#         if n[0]==n[1]:
#             return 0
#     except ValueError:
#         # print(n)
#         return False
#     else:
#         return 1  


# def is_valid(ip):
#     ip_list=ip.split('.')
#     # return ip_list

#     ip_list=[int(i) for i in ip_list if is_integer(i) and len(i) < 4 ]

#     # return len(ip.split('.')[0])

#     if len(ip_list) != 4: return 0

#     # ip_list=map(int,ip_list)

#     for i in ip_list:

#         if i >= 0 or i <= 255:
#             pass
#         else:
#             return 0

#     return 1


def ip_valid(ip):
    res = 0
    ipv4 = ip.split('.')
    if len(ipv4) == 4:
        for x in ipv4:
            if x == '' or (x[0] == '0' and len(x) != 1) or not x.isdigit() or int(x) > 255:
                res = 1
                break
        if not res:
            return 1

    return 0




if  __name__== "__main__":
    ip = "222.111.111.111"
    ip = '5555..555r'
    ip = "222.111.111.11g"
    ip = '67.53.56.29r'
    ip = '0.0.0.0'
    # ip = '0000.0000.0000.0000'
    # ip  = '00.00.00.00'
    print(ip_valid(ip))
