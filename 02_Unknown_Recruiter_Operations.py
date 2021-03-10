from docxtpl import DocxTemplate
from docx import Document
import datetime
import os

# First the Cover Letter
company_name = input("Enter name of the Company : ") 
position_name = input("Enter name of the Position: ")
address = input("Address: ")




today_date = datetime.datetime.today().strftime('%m/%d/%Y')

doc = DocxTemplate("Cover Letter - Operations - No Recruiter.docx")
context = { 'today_date': today_date, 
           'company_name' : company_name, 
           'position_name' : position_name,
           'address' : address}

doc.render(context)

os.chdir("C:\\Users\\prest\\OneDrive\\Desktop\\Learning\\Areas of Interest\\Programming, Etc\\Python\\CoverLetters\\CL")
doc.save('Cover_letter_'+company_name+'_'+position_name+'.docx')


# Now do the Resume
os.chdir("C:\\Users\\prest\\OneDrive\\Desktop\\Learning\\Areas of Interest\\Programming, Etc\\Python\\CoverLetters")
doc2 = Document('Resume_General.docx')

os.chdir("C:\\Users\\prest\\OneDrive\\Desktop\\Learning\\Areas of Interest\\Programming, Etc\\Python\\CoverLetters\\Resume")
doc2.save('Resume_'+company_name+'_'+position_name+'.docx')