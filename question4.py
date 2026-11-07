class Phone:
    def __init__(self,phoneId,os,brand,price):
        self.__phoneId=phoneId
        self.__os=os
        self.__brand=brand
        self.__price=price
    def get_phoneId(self):
        return self.__phoneId
    def set_phoneId(self,phoneId):
        self.__phoneId=phoneId

    def get_os(self):
        return self.__os
    def set_os(self,os):
        self.__os=os

    def get_brand(self):
        return self.__brand
    def set_brand(self,brand):
        self.__brand=brand

    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price=price

class Solution:
    @staticmethod
    def findPriceForGivenBrand(Phones,brand):
        total=0
        for i in Phones:
            if i.get_brand().lower()==brand.lower():
                total+=i.get_price()

        return total

    @staticmethod
    def getPhoneIdBasedOnOs(Phones,os):
        for i in Phones:
            if i.get_os().lower()==os.lower() and i.get_price()>=50000:
                return i.get_phoneId()

        return None

if __name__=="__main__":
    Phones=[]
    for i in range(4):
        phoneId=int(input())
        os=input()
        brand=input()
        price=int(input())

        obj=Phone(phoneId,os,brand,price)
        Phones.append(obj)

    brand=input()
    os=input()

    ans1=Solution.findPriceForGivenBrand(Phones,brand)

    if ans1!=0:
        print(ans1)
    else:
        print("The given Brand is not available")

    ans2=Solution.getPhoneIdBasedOnOs(Phones,os)

    if ans2 is not None:
        print(ans2)
    else:
        print("No phones are available with specified os and price range")