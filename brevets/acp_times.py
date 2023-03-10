"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#
def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    minutes = 0
    TRIGGERS = [(200,200,34),(400,200,32),(600,200,30),(1000,400,28),(1300,300,26)]
    if brevet_dist_km < control_dist_km:
        control_dist_km = brevet_dist_km
    for trigger in TRIGGERS:
        km, l, max = trigger
        if control_dist_km > km:
            minutes += (l / max) * 60
        else:
            minutes += ((control_dist_km-(km-l))/max) * 60
            break
    rounded = round(minutes)
    return brevet_start_time.shift(minutes=rounded)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    print("Closing read brevet_dist_km as:",brevet_dist_km)
    minutes = 0
    TRIGGERS = [(600,600,15),(1000,400,11.428),(1300,300,13.333)]
    if brevet_dist_km < control_dist_km:
        control_dist_km = brevet_dist_km
    for trigger in TRIGGERS:
        km, l, max = trigger
        if control_dist_km > km:
            minutes += (l / max) * 60
        else:
            if control_dist_km <= 60: #oddity
                minutes += ((control_dist_km/20) + 1) *60
                break
            else:
                minutes += ((control_dist_km-(km-l))/max) * 60
                break
    if brevet_dist_km == 200 and control_dist_km == 200:
        return brevet_start_time.shift(hours=13,minutes=30)
    if brevet_dist_km == 400 and control_dist_km == 400:
        return brevet_start_time.shift(hours=15)
    rounded = round(minutes)
    return brevet_start_time.shift(minutes=rounded)
