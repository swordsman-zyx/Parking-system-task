import time
import datetime
from Parking import carrefour_parking
while True:
    if carrefour_parking.residual_number>=1:
        #汽车入停车场
        #以下是停车信息记录
        carrefour_parking.information()
        num = input('输入你的车牌号')
        carrefour_parking.parking_record = time.strftime('%Y.%m.%d. %H:%M:%S',time.localtime(time.time()))+'\t'+num+'已经进入停车场'
        car_enter = carrefour_parking.parking_record  #入场记录
        carrefour_parking.residual_number -= 1
        print(carrefour_parking.parking_record)
        input('输入任意字符表示已停到车位上：')
        carrefour_parking.parking_record = time.strftime('%Y.%m.%d. %H:%M:%S',time.localtime(time.time()))+'\t'+num+'已经开始停车并计时'
        starttime = datetime.datetime.now()     #开始时间
        car_timing = carrefour_parking.parking_record   #计时记录
        print(carrefour_parking.parking_record)
        input('输入任意字符表示离开车位：')
        carrefour_parking.parking_record = time.strftime('%Y.%m.%d. %H:%M:%S',time.localtime(time.time()))+'\t'+num+'已经离开车位'
        endtime = datetime.datetime.now()
        car_leave = carrefour_parking.parking_record    #计时结束记录
        print(carrefour_parking.parking_record)
        hours = (endtime-starttime).seconds
        input('输入任意字符表示到达出口:')
        print('--------------订单信息-------------------')
        print(car_enter+'\n'+car_timing+'\n'+car_leave)
        print('时间是：\t'+str(hours)+'\t秒')
        print('应该支付：'+str(carrefour_parking.collection_money(hours))+'元')
        print('------------------------------------')
        while True:
            money = input('输入付了多少钱：')
            if int(money) == carrefour_parking.collection_money(hours):
                break
            print('重新输入')
        print('付款成功')





        

        











    else:
        print('车位已满')

