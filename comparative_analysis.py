#price for tshirt, shirt, jeans
tp=[[0 for i in range(5)] for j in range(8)]
sp=[[0 for i in range(6)] for j in range(8)]
jp=[[0 for i in range(9)] for j in range(8)]

#tshirt
trn=[[0 for i in range(5)] for j in range(8)]
tvn=[[0 for i in range(5)] for j in range(8)]
tpn=[[0 for i in range(5)] for j in range(8)]
tmn=[[0 for i in range(5)] for j in range(8)]
thn=[[0 for i in range(5)] for j in range(8)]
tsol=[[0 for i in range(5)] for j in range(8)]
tpri=[[0 for i in range(5)] for j in range(8)]
tstr=[[0 for i in range(5)] for j in range(8)]
tcol=[[0 for i in range(5)] for j in range(8)]
temb=[[0 for i in range(5)] for j in range(8)]
ttex=[[0 for i in range(5)] for j in range(8)]

tot_c=[[0 for i in range(5)] for j in range(8)]
tot_t=[[0 for i in range(6)] for j in range(8)]

#shirt
sss=[[0 for i in range(6)] for j in range(8)]
ssf=[[0 for i in range(6)] for j in range(8)]
srf=[[0 for i in range(6)] for j in range(8)]
scas=[[0 for i in range(6)] for j in range(8)]
scha=[[0 for i in range(6)] for j in range(8)]
sden=[[0 for i in range(6)] for j in range(8)]
semb=[[0 for i in range(6)] for j in range(8)]
sfor=[[0 for i in range(6)] for j in range(8)]
skni=[[0 for i in range(6)] for j in range(8)]
slin=[[0 for i in range(6)] for j in range(8)]
srev=[[0 for i in range(6)] for j in range(8)]
stex=[[0 for i in range(6)] for j in range(8)]

tot_sf=[[0 for i in range(3)] for j in range(8)]
tot_sd=[[0 for i in range(9)] for j in range(8)]

#jeans
jsup=[[0 for i in range(9)] for j in range(8)]
jski=[[0 for i in range(9)] for j in range(8)]
jsli=[[0 for i in range(9)] for j in range(8)]
jsls=[[0 for i in range(9)] for j in range(8)]
jslt=[[0 for i in range(9)] for j in range(8)]
jreg=[[0 for i in range(9)] for j in range(8)]
jboo=[[0 for i in range(9)] for j in range(8)]

tot_jf=[[0 for i in range(7)] for j in range(8)]


import wsurlopen
import xlwt
from xlwt import Workbook
import xlrd
import bs4
import lxml
import re
import io
import pandas as pd
import matplotlib.pyplot as plt
import time,datetime
from bs4 import BeautifulSoup
from _operator import index
'''
tct=1
sct=1
jct=1

wb=Workbook()
sheet1=wb.add_sheet('T-Shirt')
sheet1.write(0,0,"Brand")
sheet1.write(0,1,"Price")
sheet1.write(0,2,"Category")
sheet1.write(0,3,"Technique")

sheet2=wb.add_sheet('Shirt')
sheet2.write(0,0,"Brand")
sheet2.write(0,1,"Price")
sheet2.write(0,2,"Category")
sheet2.write(0,3,"Details")

sheet3=wb.add_sheet('Jean')
sheet3.write(0,0,"Brand")
sheet3.write(0,1,"Price")
sheet3.write(0,2,"Category")
wb.save('myntra.xls')

url=[]
url.append("https://www.myntra.com/amp/men-tshirts?f=Brand%3ALee&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-tshirts?f=Brand%3ALevis&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-tshirts?f=Brand%3APepe%20Jeans&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-tshirts?f=Brand%3AJack%20%26%20Jones&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-tshirts?f=Brand%3AU.S.%20Polo%20Assn.&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-tshirts?f=Brand%3AUnited%20Colors%20of%20Benetton&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-tshirts?f=Brand%3AAMERICAN%20EAGLE%20OUTFITTERS&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-tshirts?f=Brand%3ACelio&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-shirts?f=Brand%3ALee&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-shirts?f=Brand%3ALevis&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-shirts?f=Brand%3APepe%20Jeans&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-shirts?f=Brand%3AJack%20%26%20Jones&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-shirts?f=Brand%3AU.S.%20Polo%20Assn.&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-shirts?f=Brand%3AUnited%20Colors%20of%20Benetton&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-shirts?f=Brand%3AAMERICAN%20EAGLE%20OUTFITTERS&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-shirts?f=Brand%3ACelio&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-jeans?f=Brand%3ALee&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-jeans?f=Brand%3ALevis&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-jeans?f=Brand%3APepe%20Jeans&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-jeans?f=Brand%3AJack%20%26%20Jones&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-jeans?f=Brand%3AU.S.%20Polo%20Assn.&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-jeans?f=Brand%3AUnited%20Colors%20of%20Benetton&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-jeans?f=Brand%3AAMERICAN%20EAGLE%20OUTFITTERS&sort=new&rows=190")
url.append("https://www.myntra.com/amp/men-jeans?f=Brand%3ACelio&sort=new&rows=190")

for i in range(24):
    print(i)
    var1=wsurlopen.urlopen(url[i])     
    time.sleep(2)  
    readfull=bs4.BeautifulSoup(var1.text,"lxml")
    read1=readfull.select(".productInfo")
    for j in read1:
        name=j.select(".name")
        name=name[0].getText()
        
        itemname=j.select(".name-product")
        itemname=itemname[0].getText()
        
        ap=j.select(".price-discounted")
        ap=ap[0].getText()
        ap=ap[1:]
        
        dp=j.select(".price")
        if(len(dp)>0):
            dp=dp[0].text
        else:
            dp=ap 
            
        dis=j.select(".price-discount")
        if(len(dis)>0):
            dis=dis[0].text
            if dis == " (20% OFF)" or dis == " (15% OFF)" or dis == " (10% OFF)" or dis == " (5% OFF)" :
                dis="no discount"
        else:
            dis="no discount"
            
        itemnamelower=itemname.lower()
        if dis == "no discount" and itemnamelower.find("pack of") == -1:
            if i < 8:
                if itemnamelower.find("polo") != -1:
                    cat="Polo Neck T-Shirt"
                elif itemnamelower.find("mandarin") != -1:
                    cat="Mandarin Collar T-Shirt"
                elif itemnamelower.find("v-neck") != -1:
                    cat="V-Neck T-Shirt"
                elif itemnamelower.find("henley") != -1:
                    cat="Henley"
                else:
                    cat="Round Neck T-Shirt"

                if itemnamelower.find("colourblock") != -1:
                    detail="Colourblock"
                elif itemnamelower.find("printed") != -1:
                    detail="Printed"
                elif itemnamelower.find("embroider") != -1:
                    detail="Embroidered"
                elif itemnamelower.find("stripe") != -1:
                    detail="Striped"
                elif itemnamelower.find("self") != -1:
                    detail="Textured Fabric"
                else:
                    detail="Solid"
                sheet1.write(tct,0,name)
                sheet1.write(tct,1,dp)
                sheet1.write(tct,2,cat)
                sheet1.write(tct,3,detail)
                sheet1.write(tct,4,itemname)
                tct=tct+1
                
            elif i > 7 and i < 16:
                if itemnamelower.find("super slim") != -1:
                        cat="Super Slim Fit"
                elif itemnamelower.find("regular") != -1 or itemnamelower.find("tailor") != -1:
                        cat="Regular Fit"
                elif itemnamelower.find("comfort") != -1 or itemnamelower.find("oversize") != -1:
                    cat="Regular Fit"
                else:
                    cat="Slim Fit"
                    
                if itemnamelower.find("chambray") != -1:
                    detail="Chambray"
                elif itemnamelower.find("denim") != -1:
                    detail="Denim"
                elif itemnamelower.find("linen") != -1:
                    detail="Linen"
                elif itemnamelower.find("reversible") != -1:
                    detail="Reversible"
                elif itemnamelower.find("self design") != -1:
                    detail="Textured Fabric"
                elif itemnamelower.find("embroidered") != -1:
                    detail="Embroidered"
                elif itemnamelower.find("knitted") != -1:
                    detail="Knitted"
                elif itemnamelower.find("formal") != -1:
                    detail="Formal"     
                else:
                    detail="Casual"
                    
                sheet2.write(sct,0,name)
                sheet2.write(sct,1,dp)
                sheet2.write(sct,2,cat)
                sheet2.write(sct,3,detail)
                sheet2.write(sct,4,itemname)
                sct=sct+1
        
            elif i > 15 and i < 24:
                if itemnamelower.find("super") != -1:
                    cat="Super Skinny Fit"
                elif itemnamelower.find("skinny") != -1:
                    cat="Skinny Fit"
                elif itemnamelower.find("straight") != -1:
                    cat="Slim Straight Fit"         
                elif itemnamelower.find("taper") != -1 or itemnamelower.find("carrot") != -1:
                    cat="Slim Tapered Fit"
                elif itemnamelower.find("regular") != -1:
                    cat="Regular Fit"   
                elif itemnamelower.find("bootcut") != -1:
                    cat="Bootcut Fit"                
                else:
                    cat="Slim Fit"

                sheet3.write(jct,0,name)
                sheet3.write(jct,1,dp)
                sheet3.write(jct,2,cat)
                jct=jct+1
            wb.save('myntra.xls')

#def printarray(array):
#    for r in array:
#        for c in r:
#            print(c,end = " ")
#        print()

def fn_add(array, row, total, col):
    total[row][col] += 1
    if price < 1000: array[row][0] += 1
    elif price > 999 and price < 1500: array[row][1] += 1
    elif price > 1499 and price < 2000: array[row][2] += 1
    elif price > 1999 and price < 2500: array[row][3] += 1
    elif price > 2499: array[row][4] += 1
    
def fn_addpc(array, row):
    if price < 1000: array[row][0] += 1
    elif price > 999 and price < 1500: array[row][1] += 1
    elif price > 1499 and price < 2000: array[row][2] += 1
    elif price > 1999 and price < 2500: array[row][3] += 1
    elif price > 2499: array[row][4] += 1

def fn_add_shirt(array, row, total, col):
    total[row][col] += 1
    if price < 1500: array[row][0] += 1
    elif price > 1499 and price < 2000: array[row][1] += 1
    elif price > 1999 and price < 2500: array[row][2] += 1
    elif price > 2499 and price < 3000: array[row][3] += 1
    elif price > 2999 and price < 3500: array[row][4] += 1
    elif price > 3499: array[row][5] += 1

def fn_addpc_shirt(array, row):
    if price < 1500: array[row][0] += 1
    elif price > 1499 and price < 2000: array[row][1] += 1
    elif price > 1999 and price < 2500: array[row][2] += 1
    elif price > 2499 and price < 3000: array[row][3] += 1
    elif price > 2999 and price < 3500: array[row][4] += 1
    elif price > 3499: array[row][5] += 1
    
def fn_add_jean(array, row, total, col):
    total[row][col] += 1
    if price < 2000: array[row][0] += 1
    elif price > 1999 and price < 2500: array[row][1] += 1
    elif price > 2499 and price < 3000: array[row][2] += 1
    elif price > 2999 and price < 3500: array[row][3] += 1
    elif price > 3499 and price < 4000: array[row][4] += 1
    elif price > 3999 and price < 4500: array[row][5] += 1
    elif price > 4499 and price < 5000: array[row][6] += 1
    elif price > 4999 and price < 5500: array[row][7] += 1
    elif price > 5499: array[row][8] += 1

def fn_addpc_jean(array, row):
    if price < 2000: array[row][0] += 1
    elif price > 1999 and price < 2500: array[row][1] += 1
    elif price > 2499 and price < 3000: array[row][2] += 1
    elif price > 2999 and price < 3500: array[row][3] += 1
    elif price > 3499 and price < 4000: array[row][4] += 1
    elif price > 3999 and price < 4500: array[row][5] += 1
    elif price > 4499 and price < 5000: array[row][6] += 1
    elif price > 4999 and price < 5500: array[row][7] += 1
    elif price > 5499: array[row][8] += 1

def write_in_excel(sheet,array,row):
    thead=["Lee","Levis","Pepe Jeans","Jack & Jones", "U.S. Polo Assn.","United Colors of Benetton","American Eagle","Celio"]
    rowno=1
    for item in thead: 
        sheet.write(rowno, 0, item) 
        rowno += 1
    col=1
    for r in array:
        for c in r:
            sheet.write(row,col,c)
            col += 1
        row+=1
        col=1
def write_tshirt_price(sheet):
    thead=["<1000","1000-1500","1500-2000","2000-2500",">2500"]
    col = 1
    for item in thead: 
        sheet.write(0, col, item) 
        col += 1
        
def write_shirt_price(sheet):
    thead=["<1500","1500-2000","2000-2500","2500-3000","3000-3500",">3500"]
    col = 1
    for item in thead: 
        sheet.write(0, col, item) 
        col += 1
        
def write_jean_price(sheet):
    thead=["<2000","2000-2500","2500-3000","3000-3500","3500-4000","4000-4500","4500-5000","5000-5500",">5500"]
    col = 1
    for item in thead: 
        sheet.write(0, col, item) 
        col += 1

wb1 = xlrd.open_workbook("myntra.xls")
# T-SHIRT
sheet1=wb1.sheet_by_name("T-Shirt")

for i in range(sheet1.nrows-1):
    i=i+1
    price = int(sheet1.cell_value(i,1))
    brand = sheet1.cell_value(i,0)
    category = sheet1.cell_value(i,2)
    technique = sheet1.cell_value(i,3)
    if brand =="Lee": brandnumber=0
    elif brand =="Levis": brandnumber=1
    elif brand =="Pepe Jeans": brandnumber=2
    elif brand =="Jack & Jones": brandnumber=3
    elif brand =="U.S. Polo Assn.": brandnumber=4
    elif brand =="United Colors of Benetton": brandnumber=5
    elif brand =="AMERICAN EAGLE OUTFITTERS": brandnumber=6
    elif brand =="Celio": brandnumber=7       

    fn_addpc(tp,brandnumber)

    if category == "Round Neck T-Shirt": fn_add(trn,brandnumber, tot_c, 0)
    elif category == "V-Neck T-Shirt": fn_add(tvn,brandnumber, tot_c, 1)
    elif category == "Polo Neck T-Shirt": fn_add(tpn,brandnumber, tot_c, 2)
    elif category == "Mandarin Collar T-Shirt": fn_add(tmn,brandnumber,tot_c, 3)
    elif category == "Henley": fn_add(thn,brandnumber,tot_c, 4)

    if technique == "Solid": fn_add(tsol,brandnumber,tot_t, 0)
    elif technique == "Printed": fn_add(tpri,brandnumber,tot_t,1)
    elif technique == "Striped": fn_add(tstr,brandnumber,tot_t,2)
    elif technique == "Colourblock": fn_add(tcol,brandnumber,tot_t,3)
    elif technique == "Embroidered": fn_add(temb,brandnumber,tot_t,4)
    elif technique == "Textured Fabric": fn_add(ttex,brandnumber,tot_t,5)

#tp = price wise options
#trn,tvn, tpn, tmn, thn = price wise category wise options
#tsol, tpri, tstr, tcol, temb, ttex = price wise technique wise options
#tot_c = category wise options
#tot_t = technique wise options

sheet4=wb.add_sheet('T-Shirt Price')
write_tshirt_price(sheet4)
write_in_excel(sheet4,tp, 1)

sheet5=wb.add_sheet('T-Shirt Round Neck')
write_tshirt_price(sheet5)
write_in_excel(sheet5,trn, 1)

sheet6=wb.add_sheet('T-Shirt V Neck')
write_tshirt_price(sheet6)
write_in_excel(sheet6,tvn, 1)

sheet7=wb.add_sheet('T-Shirt Polo Neck')
write_tshirt_price(sheet7)
write_in_excel(sheet7,tpn, 1)

sheet8=wb.add_sheet('T-Shirt Mandarin')
write_tshirt_price(sheet8)
write_in_excel(sheet8,tmn, 1)

sheet9=wb.add_sheet('T-Shirt Henley')
write_tshirt_price(sheet9)
write_in_excel(sheet9,thn, 1)

sheet10=wb.add_sheet('T-Shirt Solid')
write_tshirt_price(sheet10)
write_in_excel(sheet10,tsol, 1)

sheet11=wb.add_sheet('T-Shirt Printed')
write_tshirt_price(sheet11)
write_in_excel(sheet11,tpri, 1)

sheet12=wb.add_sheet('T-Shirt Striped')
write_tshirt_price(sheet12)
write_in_excel(sheet12,tstr, 1)

sheet13=wb.add_sheet('T-Shirt Colorblocked')
write_tshirt_price(sheet13)
write_in_excel(sheet13,tcol, 1)

sheet14=wb.add_sheet('T-Shirt Embroidered')
write_tshirt_price(sheet14)
write_in_excel(sheet14,temb, 1)

sheet15=wb.add_sheet('T-Shirt Textured Fabric')
write_tshirt_price(sheet15)
write_in_excel(sheet15,ttex, 1)

sheet16=wb.add_sheet('T-Shirt Category')
thead=["Round Neck","V Neck","Polo Neck","Mandarin","Henley"]
col = 1
for item in thead: 
    sheet16.write(0, col, item) 
    col += 1
write_in_excel(sheet16,tot_c, 1)

sheet17=wb.add_sheet('T-Shirt Technique')
thead=["Solid","Printed","Striped","Colorblocked","Embroidered","Textured Fabric"]
col = 1
for item in thead: 
    sheet17.write(0, col, item) 
    col += 1
write_in_excel(sheet17,tot_t, 1)


# SHIRT
sheet2=wb1.sheet_by_name("Shirt")

for i in range(sheet2.nrows-1):
    i=i+1
    price = int(sheet2.cell_value(i,1))
    brand = sheet2.cell_value(i,0)
    fit = sheet2.cell_value(i,2)
    detail = sheet2.cell_value(i,3)
    if brand =="Lee": brandnumber=0
    elif brand =="Levis": brandnumber=1
    elif brand =="Pepe Jeans": brandnumber=2
    elif brand =="Jack & Jones": brandnumber=3
    elif brand =="U.S. Polo Assn.": brandnumber=4
    elif brand =="United Colors of Benetton": brandnumber=5
    elif brand =="AMERICAN EAGLE OUTFITTERS": brandnumber=6
    elif brand =="Celio": brandnumber=7       

    fn_addpc_shirt(sp,brandnumber)

    if fit == "Super Slim Fit": fn_add_shirt(sss,brandnumber, tot_sf, 0)
    elif fit == "Slim Fit": fn_add_shirt(ssf,brandnumber, tot_sf, 1)
    elif fit == "Regular Fit": fn_add_shirt(srf,brandnumber, tot_sf, 2)

    if detail == "Casual": fn_add_shirt(scas,brandnumber,tot_sd, 0)
    elif detail == "Chambray": fn_add_shirt(scha,brandnumber,tot_sd,1)
    elif detail == "Denim": fn_add_shirt(sden,brandnumber,tot_sd,2)
    elif detail == "Embroidered": fn_add_shirt(semb,brandnumber,tot_sd,3)
    elif detail == "Formal": fn_add_shirt(sfor,brandnumber,tot_sd,4)
    elif detail == "Knitted": fn_add_shirt(skni,brandnumber,tot_sd,5)
    elif detail == "Linen": fn_add_shirt(slin,brandnumber,tot_sd,6)
    elif detail == "Reversible": fn_add_shirt(srev,brandnumber,tot_sd,7)
    elif detail == "Textured Fabric": fn_add_shirt(stex,brandnumber,tot_sd,8)
        
sheet18=wb.add_sheet('Shirt Price')
write_shirt_price(sheet18)
write_in_excel(sheet18,sp,1)
        
sheet19=wb.add_sheet('Shirt Super Slim Fit')
write_shirt_price(sheet19)
write_in_excel(sheet19,sss,1)
        
sheet20=wb.add_sheet('Shirt Slim Fit')
write_shirt_price(sheet20)
write_in_excel(sheet20,ssf,1)
        
sheet21=wb.add_sheet('Shirt Regular Fit')
write_shirt_price(sheet21)
write_in_excel(sheet21,srf,1)
        
sheet22=wb.add_sheet('Shirt Casual')
write_shirt_price(sheet22)
write_in_excel(sheet22,scas,1)

sheet23=wb.add_sheet('Shirt Chambray')
write_shirt_price(sheet23)
write_in_excel(sheet23,scha,1)
        
sheet24=wb.add_sheet('Shirt Denim')
write_shirt_price(sheet24)
write_in_excel(sheet24,sden,1)
        
sheet25=wb.add_sheet('Shirt Embroidered')
write_shirt_price(sheet25)
write_in_excel(sheet25,semb,1)
        
sheet26=wb.add_sheet('Shirt Formal')
write_shirt_price(sheet26)
write_in_excel(sheet26,sfor,1)
        
sheet27=wb.add_sheet('Shirt Knitted')
write_shirt_price(sheet27)
write_in_excel(sheet27,skni,1)
        
sheet28=wb.add_sheet('Shirt Linen')
write_shirt_price(sheet28)
write_in_excel(sheet28,slin,1)
        
sheet29=wb.add_sheet('Shirt Reversible')
write_shirt_price(sheet29)
write_in_excel(sheet29,srev,1)
        
sheet30=wb.add_sheet('Shirt Textured Fabric')
write_shirt_price(sheet30)
write_in_excel(sheet30,stex,1)

sheet31=wb.add_sheet('Shirt Fits')
thead=["Super Slim Fit","Slim Fit","Regular Fit"]
col = 1
for item in thead: 
    sheet31.write(0, col, item) 
    col += 1
write_in_excel(sheet31,tot_sf, 1)

sheet32=wb.add_sheet('Shirt Detail')
thead=["Casual","Chambray","Denim","Embroidered","Formal","Knitted","Linen","Reversible","Textured Fabric"]
col = 1
for item in thead: 
    sheet32.write(0, col, item) 
    col += 1
write_in_excel(sheet32,tot_sd, 1)

# JEAN
sheet3=wb1.sheet_by_name("Jean")

for i in range(sheet3.nrows-1):
    i=i+1
    price = int(sheet3.cell_value(i,1))
    brand = sheet3.cell_value(i,0)
    fit = sheet3.cell_value(i,2)
    if brand =="Lee": brandnumber=0
    elif brand =="Levis": brandnumber=1
    elif brand =="Pepe Jeans": brandnumber=2
    elif brand =="Jack & Jones": brandnumber=3
    elif brand =="U.S. Polo Assn.": brandnumber=4
    elif brand =="United Colors of Benetton": brandnumber=5
    elif brand =="AMERICAN EAGLE OUTFITTERS": brandnumber=6
    elif brand =="Celio": brandnumber=7       

    fn_addpc_jean(jp,brandnumber)

    if fit == "Super Skinny Fit": fn_add_jean(jsup,brandnumber, tot_jf, 0)
    if fit == "Skinny Fit": fn_add_jean(jski,brandnumber, tot_jf, 1)
    if fit == "Slim Fit": fn_add_jean(jsli,brandnumber, tot_jf, 2)
    if fit == "Slim Straight Fit": fn_add_jean(jsls,brandnumber, tot_jf, 3)
    if fit == "Slim Tapered Fit": fn_add_jean(jslt,brandnumber, tot_jf, 4)
    if fit == "Regular Fit": fn_add_jean(jreg,brandnumber, tot_jf, 5)
    if fit == "Bootcut Fit": fn_add_jean(jboo,brandnumber, tot_jf, 6)
        
sheet33=wb.add_sheet('Jean Price')
write_jean_price(sheet33)
write_in_excel(sheet33,jp,1)

sheet34=wb.add_sheet('Jean Super Skinny')
write_jean_price(sheet34)
write_in_excel(sheet34,jsup,1)

sheet35=wb.add_sheet('Jean Skinny')
write_jean_price(sheet35)
write_in_excel(sheet35,jski,1)

sheet36=wb.add_sheet('Jean Slim')
write_jean_price(sheet36)
write_in_excel(sheet36,jsli,1)

sheet37=wb.add_sheet('Jean Slim Straight')
write_jean_price(sheet37)
write_in_excel(sheet37,jsls,1)

sheet38=wb.add_sheet('Jean Slim Tapered')
write_jean_price(sheet38)
write_in_excel(sheet38,jslt,1)

sheet39=wb.add_sheet('Jean Regular')
write_jean_price(sheet39)
write_in_excel(sheet39,jreg,1)

sheet40=wb.add_sheet('Jean Bootcut')
write_jean_price(sheet40)
write_in_excel(sheet40,jboo,1)
 
sheet41=wb.add_sheet('Jean Fits')
thead=["Super Skinny Fit","Skinny Fit","Slim Fit","Slim Straight Fit","Slim Tapered Fit","Regular Fit","Bootcut Fit"]
col = 1
for item in thead: 
    sheet41.write(0, col, item) 
    col += 1
write_in_excel(sheet41,tot_jf, 1)

wb.save('myntra.xls')

def graph(raw_data,heading):
    df = pd.DataFrame(raw_data, columns = ['Price', 'Lee', 'Levis', 'Pepe Jeans', 'Jack & Jones', 'U.S. Polo Assn.', 'United Colors of Benetton', 'American Eagle', 'Celio'])

    pos = list(range(len(df['Lee'])))
    width = 0.1

    fig, ax = plt.subplots(figsize=(17,7))
    
    colors=['#FFC857','#E9724C','#C5283D','#481D24','#255F85','#84828F','#8F2D56','#F3B3A6']
    r1=plt.bar(pos, df['Lee'], width, alpha=0.5, color=colors[0])
    r2=plt.bar([p + width for p in pos], df['Levis'], width, alpha=0.5, color=colors[1])
    r3=plt.bar([p + width*2 for p in pos], df['Pepe Jeans'], width, alpha=0.5, color=colors[2])
    r4=plt.bar([p + width*3 for p in pos], df['Jack & Jones'], width, alpha=0.5, color=colors[3])
    r5=plt.bar([p + width*4 for p in pos], df['U.S. Polo Assn.'], width, alpha=0.5, color=colors[4])
    r6=plt.bar([p + width*5 for p in pos], df['United Colors of Benetton'], width, alpha=0.5, color=colors[5])
    r7=plt.bar([p + width*6 for p in pos], df['American Eagle'], width, alpha=0.5, color=colors[6])
    r8=plt.bar([p + width*7 for p in pos], df['Celio'], width, alpha=0.5, color=colors[7])

    ax.set_ylabel('Options', fontweight="bold")

    ax.set_title(heading)

    ax.set_xticks([p + 4* width for p in pos])

    ax.set_xticklabels(' ')
    
    plt.xlim(min(pos)-width, max(pos)+width*8)
    leemax= max(df['Lee'])
    levismax= max(df['Levis'])
    pepemax= max(df['Pepe Jeans'])
    jackmax= max(df['Jack & Jones'])
    uspolomax= max(df['U.S. Polo Assn.'])
    ucbmax= max(df['United Colors of Benetton'])
    aemax= max(df['American Eagle'])
    celiomax= max(df['Celio'])
    plt.ylim([0, max(leemax,levismax,pepemax,jackmax,uspolomax,ucbmax,aemax,celiomax)+10])

    colors=['#FFC85750','#E9724C50','#C5283D50','#481D2450','#255F8550','#84828F50','#8F2D5650','#F3B3A650']
    colLabels=df['Price']
    rowLabels=['Lee', 'Levis', 'Pepe Jeans', 'Jack & Jones', 'U.S. Polo Assn.', 'United Colors of Benetton', 'American Eagle', 'Celio']
    cellText= [df['Lee'],df['Levis'], df['Pepe Jeans'], df['Jack & Jones'], df['U.S. Polo Assn.'], df['United Colors of Benetton'], df['American Eagle'], df['Celio']]
    the_table = plt.table(cellText=cellText,rowLabels=rowLabels, rowColours=colors,alpha=0.5, colLabels=colLabels,bbox=[0.0,-0.50,1,0.50],loc='bottom')

    plt.subplots_adjust(left=0.2, bottom=0.3)

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = int(rect.get_height())
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
            
    autolabel(r1); autolabel(r2); autolabel(r3); autolabel(r4); autolabel(r5); autolabel(r6); autolabel(r7); autolabel(r8)
    
    plt.grid(alpha=0.5)
    
def tplotgraph(sheet,heading):
    wb=xlrd.open_workbook("myntra.xls")
    sheet1=wb.sheet_by_name(sheet)
    raw_data = {'Price':                    [sheet1.cell_value(0,1),sheet1.cell_value(0,2),sheet1.cell_value(0,3),sheet1.cell_value(0,4), sheet1.cell_value(0,5)],
                'Lee':                      [int(sheet1.cell_value(1,1)),int(sheet1.cell_value(1,2)),int(sheet1.cell_value(1,3)),int(sheet1.cell_value(1,4)), int(sheet1.cell_value(1,5))],
                'Levis':                    [int(sheet1.cell_value(2,1)),int(sheet1.cell_value(2,2)),int(sheet1.cell_value(2,3)),int(sheet1.cell_value(2,4)), int(sheet1.cell_value(2,5))],
                'Pepe Jeans':               [int(sheet1.cell_value(3,1)),int(sheet1.cell_value(3,2)),int(sheet1.cell_value(3,3)),int(sheet1.cell_value(3,4)), int(sheet1.cell_value(3,5))],
                'Jack & Jones':             [int(sheet1.cell_value(4,1)),int(sheet1.cell_value(4,2)),int(sheet1.cell_value(4,3)),int(sheet1.cell_value(4,4)), int(sheet1.cell_value(4,5))],
                'U.S. Polo Assn.':          [int(sheet1.cell_value(5,1)),int(sheet1.cell_value(5,2)),int(sheet1.cell_value(5,3)),int(sheet1.cell_value(5,4)), int(sheet1.cell_value(5,5))],
                'United Colors of Benetton':[int(sheet1.cell_value(6,1)),int(sheet1.cell_value(6,2)),int(sheet1.cell_value(6,3)),int(sheet1.cell_value(6,4)), int(sheet1.cell_value(6,5))],
                'American Eagle':           [int(sheet1.cell_value(7,1)),int(sheet1.cell_value(7,2)),int(sheet1.cell_value(7,3)),int(sheet1.cell_value(7,4)), int(sheet1.cell_value(7,5))],
                'Celio':                    [int(sheet1.cell_value(8,1)),int(sheet1.cell_value(8,2)),int(sheet1.cell_value(8,3)),int(sheet1.cell_value(8,4)), int(sheet1.cell_value(8,5))],
               }
    graph(raw_data,heading)
    plt.savefig("T-Shirt/"+heading+".png")

def tplotgraph4(sheet,heading):
    wb=xlrd.open_workbook("myntra.xls")
    sheet1=wb.sheet_by_name(sheet)
    raw_data = {'Price':                    [sheet1.cell_value(0,1),sheet1.cell_value(0,2),sheet1.cell_value(0,3),sheet1.cell_value(0,4), sheet1.cell_value(0,5), sheet1.cell_value(0,6)],
                'Lee':                      [int(sheet1.cell_value(1,1)),int(sheet1.cell_value(1,2)),int(sheet1.cell_value(1,3)),int(sheet1.cell_value(1,4)), int(sheet1.cell_value(1,5)), int(sheet1.cell_value(1,6))],
                'Levis':                    [int(sheet1.cell_value(2,1)),int(sheet1.cell_value(2,2)),int(sheet1.cell_value(2,3)),int(sheet1.cell_value(2,4)), int(sheet1.cell_value(2,5)), int(sheet1.cell_value(2,6))],
                'Pepe Jeans':               [int(sheet1.cell_value(3,1)),int(sheet1.cell_value(3,2)),int(sheet1.cell_value(3,3)),int(sheet1.cell_value(3,4)), int(sheet1.cell_value(3,5)), int(sheet1.cell_value(3,6))],
                'Jack & Jones':             [int(sheet1.cell_value(4,1)),int(sheet1.cell_value(4,2)),int(sheet1.cell_value(4,3)),int(sheet1.cell_value(4,4)), int(sheet1.cell_value(4,5)), int(sheet1.cell_value(4,6))],
                'U.S. Polo Assn.':          [int(sheet1.cell_value(5,1)),int(sheet1.cell_value(5,2)),int(sheet1.cell_value(5,3)),int(sheet1.cell_value(5,4)), int(sheet1.cell_value(5,5)), int(sheet1.cell_value(5,6))],
                'United Colors of Benetton':[int(sheet1.cell_value(6,1)),int(sheet1.cell_value(6,2)),int(sheet1.cell_value(6,3)),int(sheet1.cell_value(6,4)), int(sheet1.cell_value(6,5)), int(sheet1.cell_value(6,6))],
                'American Eagle':           [int(sheet1.cell_value(7,1)),int(sheet1.cell_value(7,2)),int(sheet1.cell_value(7,3)),int(sheet1.cell_value(7,4)), int(sheet1.cell_value(7,5)), int(sheet1.cell_value(7,6))],
                'Celio':                    [int(sheet1.cell_value(8,1)),int(sheet1.cell_value(8,2)),int(sheet1.cell_value(8,3)),int(sheet1.cell_value(8,4)), int(sheet1.cell_value(8,5)), int(sheet1.cell_value(8,6))],
               }
    graph(raw_data,heading)
    plt.savefig("T-Shirt/"+heading+".png")

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
def tplotgraph2(sheet,heading,i,folder):
    wb=xlrd.open_workbook("myntra.xls")
    sheet1=wb.sheet_by_name(sheet)
    totalpie= sheet1.cell_value(i,1)+sheet1.cell_value(i,2)+sheet1.cell_value(i,3)+sheet1.cell_value(i,4)+sheet1.cell_value(i,5)
    pie1= int((sheet1.cell_value(i,1)*100/totalpie))
    pie2= int((sheet1.cell_value(i,2)*100/totalpie))
    pie3= int((sheet1.cell_value(i,3)*100/totalpie))
    pie4= int((sheet1.cell_value(i,4)*100/totalpie))
    pie5= int((sheet1.cell_value(i,5)*100/totalpie))
    sizes = [pie1,pie2,pie3,pie4,pie5]
    colors= ('#808D8E','#F8C7CC','#9F7E69','#B1F8F2','#FFFC99')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, autopct='%1.1f%%', pctdistance=1.15, colors=colors, startangle=0)

    #draw circle
    centre_circle = plt.Circle((0,0),0.80,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
        
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title(heading+"\n")
    #plt.legend(['Round Neck','V Neck','Polo','Mandarin','Henley'], loc='upper center', ncol=5,  shadow=True)
    plt.savefig("T-Shirt/"+folder+"/"+heading+".png")
    
def tplotgraph3(sheet,heading,i,folder):
    wb=xlrd.open_workbook("myntra.xls")
    sheet1=wb.sheet_by_name(sheet)
    totalpie= sheet1.cell_value(i,1)+sheet1.cell_value(i,2)+sheet1.cell_value(i,3)+sheet1.cell_value(i,4)+sheet1.cell_value(i,5)+sheet1.cell_value(i,6)
    pie1= int((sheet1.cell_value(i,1)*100/totalpie))
    pie2= int((sheet1.cell_value(i,2)*100/totalpie))
    pie3= int((sheet1.cell_value(i,3)*100/totalpie))
    pie4= int((sheet1.cell_value(i,4)*100/totalpie))
    pie5= int((sheet1.cell_value(i,5)*100/totalpie))
    pie6= int((sheet1.cell_value(i,6)*100/totalpie))
    sizes = [pie1,pie2,pie3,pie4,pie5,pie6]
    colors= ('#808D8E','#F8C7CC','#9F7E69','#B1F8F2','#BCD39C','#FFFC99')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, autopct='%1.1f%%', pctdistance=1.15, colors=colors, startangle=0)

    #draw circle
    centre_circle = plt.Circle((0,0),0.80,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
        
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title(heading+"\n")
    #plt.legend(['Solid','Printed','Striped','Colorblocked','Embroidered','Textured Fabric'], loc='upper center', ncol=3,  shadow=True)
    plt.savefig("T-Shirt/"+folder+"/"+heading+".png")

tplotgraph("T-Shirt Price","Number of Options per Price Point for T-Shirts")
tplotgraph("T-Shirt Round Neck","Number of Options per Price Point for Round Neck T-Shirts")
tplotgraph("T-Shirt V Neck","Number of Options per Price Point for V Neck T-Shirts")
tplotgraph("T-Shirt Polo Neck","Number of Options per Price Point for Polo T-Shirts")
tplotgraph("T-Shirt Mandarin","Number of Options per Price Point for Mandarin Collar T-Shirts")
tplotgraph("T-Shirt Henley","Number of Options per Price Point for Henley T-Shirts")
tplotgraph("T-Shirt Solid","Number of Options per Price Point for Solid T-Shirts")
tplotgraph("T-Shirt Printed","Number of Options per Price Point for Printed T-Shirts")
tplotgraph("T-Shirt Striped","Number of Options per Price Point for Striped T-Shirts")
tplotgraph("T-Shirt Colorblocked","Number of Options per Price Point for Colorblocked T-Shirts")
tplotgraph("T-Shirt Embroidered","Number of Options per Price Point for Embroidered T-Shirts")
tplotgraph("T-Shirt Textured Fabric","Number of Options per Price Point for Textured Fabric T-Shirts")
tplotgraph("T-Shirt Category","Number of Options per Category for T-Shirts")
tplotgraph4("T-Shirt Technique","Number of Options per Technique for T-Shirts")

tplotgraph2("T-Shirt Price", "Lee", 1,"Price")
tplotgraph2("T-Shirt Price", "Levis", 2,"Price")
tplotgraph2("T-Shirt Price", "Pepe Jeans", 3,"Price")
tplotgraph2("T-Shirt Price", "Jack & Jones", 4,"Price")
tplotgraph2("T-Shirt Price", "U.S. Polo Assn.", 5,"Price")
tplotgraph2("T-Shirt Price", "United Colors of Benetton", 6,"Price")
tplotgraph2("T-Shirt Price", "American Eagle", 7,"Price")
tplotgraph2("T-Shirt Price", "Celio", 8,"Price")

tplotgraph2("T-Shirt Category", "Lee", 1,"Category")
tplotgraph2("T-Shirt Category", "Levis", 2,"Category")
tplotgraph2("T-Shirt Category", "Pepe Jeans", 3,"Category")
tplotgraph2("T-Shirt Category", "Jack & Jones", 4,"Category")
tplotgraph2("T-Shirt Category", "U.S. Polo Assn.", 5,"Category")
tplotgraph2("T-Shirt Category", "United Colors of Benetton", 6,"Category")
tplotgraph2("T-Shirt Category", "American Eagle", 7,"Category")
tplotgraph2("T-Shirt Category", "Celio", 8,"Category")

tplotgraph3("T-Shirt Technique", "Lee", 1,"Technique")
tplotgraph3("T-Shirt Technique", "Levis", 2,"Technique")
tplotgraph3("T-Shirt Technique", "Pepe Jeans", 3,"Technique")
tplotgraph3("T-Shirt Technique", "Jack & Jones", 4,"Technique")
tplotgraph3("T-Shirt Technique", "U.S. Polo Assn.", 5,"Technique")
tplotgraph3("T-Shirt Technique", "United Colors of Benetton", 6,"Technique")
tplotgraph3("T-Shirt Technique", "American Eagle", 7,"Technique")
tplotgraph3("T-Shirt Technique", "Celio", 8,"Technique")

def splotgraph(sheet,heading):
    wb=xlrd.open_workbook("myntra.xls")
    sheet1=wb.sheet_by_name(sheet)
    raw_data = {'Price':                    [sheet1.cell_value(0,1),sheet1.cell_value(0,2),sheet1.cell_value(0,3),sheet1.cell_value(0,4), sheet1.cell_value(0,5), sheet1.cell_value(0,6),],
                'Lee':                      [int(sheet1.cell_value(1,1)),int(sheet1.cell_value(1,2)),int(sheet1.cell_value(1,3)),int(sheet1.cell_value(1,4)), int(sheet1.cell_value(1,5)), int(sheet1.cell_value(1,6)),],
                'Levis':                    [int(sheet1.cell_value(2,1)),int(sheet1.cell_value(2,2)),int(sheet1.cell_value(2,3)),int(sheet1.cell_value(2,4)), int(sheet1.cell_value(2,5)), int(sheet1.cell_value(2,6)),],
                'Pepe Jeans':               [int(sheet1.cell_value(3,1)),int(sheet1.cell_value(3,2)),int(sheet1.cell_value(3,3)),int(sheet1.cell_value(3,4)), int(sheet1.cell_value(3,5)), int(sheet1.cell_value(3,6)),],
                'Jack & Jones':             [int(sheet1.cell_value(4,1)),int(sheet1.cell_value(4,2)),int(sheet1.cell_value(4,3)),int(sheet1.cell_value(4,4)), int(sheet1.cell_value(4,5)), int(sheet1.cell_value(4,6)),],
                'U.S. Polo Assn.':          [int(sheet1.cell_value(5,1)),int(sheet1.cell_value(5,2)),int(sheet1.cell_value(5,3)),int(sheet1.cell_value(5,4)), int(sheet1.cell_value(5,5)), int(sheet1.cell_value(5,6)),],
                'United Colors of Benetton':[int(sheet1.cell_value(6,1)),int(sheet1.cell_value(6,2)),int(sheet1.cell_value(6,3)),int(sheet1.cell_value(6,4)), int(sheet1.cell_value(6,5)), int(sheet1.cell_value(6,6)),],
                'American Eagle':           [int(sheet1.cell_value(7,1)),int(sheet1.cell_value(7,2)),int(sheet1.cell_value(7,3)),int(sheet1.cell_value(7,4)), int(sheet1.cell_value(7,5)), int(sheet1.cell_value(7,6)),],
                'Celio':                    [int(sheet1.cell_value(8,1)),int(sheet1.cell_value(8,2)),int(sheet1.cell_value(8,3)),int(sheet1.cell_value(8,4)), int(sheet1.cell_value(8,5)), int(sheet1.cell_value(8,6)),],
               }
    graph(raw_data,heading)
    plt.savefig("Shirt/"+heading+".png")

def splotgraph1(sheet,heading):
    wb=xlrd.open_workbook("myntra.xls")
    sheet1=wb.sheet_by_name(sheet)
    raw_data = {'Price':                    [sheet1.cell_value(0,1),sheet1.cell_value(0,2),sheet1.cell_value(0,3),],
                'Lee':                      [int(sheet1.cell_value(1,1)),int(sheet1.cell_value(1,2)),int(sheet1.cell_value(1,3)),],
                'Levis':                    [int(sheet1.cell_value(2,1)),int(sheet1.cell_value(2,2)),int(sheet1.cell_value(2,3)),],
                'Pepe Jeans':               [int(sheet1.cell_value(3,1)),int(sheet1.cell_value(3,2)),int(sheet1.cell_value(3,3)),],
                'Jack & Jones':             [int(sheet1.cell_value(4,1)),int(sheet1.cell_value(4,2)),int(sheet1.cell_value(4,3)),],
                'U.S. Polo Assn.':          [int(sheet1.cell_value(5,1)),int(sheet1.cell_value(5,2)),int(sheet1.cell_value(5,3)),],
                'United Colors of Benetton':[int(sheet1.cell_value(6,1)),int(sheet1.cell_value(6,2)),int(sheet1.cell_value(6,3)),],
                'American Eagle':           [int(sheet1.cell_value(7,1)),int(sheet1.cell_value(7,2)),int(sheet1.cell_value(7,3)),],
                'Celio':                    [int(sheet1.cell_value(8,1)),int(sheet1.cell_value(8,2)),int(sheet1.cell_value(8,3)),],
               }
    graph(raw_data,heading)
    plt.savefig("Shirt/"+heading+".png")

def splotgraph2(sheet,heading):
    wb=xlrd.open_workbook("myntra.xls")
    sheet1=wb.sheet_by_name(sheet)
    raw_data = {'Price':                    [sheet1.cell_value(0,1),sheet1.cell_value(0,2),sheet1.cell_value(0,3),sheet1.cell_value(0,4), sheet1.cell_value(0,5), sheet1.cell_value(0,6),sheet1.cell_value(0,7),sheet1.cell_value(0,8),sheet1.cell_value(0,9),],
                'Lee':                      [int(sheet1.cell_value(1,1)),int(sheet1.cell_value(1,2)),int(sheet1.cell_value(1,3)),int(sheet1.cell_value(1,4)), int(sheet1.cell_value(1,5)), int(sheet1.cell_value(1,6)), int(sheet1.cell_value(1,7)), int(sheet1.cell_value(1,8)), int(sheet1.cell_value(1,9)),],
                'Levis':                    [int(sheet1.cell_value(2,1)),int(sheet1.cell_value(2,2)),int(sheet1.cell_value(2,3)),int(sheet1.cell_value(2,4)), int(sheet1.cell_value(2,5)), int(sheet1.cell_value(2,6)), int(sheet1.cell_value(2,7)), int(sheet1.cell_value(2,8)), int(sheet1.cell_value(2,9)),],
                'Pepe Jeans':               [int(sheet1.cell_value(3,1)),int(sheet1.cell_value(3,2)),int(sheet1.cell_value(3,3)),int(sheet1.cell_value(3,4)), int(sheet1.cell_value(3,5)), int(sheet1.cell_value(3,6)), int(sheet1.cell_value(3,7)), int(sheet1.cell_value(3,8)), int(sheet1.cell_value(3,9)),],
                'Jack & Jones':             [int(sheet1.cell_value(4,1)),int(sheet1.cell_value(4,2)),int(sheet1.cell_value(4,3)),int(sheet1.cell_value(4,4)), int(sheet1.cell_value(4,5)), int(sheet1.cell_value(4,6)), int(sheet1.cell_value(4,7)), int(sheet1.cell_value(4,8)), int(sheet1.cell_value(4,9)),],
                'U.S. Polo Assn.':          [int(sheet1.cell_value(5,1)),int(sheet1.cell_value(5,2)),int(sheet1.cell_value(5,3)),int(sheet1.cell_value(5,4)), int(sheet1.cell_value(5,5)), int(sheet1.cell_value(5,6)), int(sheet1.cell_value(5,7)), int(sheet1.cell_value(5,8)), int(sheet1.cell_value(5,9)),],
                'United Colors of Benetton':[int(sheet1.cell_value(6,1)),int(sheet1.cell_value(6,2)),int(sheet1.cell_value(6,3)),int(sheet1.cell_value(6,4)), int(sheet1.cell_value(6,5)), int(sheet1.cell_value(6,6)), int(sheet1.cell_value(6,7)), int(sheet1.cell_value(6,8)), int(sheet1.cell_value(6,9)),],
                'American Eagle':           [int(sheet1.cell_value(7,1)),int(sheet1.cell_value(7,2)),int(sheet1.cell_value(7,3)),int(sheet1.cell_value(7,4)), int(sheet1.cell_value(7,5)), int(sheet1.cell_value(7,6)), int(sheet1.cell_value(7,7)), int(sheet1.cell_value(7,8)), int(sheet1.cell_value(7,9)),],
                'Celio':                    [int(sheet1.cell_value(8,1)),int(sheet1.cell_value(8,2)),int(sheet1.cell_value(8,3)),int(sheet1.cell_value(8,4)), int(sheet1.cell_value(8,5)), int(sheet1.cell_value(8,6)), int(sheet1.cell_value(8,7)), int(sheet1.cell_value(8,8)), int(sheet1.cell_value(8,9)),],
               }
    graph(raw_data,heading)
    plt.savefig("Shirt/"+heading+".png")
    
def splotgraph3(sheet,heading,i,folder):
    wb=xlrd.open_workbook("myntra.xls")
    sheet1=wb.sheet_by_name(sheet)
    totalpie= sheet1.cell_value(i,1)+sheet1.cell_value(i,2)+sheet1.cell_value(i,3)
    pie1= int((sheet1.cell_value(i,1)*100/totalpie))
    pie2= int((sheet1.cell_value(i,2)*100/totalpie))
    pie3= int((sheet1.cell_value(i,3)*100/totalpie))
    sizes = [pie1,pie2,pie3]
    colors= ('#808D8E','#F8C7CC','#9F7E69')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, autopct='%1.1f%%', pctdistance=1.15, colors=colors, startangle=0)

    #draw circle
    centre_circle = plt.Circle((0,0),0.80,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
        
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title(heading+"\n")
    #plt.legend(['Round Neck','V Neck','Polo','Mandarin','Henley'], loc='upper center', ncol=5,  shadow=True)
    plt.savefig("Shirt/"+folder+"/"+heading+".png")
    
def splotgraph4(sheet,heading,i,folder):
    wb=xlrd.open_workbook("myntra.xls")
    sheet1=wb.sheet_by_name(sheet)
    totalpie= sheet1.cell_value(i,1)+sheet1.cell_value(i,2)+sheet1.cell_value(i,3)+sheet1.cell_value(i,4)+sheet1.cell_value(i,5)+sheet1.cell_value(i,6)
    pie1= int((sheet1.cell_value(i,1)*100/totalpie))
    pie2= int((sheet1.cell_value(i,2)*100/totalpie))
    pie3= int((sheet1.cell_value(i,3)*100/totalpie))
    pie4= int((sheet1.cell_value(i,4)*100/totalpie))
    pie5= int((sheet1.cell_value(i,5)*100/totalpie))
    pie6= int((sheet1.cell_value(i,6)*100/totalpie))
    sizes = [pie1,pie2,pie3,pie4,pie5,pie6]
    colors= ('#808D8E','#F8C7CC','#9F7E69','#B1F8F2','#FFFC99','#BCD39C')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, autopct='%1.1f%%', pctdistance=1.15, colors=colors, startangle=0)

    #draw circle
    centre_circle = plt.Circle((0,0),0.80,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
        
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title(heading+"\n")
    #plt.legend(['Round Neck','V Neck','Polo','Mandarin','Henley'], loc='upper center', ncol=5,  shadow=True)
    plt.savefig("Shirt/"+folder+"/"+heading+".png")

splotgraph("Shirt Price","Number of Options per Price Point for Shirts")
splotgraph("Shirt Super Slim Fit","Number of Options per Price Point for Super Slim Fit Shirt")
splotgraph("Shirt Slim Fit","Number of Options per Price Point for Slim Fit Shirt")
splotgraph("Shirt Regular Fit","Number of Options per Price Point for Regular Fit Shirt")
splotgraph("Shirt Casual","Number of Options per Price Point for Casual Shirt")
splotgraph("Shirt Chambray","Number of Options per Price Point for Chambray Shirt")
splotgraph("Shirt Denim","Number of Options per Price Point for Denim Shirt")
splotgraph("Shirt Embroidered","Number of Options per Price Point for Embroidered Shirt")
splotgraph("Shirt Formal","Number of Options per Price Point for Formal Shirt")
splotgraph("Shirt Knitted","Number of Options per Price Point for Knitted Shirt")
splotgraph("Shirt Linen","Number of Options per Price Point for Linen Shirt")
splotgraph("Shirt Reversible","Number of Options per Price Point for Reversible Shirt")
splotgraph("Shirt Textured Fabric","Number of Options per Price Point for Shirt with Textured Shell Fabric")
splotgraph1("Shirt Fits","Number of Options per Fit for Shirt")
splotgraph2("Shirt Detail","Number of Options per Category for Shirt")

splotgraph3("Shirt Fits", "Lee", 1,"Fits")
splotgraph3("Shirt Fits", "Levis", 2,"Fits")
splotgraph3("Shirt Fits", "Pepe Jeans", 3,"Fits")
splotgraph3("Shirt Fits", "Jack & Jones", 4,"Fits")
splotgraph3("Shirt Fits", "U.S. Polo Assn.", 5,"Fits")
splotgraph3("Shirt Fits", "United Colors of Benetton", 6,"Fits")
splotgraph3("Shirt Fits", "American Eagle", 7,"Fits")
splotgraph3("Shirt Fits", "Celio", 8,"Fits")

splotgraph4("Shirt Price", "Lee", 1,"Price")
splotgraph4("Shirt Price", "Levis", 2,"Price")
splotgraph4("Shirt Price", "Pepe Jeans", 3,"Price")
splotgraph4("Shirt Price", "Jack & Jones", 4,"Price")
splotgraph4("Shirt Price", "U.S. Polo Assn.", 5,"Price")
splotgraph4("Shirt Price", "United Colors of Benetton", 6,"Price")
splotgraph4("Shirt Price", "American Eagle", 7,"Price")
splotgraph4("Shirt Price", "Celio", 8,"Price")

def jplotgraph(sheet,heading):
    wb=xlrd.open_workbook("myntra.xls")
    sheet1=wb.sheet_by_name(sheet)
    raw_data = {'Price':                    [sheet1.cell_value(0,1),sheet1.cell_value(0,2),sheet1.cell_value(0,3),sheet1.cell_value(0,4), sheet1.cell_value(0,5), sheet1.cell_value(0,6),sheet1.cell_value(0,7), sheet1.cell_value(0,8), sheet1.cell_value(0,9),],
                'Lee':                      [int(sheet1.cell_value(1,1)),int(sheet1.cell_value(1,2)),int(sheet1.cell_value(1,3)),int(sheet1.cell_value(1,4)), int(sheet1.cell_value(1,5)), int(sheet1.cell_value(1,6)),int(sheet1.cell_value(1,7)), int(sheet1.cell_value(1,8)), int(sheet1.cell_value(1,9)),],
                'Levis':                    [int(sheet1.cell_value(2,1)),int(sheet1.cell_value(2,2)),int(sheet1.cell_value(2,3)),int(sheet1.cell_value(2,4)), int(sheet1.cell_value(2,5)), int(sheet1.cell_value(2,6)),int(sheet1.cell_value(2,7)), int(sheet1.cell_value(2,8)), int(sheet1.cell_value(2,9)),],
                'Pepe Jeans':               [int(sheet1.cell_value(3,1)),int(sheet1.cell_value(3,2)),int(sheet1.cell_value(3,3)),int(sheet1.cell_value(3,4)), int(sheet1.cell_value(3,5)), int(sheet1.cell_value(3,6)),int(sheet1.cell_value(3,7)), int(sheet1.cell_value(3,8)), int(sheet1.cell_value(3,9)),],
                'Jack & Jones':             [int(sheet1.cell_value(4,1)),int(sheet1.cell_value(4,2)),int(sheet1.cell_value(4,3)),int(sheet1.cell_value(4,4)), int(sheet1.cell_value(4,5)), int(sheet1.cell_value(4,6)),int(sheet1.cell_value(4,7)), int(sheet1.cell_value(4,8)), int(sheet1.cell_value(4,9)),],
                'U.S. Polo Assn.':          [int(sheet1.cell_value(5,1)),int(sheet1.cell_value(5,2)),int(sheet1.cell_value(5,3)),int(sheet1.cell_value(5,4)), int(sheet1.cell_value(5,5)), int(sheet1.cell_value(5,6)),int(sheet1.cell_value(5,7)), int(sheet1.cell_value(5,8)), int(sheet1.cell_value(5,9)),],
                'United Colors of Benetton':[int(sheet1.cell_value(6,1)),int(sheet1.cell_value(6,2)),int(sheet1.cell_value(6,3)),int(sheet1.cell_value(6,4)), int(sheet1.cell_value(6,5)), int(sheet1.cell_value(6,6)),int(sheet1.cell_value(6,7)), int(sheet1.cell_value(6,8)), int(sheet1.cell_value(6,9)),],
                'American Eagle':           [int(sheet1.cell_value(7,1)),int(sheet1.cell_value(7,2)),int(sheet1.cell_value(7,3)),int(sheet1.cell_value(7,4)), int(sheet1.cell_value(7,5)), int(sheet1.cell_value(7,6)),int(sheet1.cell_value(7,7)), int(sheet1.cell_value(7,8)), int(sheet1.cell_value(7,9)),],
                'Celio':                    [int(sheet1.cell_value(8,1)),int(sheet1.cell_value(8,2)),int(sheet1.cell_value(8,3)),int(sheet1.cell_value(8,4)), int(sheet1.cell_value(8,5)), int(sheet1.cell_value(8,6)),int(sheet1.cell_value(8,7)), int(sheet1.cell_value(8,8)), int(sheet1.cell_value(8,9)),],
               }
    graph(raw_data,heading)
    plt.savefig("Jean/"+heading+".png")

def jplotgraph1(sheet,heading):
    wb=xlrd.open_workbook("myntra.xls")
    sheet1=wb.sheet_by_name(sheet)
    raw_data = {'Price':                    [sheet1.cell_value(0,1),sheet1.cell_value(0,2),sheet1.cell_value(0,3),sheet1.cell_value(0,4), sheet1.cell_value(0,5), sheet1.cell_value(0,6),sheet1.cell_value(0,7),],
                'Lee':                      [int(sheet1.cell_value(1,1)),int(sheet1.cell_value(1,2)),int(sheet1.cell_value(1,3)),int(sheet1.cell_value(1,4)), int(sheet1.cell_value(1,5)), int(sheet1.cell_value(1,6)),int(sheet1.cell_value(1,7)),],
                'Levis':                    [int(sheet1.cell_value(2,1)),int(sheet1.cell_value(2,2)),int(sheet1.cell_value(2,3)),int(sheet1.cell_value(2,4)), int(sheet1.cell_value(2,5)), int(sheet1.cell_value(2,6)),int(sheet1.cell_value(2,7)),],
                'Pepe Jeans':               [int(sheet1.cell_value(3,1)),int(sheet1.cell_value(3,2)),int(sheet1.cell_value(3,3)),int(sheet1.cell_value(3,4)), int(sheet1.cell_value(3,5)), int(sheet1.cell_value(3,6)),int(sheet1.cell_value(3,7)),],
                'Jack & Jones':             [int(sheet1.cell_value(4,1)),int(sheet1.cell_value(4,2)),int(sheet1.cell_value(4,3)),int(sheet1.cell_value(4,4)), int(sheet1.cell_value(4,5)), int(sheet1.cell_value(4,6)),int(sheet1.cell_value(4,7)),],
                'U.S. Polo Assn.':          [int(sheet1.cell_value(5,1)),int(sheet1.cell_value(5,2)),int(sheet1.cell_value(5,3)),int(sheet1.cell_value(5,4)), int(sheet1.cell_value(5,5)), int(sheet1.cell_value(5,6)),int(sheet1.cell_value(5,7)),],
                'United Colors of Benetton':[int(sheet1.cell_value(6,1)),int(sheet1.cell_value(6,2)),int(sheet1.cell_value(6,3)),int(sheet1.cell_value(6,4)), int(sheet1.cell_value(6,5)), int(sheet1.cell_value(6,6)),int(sheet1.cell_value(6,7)),],
                'American Eagle':           [int(sheet1.cell_value(7,1)),int(sheet1.cell_value(7,2)),int(sheet1.cell_value(7,3)),int(sheet1.cell_value(7,4)), int(sheet1.cell_value(7,5)), int(sheet1.cell_value(7,6)),int(sheet1.cell_value(7,7)),],
                'Celio':                    [int(sheet1.cell_value(8,1)),int(sheet1.cell_value(8,2)),int(sheet1.cell_value(8,3)),int(sheet1.cell_value(8,4)), int(sheet1.cell_value(8,5)), int(sheet1.cell_value(8,6)),int(sheet1.cell_value(8,7)),],
               }
    graph(raw_data,heading)
    plt.savefig("Jean/"+heading+".png")

def jplotgraph2(sheet,heading,i,folder):
    wb=xlrd.open_workbook("myntra.xls")
    sheet1=wb.sheet_by_name(sheet)
    totalpie= sheet1.cell_value(i,1)+sheet1.cell_value(i,2)+sheet1.cell_value(i,3)+sheet1.cell_value(i,4)+sheet1.cell_value(i,5)+sheet1.cell_value(i,6)+sheet1.cell_value(i,7)
    pie1= int((sheet1.cell_value(i,1)*100/totalpie))
    pie2= int((sheet1.cell_value(i,2)*100/totalpie))
    pie3= int((sheet1.cell_value(i,3)*100/totalpie))
    pie4= int((sheet1.cell_value(i,4)*100/totalpie))
    pie5= int((sheet1.cell_value(i,5)*100/totalpie))
    pie6= int((sheet1.cell_value(i,6)*100/totalpie))
    pie7= int((sheet1.cell_value(i,7)*100/totalpie))
    sizes = [pie1,pie2,pie3,pie4,pie5,pie6,pie7]
    colors= ('#808D8E','#F8C7CC','#9F7E69','#B1F8F2','#FFFC99','#BCD39C','#D3C1C3')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, autopct='%1.1f%%', pctdistance=1.15, colors=colors, startangle=0)

    #draw circle
    centre_circle = plt.Circle((0,0),0.80,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
        
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title(heading+"\n")
    #plt.legend(['Round Neck','V Neck','Polo','Mandarin','Henley'], loc='upper center', ncol=5,  shadow=True)
    plt.savefig("Jean/"+folder+"/"+heading+".png")

def jplotgraph3(sheet,heading,i,folder):
    wb=xlrd.open_workbook("myntra.xls")
    sheet1=wb.sheet_by_name(sheet)
    totalpie= sheet1.cell_value(i,1)+sheet1.cell_value(i,2)+sheet1.cell_value(i,3)+sheet1.cell_value(i,4)+sheet1.cell_value(i,5)+sheet1.cell_value(i,6)+sheet1.cell_value(i,7)+sheet1.cell_value(i,8)+sheet1.cell_value(i,9)
    pie1= int((sheet1.cell_value(i,1)*100/totalpie))
    pie2= int((sheet1.cell_value(i,2)*100/totalpie))
    pie3= int((sheet1.cell_value(i,3)*100/totalpie))
    pie4= int((sheet1.cell_value(i,4)*100/totalpie))
    pie5= int((sheet1.cell_value(i,5)*100/totalpie))
    pie6= int((sheet1.cell_value(i,6)*100/totalpie))
    pie7= int((sheet1.cell_value(i,7)*100/totalpie))
    pie8= int((sheet1.cell_value(i,8)*100/totalpie))
    pie9= int((sheet1.cell_value(i,9)*100/totalpie))
    sizes = [pie1,pie2,pie3,pie4,pie5,pie6,pie7,pie8,pie9]
    colors= ('#808D8E','#F8C7CC','#9F7E69','#B1F8F2','#FFFC99','#BCD39C','#D3C1C3','#D4E4BC','#BEB7DF')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, autopct='%1.1f%%', pctdistance=1.15, colors=colors, startangle=0)

    #draw circle
    centre_circle = plt.Circle((0,0),0.80,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
        
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title(heading+"\n")
    #plt.legend(['Round Neck','V Neck','Polo','Mandarin','Henley'], loc='upper center', ncol=5,  shadow=True)
    plt.savefig("Jean/"+folder+"/"+heading+".png")

jplotgraph("Jean Price","Number of Options per Price Point for Jeans")
jplotgraph("Jean Super Skinny","Number of Options per Price Point for Super Skinny Fit Jean")
jplotgraph("Jean Skinny","Number of Options per Price Point for Skinny Fit Jean")
jplotgraph("Jean Slim","Number of Options per Price Point for Slim Fit Jean")
jplotgraph("Jean Slim Straight","Number of Options per Price Point for Slim Straight Fit Jean")
jplotgraph("Jean Slim Tapered","Number of Options per Price Point for Slim Tapered Fit Jean")
jplotgraph("Jean Regular","Number of Options per Price Point for Regular Fit Jean")
jplotgraph("Jean Bootcut","Number of Options per Price Point for Bootcut Fit Jean")
jplotgraph1("Jean Fits","Number of Options per Fit for Jeans")

jplotgraph2("Jean Fits", "Lee", 1,"Fits")
jplotgraph2("Jean Fits", "Levis", 2,"Fits")
jplotgraph2("Jean Fits", "Pepe Jeans", 3,"Fits")
jplotgraph2("Jean Fits", "Jack & Jones", 4,"Fits")
jplotgraph2("Jean Fits", "U.S. Polo Assn.", 5,"Fits")
jplotgraph2("Jean Fits", "United Colors of Benetton", 6,"Fits")
jplotgraph2("Jean Fits", "American Eagle", 7,"Fits")
jplotgraph2("Jean Fits", "Celio", 8,"Fits")

jplotgraph3("Jean Price", "Lee", 1,"Price")
jplotgraph3("Jean Price", "Levis", 2,"Price")
jplotgraph3("Jean Price", "Pepe Jeans", 3,"Price")
jplotgraph3("Jean Price", "Jack & Jones", 4,"Price")
jplotgraph3("Jean Price", "U.S. Polo Assn.", 5,"Price")
jplotgraph3("Jean Price", "United Colors of Benetton", 6,"Price")
jplotgraph3("Jean Price", "American Eagle", 7,"Price")
jplotgraph3("Jean Price", "Celio", 8,"Price")
'''
#conclusions
wb=xlrd.open_workbook("myntra.xls")

def findarray(sheetname,heading,phrase,a,b):
    str=""
    sheet=wb.sheet_by_name(sheetname)
    sum=[0,0,0,0,0,0,0,0]
    array=[[0 for i in range(a)] for j in range(b)]
    for i in range(b):
        for j in  range(a):
            array[i][j]=sheet.cell_value(i+1, j+1)
            sum[i]+=array[i][j]
    for x in range(a):
        avg=(array[0][x]+array[1][x]+array[2][x]+array[3][x]+array[4][x]+array[5][x]+array[6][x]+array[7][x])/8
        if int(array[0][x])==0:
            ct=0
            for y in range(b):
                if array[y][x] > 0:
                    ct += 1
            if ct > 3:
                str=str+"Most competitors provide options"+phrase+heading[x]+" unlike Lee.\n"
        elif array[0][x] == min(array[0][x],array[1][x],array[2][x],array[3][x],array[4][x],array[5][x],array[6][x],array[7][x]):
            str=str+"Lee provides least number of options"+phrase+heading[x]+".\n"
        elif array[0][x] < (0.75*avg):
            str=str+"Lee provides considerably lesser number of options than competitor brands"+phrase+heading[x]+".\n"
        elif array[0][x] == max(array[0][x],array[1][x],array[2][x],array[3][x],array[4][x],array[5][x],array[6][x],array[7][x]):
            str=str+"Lee can reduce options"+phrase+heading[x]+".\n"
        else:
            str=str+"Lee provides sufficient options"+phrase+heading[x]+".\n"
    lee=sum[0]
    sum.sort()
    if sheetname=="T-Shirt Price":
        if sum[0] == lee or sum[1] == lee or sum[2] == lee or sum[3] == lee :
            str=str+"Lee provides least number of options of "+sheetname[0:7]+".\n"
    return str
#conclusion for t-shirt price point
file1 = open("T-ShirtPrice.txt","w")
heading=['< 1000','1000 - 1500','1500 - 2000','2000 - 2500','> 2500']
str=findarray('T-Shirt Price',heading," in the price range ",5,8)
file1.write(str)
file1.close()

file1 = open("T-ShirtCategory.txt","w")
heading=['round neck t-shirt', 'v-neck t-shirt', 'polo t-shirt', 'mandarin t-shirt','henley']
str=findarray('T-Shirt Category',heading," of ",5,8)
if str != "": file1.write("Overview\n"+str)
heading=['< 1000','1000 - 1500','1500 - 2000','2000 - 2500','> 2500']
str=findarray('T-Shirt Round Neck',heading," in the price range ",5,8)
if str != "": file1.write("\nRound Neck T-Shirt\n"+str)
str=findarray('T-Shirt V Neck',heading," in the price range ",5,8)
if str != "": file1.write("\nV Neck T-Shirt\n"+str)
str=findarray('T-Shirt Polo Neck',heading," in the price range ",5,8)
if str != "": file1.write("\nPolo T-Shirt\n"+str)
str=findarray('T-Shirt Mandarin',heading," in the price range ",5,8)
if str != "": file1.write("\nMandarin T-Shirt\n"+str)
str=findarray('T-Shirt Henley',heading," in the price range ",5,8)
if str != "": file1.write("\nHenley T-Shirt\n"+str)
file1.close()

file1 = open("T-ShirtTechnique.txt","w")
heading=['solid t-shirt', 'printed t-shirt', 'striped t-shirt', 'color blocked t-shirt','embroidered t-shirt','textured fabric']
str=findarray('T-Shirt Technique',heading," of ",6,8)
if str != "": file1.write("Overview\n"+str)
heading=['< 1000','1000 - 1500','1500 - 2000','2000 - 2500','> 2500']
str=findarray('T-Shirt Solid',heading," in the price range ",5,8)
if str != "": file1.write("\nSolid T-Shirt\n"+str)
str=findarray('T-Shirt Printed',heading," in the price range ",5,8)
if str != "": file1.write("\nPrinted T-Shirt\n"+str)
str=findarray('T-Shirt Striped',heading," in the price range ",5,8)
if str != "": file1.write("\nStriped T-Shirt\n"+str)
str=findarray('T-Shirt Colorblocked',heading," in the price range ",5,8)
if str != "": file1.write("\nColorblocked T-Shirt\n"+str)
str=findarray('T-Shirt Embroidered',heading," in the price range ",5,8)
if str != "": file1.write("\nEmbroidered T-Shirt\n"+str)
str=findarray('T-Shirt Textured Fabric',heading," in the price range ",5,8)
if str != "": file1.write("\nTextured Fabric T-Shirt\n"+str)
file1.close()

#conclusion for shirt price point
file1 = open("ShirtPrice.txt","w")
heading=['< 1500','1500 - 2000','2000 - 2500','2500 - 3000','3000 - 3500','> 3500']
str=findarray('Shirt Price',heading," in the price range ",6,8)
file1.write(str)
file1.close()

file1 = open("ShirtFits.txt","w")
heading=['super slim fit','slim fit','regular fit']
str=findarray('Shirt Fits',heading," of ",3,8)
if str != "": file1.write("Overview\n"+str)
heading=['< 1500','1500 - 2000','2000 - 2500','2500 - 3000','3000 - 3500','> 3500']
str=findarray('Shirt Super Slim Fit',heading," in the price range ",5,8)
if str != "": file1.write("\nSuper Slim Fit Shirt\n"+str)
str=findarray('Shirt Slim Fit',heading," in the price range ",5,8)
if str != "": file1.write("\nSlim Fit Shirt\n"+str)
str=findarray('Shirt Regular Fit',heading," in the price range ",5,8)
if str != "": file1.write("\nRegular Fit Shirt\n"+str)

file1.close()

file1 = open("ShirtDetail.txt","w")
heading=['casual shirt','chambray shirt','denim shirt','embroidered shirt','formal shirt','knitted shirt','linen shirt','reversible shirt','textured fabric shirt']
str=findarray('Shirt Detail',heading," of ",9,8)
if str != "": file1.write("Overview\n"+str)
heading=['< 1000','1000 - 1500','1500 - 2000','2000 - 2500','> 2500']
str=findarray('Shirt Casual',heading," in the price range ",5,8)
if str != "": file1.write("\nCasual Shirt\n"+str)
str=findarray('Shirt Chambray',heading," in the price range ",5,8)
if str != "": file1.write("\nChambray Shirt\n"+str)
str=findarray('Shirt Denim',heading," in the price range ",5,8)
if str != "": file1.write("\nDenim Shirt\n"+str)
str=findarray('Shirt Embroidered',heading," in the price range ",5,8)
if str != "": file1.write("\nEmbroidered Shirt\n"+str)
str=findarray('Shirt Formal',heading," in the price range ",5,8)
if str != "": file1.write("\nFormal Shirt\n"+str)
str=findarray('Shirt Knitted',heading," in the price range ",5,8)
if str != "": file1.write("\nKnitted Shirt\n"+str)
str=findarray('Shirt Linen',heading," in the price range ",5,8)
if str != "": file1.write("\nLinen Shirt\n"+str)
str=findarray('Shirt Reversible',heading," in the price range ",5,8)
if str != "": file1.write("\nReversible Shirt\n"+str)
str=findarray('Shirt Textured Fabric',heading," in the price range ",5,8)
if str != "": file1.write("\nTextured Fabric Shirt\n"+str)
file1.close()

#conclusion for jean price point
file1 = open("JeanPrice.txt","w")
heading=['< 2000','2000 - 2500','2500 - 3000','3000 - 3500','3500 - 4000','4000 - 4500','4500 - 5000','5000 - 5500','> 5500']
str=findarray('Jean Price',heading," in the price range ",9,8)
file1.write(str)
file1.close()

file1 = open("JeanFits.txt","w")
heading=['super skinny fit','skinny fit','slim fit','slim straight fit','slim tapered fit','regular fit','bootcut fit']
str=findarray('Jean Fits',heading," of ",7,8)
if str != "": file1.write("Overview\n"+str)
heading=['< 2000','2000 - 2500','2500 - 3000','3000 - 3500','3500 - 4000','4000 - 4500','4500 - 5000','5000 - 5500','> 5500']
str=findarray('Jean Super Skinny',heading," in the price range ",5,8)
if str != "": file1.write("\nSuper Skinny Fit Jeans\n"+str)
str=findarray('Jean Skinny',heading," in the price range ",5,8)
if str != "": file1.write("\nSkinny Fit Jeans\n"+str)
str=findarray('Jean Slim',heading," in the price range ",5,8)
if str != "": file1.write("\nSlim Fit Jean\n"+str)
str=findarray('Jean Slim Straight',heading," in the price range ",5,8)
if str != "": file1.write("\nSlim Straight Fit Jean\n"+str)
str=findarray('Jean Slim Tapered',heading," in the price range ",5,8)
if str != "": file1.write("\nSlim Tapered Fit Jean\n"+str)
str=findarray('Jean Regular',heading," in the price range ",5,8)
if str != "": file1.write("\nRegular Fit Jean\n"+str)
str=findarray('Jean Bootcut',heading," in the price range ",5,8)
if str != "": file1.write("\nBootcut Jean\n"+str)
file1.close()

print("done")
