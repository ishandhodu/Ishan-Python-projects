import datetime

def get_free_times():
    free_times = []
    for i in range(4):
        name = input(f"Enter the name of person {i+1}: ")
        date_str = input(f"Enter the date of availability for {name} (YYYY-MM-DD): ")
        start_time_str = input(f"Enter the start time for {name} (HH:MM): ")
        end_time_str = input(f"Enter the end time for {name} (HH:MM): ")
        
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        start_time = datetime.datetime.strptime(start_time_str, "%I:%M %p")
        end_time = datetime.datetime.strptime(end_time_str, "%I:%M %p")
        
        start_time = datetime.datetime.combine(date.date(), start_time.time())
        end_time = datetime.datetime.combine(date.date(), end_time.time())
        
        free_times.append((name, start_time, end_time))
    return free_times

def suggest_meeting_times(free_times):
    # Find the intersection of all available time slots
    common_start = max(time[1] for time in free_times)
    common_end = min(time[2] for time in free_times)
    if common_start >= common_end:
        return None
    
    # Generate a list of suggested meeting times
    suggested_times = []
    current_time = common_start
    while current_time <= common_end:
        available = all(time[1] <= current_time < time[2] for time in free_times)
        if available:
            suggested_times.append(current_time)
        current_time += datetime.timedelta(minutes=30)  # Assuming 30-minute slots
    
    return suggested_times

def recommend_time(suggested_times):
    if suggested_times:
        earliest_time = min(suggested_times)
        return earliest_time.strftime("%Y-%m-%d %I:%M %p")
    else:
        return None

# Example usage
free_times = get_free_times()
suggested_times = suggest_meeting_times(free_times)

if suggested_times:
    print("Suggested meeting times:")
    for time in suggested_times:
        print(time.strftime("%Y-%m-%d %I:%M %p"))
    
    recommended_time = recommend_time(suggested_times)
    if recommended_time:
        print(f"\nRecommended meeting time: {recommended_time}")
    else:
        print("No recommended meeting time found.")
else:
    print("No common free time found.")
