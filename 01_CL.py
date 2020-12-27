from docxtpl import DocxTemplate
import datetime
import os


company_name = input("Enter name of the Company : ") 
position_name = input("Enter name of the Position: ")
address = input("Address: ")
employee = input("HR person or Hiring Manager: ")
employee_title = input("HR title: ")



today_date = datetime.datetime.today().strftime('%m/%d/%Y')

doc = DocxTemplate("Cover Letter - Very General.docx")
context = { 'today_date': today_date, 
           'company_name' : company_name, 
           'position_name' : position_name,
           'address' : address, 
           'employee' : employee,
           'employee_title' : employee_title}

doc.render(context)

os.chdir("C:\\Users\\prest\\OneDrive\\Desktop\\Learning\\Areas of Interest\\Programming, Etc\\Python\\CoverLetters\\CoverLetter\\Completed_word")
doc.save('Cover_letter_'+company_name+'_'+position_name+'.docx')

os.chdir("C:\\Users\\prest\\OneDrive\\Desktop\\Learning\\Areas of Interest\\Programming, Etc\\Python\\CoverLetters\\CoverLetter\\Completed_pdf")
doc.save('Cover_letter_'+company_name+'_'+position_name+'.pdf')
