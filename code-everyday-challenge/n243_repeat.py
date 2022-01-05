


def search_rotated(a,l,r,k):
    if l > r:
        return -1


    mid = ((l+r)//2)

    if a[mid] == k:
        return mid

    # print(l, r, mid)
    

    if a[l] <= a[mid]:

        if k >= a[l] and k <= a[mid]:

            return search_rotated(a, l, mid-1, k)

        return search_rotated(a,mid+1, r, k) 

    if a[mid]<= k and k <=a[r]:

        return search_rotated(a, mid+1, r, k)

    return search_rotated(a,l, mid-1, k)




if  __name__ == "__main__":
    a =[203,246,321,91,102,198]
    k = 199 #246#91
    print(search_rotated(a, 0, len(a)-1, k))


from scikit import Base_Estimator

class model(Base_Estimator):
    def __init__(self, n_tree = 10):
        self.n_tree= n_tree

    def train(self,model, x, y):

        fit_name = Base_Estimator(model)

        model=fit_name.fit(x,y)
        return model

    def predict(self, x):
        return self.model.predict(x)
    
        
        

m = model()

m.train('RandomForest', x, y)

out = m.predict(x)