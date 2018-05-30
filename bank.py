from datetime import date
from time import ctime
class Person:
	"""
	Parent class for Employee and Customer class 
	"""
	def __init__(self, name, birthdate):
		"""initializer for Person class"""
		self.__name = name
		self.__birthdate = birthdate
		try:
			month, day, year = self.__birthdate.split('/')
			month, day, year = int(month), int(day), int(year)
			if year < 1000:
				print("Wrong format of year")
				raise Exception('')
			elif year > date.today().year:
				print("Year is in the future.")
				raise Exception('')
		except Exception:
			raise ValueError("Correct format of date: MM/DD/YYYY")
		
	def get_name(self):
		"""Function to return the name of an object"""	
		return self.__name
	
	def is_birthday(self):
		"""Function testing is the birthday input for a specific object match today's date"""

		current_date = date.today()
		month, day, year = self.__birthdate.split('/')
		return (int(month), int(day))==(current_date.month, current_date.day)
		
	def age(self):
		"""Function that calculates the age of an object"""

		current_date = date.today()
		month, day, year = self.__birthdate.split('/')
		month, day, year = int(month), int(day), int(year)
		age = current_date.year - year
		if (month, day) > (current_date.month, current_date.day):
			age-=1
		return age
		

class Employee(Person):
	"""
	Employee class is is a child class of its parent, the Person class. Employee inherits attributes from the Person class
	
	"""
	customers={}
	def __init__(self, name, birthdate):
		"""Initializer for the Employee class"""
		Person.__init__(self, name, birthdate)
		
	def num_of_customers():
		"""Function to add money to one certain customer's bank account"""
		return len(Employee.customers)
		
	def is_customer(name):
		"""function returns a boolean variable is the object a bank customers"""
		return name in Employee.customers
		
	def withdraw(self, name, amount):
		"""
		Function that returns string, "Permission denied" 
		when Employee attempts to withdraw money
		"""
		raise Exception("Permission denied")
		
	def deposit(self, name, amount):
		"""
		Function that returns string, "Permission denied" 
		when Employee attempts to deposit money
		"""
		raise Exception("Permission denied")
		
	def greetings(self):
		"""This function prints the name of the Employee and greets the customer as a string"""
		print("Hello, my name is {}".format(self.get_name()))
	
		
class Customer(Person):
	"""
	The children class of the Person Class, inherit the name and 
	birthday variables from the Person Class
	"""
	
	def __init__(self, name, birthdate, balance):
		"""Initializer for Customer class"""

		Person.__init__(self, name, birthdate)
		self.__account=balance
		self.__loans=0
		self.__account_changes={}
		self.__loan_changes={}

	def __check_bank_status(self):
		"""Private function check the where a customer account is 
		available in the bank or not"""

		inbank = Employee.is_customer(self.get_name())
		if not inbank:
			raise Exception("{} is not in bank".format(self.get_name()))
		
	def bank_statement(self):
		"""Function return a table of bank statement for a certain 
		customer object, including loans payment and account changes"""

		self.__check_bank_status()
		statement_str = "Account Changes\n"
		if len(self.__account_changes)==0:
			statement_str += 'None\n'
		for date in self.__account_changes:
			change = self.__account_changes[date]
			symbol = ''
			if (change >= 0):
				symbol = '+'
			else:
				symbol = '-'
			statement_str += "{}: {}${}\n".format(date, symbol, abs(change))
		statement_str += "Loan Changes\n"
		if len(self.__loan_changes)==0:
			statement_str += 'None\n'
		for date in self.__loan_changes:
			change = self.__loan_changes[date]
			symbol = ''
			if (change >= 0):
				symbol = '+'
			else:
				symbol = '-'
			statement_str += "{}: {}${}\n".format(date, symbol, abs(change))
		return statement_str

	def print_statement(self):
		"""
		Prints the bank statement onto the console
		"""
		print(self.bank_statement())
		
	def make_payment(self, payment):
		"""Function transfer money from one specific customer's bank 
		account to his/her loan payment"""

		self.__check_bank_status()
		if payment > self.__loans:
			print("Payment is greater than loan.  Readjusting payment.")
			payment = self.__loans
		amount = self.withdraw(payment)
		if amount <= 0:
			print("Unable to make loan payment")
			return
		self.__loans = round(self.__loans - amount, 2)
		date = ctime()
		self.__loan_changes[date]=amount*-1
		return self.__loans

	def borrow_loans(self, amount):
		"""Function to let the customer borrow a loan and keep track 
		of the loan amount"""
		rounded_amount = round(amount, 2)
		if rounded_amount <= 0:
			print("Invalid loan amount. Borrowing halted.")
			return self.__loans
		self.__check_bank_status()
		self.__loans = round(self.__loans + rounded_amount, 2)
		current_date = ctime()
		self.__loan_changes[current_date]= rounded_amount
		self.deposit(rounded_amount)
		return self.__loans
	
	def withdraw(self, amount):
		"""Function to subtract money from one certain customer's bank account"""
		self.__check_bank_status()
		rounded_amount = round(amount, 2)
		if (rounded_amount <= 0.00):
			print("Invalid withdrawal amount. Withdrawal halted.")
			return 0
		elif (rounded_amount <= self.__account):
			self.__account = round(self.__account - rounded_amount, 2)
			self.__account_changes[ctime()] = rounded_amount * -1
			return rounded_amount
		else:
			print("Withdrawal denied.  There is not enough money in the account")
			return 0
		
	def deposit(self, amount):
		"""Function to add money to one certain customer's bank account"""
		self.__check_bank_status()
		rounded_amount = round(amount, 2)
		if rounded_amount <= 0.00:
			print("Invalid deposit amount. Deposit halted.")
			return self.__account
		self.__account = round(self.__account + rounded_amount, 2)
		self.__account_changes[ctime()] = rounded_amount
		return self.__account
	
	def get_balance(self):
		"""Function to get total amount of one certain customer's bank balance 
		(This function first check the bank status of the customer using __check_bank_status,
		it will only execute if the __check_bank_status returns True)"""

		self.__check_bank_status()
		return self.__account
		
	def get_loans(self):
		"""Function to get total amount of one certain customer's loan balance 
		(This function first check the bank status of the customer using __check_bank_status, 
		it will only execute if the __check_bank_status returns True)"""

		self.__check_bank_status()
		return self.__loans
		
class Teller(Employee):
	"""
	Class that handles the operations of a regular bank teller
	"""
	def __init__(self, name, birthdate):
		Employee.__init__(self, name, birthdate)
	
	def withdraw(self, name, amount):
		"""Withdraws a given amount of money to a 
		visiting customer from the customer’s account"""
		if not Employee.is_customer(name):
			print("{} is not enrolled in the bank.".format(name))
			return 0.0
		return Employee.customers[name].withdraw(amount)
		
	def deposit(self, name, amount):
		"""Inserts a given money into a visiting customer's account"""
		if not Employee.is_customer(name):
			print("{} is not enrolled in the bank.".format(name))
			return 0.0
		customer_obj = Employee.customers[name]
		return customer_obj.deposit(amount)
		
	def greetings(self):
		"""Greets and lets customer know he/she is the teller."""
		print("Hi, I'm {}. I will be your teller today".format(self.get_name()))
	
class Assistant(Employee):
	"""
	Assistant is a child class of its parent, the Employee. Assistant inherits attributes from the Employee and Person class
	"""

	def __init__(self, name, birthdate, interest_rate=0.02):
		"""Function to add money to one certain customer's bank account
		"""
		Employee.__init__(self, name, birthdate)
		self.__interest_rate = interest_rate
	
	
	def remind_birthday(self, customer):
		"""
		Returns the string if the day the customer deposited/withdraw the money on 
		his/her birthday 
		"""
		if (customer.is_birthday()):
			print("Oh, by the way, it's your birthday")
		
	def withdraw(self, name, amount):
		"""Function to withdraw money to one certain customer's bank 
		account with charging certain fee"""

		if not Employee.is_customer(name):
			print("{} is not in the bank system.".format(name))
			return 0.0
		customer=Employee.customers[name]
		percent_interest = int(self.__interest_rate * 100)
		print("Assistant fee: {}%".format(percent_interest))
		self.remind_birthday(customer)
		interest = amount * self.__interest_rate
		net_withdrawal = customer.withdraw(amount*(1+self.__interest_rate)) - interest
		if net_withdrawal <= 0.00:
			return 0
		return round(net_withdrawal, 2)
		
	def deposit(self, name, amount):
		"""This function will add money to his/her bank account. """
		if not Employee.is_customer(name):
			print("{} is not in the bank system.".format(name))
			return 0.0
		customer_obj = Employee.customers[name]
		fee = self.__interest_rate * amount
		return customer_obj.deposit(amount - fee)
		
	def greetings(self):
		"""Function that returns the name of the Assistant and asks if the customer needs assistance
		"""
		print("Hi, I'm {}. How may I assist you?".format(self.get_name()))
		
class Manager(Teller):
	"""
	Class that handles operations of the bank manager,
	which is the same as a teller plus adding and deleting accounts.
	"""
	def __init__(self, name, birthdate):
		"""Initializer for the Manager class"""
		Teller.__init__(self, name, birthdate)
		
	def delete_account(self, name):
		"""Deletes an existing bank account under a certain name"""
		if not Employee.is_customer(name):
			print("{} is not in the bank system.".format(name))
		else:
			del Employee.customers[name]
	
	def add_account(self, name, birthdate, balance=100):
		"""Creates a new bank account for a new customer"""
		customer=Customer(name, birthdate, balance)
		if (customer.age() < 16):
			print("{} is too young to have an account.".format(name))
		elif Employee.is_customer(name):
			print("{} is already in the bank system.  Cannot add account".format(name))
		else:
			Employee.customers[name]=customer
		
	def get_account(self, name):
		"""Obtains the customer account under a given name"""
		if not Employee.is_customer(name):
			print("{} is not a customer of this bank.".format(name))
			return None
		return Employee.customers[name]
		
	def greetings(self):
		"""Greets the customer and informs them that he/she is a manager."""
		print("Hi, I'm {}, the bank's manager.".format(self.get_name()))