import random
class Parking():#停车场类
    def __init__(self,spaces_number,parking_address,parking_name):
        self.spaces_number = spaces_number  #停车位总数量
        self.residual_number = 5  #剩余数量
        self.parking_address = parking_address
        self.parking_name = parking_name
        self.parking_record = '无'

    def information(self):  #剩余车位信息
        print('还有'+str(self.residual_number)+'个停车位')

    def getinformation(self):   #获取车牌信息
        pass
       
    def collection_money(self,seconds):     #付款提示
        if seconds%3600 == 0:
            a = seconds/3600*5
            return a
        else:
            a = seconds/3600*5+1
            return a

        return a

    def count_money(self,parking_hour):     #停车花费多少钱
        parking_money = parking_hour*5
        return parking_money

    def count_time(self):   #停车时间
        parking_hour = random.randint(1,24)
        return parking_hour
carrefour_parking = Parking(5,'家乐福地下一楼','1号停车场')
