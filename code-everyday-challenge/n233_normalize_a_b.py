# Create a normalized form for a series whose values range exactly between a and b so that the minimum has value a and maximum has value b 
# # Input 
# [90,200,10,100,50.3,0]  , a , b 
# # Desired output when a set to 0 and b set to 1 
# 0.4500 
# 1.0000 
# 0.0500 
# 0.5000 
# 0.2515 
# 0.0000 


def normalize(X, a, b):
    # print(min(X))
    X_std =   [(e - min(X)) / (max(X) - min(X)) for e in X]
    X_scaled = [e * (b - a) + a for e in X_std]


    return X_scaled


if  __name__ == "__main__":
    a= 0
    b = 2
    print(normalize([90,200,10,100,50.3,0]  , a , b))




