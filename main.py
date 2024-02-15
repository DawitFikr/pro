import kivy
from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.image import Image 
import shutil 
import geocoder
import requests 

import datetime 



class WindowManager (ScreenManager):
	pass
	
class LoginWindow(Screen):
	def worksheet(self):
		with open("Time_sheets.txt", "r") as time_sheet:
			calendar = str(datetime.datetime.now())
			today = str(calendar[0:10])
			time = str(calendar [0:17])
			check_date = time_sheet.read()
			if not today in check_date.split():
							
				with open ("Time_sheets.txt", "w") as time_sheet:
					time_sheet.write ("●00 DULICOM Digital Solutions")
					time_sheet.write ("\n" + "●01 DATE: " + today + "   " + "agent_1" + " " + ": " + "time_1" + " " + "finish_1" + "   " + "agent_2" + " " + ": " + "time_2" + " " + "finish_2")
					time_sheet.write ("\n" + "●02 ------------------------- Logged in as: " + "agent_1" + "     " + "Location: " + "log_in_location")
					time_sheet.write ("\n" + "●03 CASH-IN: [" + "cash_in_end" + "]")
					time_sheet.write ("\n" + "●04 TOTAL CASH-IN ETB: " + "0")
					time_sheet.write ("\n" + "●05 CASH-IN USERS: [" +" " + "0" + " " + "]")
					time_sheet.write ("\n" + "●06 SERVICE CHARGES: [" +" " + "0" + " " + "]")
					time_sheet.write ("\n" + "●07 -------------------------")
					time_sheet.write ("\n" + "●08 WITHDRAW: [" +"withdraw_end" + "]")
					time_sheet.write ("\n" + "●09 TOTAL WITHDRAW ETB: " + "0")
					time_sheet.write ("\n" + "●10 WITHDRAW USERS: [" +" " + "0" + " " + "]")
					time_sheet.write ("\n" + "●11 -------------------------")
					time_sheet.write ("\n" + "●12 AIR-TIME: [" +"airtime_end" + "]")
					time_sheet.write ("\n" + "●13 TOTAL AIR TIME ETB: " + "0")
					time_sheet.write ("\n" + "●14 AIR TIME USERS: [" +" " + "0" + " " + "]")
					time_sheet.write ("\n" + "●15 -------------------------")
					time_sheet.write ("\n" + "●16 PACKAGES: [" +"package_end" + "]")
					time_sheet.write ("\n" + "●17 TOTAL PACKAGES ETB: " + "0")
					time_sheet.write ("\n" + "●18 PACKAGES USERS: [" +" " + "0" + " " + "]")
					time_sheet.write ("\n" + "●19 -------------------------")
					time_sheet.write ("\n" + "●20 TELECOM BILL: [" +"telecom_bill_end" + "]")
					time_sheet.write ("\n" + "●21 TOTAL TELECOM BILL ETB: " + "0")
					time_sheet.write ("\n" + "●22 TELECOM BILL USERS: [" +" " + "0" + " " + "]")
					time_sheet.write ("\n" + "●23 -------------------------")
					time_sheet.write ("\n" + "●24 ELECTRIC BILL: [" +"electric_bill_end" + "]")
					time_sheet.write ("\n" + "●25 TOTAL ELECTRIC BILL ETB: " + "0")
					time_sheet.write ("\n" + "●26 ELECTRIC BILL USERS: [" +" " + "0" + " " + "]")
					time_sheet.write ("\n" + "●27 -------------------------")
					time_sheet.write ("\n" + "●28 DSTV: [" +"dstv_end" + "]")
					time_sheet.write ("\n" + "●29 TOTAL DSTV ETB: " + "0")
					time_sheet.write ("\n" + "●30 DSTV USERS: [" +" " + "0" + " " + "]")
					time_sheet.write ("\n" + "●31 -------------------------")
					time_sheet.write ("\n" + "●32 SIM CARD: [" +"sim_card_end" + "]")
					time_sheet.write ("\n" + "●33 TOTAL SIM CARD ETB: " + "0")
					time_sheet.write ("\n" + "●34 SIM CARD USERS: " + "0" + "          " + "AVAILABLE SIM CARD: " + "0")
					time_sheet.write ("\n" + "●35 -------------------------")
					time_sheet.write ("\n" + "●36 PASSPORT: [" +"passport_end" + "]")
					time_sheet.write ("\n" + "●37 TOTAL PASSPORT ETB: " + "0")
					time_sheet.write ("\n" + "●38 PASSPORT USERS: [" +" " + "0" + " " + "]")
					time_sheet.write ("\n" + "●39 -------------------------")
					time_sheet.write ("\n" + "●40 LICENSE: [" +"license_end" + "]")
					time_sheet.write ("\n" + "●41 TOTAL LICENSE ETB: " + "0")
					time_sheet.write ("\n" + "●42 LICENSE USERS: [" +" " + "0" + " " + "]")
					time_sheet.write ("\n" + "●43 -------------------------")
					time_sheet.write ("\n" + "●44 BANK DEPOSIT: [" +"bank_deposit_end" + "]")
					time_sheet.write ("\n" + "●45 TOTAL BANK DEPOSIT ETB: " + "0")
					time_sheet.write ("\n" + "")
					time_sheet.write ("\n" + "●●●●●●●●●●●●●●●●●●●●●●●")
					time_sheet.write ("\n" + "TOTAL DEBITED ETB: " + "0")
					time_sheet.write ("\n" + "TOTAL DEBITED ETB: " + "0")
					time_sheet.write ("\n" + "BALANCE ETB: " + "0")
					time_sheet.write ("\n" + "●●●●●●●●●●●●●●●●●●●●●●●")
								
					time_sheet.close ()
				
			else:
				pass
				
	
							
	def login_user(self):					
		names = ["dawit", "lily"]
		passwords = ["7156", "2956"]
		operators = ["203036", "420209"]
		
		name=self.ids.name.text.strip()
		operator =self.ids.operator.text.strip()
		password=self.ids.password.text.strip()
		
		# define login time for agent_1 
		calendar = str(datetime.datetime.now())
		today = str(calendar[0:10])
		time = str(calendar [10:16])
		
		# read the file
		for i in range(len(names)):
			if not name in names:
				self.ids.error.text = "[color=ff3333] Agent Name not registered! [/color]"
				
			elif name == names [i]:
				agent_name = names [i]
				agent_password = passwords [i]
				
				if password != agent_password:
					self.ids.error.text = "[color=ff3333] Agent Password wrong! [/color]"
					
				if password == agent_password:
					App.get_running_app().root.current = "main"
					with open("Time_sheets.txt", "r") as file:
						calendar = str(datetime.datetime.now())
						today = str(calendar[0:10])
						time = str(calendar [10:16])
						agent = file.read()
						r = requests.get("https://get.geojs.io/")
						ip_request= requests.get("https://get.geojs.io/v1/ip.json")
						ipAdd = ip_request.json()["ip"]
								
						url = "https://get.geojs.io/v1/ip/geo/" + ipAdd + ".json"
						geo_request = requests.get (url)
						geo_data = geo_request.json()
						latitude = geo_data ["latitude"]
						longitude = geo_data ["longitude"]
						ip = geo_data ["ip"]
						
						if "agent_1" in agent:
							agent = agent.replace("agent_1",  agent_name + " ")
							agent = agent.replace ("time_1", time)
							agent = agent.replace ("log_in_location", (ip + " " + latitude + " " +  longitude))
							
							with open ("Time_sheets.txt", "w") as file:
								file.write(agent)
								file.close ()
								
								break 
										
						if not "agent_1" in agent and "agent_2" in agent and not agent_name in agent:
							
							agent = agent.replace("agent_2",  agent_name + " ")
							agent = agent.replace ("time_2", time)
							agent = agent.replace ("log_in_location",  (ip+" "+latitude+" "+longitude))
							with open ("Time_sheets.txt", "w") as file:
								file.write(agent)
								file.close ()
								file.close () 	

				else:
					App.get_running_app().root.current = "login"







class LogoutWindow (Screen):
	def logout_user(self):					
		names = ["dawit", "lily"]
		passwords = ["7156", "2956"]
		operators = ["203036", "420209"]
		
		name=self.ids.name.text.strip()
		operator =self.ids.operator.text.strip()
		password=self.ids.password.text.strip()
		
		# define login time for agent_1 
		calendar = str(datetime.datetime.now())
		today = str(calendar[0:10])
		time = str(calendar [10:16])
		
		# read the file
		for i in range(len(names)):
			if not name in names:
				self.ids.error.text = "[color=ff3333] Agent Name not registered! [/color]"
				
			elif name == names [i]:
				agent_name = names [i]
				agent_password = passwords [i]
				
				if password != agent_password:
					self.ids.error.text = "[color=ff3333] Agent Password wrong! [/color]"
					
				if password == agent_password:
					with open("Time_sheets.txt", "r") as file:
						calendar = str(datetime.datetime.now())
						today = str(calendar[0:10])
						time = str(calendar [10:16])
						logout = file.read()
						logout_time = logout.split()
						
						if "finish_1" in logout or "finish_2" in logout:
							for i in range (len(logout_time)):
								if agent_name == logout_time[i]:
									logout_time = logout_time [i + 3]
									agent_logout =logout.replace(logout_time, time)
									with open ("Time_sheets.txt", "w") as file:
										file.write (agent_logout)
										file.close ()
										App.get_running_app().root.current = "main"
										break 
										
						else:
							self.ids.error.text = "[color=ff3333] All Agents arelogged out![/color]"
								

				else:
					App.get_running_app().root.current = "logout"




	def daily_report(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			calendar = str(datetime.datetime.now())
			today = str(calendar[0:10])
			now = str(calendar[10:13] + "-" + str(calendar [14:16]))
			s = "Time_sheets.txt"
			scr = time_sheet.read()
			if not "finish_1" in scr and not "finish_2" in scr:
				if today in scr:
					dst = today + "-" + now + " Daily Report.txt"
					shutil.copy2(s, dst)
					App.get_running_app().root.current = "login"
			else:
				pass
				










class RegistrationWindow(Screen):
	def register_user(self):
		fname = self.ids.fname.text.strip()
		lname = self.ids.lname.text.strip()
		phone = self.ids.phone.text.strip()
		email = self.ids.email.text.strip().lower ()
		gender = self.ids.gender.text.strip()
		idnumber = self.ids.idnumber.text.strip()
		address = self.ids.address.text.strip()
		password = self.ids.password.text.strip()
		
		# validation of the user inputs
		
		if fname == "" or lname == "" or phone == "" or idnumber == "" or password == "":
			self.ids.error.text = "[color=ff3333] The fields with * sign are required! [/color]"
		else:
			if "09" in phone:
				self.ids.fname.text = ""
				self.ids.lname.text = ""
				self.ids.phone.text = ""
				self.ids.email.text = ""
				self.ids.gender.text = ""
				self.ids.idnumber.text = ""
				self.ids.address.text = ""
				self.ids.password.text = ""
				
				self.ids.error.text = "[color=11ff33] You have successfully Registered![/color]"
			
			else:
				self.ids.error.text = "[color=ff3333] Enter a valid Phone Number![/color]"
				
		
		
		
	
class ForgotPasswordWindow(Screen):
	pass
	
class PasswordResetDone(Screen):
	pass 
	
class MainWindow(Screen):
	pass
	
	
	
class CashinWindow (Screen):
	def cash_in(self):
		phoneno = self.ids.phoneno.text.strip()
		cashinamount = self.ids.cashinamount.text.strip()
		
		if phoneno.isdigit() and phoneno [0:2] == "09" and len(phoneno) == 10:
			pass
					
		else:
			self.ids.error.text = "[color=ff3333] Enter a valid Phone Number![/color]"
			return 
			
		if cashinamount.isdigit() and 50 <= int(cashinamount) <= 10000:
			with open("Time_sheets.txt", "r") as file:
				cash_in_amount = file.read()
				cash_in_amount = cash_in_amount.replace("cash_in_end", " " + cashinamount  +  " " + "+" + "cash_in_end")
				
				with open ("Time_sheets.txt", "w") as file:
					file.write(cash_in_amount)
					file.close ()
					App.get_running_app().root.current = "main"
					
					
		else:
			self.ids.error.text = "[color=ff3333] Enter Eligible Amount![/color]"
			
	

			
	def total_cash_in (self):
		cash_in_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		cash_in_line = lines[3]
		cash = cash_in_line.split()
		total_cash_in = 0
	
		for amount in cash:
			if amount.isdigit () and amount  != cash[0]:
				cash_in_list.append (int(amount ))
				for i in cash_in_list:
					total_cash_in = total_cash_in + int(amount)
					break 
	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [4] = "●04 TOTAL CASH-IN ETB: " + str(total_cash_in) +"\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
			
	def cash_in_users(self):
		cash_in_users = 0
		cash_in_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		cash_in_line = lines[3]
		cash = cash_in_line.split()
		for amount in cash:
			if amount.isdigit () and amount != cash [0]:
				cash_in_list.append (cash)
				for i in cash_in_list:
					cash_in_users = cash_in_users + 1
					break 
			      	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [5] = "●05 CASH-IN USERS: [ " + str(cash_in_users) + " ]" + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
			
	def service_charges (self):
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		cash_in_line = lines[3]
		cash = cash_in_line.split()
		service_charges = 0
	
		for amount in cash:
			if amount.isdigit ():
				if int(amount) >= 1000 and int(amount ) <= 5000:
					service_charges = service_charges + 5
				elif int(amount ) > 5000 and int(amount ) <= 10000:
					service_charges = service_charges + 10
					
	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [6] = "●06 SERVICE CHARGES: [ " + str(service_charges) + " ]" + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
	def total_debt(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			total_debt= time_sheet.readlines ()
			total_cash_in_line = total_debt[4].split()
			total_cash_in = total_cash_in_line [-1]
			total_air_time_line = total_debt[13]. split()
			total_air_time = total_air_time_line [-1]
			total_packages_line = total_debt[17].split ()
			total_packages = total_packages_line [-1]
			
			total_telecom_bill_line = total_debt[21].split()
			total_telecom_bill = total_telecom_bill_line[-1]
			total_electric_bill_line = total_debt[25].split()
			total_electric_bill = total_electric_bill_line[-1]
			total_dstv_line = total_debt[29].split()
			total_dstv = total_dstv_line[-1]
					
			total_debt_list = []
			total_debt = 0
			total_debt_list.append(total_cash_in)
			total_debt_list.append (total_air_time)
			total_debt_list.append (total_packages)
			total_debt_list.append (total_telecom_bill)
			total_debt_list.append (total_electric_bill)
			total_debt_list.append(total_dstv)
			for amount in total_debt_list:
				if amount.isdigit():
					total_debt= total_debt + int(amount)
					
					with open("Time_sheets.txt", "r") as file:
						content = file.readlines ()
						
					content [48] = "TOTAL DEBITED ETB: " + str(total_debt)  +"\n"
					
					with open ("Time_sheets.txt", "w") as file:
						file.writelines(content )
						file.close ()
						
						
						
	def balance(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			balance_line = time_sheet.readlines ()
			credited = balance_line[49].split()
			credited = int(credited [-1])
			debited = balance_line[48].split()
			debited = int(debited [-1])
			balance = str(credited - debited)
				
			balance_line [50] = "BALANCE ETB: " + balance +"\n"
			time_sheet.close()
			with open ("Time_sheets.txt", "w") as file:
				file.writelines(balance_line )
				file.close ()
	
	
	
class WithdrawWindow(Screen):
	def withdraw (self):
		phoneno = self.ids.phoneno.text.strip()
		withdrawamount = self.ids.withdrawamount.text.strip()
		if phoneno.isdigit() and phoneno [0:2] == "09" and len(phoneno) == 10:
			pass
			
		else:
			self.ids.error.text = "[color=ff3333] Enter a valid Phone Number![/color]"
			return
		if withdrawamount.isdigit():
			time_sheet = open ("Time_sheets.txt", "r")
			withdraw_amount = time_sheet.read()
			withdraw_amount = withdraw_amount. replace("withdraw_end", " " + withdrawamount  +  " " + "+" + "withdraw_end")
			time_sheet.close ()
			time_sheet = open ("Time_sheets.txt", "w")
			time_sheet.write(withdraw_amount )
			time_sheet.close ()
			App.get_running_app().root.current = "main"
		else:
			self.ids.error.text = "[color=ff3333] Enter Eligible Amount![/color]"
			
			
	def total_withdraw (self):
		withdraw_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		withdraw_line = lines[8]
		withdraw = withdraw_line.split()
		total_withdraw = 0	
		
		for amount in withdraw:
			if amount.isdigit () and amount!= withdraw [0]:
				withdraw_list.append (int(amount ))
				for i in withdraw_list:
					total_withdraw= total_withdraw + int(amount)
					break 
	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [9] = "●09 TOTAL WITHDRAW ETB: " + str(total_withdraw) + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
	def withdraw_users(self):
		withdraw_users = 0
		withdraw_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		withdraw_line = lines[8]
		withdraw = withdraw_line.split()
		for amount in withdraw:
			if amount.isdigit () and amount != withdraw [0]:
				withdraw_list.append (withdraw)
				for i in withdraw_list:
					withdraw_users = withdraw_users + 1
					break 
			      	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [10] = "●10 WITHDRAW USERS: [ " + str(withdraw_users) + " ]" + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
	def total_credit(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			total_credit= time_sheet.readlines ()
			total_withdraw_line = total_credit[9].split()
			total_withdraw = total_withdraw_line [-1]
			total_sim_card_line = total_credit[33]. split()
			total_sim_card = total_sim_card_line [-1]
			total_passport_line = total_credit[37].split ()
			total_passport = total_passport_line [-1]
			
			total_license_line = total_credit[41].split()
			total_license = total_license_line[-1]
			
					
			total_credit_list = []
			total_credit = 0
			total_credit_list.append(total_withdraw)
			total_credit_list.append (total_sim_card)
			total_credit_list.append (total_passport)
			total_credit_list.append (total_license)
			
			for amount in total_credit_list:
				if amount.isdigit():
					total_credit= total_credit + int(amount)
					
					with open("Time_sheets.txt", "r") as file:
						content = file.readlines ()
						
					content [49] = "TOTAL CREDITED ETB: " + str(total_credit)  +"\n"
					
					with open ("Time_sheets.txt", "w") as file:
						file.writelines(content )
						file.close ()
						
						
	def balance(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			balance_line = time_sheet.readlines ()
			credited = balance_line[49].split()
			credited = int(credited [-1])
			debited = balance_line[48].split()
			debited = int(debited [-1])
			balance = str(credited - debited)
				
			balance_line [50] = "BALANCE ETB: " + balance +"\n"
			time_sheet.close()
			with open ("Time_sheets.txt", "w") as file:
				file.writelines(balance_line )
				file.close ()
			
			
			
class AirTimeWindow(Screen):
	def air_time(self):
		phoneno = self.ids.phoneno.text.strip()
		airtimeamount = self.ids.airtimeamount.text.strip()
		
		if phoneno.isdigit() and phoneno [0:2] == "09" and len(phoneno) == 10:
			pass
					
		else:
			self.ids.error.text = "[color=ff3333] Enter a valid Phone Number![/color]"
			return 
			
		if airtimeamount.isdigit() and 5 <= int(airtimeamount) <= 10000:
			with open("Time_sheets.txt", "r") as file:
				airtime_amount = file.read()
				airtime_amount = airtime_amount.replace("airtime_end", " " + airtimeamount  +  " " + "+" + "airtime_end")
				
				with open ("Time_sheets.txt", "w") as file:
					file.write(airtime_amount)
					file.close ()
					App.get_running_app().root.current = "main"
					
		else:
			self.ids.error.text = "[color=ff3333] Enter Eligible Amount![/color]"
			
			
	def total_air_time(self):
		airtime_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		airtime_line = lines[12]
		airtime = airtime_line.split()
		total_airtime = 0	
		
		for amount in airtime:
			if amount.isdigit () and amount!= airtime[0]:
				airtime_list.append (int(amount ))
				for i in airtime_list:
					total_airtime= total_airtime + int(amount)
					break 
	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [13] = "●13 TOTAL AIR TIME ETB: " + str(total_airtime) + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content)
			file.close ()
			
			
	def airtime_users(self):
		airtime_users = 0
		airtime_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		airtime_line = lines[12]
		airtime = airtime_line.split()
		for amount in airtime:
			if amount.isdigit () and amount != airtime [0]:
				airtime_list.append (airtime)
				for i in airtime_list:
					airtime_users = airtime_users + 1
					break 
			      	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [14] = "●14 AIRTIME USERS: [ " + str(airtime_users) + " ]" + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
			
	def total_debt(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			total_debt= time_sheet.readlines ()
			total_cash_in_line = total_debt[4].split()
			total_cash_in = total_cash_in_line [-1]
			total_air_time_line = total_debt[13]. split()
			total_air_time = total_air_time_line [-1]
			total_packages_line = total_debt[17].split ()
			total_packages = total_packages_line [-1]
			
			total_telecom_bill_line = total_debt[21].split()
			total_telecom_bill = total_telecom_bill_line[-1]
			total_electric_bill_line = total_debt[25].split()
			total_electric_bill = total_electric_bill_line[-1]
			total_dstv_line = total_debt[29].split()
			total_dstv = total_dstv_line[-1]
					
			total_debt_list = []
			total_debt = 0
			total_debt_list.append(total_cash_in)
			total_debt_list.append (total_air_time)
			total_debt_list.append (total_packages)
			total_debt_list.append (total_telecom_bill)
			total_debt_list.append (total_electric_bill)
			total_debt_list.append(total_dstv)
			for amount in total_debt_list:
				if amount.isdigit():
					total_debt= total_debt + int(amount)
					
					with open("Time_sheets.txt", "r") as file:
						content = file.readlines ()
						
					content [48] = "TOTAL DEBITED ETB: " + str(total_debt)  +"\n"
					
					with open ("Time_sheets.txt", "w") as file:
						file.writelines(content )
						file.close ()
						
						
	def balance(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			balance_line = time_sheet.readlines ()
			credited = balance_line[49].split()
			credited = int(credited [-1])
			debited = balance_line[48].split()
			debited = int(debited [-1])
			balance = str(credited - debited)
				
			balance_line [50] = "BALANCE ETB: " + balance +"\n"
			time_sheet.close()
			with open ("Time_sheets.txt", "w") as file:
				file.writelines(balance_line )
				file.close ()
			
			
			
			
class PackagesWindow (Screen):
	def packages(self):
		phoneno = self.ids.phoneno.text.strip()
		packagesamount = self.ids.packagesamount.text.strip()
		
		if phoneno.isdigit() and phoneno [0:2] == "09" and len(phoneno) == 10:
			pass
					
		else:
			self.ids.error.text = "[color=ff3333] Enter a valid Phone Number![/color]"
			return 
			
		if packagesamount.isdigit():
			with open("Time_sheets.txt", "r") as file:
				packages_amount = file.read()
				packages_amount = packages_amount.replace("package_end", " " + packagesamount  +  " " + "+" + "package_end")
				
				with open ("Time_sheets.txt", "w") as file:
					file.write(packages_amount)
					file.close ()
					App.get_running_app().root.current = "main"
					
		else:
			self.ids.error.text = "[color=ff3333] Enter Eligible Amount![/color]"
			
			
	def total_packages(self):
		packages_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		packages_line = lines[16]
		packages = packages_line.split()
		total_packages = 0	
		
		for amount in packages:
			if amount.isdigit () and amount!= packages[0]:
				packages_list.append (int(amount ))
				for i in packages_list:
					total_packages = total_packages + int(amount)
					break 
	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [17] = "●17 TOTAL PACKAGES ETB: " + str(total_packages) + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
	def packages_users(self):
		packages_users = 0
		packages_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		packages_line = lines[16]
		packages = packages_line.split()
		for amount in packages:
			if amount.isdigit () and amount != packages [0]:
				packages_list.append (packages)
				for i in packages_list:
					packages_users = packages_users + 1
					break 
			      	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [18] = "●18 PACKAGES USERS: [ " + str(packages_users) + " ]" + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
			
	def total_debt(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			total_debt= time_sheet.readlines ()
			total_cash_in_line = total_debt[4].split()
			total_cash_in = total_cash_in_line [-1]
			total_air_time_line = total_debt[13]. split()
			total_air_time = total_air_time_line [-1]
			total_packages_line = total_debt[17].split ()
			total_packages = total_packages_line [-1]
			
			total_telecom_bill_line = total_debt[21].split()
			total_telecom_bill = total_telecom_bill_line[-1]
			total_electric_bill_line = total_debt[25].split()
			total_electric_bill = total_electric_bill_line[-1]
			total_dstv_line = total_debt[29].split()
			total_dstv = total_dstv_line[-1]
					
			total_debt_list = []
			total_debt = 0
			total_debt_list.append(total_cash_in)
			total_debt_list.append (total_air_time)
			total_debt_list.append (total_packages)
			total_debt_list.append (total_telecom_bill)
			total_debt_list.append (total_electric_bill)
			total_debt_list.append(total_dstv)
			for amount in total_debt_list:
				if amount.isdigit():
					total_debt= total_debt + int(amount)
					
					with open("Time_sheets.txt", "r") as file:
						content = file.readlines ()
						
					content [48] = "TOTAL DEBITED ETB: " + str(total_debt)  +"\n"
					
					with open ("Time_sheets.txt", "w") as file:
						file.writelines(content )
						file.close ()
						
						
	def balance(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			balance_line = time_sheet.readlines ()
			credited = balance_line[49].split()
			credited = int(credited [-1])
			debited = balance_line[48].split()
			debited = int(debited [-1])
			balance = str(credited - debited)
				
			balance_line [50] = "BALANCE ETB: " + balance +"\n"
			time_sheet.close()
			with open ("Time_sheets.txt", "w") as file:
				file.writelines(balance_line )
				file.close ()
			
			
			
			
class TelecomBillWindow (Screen):
	def telecom_bill(self):
		phoneno = self.ids.phoneno.text.strip()
		telecombillamount = self.ids.telecombillamount.text.strip()
		
		if phoneno.isdigit() and len(phoneno) >= 5:
			pass
					
		else:
			self.ids.error.text = "[color=ff3333] Enter a valid Account/Service Number![/color]"
			return 
			
		if telecombillamount.isdigit():
			with open("Time_sheets.txt", "r") as file:
				telecombill_amount = file.read()
				telecombill_amount = telecombill_amount.replace("telecom_bill_end", " " + telecombillamount  +  " " + "+" + "telecom_bill_end")
				
				with open ("Time_sheets.txt", "w") as file:
					file.write(telecombill_amount)
					file.close ()
					App.get_running_app().root.current = "main"
					
		else:
			self.ids.error.text = "[color=ff3333] Enter Eligible Amount![/color]"
			
			
	def total_telecom_bill(self):
		telecom_bill_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		telecom_bill_line = lines[20]
		telecom_bill = telecom_bill_line.split()
		total_telecom_bill = 0	
		
		for amount in telecom_bill:
			if amount.isdigit ():
				telecom_bill_list.append (int(amount ))
				for i in telecom_bill_list:
					total_telecom_bill = total_telecom_bill + int(amount)
					break 
	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [21] = "●21 TOTAL TELECOM BILL ETB: " + str(total_telecom_bill) + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
	
	def telecom_bill_users(self):
		telecom_bill_users = 0
		telecom_bill_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		telecom_bill_line = lines[20]
		telecom_bill = telecom_bill_line.split()
		for amount in telecom_bill:
			if amount.isdigit ():
				telecom_bill_list.append (telecom_bill)
				for i in telecom_bill_list:
					telecom_bill_users = telecom_bill_users + 1
					break 
			      	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [22] = "●22 TELECOM BILL USERS: [ " + str(telecom_bill_users) + " ]" + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
			
	def total_debt(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			total_debt= time_sheet.readlines ()
			total_cash_in_line = total_debt[4].split()
			total_cash_in = total_cash_in_line [-1]
			total_air_time_line = total_debt[13]. split()
			total_air_time = total_air_time_line [-1]
			total_packages_line = total_debt[17].split ()
			total_packages = total_packages_line [-1]
			
			total_telecom_bill_line = total_debt[21].split()
			total_telecom_bill = total_telecom_bill_line[-1]
			total_electric_bill_line = total_debt[25].split()
			total_electric_bill = total_electric_bill_line[-1]
			total_dstv_line = total_debt[29].split()
			total_dstv = total_dstv_line[-1]
					
			total_debt_list = []
			total_debt = 0
			total_debt_list.append(total_cash_in)
			total_debt_list.append (total_air_time)
			total_debt_list.append (total_packages)
			total_debt_list.append (total_telecom_bill)
			total_debt_list.append (total_electric_bill)
			total_debt_list.append(total_dstv)
			for amount in total_debt_list:
				if amount.isdigit():
					total_debt= total_debt + int(amount)
					
					with open("Time_sheets.txt", "r") as file:
						content = file.readlines ()
						
					content [48] = "TOTAL DEBITED ETB: " + str(total_debt)  +"\n"
					
					with open ("Time_sheets.txt", "w") as file:
						file.writelines(content )
						file.close ()
						
						
						
	def balance(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			balance_line = time_sheet.readlines ()
			credited = balance_line[49].split()
			credited = int(credited [-1])
			debited = balance_line[48].split()
			debited = int(debited [-1])
			balance = str(credited - debited)
				
			balance_line [50] = "BALANCE ETB: " + balance +"\n"
			time_sheet.close()
			with open ("Time_sheets.txt", "w") as file:
				file.writelines(balance_line )
				file.close ()
			
			
			
			
class ElectricBillWindow (Screen):
	def electric_bill(self):
		phoneno = self.ids.phoneno.text.strip()
		electricbillamount = self.ids.electricbillamount.text.strip()
		
		if phoneno.isdigit() and len(phoneno) >= 5:
			pass
					
		else:
			self.ids.error.text = "[color=ff3333] Enter a valid Account/Service Number![/color]"
			return 
			
		if electricbillamount.isdigit():
			with open("Time_sheets.txt", "r") as file:
				electricbill_amount = file.read()
				electricbill_amount = electricbill_amount.replace("electric_bill_end", " " + electricbillamount  +  " " + "+" + "electric_bill_end")
				
				with open ("Time_sheets.txt", "w") as file:
					file.write(electricbill_amount)
					file.close ()
					App.get_running_app().root.current = "main"
					
		else:
			self.ids.error.text = "[color=ff3333] Enter Eligible Amount![/color]"
			
			
	def total_electric_bill(self):
		electric_bill_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		electric_bill_line = lines[24]
		electric_bill = electric_bill_line.split()
		total_electric_bill = 0	
		
		for amount in electric_bill:
			if amount.isdigit ():
				electric_bill_list.append (int(amount ))
				for i in electric_bill_list:
					total_electric_bill = total_electric_bill + int(amount)
					break 
	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [25] = "●25 TOTAL ELECTRIC BILL ETB: " + str(total_electric_bill) + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
	
	def electric_bill_users(self):
		electric_bill_users = 0
		electric_bill_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		electric_bill_line = lines[24]
		electric_bill = electric_bill_line.split()
		for amount in electric_bill:
			if amount.isdigit ():
				electric_bill_list.append (electric_bill)
				for i in electric_bill_list:
					electric_bill_users = electric_bill_users + 1
					break 
			      	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [26] = "●26 ELECTRIC BILL USERS: [ " + str(electric_bill_users) + " ]" + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
			
	def total_debt(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			total_debt= time_sheet.readlines ()
			total_cash_in_line = total_debt[4].split()
			total_cash_in = total_cash_in_line [-1]
			total_air_time_line = total_debt[13]. split()
			total_air_time = total_air_time_line [-1]
			total_packages_line = total_debt[17].split ()
			total_packages = total_packages_line [-1]
			
			total_telecom_bill_line = total_debt[21].split()
			total_telecom_bill = total_telecom_bill_line[-1]
			total_electric_bill_line = total_debt[25].split()
			total_electric_bill = total_electric_bill_line[-1]
			total_dstv_line = total_debt[29].split()
			total_dstv = total_dstv_line[-1]
					
			total_debt_list = []
			total_debt = 0
			total_debt_list.append(total_cash_in)
			total_debt_list.append (total_air_time)
			total_debt_list.append (total_packages)
			total_debt_list.append (total_telecom_bill)
			total_debt_list.append (total_electric_bill)
			total_debt_list.append(total_dstv)
			for amount in total_debt_list:
				if amount.isdigit():
					total_debt= total_debt + int(amount)
					
					with open("Time_sheets.txt", "r") as file:
						content = file.readlines ()
						
					content [48] = "TOTAL DEBITED ETB: " + str(total_debt)  +"\n"
					
					with open ("Time_sheets.txt", "w") as file:
						file.writelines(content )
						file.close ()
						
						
	def balance(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			balance_line = time_sheet.readlines ()
			credited = balance_line[49].split()
			credited = int(credited [-1])
			debited = balance_line[48].split()
			debited = int(debited [-1])
			balance = str(credited - debited)
				
			balance_line [50] = "BALANCE ETB: " + balance +"\n"
			time_sheet.close()
			with open ("Time_sheets.txt", "w") as file:
				file.writelines(balance_line )
				file.close ()
			
			
			
class DstvWindow (Screen):
	def dstv(self):
		phoneno = self.ids.phoneno.text.strip()
		dstvamount = self.ids.dstvamount.text.strip()
		
		if phoneno.isdigit():
			pass
					
		else:
			self.ids.error.text = "[color=ff3333] Enter a valid Account Number![/color]"
			return 
			
		if dstvamount.isdigit():
			with open("Time_sheets.txt", "r") as file:
				dstv_amount = file.read()
				dstv_amount = dstv_amount.replace("dstv_end", " " + dstvamount  +  " " + "+" + "dstv_end")
				
				with open ("Time_sheets.txt", "w") as file:
					file.write(dstv_amount)
					file.close ()
					App.get_running_app().root.current = "main"
					
					
		else:
			self.ids.error.text = "[color=ff3333] Enter Eligible Amount![/color]"
			
	

			
			
	def total_dstv (self):
		dstv_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		dstv_line = lines[28]
		dstv = dstv_line.split()
		total_dstv = 0
	
		for amount in dstv:
			if amount.isdigit ():
				dstv_list.append (int(amount ))
				for i in dstv_list:
					total_dstv = total_dstv + int(amount)
					break 
	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [29] = "●29 TOTAL DSTV ETB: " + str(total_dstv) +"\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
			
	def dstv_users(self):
		dstv_users = 0
		dstv_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		dstv_line = lines[28]
		dstv = dstv_line.split()
		for amount in dstv:
			if amount.isdigit ():
				dstv_list.append (dstv)
				for i in dstv_list:
					dstv_users = dstv_users + 1
					break 
			      	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [30] = "●30 DSTV USERS: [ " + str(dstv_users) + " ]" + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
			
	def total_debt(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			total_debt= time_sheet.readlines ()
			total_cash_in_line = total_debt[4].split()
			total_cash_in = total_cash_in_line [-1]
			total_air_time_line = total_debt[13]. split()
			total_air_time = total_air_time_line [-1]
			total_packages_line = total_debt[17].split ()
			total_packages = total_packages_line [-1]
			
			total_telecom_bill_line = total_debt[21].split()
			total_telecom_bill = total_telecom_bill_line[-1]
			total_electric_bill_line = total_debt[25].split()
			total_electric_bill = total_electric_bill_line[-1]
			total_dstv_line = total_debt[29].split()
			total_dstv = total_dstv_line[-1]
					
			total_debt_list = []
			total_debt = 0
			total_debt_list.append(total_cash_in)
			total_debt_list.append (total_air_time)
			total_debt_list.append (total_packages)
			total_debt_list.append (total_telecom_bill)
			total_debt_list.append (total_electric_bill)
			total_debt_list.append(total_dstv)
			for amount in total_debt_list:
				if amount.isdigit():
					total_debt= total_debt + int(amount)
					
					with open("Time_sheets.txt", "r") as file:
						content = file.readlines ()
						
					content [48] = "TOTAL DEBITED ETB: " + str(total_debt)  +"\n"
					
					with open ("Time_sheets.txt", "w") as file:
						file.writelines(content )
						file.close ()
						
						
						
	def balance(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			balance_line = time_sheet.readlines ()
			credited = balance_line[49].split()
			credited = int(credited [-1])
			debited = balance_line[48].split()
			debited = int(debited [-1])
			balance = str(credited - debited)
				
			balance_line [50] = "BALANCE ETB: " + balance +"\n"
			time_sheet.close()
			with open ("Time_sheets.txt", "w") as file:
				file.writelines(balance_line )
				file.close ()
			
			
			
			
class SimCardWindow (Screen):
	def sim_card(self):
		phoneno = self.ids.phoneno.text.strip()
		simcardamount = self.ids.simcardamount.text.strip()
		
		if phoneno.isdigit() and phoneno [0:2] == "09" and len(phoneno) == 10:
			pass
					
		else:
			self.ids.error.text = "[color=ff3333] Enter a valid Phone Number![/color]"
			return 
			
		if simcardamount.isdigit():
			with open("Time_sheets.txt", "r") as file:
				sim_card_amount = file.read()
				sim_card_amount = sim_card_amount.replace("sim_card_end", " " + simcardamount  +  " " + "+" + "sim_card_end")
				
				with open ("Time_sheets.txt", "w") as file:
					file.write(sim_card_amount)
					file.close ()
					App.get_running_app().root.current = "main"
					
					
		else:
			self.ids.error.text = "[color=ff3333] Enter Eligible Amount![/color]"
			
			
	def total_sim_card (self):
		sim_card_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		sim_card_line = lines[32]
		sim_card = sim_card_line.split()
		total_sim_card = 0
	
		for amount in sim_card:
			if amount.isdigit ():
				sim_card_list.append (int(amount ))
				for i in sim_card_list:
					total_sim_card = total_sim_card + int(amount)
					break 
	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [33] = "●33 TOTAL SIM CARD ETB: " + str(total_sim_card) +"\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
			
	def sim_card_users(self):
		sim_card_users = 0
		sim_card_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		sim_card_line = lines[32]
		sim_card = sim_card_line.split()
		for amount in sim_card:
			if amount.isdigit ():
				sim_card_list.append (sim_card)
				for i in sim_card_list:
					sim_card_users = sim_card_users + 1
					break 
			      	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [34] = "●34 SIM CARD USERS: [ " + str(sim_card_users) + " ]" + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
	def total_credit(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			total_credit= time_sheet.readlines ()
			total_withdraw_line = total_credit[9].split()
			total_withdraw = total_withdraw_line [-1]
			total_sim_card_line = total_credit[33]. split()
			total_sim_card = total_sim_card_line [-1]
			total_passport_line = total_credit[37].split ()
			total_passport = total_passport_line [-1]
			
			total_license_line = total_credit[41].split()
			total_license = total_license_line[-1]
			
					
			total_credit_list = []
			total_credit = 0
			total_credit_list.append(total_withdraw)
			total_credit_list.append (total_sim_card)
			total_credit_list.append (total_passport)
			total_credit_list.append (total_license)
			
			for amount in total_credit_list:
				if amount.isdigit():
					total_credit= total_credit + int(amount)
					
					with open("Time_sheets.txt", "r") as file:
						content = file.readlines ()
						
					content [49] = "TOTAL CREDITED ETB: " + str(total_credit)  +"\n"
					
					with open ("Time_sheets.txt", "w") as file:
						file.writelines(content )
						file.close ()
						
						
						
	def balance(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			balance_line = time_sheet.readlines ()
			credited = balance_line[49].split()
			credited = int(credited [-1])
			debited = balance_line[48].split()
			debited = int(debited [-1])
			balance = str(credited - debited)
				
			balance_line [50] = "BALANCE ETB: " + balance +"\n"
			time_sheet.close()
			with open ("Time_sheets.txt", "w") as file:
				file.writelines(balance_line )
				file.close ()
			
			
			
class PassportWindow (Screen):
	def passport(self):
		phoneno = self.ids.phoneno.text.strip()
		passportamount = self.ids.passportamount.text.strip()
		
		if phoneno.isdigit():
			pass
					
		else:
			self.ids.error.text = "[color=ff3333] Enter a valid Passport Number![/color]"
			return 
			
		if passportamount.isdigit():
			with open("Time_sheets.txt", "r") as file:
				passport_amount = file.read()
				passport_amount = passport_amount.replace("passport_end", " " + passportamount  +  " " + "+" + "passport_end")
				
				with open ("Time_sheets.txt", "w") as file:
					file.write(passport_amount)
					file.close ()
					App.get_running_app().root.current = "main"
					
					
		else:
			self.ids.error.text = "[color=ff3333] Enter Eligible Amount![/color]"
			
	

			
			
	def total_passport (self):
		passport_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		passport_line = lines[36]
		passport = passport_line.split()
		total_passport = 0
	
		for amount in passport:
			if amount.isdigit ():
				passport_list.append (int(amount ))
				for i in passport_list:
					total_passport = total_passport + int(amount)
					break 
	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [37] = "●37 TOTAL PASSPORT ETB: " + str(total_passport) +"\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
			
	def passport_users(self):
		passport_users = 0
		passport_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		passport_line = lines[36]
		passport = passport_line.split()
		for amount in passport:
			if amount.isdigit ():
				passport_list.append (passport)
				for i in passport_list:
					passport_users = passport_users + 1
					break 
			      	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [38] = "●38 PASSPORT USERS: [ " + str(passport_users) + " ]" + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
			
	def total_credit(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			total_credit= time_sheet.readlines ()
			total_withdraw_line = total_credit[9].split()
			total_withdraw = total_withdraw_line [-1]
			total_sim_card_line = total_credit[33]. split()
			total_sim_card = total_sim_card_line [-1]
			total_passport_line = total_credit[37].split ()
			total_passport = total_passport_line [-1]
			
			total_license_line = total_credit[41].split()
			total_license = total_license_line[-1]
			
					
			total_credit_list = []
			total_credit = 0
			total_credit_list.append(total_withdraw)
			total_credit_list.append (total_sim_card)
			total_credit_list.append (total_passport)
			total_credit_list.append (total_license)
			
			for amount in total_credit_list:
				if amount.isdigit():
					total_credit= total_credit + int(amount)
					
					with open("Time_sheets.txt", "r") as file:
						content = file.readlines ()
						
					content [49] = "TOTAL CREDITED ETB: " + str(total_credit)  +"\n"
					
					with open ("Time_sheets.txt", "w") as file:
						file.writelines(content )
						file.close ()
			
			
			
	def balance(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			balance_line = time_sheet.readlines ()
			credited = balance_line[49].split()
			credited = int(credited [-1])
			debited = balance_line[48].split()
			debited = int(debited [-1])
			balance = str(credited - debited)
				
			balance_line [50] = "BALANCE ETB: " + balance +"\n"
			time_sheet.close()
			with open ("Time_sheets.txt", "w") as file:
				file.writelines(balance_line )
				file.close ()
			
			
			
			
class LicenseWindow (Screen):
	def license(self):
		phoneno = self.ids.phoneno.text.strip()
		licenseamount = self.ids.licenseamount.text.strip()
		
		if phoneno.isdigit():
			pass
					
		else:
			self.ids.error.text = "[color=ff3333] Enter a valid License Number![/color]"
			return 
			
		if licenseamount.isdigit():
			with open("Time_sheets.txt", "r") as file:
				license_amount = file.read()
				license_amount = license_amount.replace("license_end", " " + licenseamount  +  " " + "+" + "license_end")
				
				with open ("Time_sheets.txt", "w") as file:
					file.write(license_amount)
					file.close ()
					App.get_running_app().root.current = "main"
					
					
		else:
			self.ids.error.text = "[color=ff3333] Enter Eligible Amount![/color]"
			
	

			
			
	def total_license (self):
		license_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		license_line = lines[40]
		license = license_line.split()
		total_license = 0
	
		for amount in license:
			if amount.isdigit ():
				license_list.append (int(amount ))
				for i in license_list:
					total_license = total_license + int(amount)
					break 
	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [41] = "●41 TOTAL LICENSE ETB: " + str(total_license) +"\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
			
	def license_users(self):
		license_users = 0
		license_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		license_line = lines[40]
		license = license_line.split()
		for amount in license:
			if amount.isdigit ():
				license_list.append (license)
				for i in license_list:
					license_users = license_users + 1
					break 
			      	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [42] = "●42 LICENSE USERS: [ " + str(license_users) + " ]" + "\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
			
	def total_credit(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			total_credit= time_sheet.readlines ()
			total_withdraw_line = total_credit[9].split()
			total_withdraw = total_withdraw_line [-1]
			total_sim_card_line = total_credit[33]. split()
			total_sim_card = total_sim_card_line [-1]
			total_passport_line = total_credit[37].split ()
			total_passport = total_passport_line [-1]
			
			total_license_line = total_credit[41].split()
			total_license = total_license_line[-1]
			
					
			total_credit_list = []
			total_credit = 0
			total_credit_list.append(total_withdraw)
			total_credit_list.append (total_sim_card)
			total_credit_list.append (total_passport)
			total_credit_list.append (total_license)
			
			for amount in total_credit_list:
				if amount.isdigit():
					total_credit= total_credit + int(amount)
					
					with open("Time_sheets.txt", "r") as file:
						content = file.readlines ()
						
					content [49] = "TOTAL CREDITED ETB: " + str(total_credit)  +"\n"
					
					with open ("Time_sheets.txt", "w") as file:
						file.writelines(content )
						file.close ()
						
						
						
	def balance(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			balance_line = time_sheet.readlines ()
			credited = balance_line[49].split()
			credited = int(credited [-1])
			debited = balance_line[48].split()
			debited = int(debited [-1])
			balance = str(credited - debited)
				
			balance_line [50] = "BALANCE ETB: " + balance +"\n"
			time_sheet.close()
			with open ("Time_sheets.txt", "w") as file:
				file.writelines(balance_line )
				file.close ()
			
			
			
			
			


class BankDepositWindow(Screen):
	def bank_deposit (self):
		phoneno = self.ids.phoneno.text.strip()
		bankdepositamount = self.ids.bankdepositamount.text.strip()
		
		if phoneno.isdigit() and phoneno [0:2] == "09" and len(phoneno) == 10:
			pass
					
		else:
			self.ids.error.text = "[color=ff3333] Enter a valid Transaction Number![/color]"
			return 
			
		if bankdepositamount.isdigit():
			with open("Time_sheets.txt", "r") as file:
				bank_deposit_amount = file.read()
				bank_deposit_amount = bank_deposit_amount.replace("bank_deposit_end", " " + bankdepositamount  +  " " + "+" + "bank_deposit_end")
				
				with open ("Time_sheets.txt", "w") as file:
					file.write(bank_deposit_amount)
					file.close ()
					App.get_running_app().root.current = "main"		
					
		else:
			self.ids.error.text = "[color=ff3333] Enter Eligible Amount![/color]"
			

			
	def total_bank_deposit (self):
		bank_deposit_list = []
		time_sheet = open ("Time_sheets.txt", "r")
		lines = time_sheet.readlines()
		time_sheet.close ()
		bank_deposit_line = lines[44]
		bank_deposit = bank_deposit_line.split()
		total_bank_deposit = 0
	
		for amount in bank_deposit:
			if amount.isdigit ():
				bank_deposit_list.append (int(amount ))
				for i in bank_deposit_list:
					total_bank_deposit = total_bank_deposit + int(amount)
					break 
	
		with open("Time_sheets.txt", "r") as file:
			content = file.readlines ()
		
		content [45] = "●45 TOTAL BANK DEPOSIT ETB: " + str(total_bank_deposit) +"\n"
	
		with open ("Time_sheets.txt", "w") as file:
			file.writelines(content )
			file.close ()
			
			
			
	def total_credit(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			total_credit= time_sheet.readlines ()
			total_withdraw_line = total_credit[9].split()
			total_withdraw = total_withdraw_line [-1]
			total_sim_card_line = total_credit[33]. split()
			total_sim_card = total_sim_card_line [-1]
			total_passport_line = total_credit[37].split ()
			total_passport = total_passport_line [-1]
			
			total_license_line = total_credit[41].split()
			total_license = total_license_line[-1]
			total_bank_deposit_line = total_credit[45].split()
			total_bank_deposit = total_bank_deposit_line[-1]
			
					
			total_credit_list = []
			total_credit = 0
			total_credit_list.append(total_withdraw)
			total_credit_list.append (total_sim_card)
			total_credit_list.append (total_passport)
			total_credit_list.append (total_license)
			total_credit_list.append (total_bank_deposit)
			
			for amount in total_credit_list:
				if amount.isdigit():
					total_credit= total_credit + int(amount)
					
					with open("Time_sheets.txt", "r") as file:
						content = file.readlines ()
						
					content [49] = "TOTAL CREDITED ETB: " + str(total_credit)  +"\n"
					
					with open ("Time_sheets.txt", "w") as file:
						file.writelines(content )
						file.close ()
						
						
						
	def balance(self):
		with open ("Time_sheets.txt", "r") as time_sheet:
			balance_line = time_sheet.readlines ()
			credited = balance_line[49].split()
			credited = int(credited [-1])
			debited = balance_line[48].split()
			debited = int(debited [-1])
			balance = str(credited - debited)
				
			balance_line [50] = "BALANCE ETB: " + balance +"\n"
			time_sheet.close()
			with open ("Time_sheets.txt", "w") as file:
				file.writelines(balance_line )
				file.close ()
			
			
			

		
	

class ManagementSystem(App):
	def build(self):
		self.title= "Basic Managemen App"
		
		return WindowManager()
		
		
		
if __name__== "__main__":
	ManagementSystem().run()