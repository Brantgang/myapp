import re
from datetime import datetime,timedelta,timezone
def to_timestamp(dt_str,tz_str):
    cday=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    dt_tz = timezone(timedelta(hours=int(int(re.split(r'[UTC\:]', tz_str)[3]))))
    tz_zone_utc=timezone(timedelta(hours=7))
    dt = cday.replace(tzinfo=dt_tz)
    print(dt.timestamp())



t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')


t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')