def clock_angle(time):
    hour, minute = time.split(":")
    hour = int(hour) % 12
    minute = int(minute)
    hour_angle = 30.0 * (hour + minute / 60.0)
    minute_angle = 6.0 * minute
    angle = (minute_angle - hour_angle) % 360
    if angle > 180:
        angle = 360 - angle
    return angle


if __name__ == "__main__":

    assert clock_angle("00:00") == 0
    assert clock_angle("18:00") == 180
    assert clock_angle("01:00") == 30
