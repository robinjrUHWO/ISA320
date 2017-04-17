import sqlite3

print "\n"
border = "-----------------------------------------------------\n"
print border
msg = "Welcome to Bank of West Oahu!\n\nPlease login to your account to start...\n"
print msg
print border + "\n"
name = raw_input("User Name:")
acct = raw_input("Account Number:")

conn = sqlite3.connect('accounts.database')
c = conn.cursor()
sql = "SELECT count(*) FROM users WHERE name = '" + name + "' AND acct = '" + acct + "'"
acct_count = c.execute(sql).fetchone()[0]
if acct_count == 0:
	print "Account does not exist.  Exiting."
	exit()

tran = "Select what you would like to do:\n\n1. Deposit Funds\n2. Withdraw Funds\n3. Print Report\n4. Quit\n5. Enter Management Mode\n\n"
print tran

sel = raw_input("\nSelect 1, 2, 3, 4 or 5: ")

if sel == "1":
	amount = raw_input("How much would you like to DEPOSIT? $")
	sql = "INSERT INTO accounts (acct, name, transaction_type, transaction_amount, transaction_date) VALUES ('" + acct + "', '" + name + "', 'deposit', " + amount + ", datetime('now'))"
	conn = sqlite3.connect('accounts.database')
	c = conn.cursor()
	c.execute(sql)
	conn.commit()
	conn.close()

elif sel == "2":
	amount = raw_input("How much would you like to WITHDRAW? $")
	sql = "INSERT INTO accounts (acct, name, transaction_type, transaction_amount, transaction_date) VALUES ('" + acct + "', '" + name + "', 'deposit', -" + amount + ", datetime('now'))"
	conn = sqlite3.connect('accounts.database')
	c = conn.cursor()
	c.execute(sql)
	conn.commit()
	conn.close()
elif sel == "3": 
	conn = sqlite3.connect('accounts.database')
	c = conn.cursor()
	for row in c.execute("SELECT * FROM accounts WHERE acct = '" + acct + "'"):
		print row
	sql = "SELECT sum(transaction_amount) FROM accounts WHERE name = '" + name + "' AND acct = '" + acct + "'"
	balance = c.execute(sql).fetchone()[0]
	print "---------------------\n"
	print "BALANCE (" + name + ", " + acct + "): $" + str(balance) 
	conn.close()
elif sel == "4":
	print "4 selected\n";
elif sel == "5":
	management_password = "password123"
	mpwd = raw_input("\nProvide the Management Password:")
	if mpwd != management_password:
		print "Incorrect Management Password! Exiting."
		exit();
	conn = sqlite3.connect('accounts.database')
	c = conn.cursor()
	for row in c.execute("SELECT * FROM accounts"):
		print row
	sql = "SELECT sum(transaction_amount) FROM accounts"
	balance = c.execute(sql).fetchone()[0]
	print "---------------------\n"
	print "BALANCE (ALL ACCOUNTS): $" + str(round(balance, 2)) 
	conn.close()
else:
	print "Invalid Selection....Logging Out.\n";

