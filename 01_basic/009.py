from datetime import datetime

exam_st_date = (11, 12, 2014)

examination_date = datetime(exam_st_date[2], exam_st_date[1], exam_st_date[0])

print("The examination will start from : " + examination_date.strftime("%d / %m / %Y"))