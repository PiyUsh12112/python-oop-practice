class Medicine:
    def __init__(self,MedicineName,batch,disease,price):
        self.__MedicineName=MedicineName
        self.__batch=batch
        self.__disease=disease
        self.__price=price

    def get_MedicineName(self):
        return self.__MedicineName
    def set_MedicineName(self,MedicineName):
        self.__MedicineName=MedicineName

    def get_batch(self):
        return self.__batch
    def set_batch(self,batch):
        self.__batch=batch

    def get_disease(self):
        return self.__disease
    def set_disease(self,disease):
        self.__disease=disease

    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price=price

class Solution:
    @staticmethod
    def getPriceByDisease(Medicines,disease):
        ans=[]
        for i in Medicines:
            if i.get_disease().lower()==disease.lower():
                ans.append(i.get_price())
        ans=sorted(ans)
        return ans

if __name__=="__main__":
    Medicines=[]
    for i in range(4):
        MedicineName=input()
        batch=input()
        disease=input()
        price=int(input())

        c=Medicine(MedicineName,batch,disease,price)
        Medicines.append(c)

    disease=input()

    result = Solution.getPriceByDisease(Medicines, disease)

    for price in result:
        print(price)