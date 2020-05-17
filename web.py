from flask import Flask,render_template,request,redirect
import csv
web = Flask(__name__)


@web.route('/')
def my_home():
    return render_template('index.html') 

@web.route('/<string:page_name>')
def page_html(page_name):
    return render_template(page_name) 

def write_data(data):
    email=data['email']
    subject=data['subject']
    message=data['message']
    with open('database.txt', mode='a') as database: 
        file=database.write(f'\n*   {email} , \t{subject} , \t{message}')

def write_datacsv(data):
    Name=data['Name']
    subject=data['subject']
    message=data['message']
    with open('database2.csv', mode='a') as database21: 
        csv_writer=csv.writer(database21,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([Name,subject,message])

@web.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            write_datacsv(data)
            return redirect('/thankyou.html')
        except:
            return 'data did not saved to database'
    else:
        return "form not submitted!"