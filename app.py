# Now the import commands below are used to access further required data for the code which will allow it to work with the other files and commands properly. 
import csv
import os
from flask import Flask, render_template, request
from datetime import *
import pandas as pd

# Now this code reads the CSVs to get the data ready to move to HTML, however the reason customer log is having its amount of records outputted is for security, this code has been re-entered in other parts of this file to allow for information to be up to date.
Customer_log = pd.read_csv('Customer.csv', usecols=[0,2,3])
Services_log = pd.read_csv('Services.csv')
Bookings_log = pd.read_csv('Booking.csv')

# Now this code turns the data into the HTML files allowing for them to be read moved into templates to update the user, this code has been re-entered in other parts of this file to allow for information to be up to date. 
pd.DataFrame.to_html(Customer_log, 'Customer_log.html', index=False)
pd.DataFrame.to_html(Services_log, 'Services_pricing_log.html', index=False)
pd.DataFrame.to_html(Bookings_log, 'Booking_log.html', table_id='/workspaces/Feedback/static/style.css')

# Now this code takes the files and moves them into the templates folder while deleting the old HTML files so they do not cause a problems in the code, this code has been re-entered in other parts of this file to allow for information to be up to date.
os.replace('/workspaces/Feedback/Customer_log.html', '/workspaces/Feedback/templates/Customer_log.html')
os.replace('/workspaces/Feedback/Services_pricing_log.html', '/workspaces/Feedback/templates/Services_pricing_log.html')
os.replace('/workspaces/Feedback/Booking_log.html', '/workspaces/Feedback/templates/Booking_log.html')

# Now this code allows the values that require it to have the right number when used since some of the carbon footprint is multiplied. 
def multiply(number_1, number_2):
    return number_1 * number_2

# Now this code will be used to add the total of the users carbon footprint so it can be displayed clear to them. 
def addition(number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8):
    return number_1 + number_2 + number_3 + number_4 + number_5 + number_6 + number_7 + number_8

# Now the code below is to check the data from the CSV files to the gathered data from Customer_sign_in and if its found will output the boolean value true, if it doesn't find the data it will output the boolean value false. 
def details_check_for_customers(Email, Password):
    check_list = []
    with open('Customer.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            check_list.append(row)
        row_search = 0
        email_check = check_list[row_search].get('Email', '').strip()
        while email_check != Email and row_search <= len(check_list):
            row_search += 1
            if IndexError:
                return False
            email_check = check_list[row_search].get('Email', '').strip()
        else:
            password_check = check_list[row_search].get('Password', '').strip()
            if password_check == Password and email_check == Email:
                return True
            else:
                return False

# Now the code below deletes a record which matches the users input, at this moment it only removes one record, this works for 
def delete_record(File_requested, Email_of_client):
    checklist = []

    with open(File_requested, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            checklist.append(row)
        row_search = 0
        email_check = checklist[int(row_search)].get('Email', '').rstrip()
        while email_check != Email_of_client and row_search <= len(checklist):
            row_search += 1
            # Now the index error here is to allow for data that dose not exist or miss entered data to not crash the code by exiting the function and bringing up the error page.z
            if IndexError:
                return False
            email_check = checklist[int(row_search)].get('Email').rstrip()
        else:
            if email_check == Email_of_client:
                df = pd.read_csv(File_requested)
                df = df.drop(index=row_search)
                df.to_csv(File_requested, index=False)
                return True
            else:
                return False
            
# Now the code below was is a copy of the delete code, however this has been done to  save time in the re-writing of the code, since they both follow a similar format of function. 
def amend_record(File_requested, Data_column, Old_data, New_data):
    checklist = []
    with open(str(File_requested), 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            checklist.append(row)
        row_search = 0
        old_data_check = checklist[int(row_search)].get(Data_column, '').rstrip()
        while old_data_check != Old_data and row_search <= len(checklist):
            row_search += 1
            # Now the index error here is to allow for data that dose not exist or miss entered data to not crash the code by exiting the function and bringing up the error page. 
            if IndexError:
                 return False
            old_data_check = checklist[int(row_search)].get(Data_column).rstrip()
        else:
            # Now the reason for the mass of code here is to allow all parts of the files to be altered according to the request of the customer. It has been shown to work with no problem since it was updated.
            if old_data_check == Old_data:
                if File_requested == 'Customer.csv':
                    if Data_column == 'Name':
                        df = pd.read_csv(File_requested)
                        df.loc[row_search, 'Name'] = New_data
                        df.to_csv(File_requested, index=False)
                        return True
                    elif Data_column == 'Password':
                        df = pd.read_csv(File_requested)
                        df.loc[row_search, 'Password'] = New_data
                        df.to_csv(File_requested, index=False)
                        return True
                    elif Data_column == 'Email':
                        df = pd.read_csv(File_requested)
                        df.loc[row_search, 'Email'] = New_data
                        df.to_csv(File_requested, index=False)
                        return True
                    elif Data_column == 'Phone Number':
                        df = pd.read_csv(File_requested)
                        df.loc[row_search, 'Phone Number'] = New_data
                        df.to_csv(File_requested, index=False)
                        return True
                    elif Data_column == 'Security Question':
                        df = pd.read_csv(File_requested)
                        df.loc[row_search, 'Security Question'] = New_data
                        df.to_csv(File_requested, index=False)
                        return True
                    elif Data_column == 'Security Answer':
                        df = pd.read_csv(File_requested)
                        df.loc[row_search, 'Security Answer'] = New_data
                        df.to_csv(File_requested, index=False)
                        return True
            elif File_requested == 'Bookings.csv':
                    if Data_column == 'Name':
                        df = pd.read_csv(File_requested)
                        df.loc[row_search, 'Name'] = New_data
                        df.to_csv(File_requested, index=False)
                        return True
                    elif Data_column == 'Phone Number':
                        df = pd.read_csv(File_requested)
                        df.loc[row_search, 'Phone Number'] = New_data
                        df.to_csv(File_requested, index=False)
                        return True
                    elif Data_column == 'Email':
                        df = pd.read_csv(File_requested)
                        df.loc[row_search, 'Email'] = New_data
                        df.to_csv(File_requested, index=False)
                        return True
                    elif Data_column == 'Address':
                        df = pd.read_csv(File_requested)
                        df.loc[row_search, 'Address'] = New_data
                        df.to_csv(File_requested, index=False)
                        return True
                    elif Data_column == 'Post Code':
                        df = pd.read_csv(File_requested)
                        df.loc[row_search, 'Post Code'] = New_data
                        df.to_csv(File_requested, index=False)
                        return True
                    elif Data_column == 'Date of Booking':
                        df = pd.read_csv(File_requested)
                        df.loc[row_search, 'Date of Booking'] = New_data
                        df.to_csv(File_requested, index=False)
                        return True
                    elif Data_column == 'Requested Service':
                        df = pd.read_csv(File_requested)
                        df.loc[row_search, 'Requested Service'] = New_data
                        df.to_csv(File_requested, index=False)
                        return True
            else:
                return False
            
# Now the code below is to check the data from the CSV files to the gathered data from Staff_sign_in and if its found will output the boolean value true, if it doesn't find the data it will output the boolean value false. 
def details_check_for_staff(Email, Password):
    check_list = []
    with open('Staff.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            check_list.append(row)
        row_search = 0
        email_check = check_list[row_search].get('Email', '').strip()
        while email_check != Email and row_search <= len(check_list):
            row_search += 1
            if IndexError:
                return False
            email_check = check_list[row_search].get('Email', '').strip()
        else:
            password_check = check_list[row_search].get('Password', '').strip()
            if password_check == Password and email_check == Email:
                return True
            else:
                return False

            
# Now this code is going to be used to stop a user from booking a date that has passed is the current date, this has been done to limit any problems that could be caused on the system. 
def past_date_stop(Date_of_booking):
    Users_date = datetime.fromisoformat(Date_of_booking)
    Current_date = datetime.now()
    if Current_date <= Users_date:
        return False
    else:  
        return True

# The code below is used to check the password used when the customer first signs up, there is version which works with the sign in for users and staff however the methods used do not apply here.  
def Password_verify(Password, Password_check):
    if Password == Password_check:
        return True
    elif Password != Password_check:
        return False

# Now this check has been made to check the entered data of the user for discrepancies and to make the app route more clear.
def check_for_security_question_amend(Security_answer, Email):
    check_list = []
    with open('Record amend.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            check_list.append(row)
        row_search = 0
        email_check = check_list[int(row_search)].get('Email', '').strip()
        while email_check != Email and row_search <= len(check_list):
            row_search += 1
            email_check = check_list[int(row_search)].get('Email', '').strip()
        else:
            if email_check == Email:
                # Now this segment of code is to verify the answer entered here against the one within the CSV so any discrepancies are found.
                check_list = []
                with open('customer.csv', 'r') as file:
                    csv_reader = csv.DictReader(file)
                    for row in csv_reader:
                        check_list.append(row)
                    row_search = 0
                    email_check = check_list[row_search].get('Email', '').strip()
                    while email_check != Email and row_search <= len(check_list):
                        row_search += 1
                        email_check = check_list[row_search].get('Email', '').strip()
                    else:
                        Customer_security_answer = check_list[row_search].get('Security Answer', '').strip()
                        if Customer_security_answer == Security_answer:
                            return True
                        else:
                            return False
            else:
                return False

# Now this check has been made to check the entered data of the user for discrepancies and to make the app route more clear.
def check_for_security_question_deletion(Security_answer, Email):
    check_list = []
    # Now this segment of code is to verify the answer entered here against the one within the CSV so any discrepancies are found.
    with open('Customer.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            check_list.append(row)
        row_search = 0
        email_check = check_list[int(row_search)].get('Email', '').strip()
        while email_check != Email and row_search <= len(check_list):
            row_search =+1
            email_check = check_list[int(row_search)].get('Email', '').strip()
        else:
            Customer_security_answer = check_list[row_search].get('Security Answer', '').strip()
            if Customer_security_answer == Security_answer:
                return True
            else:
                return False

# Now this line here takes gets the name of this python file and stores it under name which allows it to be used as the back-end of the solution.
app = Flask(__name__)

# The reason the file names are written the way they are is so a third party can easily find the page that they need to maintain, edit or remove with ease, this can be changed later if it is asked for however whoever changes the file names will need to check the rest of the code to make sure no problems have occurred because of this. 
# Now this segment of code calls the first HTML file to appear when the main URL is called, I have set it to the homepage since it allows the user to become informed about this business quickly and limits any confusion they may have. 
@app.route('/')
def Homepage():
    Services_log = pd.read_csv('Services.csv')
    pd.DataFrame.to_html(Services_log, 'Services_pricing_log.html', index=False)
    os.replace('/workspaces/Feedback/Services_pricing_log.html', '/workspaces/Feedback/templates/Services_pricing_log.html')
    return render_template('Homepage.html')

# Now this code takes the data contained within the booking CSV file and makes it accessible on the webpage for users to see. 
@app.route('/Booking_log')
def Booking_table():
    Bookings_log = pd.read_csv('Booking.csv')
    pd.DataFrame.to_html(Bookings_log, 'Booking_log.html', index=False)
    os.replace('/workspaces/Feedback/Booking_log.html', '/workspaces/Feedback/templates/Booking_log.html')
    return render_template('Booking_log.html')

# Now this segment of code gathers all of the needed information from the user then works out the total carbon footprint, then sends the user to the page which will display the total and a sales pitch to increase the chances of them using the service.
# If there is a error the user will be directed to the related error page and informed on what happened and how to fix he problem. 
@app.route('/Carbon_footprint', methods = ['GET', 'POST'])
def Carbon_footprint():
    if request.method == 'POST':
        Electric = request.form.get('electric bill')
        Gas = request.form.get('gas bill')
        Fuel = request.form.get('fuel bill')
        Total_milage = request.form.get('total milage')
        Flights_under_4_hours = request.form.get('flights under 4 hours')
        Flights_over_4_hours = request.form.get('flights over 4 hours')
        Do_not_recycle_newspaper = request.form.get('do not recycle newspaper')
        if Do_not_recycle_newspaper == 'True':
            Recycle_newspaper = 184
        else:
            Recycle_newspaper = 0
        Do_not_recycle_aluminum_and_tin = request.form.get('do not recycle aluminum and tin')
        if Do_not_recycle_aluminum_and_tin== 'True':
            Recycle_aluminum_and_tin = 184
        else:
            Recycle_aluminum_and_tin = 0
        # Now all the code below is used to workout the total footprint and give the right sales pitch to the user.
        Impact_of_electric = multiply(int(Electric),105)
        Impact_of_gas = multiply(int(Gas),105)
        Impact_of_fuel = multiply(int(Fuel),113)
        Impact_of_total_milage = multiply(float(Total_milage), 0.79)
        Impact_of_flights_under_4_hours = multiply(int(Flights_under_4_hours),1100)
        Impact_of_flights_over_4_hours = multiply(int(Flights_over_4_hours),4400)
        Carbon_total = addition(Impact_of_electric, Impact_of_gas, Impact_of_fuel, Impact_of_total_milage, Impact_of_flights_under_4_hours, Impact_of_flights_over_4_hours, Recycle_newspaper, Recycle_aluminum_and_tin)
        if int(Carbon_total) <= 6000:
            Sales_pitch = 'you may not need our services however you would still gain a great benefit from our solar panels since they can help you save money by storing power in batteries which will active and limit the amount of harmful energy providers being used and keeping them away from more of your money.'
            return render_template('Total_of_carbon_footprint.html', Carbon_total = Carbon_total, Sales_pitch = Sales_pitch)
        elif int(Carbon_total) > 6000 and int(Carbon_total) <= 16000:
            Sales_pitch = 'your level puts you on the lesser side of the carbon footprint scale which means it could be better and if you want better control over the heating and power of your home, you could have a smart home system which lets you limit the amount of gas and electric going to certain rooms so you can save money easier, in addition you can do it through your phone so if you wanted to come back to a nice warm home you could with ease by setting it so your heating would be on for a set amount of time.'
            return render_template('Total_of_carbon_footprint.html', Carbon_total = Carbon_total, Sales_pitch = Sales_pitch)
        elif int(Carbon_total) > 16000 and int(Carbon_total) <= 22000:
            Sales_pitch = 'your level puts your footprint the in the average area which means there is room to improve, you could have your life improved with a EV (Electric Vehicle) charger, since the way cards are going to be made the way of petrol and diesel is coming to and end with hybrid of petrol and electric and fully electric cars, you would  be able to have your car topped up and ready to go on the electric motor and saving your fuel for when you need it which saves money on fuel at the same time.'
            return render_template('Total_of_carbon_footprint.html', Carbon_total = Carbon_total, Sales_pitch = Sales_pitch)
        elif int(Carbon_total) > 22000:
            Sales_pitch = 'your level is very high which means you should really invest in our services since we can save you money on power, gas and fuel, while you help limit the carbon footprint being produced.'
            return render_template('Total_of_carbon_footprint.html', Carbon_total = Carbon_total, Sales_pitch = Sales_pitch)
    return render_template('Carbon_footprint.html')

# Now this page informs the customer the booking has been logged and if they need to change or cancel it that they should inform us with the contact information found in the contact information file. 
@app.route('/Conformation_page_for_customer_booking')
def Conformation_page_for_customer_booking():
    return render_template('Conformation_page_for_customer_booking.html')

# Now this page informs the staff member about the deletion of the record and that they should inform the affected person.  
@app.route('/Conformation_page_for_staff_record_deletion')
def Conformation_page_for_staff_record_deletion():
    return render_template('Conformation_page_for_staff_record_deletion.html')

# Now this page informs the staff member about the change being done to record and that they should inform the affected person.  
@app.route('/Conformation_page_for_staff_record_amend')
def Conformation_page_for_staff_record_amend():
    return render_template('Conformation_page_for_staff_record_amend.html')

# Now this segment of code displays contact information to the user so if they needed to contact the business about a query or a problem they have they can do it easily and without hassle. 
@app.route('/Contact_information')
def Contact_information():
    return render_template('Contact_information.html')

# Now this segment of code gathers all of the needed information from the user that they have inputted makes sure that is is valid information and that staff within the business are able to meet the requirements of the user, then stores it into the system.
# But if there is false data or the staff cannot meet the needs at that time they will be taken to a error page that informs the user on what happened and how it can be fixed. 
# The code below has been copied from inside the document and pasted, this is down to writing it into the wrong function, so I have done this to save the time of re-writing the code. 
@app.route('/Customer_booking', methods = ['GET', 'POST'])
def Customer_booking():
    if request.method == 'POST':
        Name = request.form.get('customer name')
        Phone_number = request.form.get('customer phone number')
        Email = request.form.get('customer email')
        Address = request.form.get('customer address')
        Post_code = request.form.get('customer post code')
        Date_of_booking = request.form.get('date of booking')
        date_check = past_date_stop(Date_of_booking)
        Requested_service = request.form.get('requested service')
        if date_check == True:
            return render_template('Error_page_for_customer_booking.html', Name = Name, Date_of_booking = Date_of_booking)
        elif date_check == False:
            # The code below writes all of the inputted data into the bookings CSV.
            price_check_list = []
            with open('Services.csv', 'r') as file:
                csv_reader = csv.DictReader(file)            
                for row in csv_reader:
                    price_check_list.append(row)
                row_search = 0
                Price_locator = price_check_list[row_search].get('Type of service', '').strip()
                while Price_locator != Requested_service and row_search <= len(price_check_list):
                    row_search =+1
                    Price_locator != Requested_service and row_search <= len(price_check_list)
                else:
                    Price_holder = price_check_list[row_search].get('Price', '').strip()
            with open('Booking.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([Name,Phone_number,Email,Address,Post_code,Date_of_booking,Requested_service])
                return render_template('Conformation_page_for_customer_booking.html', Date_of_booking = Date_of_booking, Price_holder = Price_holder)
    return render_template('Customer_booking.html')

# Now this code takes the data contained within the booking CSV file and makes it accessible on the webpage for users to see. 
@app.route('/Customer_log')
def Customer_table():
    Customer_log = pd.read_csv('Customer.csv', usecols=[0,2,3])
    pd.DataFrame.to_html(Customer_log, 'Customer_log.html', index=False)
    os.replace('/workspaces/Feedback/Customer_log.html', '/workspaces/Feedback/templates/Customer_log.html')
    return render_template('Customer_log.html')

# Now this segment of code allows the user to sign up with the webpage, so if they haven't got a account it gets the data seen below checks to make sure no data in the system matches and logs the it into the system for the future. 
# If it encounters a problem with the user data it will take them to the error page and inform them on what has happened and to try again. 
@app.route('/Customer_sign_up', methods = ['GET', 'POST'])
def Customer_sign_up():
    if request.method == 'POST':
        Name = request.form.get('customer_name')
        Password = request.form.get('customer_password')
        Password_check = request.form.get('password_check')
        # Now the line below runs the function which will see if the user has entered the same password twice, this is done so it can be confirmed that they know what password they use for this site.
        password_match = Password_verify(Password, Password_check)
        if password_match == True:
            Email = request.form.get('customer_email')
            Phone_Number = request.form.get('customer_phone_number')
            Security_Question = request.form.get('security_question')
            Security_Answer = request.form.get('security_answer')
            # With the next set of lines, they are wrote to make sure that all of the data is entered in to customer CSV file with no errors and in the right format.
            # This is done through the listing of the variables which follows the same conventions as the file. 
            with open('Customer.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([Name, Password,Email,Phone_Number,Security_Question,Security_Answer])
                return render_template('Customer_booking.html')
        else:
            if password_match == False:
                Reason_for_error = 'The error that has been encountered is because the password you entered did not match in the check, please try again and be careful when entering the password.'
                return render_template('Error_page_for_customer_sign_up.html', Reason_for_error = Reason_for_error)
    return render_template('Customer_sign_up.html')

# Now this code checks if the users data is already on system and matches what is stored, if it does it allows them to go further into the system.
# If it flags any data it shows the error page and explains the fix to them. 
@app.route('/Customer_sign_in', methods = ['GET', 'POST'])
def Customer_sign_in():
    if request.method == 'POST':
        Email = request.form.get('customer_email')
        Password = request.form.get('customer_password')
        check_value = details_check_for_customers(Email, Password)
        if check_value == True:
            return render_template('Customer_booking.html')
        elif check_value == False:
            return render_template('Error_page_for_customer_sign_in.html')
    return render_template('Customer_sign_in.html')

# Now this is the error page for customer making accounts with the system, it flags if the data entered doesn't meet requirements or is already in the system. 
@app.route('/Error_page_for_customer_sign_up')
def Error_page_for_customer_sign_up():
    return render_template('Error_page_for_customer_sign_up.html')

# Now this HTML file informs the customer that their booking didn't go through and they should try again with a different booking date. 
@app.route('/Error_page_for_customer_booking')
def Error_page_for_customer_booking():
    return render_template('Error_page_for_customer_booking.html')

# Now this is the error page for customers who entered their details wrong, which it will explain to them that they may need to re-check the data they entered to make sure its for this system.
@app.route('/Error_page_for_customer_sign_in')
def Error_page_for_customer_sign_in():
    return render_template('Error_page_for_customer_sign_in.html')

# Now this error page will select from some responses whether it needs to ask the staff member to try and enter information or validate that the customer asked for this change.
@app.route('/Error_page_for_staff_record_amend')
def Error_page_for_staff_record_amend():
    return render_template('Error_page_for_staff_record_amend.html')

# Now this error page will select from some responses whether it needs to tell the staff member to trt and enter the information again or validate that the customer is the one who made the deletion request. 
@app.route('/Error_page_for_staff_record_deletion')
def Error_page_for_staff_record_deletion():
    return render_template('Error_page_for_staff_record_deletion.html')

# Now this is the error page for staff who entered their details wrong, which it will explain to them that they need to re-check the data they entered.
@app.route('/Error_page_for_staff_sign_in')
def Error_page_for_staff_sign_in():
    return render_template('Error_page_for_staff_sign_in.html')

# Now this HTML file checks that the requested change can be done, since if it flags as the wrong answer the staff member will need to verify that the customer has asked for this change.
@app.route('/Security_check_for_staff_record_amend', methods = ['GET', 'POST'])
def Security_check_for_staff_record_amend():
    if request.method == 'POST':
        Security_answer = request.form.get('security_answer')
        Email =  request.form.get('email')
        check_list = []
        with open('Record amend.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                check_list.append(row)
            row_search = 0
            email_check = check_list[row_search].get('Email', '').strip()
            while email_check != Email and row_search <= len(check_list):
                row_search =+1
                if IndexError:
                    os.remove('/workspaces/Feedback/Record amend.csv')
                    return render_template('Error_page_for_staff_record_deletion,html')
                email_check = check_list[row_search].get('Email', '').strip()
            else:
                if email_check == Email:
                # Now this segment of code is to verify the answer entered here against the one within the CSV so any discrepancies are found.
                    check_list = []
                    with open('Customer.csv', 'r') as file:
                        csv_reader = csv.DictReader(file)
                        for row in csv_reader:
                            check_list.append(row)
                        row_search = 0
                        email_check = check_list[row_search].get('Email', '').strip()
                        while email_check != Email and row_search <= len(check_list):
                            row_search =+1
                            if IndexError:
                                os.remove('/workspaces/Feedback/Record amend.csv')
                                return render_template('Error_page_for_staff_record_deletion,html')
                            email_check = check_list[row_search].get('Email', '').strip()
                        else:
                            Customer_security_answer = check_list[row_search].get('Security Answer', '').strip()
                            if Customer_security_answer == Security_answer:
                                # Now the code below amends the records from the requested file and deletes Record amend.csv so their are no old  sets of data stored within the file.
                                check_list = []
                                with open('Record amend.csv', 'r') as file:
                                    csv_reader = csv.DictReader(file)
                                    for row in csv_reader:
                                        check_list.append(row)
                                    row_search = 0
                                    File_requested = check_list[int(row_search)].get('File requested')
                                    Data_column  = check_list[int(row_search)].get('Data column')
                                    Old_data = check_list[int(row_search)].get('Old data')
                                    New_data = check_list[int(row_search)].get('New data')
                                    amend_check = amend_record(File_requested, Data_column, Old_data, New_data)
                                    if amend_check == True:
                                        os.remove('/workspaces/Feedback/Record amend.csv')
                                        return render_template('Conformation_page_for_staff_record_amend.html')
                                    else:
                                        return render_template('Error_page_for_staff_record_amend.html')
                            else:
                                return render_template('Error_page_for_staff_record_amend.html')
                else:
                    return render_template('Error_page_for_staff_record_amend.html')
    return render_template('Security_check_for_staff_record_amend.html')

# Now this HTML file checks that the requested change can be done, since itf it flags the as the wrong answer the staff member will need to verify that the customer has asked for the deletion of records related to them. 
@app.route('/Security_check_for_staff_record_deletion', methods = ['GET', 'POST'])
def Security_check_for_staff_record_deletion():
    if request.method == 'POST':
        Security_answer = request.form.get('security_answer')
        Email =  request.form.get('email')
        security_check = check_for_security_question_deletion(Security_answer, Email)
        if security_check == True:
            check_list = []
            with open('Record deletion.csv', 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    check_list.append(row)
                # Now the code below deletes the record from the requested file and deletes Record deletion.csv so their are no old sets of data stored within the file.
                row_search = 0
                File_requested = check_list[int(row_search)].get('File', '').strip()
                deletion_check = delete_record(File_requested, Email)
                if deletion_check == True:
                    os.remove('/workspaces/Feedback/Record deletion.csv')
                    return render_template('Conformation_page_for_staff_record_deletion.html')
                else:
                    return render_template('Error_page_for_staff_record_deletion.html')
        else:
            return render_template('Error_page_for_staff_record_deletion.h')

    return render_template('Security_check_for_staff_record_deletion.html')

# Now this HTML file will display information about the services offered within the business so the user is able acknowledge the information better. 
@app.route('/Services_pricing_log')
def Services_pricing_log():
    Services_log = pd.read_csv('Services.csv')
    pd.DataFrame.to_html(Services_log, 'Services_pricing_log.html')
    os.replace('/workspaces/Feedback/Services_pricing_log.html', '/workspaces/Feedback/templates/Services_pricing_log.html')
    return render_template('Services_pricing_log.html')

# Now this HTML file informs the user on the wide range of services this business offers alongside the cost and benefits of using their services. 
@app.route('/Services')
def Services():
    return render_template('Services.html')

# Now this HTML file gives the staff member access to the record editing and viewing links, so if a customer requests information be deleted or amended the staff member can assist them to do that. 
# The code within the homepage below is to keep resources that the user can view up to date. 
@app.route('/Staff_homepage')
def Staff_homepage():
    Customer_log = pd.read_csv('Customer.csv', usecols=[0,2,3])
    Services_log = pd.read_csv('Services.csv')
    Bookings_log = pd.read_csv('Booking.csv')
    pd.DataFrame.to_html(Customer_log, 'Customer_log.html')
    pd.DataFrame.to_html(Services_log, 'Services_pricing_log.html')
    pd.DataFrame.to_html(Bookings_log, 'Booking_log.html')
    os.replace('/workspaces/Feedback/Customer_log.html', '/workspaces/Feedback/templates/Customer_log.html')
    os.replace('/workspaces/Feedback/Services_pricing_log.html', '/workspaces/Feedback/templates/Services_pricing_log.html')
    os.replace('/workspaces/Feedback/Booking_log.html', '/workspaces/Feedback/templates/Booking_log.html')
    return render_template('Staff_homepage.html')

# Now this HTML file allows the staff member to input the required data to alter a record stored within the system. 
@app.route('/Staff_record_amend', methods = ['GET', 'POST'])
def Staff_record_amend():
    if request.method == 'POST':
        File_requested = request.form.get('file requested', type=str)
        Column_altered = request.form.get('column altered', type=str)
        Old_data = request.form.get('old data')
        New_data = request.form.get('new data')
        Email_of_client = request.form.get('email')
        store_user_data = os.path.isfile('Record amend.csv')
        with open('Record amend.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if not store_user_data:
                writer.writerow(['File requested', 'Data column', 'Old data', 'New data', 'Email'])
                writer.writerow([File_requested, Column_altered, Old_data, New_data, Email_of_client])
        # Now the code below is used to get the security question that the user first gave when they signed up for this service.
        check_list = []
        with open('Customer.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                check_list.append(row)
            row_search = 0
            email_check = check_list[row_search].get('Email', '').strip()
            while email_check != Email_of_client and row_search <= len(check_list):
                row_search =+1
                if IndexError:
                    return render_template('Error_page_for_staff_record_amend,html')
                email_check = check_list[row_search].get('Email', '').strip()
            else:
                if email_check == Email_of_client:
                    Customer_security_question = check_list[row_search].get('Security Question', '').strip()
                    return render_template('Security_check_for_staff_record_amend.html', Customer_security_question = Customer_security_question)
    return render_template('Staff_record_amend.html')

# Now this HTML file allows the staff member to input the required data to delete a record stored within the system.  
# The reason email has been used is that they are not going to be found in the system under other users account, so this helps reduce any accidental data deletion. 
@app.route('/Staff_record_deletion', methods = ['GET', 'POST'])
def Staff_record_deletion():
    if request.method == 'POST':
        File_requested = request.form.get('file requested', type=str)
        Email_of_client = request.form.get('email of client')
        store_user_data = os.path.isfile('Record deletion.csv')
        with open('Record deletion.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if not store_user_data:
                writer.writerow(['File', 'Email'])
                writer.writerow([File_requested, Email_of_client])
        # Now the code below is used to get the security question that the user first gave when they signed up for this service.
        check_list = []
        with open('Customer.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                check_list.append(row)
            row_search = 0
            email_check = check_list[row_search].get('Email', '').strip()
            while email_check != Email_of_client and row_search <= len(check_list):
                row_search =+1
                if IndexError:
                    return render_template('Error_page_for_staff_record_deletion,html')
                email_check = check_list[row_search].get('Email', '').strip()
            else:
                if email_check == Email_of_client:
                    Customer_security_question = check_list[row_search].get('Security Question', '').strip()
                    return render_template('Security_check_for_staff_record_deletion.html', Customer_security_question = Customer_security_question)
    return render_template('Staff_record_deletion.html')

# Now this HTML file allows the staff member to log in into the staff section of the webpage if their credentials are correct.
# If they are not the error page will explain what they need to do to fix the problem. 
@app.route('/Staff_sign_in', methods=['GET', 'POST'])
def Staff_sign_in():
    if request.method == 'POST':
        Email = request.form.get('staff email')
        Password = request.form.get('staff password')
        check_value = details_check_for_staff(Email, Password)
        if check_value == True:
            return render_template('Staff_homepage.html')
        elif check_value == False:
            return render_template('Error_page_for_staff_sign_in.html')
    return render_template('Staff_sign_in.html')

@app.route('/Total_of_carbon_footprint')
def Total_of_carbon_footprint():
    return render_template('Total_of_carbon_footprint.html')

if __name__ == '__main__':
    app.run(debug=True)