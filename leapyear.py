def is_leap(year):
    leap = False
    # If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
    # If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
    # If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
    # The year is a leap year (it has 366 days).
    # The year is not a leap year (it has 365 days).
    # Write your logic here
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            lead = True
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leadp = False
    else:
        leap = False       
     
    return leap
