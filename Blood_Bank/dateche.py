last_db = str(raw_input("Enter Last Donate Date(Formatt:yyyy-mm-dd):"))
today = datetime.date.today()
check = today - last_db

print check
