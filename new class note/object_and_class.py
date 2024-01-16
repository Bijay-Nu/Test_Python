class Shop:
    def __init__(self,product_name,price,qty):
        # validation to argument
        assert price>=0, f'Your price is {price} shouldnnot  be negative'
        assert qty>=0, f'your qty {qty} should not be negative'
        self.name = product_name
        self.price = price
        self.qty = qty

    def totalpprice(self):
        print(self.name,'price',self.price,'qty',self.qty)
        return self.price*self.qty
a=Shop('Book',-500,2)
print('total price: ',a.totalpprice(),'Rs')


