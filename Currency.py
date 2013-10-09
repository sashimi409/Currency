#Project 11
#Section 11 12-5-12

import urllib.request
import string

class Currency:
    def __init__(self, amount = 1, sym = "USD"):
        self.amount = 1
        if type(amount) == int or type(amount) == float:
            self.amount = amount
        if type(sym) == str:
            sym = sym.lower()
            if sym in ['usd','eur','gbp','aud','cny','thb']:
                self.symbol = sym.upper()

    def __add__(self,v):
        if type(v) == float or type(v) == int:
            new_amount = self.amount + v
            return Currency(new_amount,self.symbol)
        else:
            try:
                if self.symbol == v.symbol:
                    new_amount = self.amount + v.amount
                else:
                    converted = v.convert_to(self.symbol)
                    new_amount = self.amount + converted.amount
                return Currency(new_amount,self.symbol)
            except TypeError:
                print("can not preform that operation")
                return self

    def __radd__(self,v):
        output = self.__add__(v)
        return output

    def __sub__(self,v):
        if type(v) == float or type(v) == int:
            new_amount = self.amount - v
            return Currency(new_amount,self.symbol)
        else:
            try:
                if self.symbol == v.symbol:
                    new_amount = self.amount - v.amount
                else:
                    converted = v.convert_to(self.symbol)
                    new_amount = self.amount - converted.amount
                return Currency(new_amount,self.symbol)
            except TypeError:
                print("can not preform that operation")
                return self

    def __rsub__(self,v):
        if type(v) == float or type(v) == int:
            new_amount = v - self.amount
            return Currency(new_amount,self.symbol)
        else:
            print("that is not possible")
            return v

    def __str__(self):
        output = str(self.amount) + " " + str(self.symbol)
        return output

    def __repr__(self):
        output = self.__str__()
        return output

    def __gt__(self,v):
        if type(v) == float or type(v) == int:
            if self.amount > v:
                return True
            else:
                return False
        else:
            try:
                if self.amount > v.amount:
                    return True
                else:
                    return False
            except TypeError:
                print("can not preform that operation")
                

    def convert_to(self, sym):
        if type(sym) == str:
            Url ="http://www.google.com/ig/calculator?hl=en&q=" + str(self.amount) + self.symbol + "=?" + sym
            web_obj = urllib.request.urlopen(Url)
            results_str = str(web_obj.read())
            web_obj.close()
            tmp = results_str.split(",")
            check = tmp[2].split(" ")
            error = check[1].strip(string.punctuation)
            if error == "4":
                print("not a valid currency code")
                return self
            else:            
                answer = tmp[1].split(" ")
                num = answer[1]
                num = num.strip(string.punctuation)
                Amount_new = float(num)
                return Currency(Amount_new,sym)
        else:
            print("Not a valid symbol")
def main():
    curr = Currency(7.50, 'USD')
    print(curr)
    curr2 = Currency(2, 'EUR')
    print(curr2)
    new_curr = curr2.convert_to('USD')
    print(new_curr)
    sum_curr = curr + curr2
    print(sum_curr)
    sum_curr2 = curr + 5.5
    print(sum_curr2)
    sum_curr3 = 4 + curr
    print(sum_curr3)
    curr3 = Currency(4, 'EUR')
    sum_with_convert = curr + curr3
    print(curr)
    print(curr3)
    print(sum_with_convert)
if __name__ == "__main__":
    main()
