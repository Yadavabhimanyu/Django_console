import pandas as pd
##import openpyxl
from xlsxwriter.workbook import Workbook
import xlsxwriter

from datetime import date

today = date.today()

d1 = 'Cumulative  Till '+today.strftime("%d/%m/%Y")
d2 = today.strftime("%d/%m/%Y")


data = pd.read_csv(r"C:\Users\vaio\Desktop\daily_report_12.csv")
data2 = pd.read_csv(r"C:\Users\vaio\Downloads\11_report.csv")
##
print(data.head(100))
##
columns_li=data.columns
for col in columns_li:
    data[col].fillna('NULL',inplace=True)

columns_li2=data2.columns
for col2 in columns_li2:
    data2[col2].fillna('NULL',inplace=True)



data1=data.drop_duplicates(subset=['vendor_name','invoice_number','invoice_date','file_name'], keep='first', inplace=False)
print(data1.shape)
data11=data2.drop_duplicates(subset=['vendor_name','invoice_number','invoice_date','file_name'], keep='first', inplace=False)



########33
data_1=data.copy()
print(data_1.shape)
data_1=data_1.drop_duplicates(subset=['vendor_name','invoice_number','invoice_date','file_name'], keep='first', inplace=False)
print(data_1.shape)
data_2=data2.copy()
print(data_2.shape)
data_2=data_2.drop_duplicates(subset=['vendor_name','invoice_number','invoice_date','file_name'], keep='first', inplace=False)
print(data_2.shape)
##########

inv="=COUNTA('Final_Report'!$S:$S)-1"
data_fail="=COUNTIF('Final_Report'!$T:$T,Nos!$B$3)"
ext_pass="=COUNTIF('Final_Report'!$T:$T,Nos!$B$4)"
po_fun="=COUNTIF('Final_Report'!$AD:$AD,Nos!$B$5)"
po_not_found="=COUNTA('Final_Report'!$AD:$AD)-C5"
eway_bill="=COUNTIF('Final_Report'!$AM:$AM,Nos!$B$7)"
IBD_vnd_prt="=COUNTIF('Final_Report'!$AO:$AO,Nos!$B$8)"
IBD_cr_fd="=COUNT('Final_Report'!$AN:$AN)"
IBD_nt_cr="=COUNTIF('Final_Report'!$AO:$AO,Nos!$B$10)"
GRN_fd="=COUNT('Final_Report'!$AQ:$AQ)"
miro_cr="=COUNT('Final_Report'!$AU:$AU)"
miro_fail="=C11-C12"

inv1="=COUNTA('Today_Report'!$S:$S)-1"
data_fail1="=COUNTIF('Today_Report'!$T:$T,Nos!$B$3)"
ext_pass1="=COUNTIF('Today_Report'!$T:$T,Nos!$B$4)"
po_fun1="=COUNTIF('Today_Report'!$AD:$AD,Nos!$B$5)"
po_not_found1="=COUNTA('Today_Report'!$AD:$AD)-D5"
eway_bill1="=COUNTIF('Today_Report'!$AM:$AM,Nos!$B$7)"
IBD_vnd_prt1="=COUNTIF('Today_Report'!$AO:$AO,Nos!$B$8)"
IBD_cr_fd1="=COUNT('Today_Report'!$AN:$AN)"
IBD_nt_cr1="=COUNTIF('Today_Report'!$AO:$AO,Nos!$B$10)"
GRN_fd1="=COUNT('Today_Report'!$AQ:$AQ)"
miro_cr1="=COUNT('Today_Report'!$AU:$AU)"
miro_fail1="=D11-D12"


d2 = today.strftime("%d/%m/%Y")

df = pd.DataFrame({'Bot Detail':['BOT 1','BOT 1','BOT 1','BOT 1','BOT 1','BOT 1','BOT 1','BOT 1','BOT 1','BOT 2','BOT 2','BOT 2'],"Pariculars":['Invoice Received','Data_Extraction_Failed','Extraction Pass','PO Found through Function module','PO Not Found/IBD not found/Scroll Error','EwayBill Portal connection not established','IBD should be created thru Vendor Portal','IBD Created/ Found','IBD Not Created*','GRN Found','MIRO Created','MIRO failed for exception'],
                   d1:[inv,data_fail,ext_pass,po_fun,po_not_found,eway_bill,IBD_vnd_prt,IBD_cr_fd,IBD_nt_cr,GRN_fd,miro_cr,miro_fail],d2:[inv1,data_fail1,ext_pass1,po_fun1,po_not_found1,eway_bill1,IBD_vnd_prt1,IBD_cr_fd1,IBD_nt_cr1,GRN_fd1,miro_cr1,miro_fail1]})


with pd.ExcelWriter(r"C:\Users\vaio\Downloads\report_11.xlsx") as writer:
   
    # use to_excel function and specify the sheet_name and index
    # to store the dataframe in specified sheet
    data.to_excel(writer, sheet_name="miro_report_final", index=False)
    df.to_excel(writer,sheet_name='Nos',index=False)
    data1.to_excel(writer, sheet_name="Final_Report", index=False)
    data11.to_excel(writer, sheet_name="Today_Report", index=False)

print(data_1.shape,data_2.shape)
#############
d2 = today.strftime("%d/%m/%Y")

df2 = pd.DataFrame({'Bot Detail':['BOT 1','BOT 1','BOT 1','BOT 1','BOT 1','BOT 1','BOT 1','BOT 1','BOT 1','BOT 2','BOT 2','BOT 2'],"Pariculars":['Invoice Received','Data_Extraction_Failed','Extraction Pass','PO Found through Function module','PO Not Found/IBD not found/Scroll Error','EwayBill Portal connection not established','IBD should be created thru Vendor Portal','IBD Created/ Found','IBD Not Created*','GRN Found','MIRO Created','MIRO failed for exception'],
                   d1:[inv,data_fail,ext_pass,po_fun,po_not_found,eway_bill,IBD_vnd_prt,IBD_cr_fd,IBD_nt_cr,GRN_fd,miro_cr,miro_fail],d2:[inv1,data_fail1,ext_pass1,po_fun1,po_not_found1,eway_bill1,IBD_vnd_prt1,IBD_cr_fd1,IBD_nt_cr1,GRN_fd1,miro_cr1,miro_fail1]})


with pd.ExcelWriter(r"C:\Users\vaio\Downloads\report_11_2.xlsx") as writer:
   
    # use to_excel function and specify the sheet_name and index
    # to store the dataframe in specified sheet
    data.to_excel(writer, sheet_name="miro_report_final", index=False)
    df2.to_excel(writer,sheet_name='Nos',index=False)
    data_1.to_excel(writer, sheet_name="Final_Report", index=False)
    data_2.to_excel(writer, sheet_name="Today_Report", index=False)




