def make_readable(seconds):
    HH = seconds // 3600
    MM = (seconds % 3600) // 60
    SS = seconds % 100
    if HH < 9:
        HH = str(HH).zfill(2)
    if MM < 9:
        MM = str(HH).zfill(2)
    if SS < 9:
        SS = str(HH).zfill(2)
    return '{}:{}:{}'.format(HH, MM, SS)


seconds = 5
print(make_readable(seconds))
