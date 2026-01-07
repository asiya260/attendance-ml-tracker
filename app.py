import streamlit as st
from datetime import datetime, timedelta
import calendar

GLOBAL_CSS = """
<style>
/* Whole page pink background */
[data-testid="stAppViewContainer"], 
[data-testid="stSidebar"], 
[data-testid="stHeader"], 
[data-testid="stToolbar"] {
    background-color: #ffe4f0 !important;  /* soft pink */
}

/* Main content area transparent to show pink */
.css-18e3th9 {
    background-color: transparent !important;
    color: #d81b60 !important;
    font-family: 'Poppins', sans-serif !important;
}

/* Sidebar background pink */
[data-testid="stSidebar"] > div:first-child {
    background-color: #ffe4f0 !important;
    color: #d81b60 !important;
    font-family: 'Poppins', sans-serif !important;
}

/* Titles centered, pink, with subtle shadow */
h1, h2, h3 {
    color: #d81b60 !important;
    font-weight: 700 !important;
    text-shadow: 1px 1px 2px rgba(216,27,96,0.6);
    text-align: center;
    font-family: 'Poppins', sans-serif !important;
}

/* Inputs label texts */
.css-1vtxz9g,       
[data-testid="stDateInput"] label,  
[data-testid="stMultiSelect"] label, 
[data-testid="stSelectbox"] label {
    color: #880e4f !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    font-family: 'Poppins', sans-serif !important;
}

/* Input boxes (date inputs) */
input[type="text"], input[type="date"] {
    background-color: #ffffff !important;
    color: #000000 !important;
    border: 2px solid #f48fb1 !important;
    border-radius: 10px !important;
    padding: 8px !important;
    font-family: 'Poppins', sans-serif !important;
}

/* Fix selectbox dropdown background & text */
div[role="combobox"] > div {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 10px !important;
    border: 2px solid #f48fb1 !important;
    padding: 6px 12px !important;
    font-family: 'Poppins', sans-serif !important;
}

/* Fix dropdown list background & text */
div[role="listbox"] {
    background-color: #ffffff !important;
    color: #000000 !important;
    font-family: 'Poppins', sans-serif !important;
}

/* Fix dropdown options background & text */
div[role="listbox"] div[role="option"] {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* Hover and selected option styles */
div[role="listbox"] div[role="option"]:hover,
div[role="listbox"] div[aria-selected="true"] {
    background-color: #f48fb1 !important; /* pink highlight */
    color: white !important;
}

/* Fix multiselect tags text */
.css-1n76uvr {
    color: #000000 !important;
    background-color: #ffffff !important;
    border-radius: 8px !important;
    padding: 2px 6px !important;
}

/* Fix multiselect placeholder text */
.css-1gkfj9j, .css-1gkfj9, .css-1vtxz9g::placeholder {
    color: #888 !important;  /* lighter grey */
    opacity: 1 !important;
}

/* Placeholder text inside combobox (for selectbox and multiselect) */
div[role="combobox"] > div > span[aria-disabled="true"] {
    color: #888 !important;
}

/* Buttons */
.stButton>button {
    background-color: #e91e63 !important;
    color: white !important;
    font-weight: 700 !important;
    border-radius: 20px !important;
    padding: 8px 20px !important;
    border: none !important;
    transition: background-color 0.3s ease !important;
}
.stButton>button:hover {
    background-color: #c2185b !important;
    cursor: pointer;
}

/* Calendar container: white box with rounded corners and padding */
.calendar-container {
    background-color: white;
    border-radius: 20px;
    padding: 20px;
    color: #d81b60;
    max-width: 900px;
    margin: 0 auto 30px auto;
    box-shadow: 0 4px 10px rgba(216,27,96,0.2);
}

/* Calendar table */
table.calendar {
    width: 100%;
    border-collapse: collapse;
    font-family: 'Poppins', sans-serif !important;
}

/* Table header */
table.calendar th {
    background-color: #f8bbd0;
    color: #880e4f;
    padding: 10px;
    border: 1px solid #f48fb1;
}

/* Table cells */
table.calendar td {
    border: 1px solid #f48fb1;
    vertical-align: top;
    height: 90px;
    padding: 6px 8px;
    font-size: 14px;
    position: relative;
    color: #880e4f;
}

/* Date number in top left */
.date-num {
    font-weight: 700;
    margin-bottom: 6px;
    display: block;
}

/* Badge styles */
.badge {
    display: inline-block;
    padding: 4px 8px;
    margin: 2px 0;
    border-radius: 10px;
    font-size: 0.75rem;
    color: white;
    max-width: 100%;
    line-height: 1.2;
    white-space: normal;
    text-align: center;
}

.leave {
    background-color: #d9534f;  /* red */
}

.festive {
    background-color: #5cb85c;  /* green */
}

.sat-off {
    background-color: #999999;  /* grey */
}

/* Output text (st.write / st.markdown results) */
.stMarkdown > div > p, 
.stWrite > div > p,
.css-1v5f0fr p {
    color: #880e4f !important;
    font-weight: 700 !important;
    font-size: 18px !important;
    font-family: 'Poppins', sans-serif !important;
    text-align: center;
    margin: 10px 0;
}

/* Force dark pink on all output text */
.css-1v5f0fr,
.stMarkdown > div > p,
.stWrite > div > p,
[data-testid="stMarkdownContainer"] p,
div.stMarkdown,
div.css-1v5f0fr p,
div.css-1v5f0fr {
    color: #880e4f !important;
    font-weight: 700 !important;
    font-size: 18px !important;
    font-family: 'Poppins', sans-serif !important;
    margin: 5px 0;
}

/* Selectbox and Multiselect container */
div[role="combobox"] > div {
    background-color: white !important;  /* white background */
    color: black !important;              /* black text */
    border-radius: 10px !important;
    border: 2px solid #f48fb1 !important; /* pink border */
    padding: 6px 12px !important;
    font-family: 'Poppins', sans-serif !important;
}

/* Dropdown options container */
div[role="listbox"] {
    background-color: white !important;  /* white dropdown */
    color: black !important;              /* black option text */
    font-family: 'Poppins', sans-serif !important;
}

/* Placeholder text color */
.css-1gkfj9 {
    color: #555 !important;  /* dark grey placeholder */
}

/* Selected tags in multiselect */
.css-1n76uvr {
    background-color: #fce4ec !important;  /* very light pink */
    color: #880e4f !important;              /* dark pink text */
    border-radius: 8px !important;
    padding: 2px 6px !important;
}


/* Target the top-right deploy button and menu */
[data-testid="stToolbar"] button,
[data-testid="stToolbar"] div[role="button"] {
    background-color: #000000 !important;  /* black background */
    color: #ffffff !important;             /* white text */
}

/* For the three-dot menu icon */
[data-testid="stToolbar"] svg {
    fill: #ffffff !important;              /* white icon */
}

/* Optional: hover effects */
[data-testid="stToolbar"] button:hover,
[data-testid="stToolbar"] div[role="button"]:hover {
    background-color: #333333 !important;
    color: #ffffff !important;
}
</style>


"""

# Calendar HTML builder function
def build_calendar_html(year, month, leave_dates, festive_dates, saturday_off_dates):
    cal = calendar.Calendar(firstweekday=0)  # Monday=0

    html = GLOBAL_CSS  # Inject CSS once per render

    html += "<div class='calendar-container'>"
    html += "<table class='calendar'>"
    # Weekday headers
    html += "<tr>"
    for day_name in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
        html += f"<th>{day_name}</th>"
    html += "</tr>"

    month_days = cal.monthdayscalendar(year, month)
    for week in month_days:
        html += "<tr>"
        for day in week:
            if day == 0:
                html += "<td></td>"  # empty cell
            else:
                date_str = f"{year}-{month:02d}-{day:02d}"
                badges_html = ""
                if date_str in leave_dates:
                    badges_html += "<div class='badge leave'>Took leave ❌</div>"
                if date_str in festive_dates:
                    badges_html += "<div class='badge festive'>Festive 🎉</div>"
                if date_str in saturday_off_dates:
                    badges_html += "<div class='badge sat-off'>Sat off</div>"

                html += f"<td><span class='date-num'>{day}</span>{badges_html}</td>"
        html += "</tr>"
    html += "</table></div>"

    return html

# -- Streamlit app starts here --

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

st.title("College Attendance Tracker with Calendar View")

# Semester inputs
start_date = st.date_input("Semester Start Date", datetime.today())
end_date = st.date_input("Semester End Date", datetime.today() + timedelta(days=100))
if end_date < start_date:
    st.error("End date must be after start date.")
    st.stop()

# Leave dates input
leave_dates = st.multiselect(
    "Select Leave Dates",
    options=[start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)],
    format_func=lambda d: d.strftime("%Y-%m-%d")
)
leave_dates_str = [d.strftime("%Y-%m-%d") for d in leave_dates]

# Festive holidays input
festive_dates = st.multiselect(
    "Select Festive Holidays",
    options=[start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)],
    format_func=lambda d: d.strftime("%Y-%m-%d")
)
festive_dates_str = [d.strftime("%Y-%m-%d") for d in festive_dates]

# Saturday off mode input
saturday_off_mode = st.selectbox("Select Saturdays Off Mode", ["None", "Odd Saturdays Off", "Even Saturdays Off"])

def get_saturdays_off(start_date, end_date, mode):
    saturdays = []
    date = start_date
    while date <= end_date:
        if date.weekday() == 5:  # Saturday
            week_num = ((date - start_date).days // 7) + 1
            if mode == "Odd Saturdays Off" and week_num % 2 == 1:
                saturdays.append(date.strftime("%Y-%m-%d"))
            elif mode == "Even Saturdays Off" and week_num % 2 == 0:
                saturdays.append(date.strftime("%Y-%m-%d"))
        date += timedelta(days=1)
    return saturdays

saturday_off_dates = get_saturdays_off(start_date, end_date, saturday_off_mode)

# New function to count Sundays in the range
def count_sundays(start_date, end_date):
    count = 0
    date = start_date
    while date <= end_date:
        if date.weekday() == 6:  # Sunday
            count += 1
        date += timedelta(days=1)
    return count

total_days = (end_date - start_date).days + 1
total_saturdays_off = len(saturday_off_dates)
total_festive = len(festive_dates_str)
total_sundays = count_sundays(start_date, end_date)

working_days = total_days - total_saturdays_off - total_festive - total_sundays

# Leaves taken only on working days (exclude saturdays off, festive days, and Sundays)
leaves_taken = sum(
    1 for d in leave_dates_str 
    if d not in saturday_off_dates 
    and d not in festive_dates_str
    and datetime.strptime(d, "%Y-%m-%d").weekday() != 6
)

attendance_percentage = ((working_days - leaves_taken) / working_days) * 100 if working_days > 0 else 0

max_additional_leaves = int((working_days * 0.25) - leaves_taken)
max_additional_leaves = max(0, max_additional_leaves)

# Display stats
st.write(f"Total Working Days: {working_days}")
st.write(f"Leaves Taken (working days only): {leaves_taken}")
st.write(f"Attendance Percentage: {attendance_percentage:.2f}%")
st.write(f"Maximum additional leaves to stay above 75%: {max_additional_leaves}")

# Helper to get all months in range
def months_in_range(start_date, end_date):
    months = []
    current = start_date.replace(day=1)
    while current <= end_date:
        months.append((current.year, current.month))
        if current.month == 12:
            current = current.replace(year=current.year + 1, month=1)
        else:
            current = current.replace(month=current.month + 1)
    return months

# Render calendar for each month in range
for year, month in months_in_range(start_date, end_date):
    st.markdown(f"### {datetime(year, month, 1).strftime('%B %Y')}")
    calendar_html = build_calendar_html(year, month, leave_dates_str, festive_dates_str, saturday_off_dates)
    st.markdown(calendar_html, unsafe_allow_html=True)
