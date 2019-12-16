from datetime import date

print("Please input the dates in the following format: yyyy, mm, dd")
date_one = date(*map(int, input("Date one: ").split(", ")))
date_two = date(*map(int, input("Date two: ").split(", ")))

print("""Days between %s and %s are = %i""" % (date_one, date_two, (date_one - date_two).days))