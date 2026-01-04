from datetime import datetime, timedelta

def get_all_dates(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    days = (end_date - start_date).days + 1
    return [start_date + timedelta(days=i) for i in range(days)]

def is_saturday_off(date_obj, saturday_mode, start_date_obj):
    # Saturday mode: odd_off, even_off, none
    if date_obj.weekday() != 5:
        return False
    week_num = ((date_obj - start_date_obj).days // 7) + 1
    if saturday_mode == "odd_off":
        return week_num % 2 == 1
    elif saturday_mode == "even_off":
        return week_num % 2 == 0
    else:
        return False

def calculate_attendance(
    start_date,
    end_date,
    saturday_mode,
    festive_holidays,
    personal_leaves
):
    all_dates = get_all_dates(start_date, end_date)
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")

    working_days = 0
    leaves = 0

    for d in all_dates:
        # Weekends other than Saturdays are working days (assumed)
        if d.weekday() == 6:
            # Sunday assumed working day
            working_days += 1
            if d.strftime("%Y-%m-%d") in personal_leaves:
                leaves += 1
            elif d.strftime("%Y-%m-%d") in festive_holidays:
                leaves += 1
            continue

        if is_saturday_off(d, saturday_mode, start_date_obj):
            # Saturday off (holiday)
            continue

        if d.strftime("%Y-%m-%d") in festive_holidays:
            # Festival leave
            continue

        working_days += 1
        if d.strftime("%Y-%m-%d") in personal_leaves:
            leaves += 1

    present_days = working_days - leaves
    attendance_percentage = (present_days / working_days) * 100 if working_days > 0 else 0

    return {
        "total_working_days": working_days,
        "leaves_taken": leaves,
        "attendance_percentage": round(attendance_percentage, 2)
    }

def max_leaves_allowed(
    start_date,
    end_date,
    saturday_mode,
    festive_holidays,
    current_leaves,
    threshold=75
):
    # Binary search max leaves before attendance drops below threshold
    low = 0
    high = 365  # max leaves guess

    def attendance_if_leaves(leaves_count):
        all_dates = get_all_dates(start_date, end_date)
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")

        working_days = 0
        leaves = 0

        # Distribute leaves evenly after current leaves
        # For simplicity, add leaves on earliest working days after current leaves
        leaves_to_assign = leaves_count + current_leaves
        leaves_assigned = 0

        for d in all_dates:
            if d.weekday() == 6:
                working_days += 1
                continue
            if is_saturday_off(d, saturday_mode, start_date_obj):
                continue
            if d.strftime("%Y-%m-%d") in festive_holidays:
                continue
            working_days += 1

        if working_days == 0:
            return 0

        present = working_days - leaves_to_assign
        if present < 0:
            present = 0
        return (present / working_days) * 100

    while low < high:
        mid = (low + high) // 2
        att = attendance_if_leaves(mid)
        if att >= threshold:
            low = mid + 1
        else:
            high = mid

    return low - 1
