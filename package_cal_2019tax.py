# -*- coding:utf-8 -*-

class Solution(object):
    def cal_month_and_year_package(self, pay,ss):
        """
        :type s: str
        :rtype: int
        """
        def cal_month(income,sumtaxin,taxal,ss = 5641.9):
            income = income - 5000 - ss
            if sumtaxin >= 0 and sumtaxin < 36000:
                tax = sumtaxin * 0.03 - taxal
            elif sumtaxin < 144000:
                tax = sumtaxin * 0.1 - 2520 - taxal
            elif sumtaxin < 300000:
                tax = sumtaxin * 0.2 -16920 - taxal
            elif sumtaxin < 420000:
                tax = sumtaxin * 0.25 - 31920 - taxal
            elif sumtaxin < 660000:
                tax = sumtaxin * 0.3 - 52920 - taxal
            elif sumtaxin < 960000:
                tax = sumtaxin * 0.35 - 85920 - taxal
            else:
                tax = sumtaxin * 0.45 - 181920 - taxal
            real_income = income - tax + 5000
            return tax,real_income

        monthpay = pay
        social = ss
        sumall = 0
        sum_house = 0
        sumtaxin = 0
        taxal = 0
        tax = 0
        house = 1490 #monthpay * 0.12 if monthpay*0.12<3048 else 3048
        for i in xrange(1,13):
            sumtaxin += monthpay - 5000 - social
            taxal += tax
            tax,real_income = cal_month(monthpay,sumtaxin,taxal,social)
            add_house = real_income + house*2
            sumall += real_income
            sum_house += add_house
            print "month: %d ,tax: %.2f ,real_income: %.2f ,add_house: %.2f ,sum: %.2f, sum_house: %.2f" % (i,tax,real_income,add_house,sumall,sum_house)

if __name__ == "__main__":
    a = Solution()
    a.cal_month_and_year_package(18000,2741)
