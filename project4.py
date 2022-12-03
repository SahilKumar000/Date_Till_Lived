from datetime import datetime, timedelta
# We Are using datetime,timedelta module
a,b,c=map(int,input('Enter your date of birth seperated by space: ').split())
# taking input in format of year/month/date
given_DOB=datetime(a,b,c)
current_date=datetime.today()
# Now this will count days till the given date
age_in_days=current_date -given_DOB
print('The no. of days user lived is= ',age_in_days.days)
# it print the lived days