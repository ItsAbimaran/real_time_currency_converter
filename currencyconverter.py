#pip install forex-python
#import currencyrates class to retrieve rates between different countries
from forex_python.converter import CurrencyRates
cr=CurrencyRates()
#prompt the user to enter the amount
am=int(input("Enter the amount that you want to convert:"))
print("\nEUR/USD - euro / U.S. dollar\nGBP/USD - Great Britain pound (sterling) / U.S. dollar\nUSD/JPY - U.S. dollar / Japanese yen\nUSD/CHF - U.S. dollar / Swiss France\nAUD - Australian dollar")
print("CAD - Canadian dollar\nCNY - China yuan renminbi\nNZD - New Zealand dollar\nINR - Indian rupee\nBZR - Brazilian real\nSEK - Swedish krona\nZAR - South African rand\nHKD - Hong Kong dollar\n")
#source currency code
fr=input("Enter the currency code that has to convert:").upper()
#target currency code
to=input("Enter the currency code to convert:").upper()
#conversion
a= cr.convert(fr, to, am)
#printing the cenversion value
print("The conversion of currency",am,"from",fr,"to",to,"is",a)
    
