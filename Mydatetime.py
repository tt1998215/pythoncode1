from datetime import datetime,timezone,timedelta
# print(datetime.now())
# utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
# bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
# print(bj_dt)
import re
def to_timestmap(dt_str,tz_str):
    input_dt=datetime.strptime(dt_str)
    time_zone_num=re.match(r'UTC([+|-][\d]{1,2}):00',tz_str).group(1)
    time_zone=timezone(timedelta(hours=int(time_zone_num)))
    input_dt_tz=input_dt.replace(tzinfo=time_zone)
    return input_dt_tz.timestamp()