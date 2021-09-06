
import os
import calendar
from datetime import datetime

calendar.setfirstweekday(calendar.SUNDAY)

time_now = datetime.now()
days = calendar.monthrange(2021, 12)
for i in range(1, days[1]+1):
    os.mkdir('../timeline/2021/12/{}'.format(i))
    with open('../timeline\\\\2021\\\\12\\\\{}\\\\Requirements.json'.format(i), 'w') as Requirementsjs:
        pass
    with open('../timeline\\\\2021\\\\12\\\\{}\\\\Attendees.json'.format(i), 'w') as Attendeesjs:
        pass
    with open('../timeline\\\\2021\\\\12\\\\{}\\\\Report.json'.format(i), 'w') as Reportjs:
        pass
    with open('../timeline\\\\2021\\\\12\\\\{}\\\\Requirements.txt'.format(i), 'w') as Requirements:
        pass
    with open('../timeline\\\\2021\\\\12\\\\{}\\\\Attendees.txt'.format(i), 'w') as Attendees:
        pass
    with open('../timeline\\\\2021\\\\12\\\\{}\\\\Report.txt'.format(i), 'w') as Report:
        pass
"""
url = input('paset your url: ')
with open('timeline\\\\2021\\\\subjects\\\\css.bat', 'w') as test:
    test.write("start {}".format(url))

import subprocess
subprocess.call([r'timeline\\\\2021\\\\subjects\\\\css.bat'])

import os
os.system('timeline\\\\2021\\\\subjects\\\\css.bat')
"""
