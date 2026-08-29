import calendar

months = [
    (8, 31, [31]),
    (9, 30, [14, 21, 28]),
    (10, 31, [5, 12, 19, 26]),
    (11, 30, [2, 9, 16, 23, 30]),
    (12, 31, [7, 14, 21, 28])
]

names = {8: "Augustus", 9: "September", 10: "Oktober", 11: "November", 12: "December"}

html = '<div class="calendar-container">\n'

for m, days_in_month, play_dates in months:
    # 2026 calendar
    first_weekday, _ = calendar.monthrange(2026, m) # 0 = Mon, 6 = Sun
    
    html += f'  <div class="month">\n'
    html += f'    <div class="month-title">{names[m]}</div>\n'
    html += f'    <div class="days-grid">\n'
    for day in ['Ma', 'Di', 'Wo', 'Do', 'Vr', 'Za', 'Zo']:
        html += f'      <div class="day-header">{day}</div>\n'
    
    # Empty days
    for _ in range(first_weekday):
        html += '      <div class="day empty-day"></div>\n'
        
    for day in range(1, days_in_month + 1):
        if day in play_dates:
            html += f'      <div class="day play-date">{day}</div>\n'
        else:
            html += f'      <div class="day">{day}</div>\n'
            
    html += f'    </div>\n'
    html += f'  </div>\n'

html += '</div>'

print(html)
