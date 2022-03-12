from yt_stats import YTstats
import pandas as pd

# python_engineer_id = 'UCbXgNpp0jedKWcQiULLbDTA'
# channel_id = python_engineer_id

API_KEY='AIzaSyB0xtryRhKPRgzw2msX5ccAAW02MFNJo4I'
channel_id='UC_qFl5IF_t1yFk68XP34UYQ'

yt = YTstats(API_KEY, channel_id)
data = yt.get_channel_statistics()
print(data)

d = yt.get_channel_video_data()
# print(d)

yt1 = pd.DataFrame.from_dict([data])
yt2 = pd.DataFrame.from_dict([d])

yt1.to_csv('yt_channel_stat.csv')
yt2.to_csv('yt_vid_data.csv')


yt.extract_all()
yt.dump() 