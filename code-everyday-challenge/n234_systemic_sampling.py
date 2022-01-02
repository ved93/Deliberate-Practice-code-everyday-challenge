# Create a systematic sampling (select units based on fixed intervals – nth unit) 
# Input  
# product_id  measure 
# 0           1   10.248 
# 1           2    9.931 
# 2           3   10.324 
# 3           4   10.762 
# 4           5    9.883 
# 5           6    9.883 
# 6           7   10.790 
# 7           8   10.384 
# 8           9    9.765 
# 9          10   10.271 

# Desired output 
# product_id  measure 
# 0           1   10.248 
# 3           4   10.762 
# 6           7   10.790 
# 9          10   10.271 

def get_every_nth(prd, measure,n):
    ind=[x for x in prd if (x-1)%n ==0]
    m = [measure[x-1] for x in ind]

    return ind,m



if __name__ == "__main__":
    prd = [1,2,3,4,5,6,7,8,9,10]
    measure = [10.248 , 9.931 ,10.324 ,10.762 , 9.883 , 9.883 ,10.790 ,10.384 , 9.765 ,10.271 ]

    print(get_every_nth(prd,measure,3))


