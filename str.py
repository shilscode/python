name  = '''Mr/Ms. <name>                                                                Date :<date>
<adress>

Dear <name>:

Last week, we evaluated all the applications we received for the position of Assistant Manager at Make Your Business Better.

It was tough to decide on the select group chosen for an interview, because we received so many good resumes.

You were one of those selected for an interview. We’d like to find out more about the skills you would bring to the job. Ideally, we’d like to meet with you April 10 or 11 at a time that works for you. Give us a call at (714) 555-1212 to work out a time and get directions.

I’ll look forward to meeting you. You can expect to be here about 90 minutes total, with a short assessment of your work preferences followed by the interview.

Sincerely,

 

Jane Doe
Recitation of Tabla'''
n=input("enter your name:\n ")
ad=input("enter your adress:\n ")
dt=input("enter date:\n ")
Let= name.replace("<name>",n)
Let=name.replace("<adress>",ad)
Let=name.replace("<date>",dt)
print(Let)