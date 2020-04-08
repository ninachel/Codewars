def make_readable(seconds):
    HH = seconds // 3600
    MM = (seconds % 3600) // 60
    SS = (seconds % 3600) % 60
    if HH < 9:
        HH = str(HH).zfill(2)
    if MM < 9:
        MM = str(MM).zfill(2)
    if SS < 9:
        SS = str(SS).zfill(2)
    return '{}:{}:{}'.format(HH, MM, SS)
