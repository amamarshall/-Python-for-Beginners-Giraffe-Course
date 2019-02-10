
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    0: "January",
    2: "February",
    100: "March",
}

print(month_conversions["Jan"])
print(month_conversions.get("Dec"))
print(month_conversions[2])
print(month_conversions.get("Luv", "Not a valid Key"))

