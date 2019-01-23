# [daynum_calc.py](https://github.com/scuwjw/other/blob/master/daynum_calc.py)
计算两个日期之间的天数；

eq：
  input：'20030302','20030303'，
  output：1

# [json_zhongwen_write.py](https://github.com/scuwjw/other/blob/master/json_zhongwen_write.py)
文件记录两种json.dumps中文的办法：  
method1() ：通过__future__引入python新特性实现；  
method2() ：通过chardet 检测字符串编码，然后修改编码格式进行实现；  
参考文章：https://blog.csdn.net/u014431852/article/details/53058951  

# [package_cal_2019.py](https://github.com/scuwjw/other/blob/master/package_cal_2019tax.py)

文件根据2019年税率，在给定每月收入及社保扣除款之后，可以计算每月随后所得，公积金所得，税后包含公积金所得，同时计算年累计所得和交税情况；一目了然；

e.g.：月所得20000，每月五险一金扣除3000元；  
调用如下：  
a = Solution()   
a.cal_month_and_year_package(20000,3000)   

输出：  
month: 1 ,tax: 360.00 ,real_income: 16640.00 ,add_house: 19620.00 ,sum: 16640.00, sum_house: 19620.00  
month: 2 ,tax: 360.00 ,real_income: 16640.00 ,add_house: 19620.00 ,sum: 33280.00, sum_house: 39240.00  
month: 3 ,tax: 360.00 ,real_income: 16640.00 ,add_house: 19620.00 ,sum: 49920.00, sum_house: 58860.00  
month: 4 ,tax: 1200.00 ,real_income: 15800.00 ,add_house: 18780.00 ,sum: 65720.00, sum_house: 77640.00  
month: 5 ,tax: 1200.00 ,real_income: 15800.00 ,add_house: 18780.00 ,sum: 81520.00, sum_house: 96420.00  
month: 6 ,tax: 1200.00 ,real_income: 15800.00 ,add_house: 18780.00 ,sum: 97320.00, sum_house: 115200.00  
month: 7 ,tax: 1200.00 ,real_income: 15800.00 ,add_house: 18780.00 ,sum: 113120.00, sum_house: 133980.00  
month: 8 ,tax: 1200.00 ,real_income: 15800.00 ,add_house: 18780.00 ,sum: 128920.00, sum_house: 152760.00  
month: 9 ,tax: 1200.00 ,real_income: 15800.00 ,add_house: 18780.00 ,sum: 144720.00, sum_house: 171540.00  
month: 10 ,tax: 1200.00 ,real_income: 15800.00 ,add_house: 18780.00 ,sum: 160520.00, sum_house: 190320.00  
month: 11 ,tax: 1200.00 ,real_income: 15800.00 ,add_house: 18780.00 ,sum: 176320.00, sum_house: 209100.00  
month: 12 ,tax: 1200.00 ,real_income: 15800.00 ,add_house: 18780.00 ,sum: 192120.00, sum_house: 227880.00  
