#This was written by Yasar Azimi, Irfan Momand, Nisar Arif. 
import Read_Hospital_Excel_Sheet
import Write_Hospital_Excel_Sheet

	
def AppointmentIndexInDoctorsDataBase (patient_ID) :
	for i in Doctors_DataBase :
		for j in Doctors_DataBase[i] :							
			if str(patient_ID) == str(j[0]) :
				Appointment_index = Doctors_DataBase[i].index(j)
				return Appointment_index,i

print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome Hospital Management System                     *")
print("*                                                                          *")
print("****************************************************************************")
	
	
tries = 0
tries_flag = ""
while tries_flag != "Close the program" :

		Pateints_DataBase = Read_Hospital_Excel_Sheet.Read_Patients_DataBase()
		Doctors_DataBase  = Read_Hospital_Excel_Sheet.Read_Doctors_DataBase()
				
		print("-----------------------------------------")
		print("|Enter 1 for Admin mode			|\n|Enter 2 for user mode			|")
		print("-----------------------------------------")
		Admin_user_mode = input("Enter your mode : ") 
		

		if Admin_user_mode == "1" :																			#Admin mode
				print("*****************************************\n|         Welcome to admin mode         |\n*****************************************")
				Password = input("Please enter your password : ")
				while True :
					
					if Password == "1234" :
						print("-----------------------------------------")
						print("|To manage patients Enter 1 		|\n|To manage docotrs Enter 2	 	|\n|To manage appointments Enter 3 	|\n|To be back Enter E			|")
						print("-----------------------------------------")
						AdminOptions = input ("Enter your choice : ")
						AdminOptions = AdminOptions.upper()
						
						if AdminOptions == "1" :															#Admin mode --> Pateints Management
								print("-----------------------------------------")
								print("|To add new patient Enter 1	  	|")
								print("|To display patient Enter 2	  	|")
								print("|To delete patient data Enter 3		|")
								print("|To edit patient data Enter 4    	|")
								print("|To Back enter B      			|")
								print("-----------------------------------------")
								Admin_choice = input ("Enter your choice : ")
								Admin_choice = Admin_choice.upper()
								
								if Admin_choice == "1" : 										#Admin mode --> Pateints Management --> Enter new patient data
											try :		#To avoid non integer input
												patient_ID = int(input("Enter patient ID : "))
												while patient_ID in Pateints_DataBase :		#if Admin entered used ID
													patient_ID = int(input("This ID is unavailable, please try another ID : "))					
												Department=input("Enter patient department                : ")
												DoctorName=input("Enter name of doctor following the case : ")
												Name      =input("Enter patient name                      : ")
												Age       =input("Enter patient age                       : ")
												Gender    =input("Enter patient gender                    : ")
												Address   =input("Enter patient address                   : ")
												RoomNumber=input("Enter patient room number               : ")
												Pateints_DataBase[patient_ID]=[Department,DoctorName,Name,Age,Gender,Address,RoomNumber]
												print("----------------------Patient added successfully----------------------")
											except :
												print("Patient ID should be an integer number")
										
								elif Admin_choice == "2" :										#Admin mode --> Pateints Management --> Display patient data
											try :		#To avoid non integer input
												patient_ID = int(input("Enter patient ID : "))
												while patient_ID not in Pateints_DataBase :
													patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
												print("\npatient name        : ",Pateints_DataBase[patient_ID][2])
												print("patient age         : ",Pateints_DataBase[patient_ID][3])
												print("patient gender      : ",Pateints_DataBase[patient_ID][4])
												print("patient address     : ",Pateints_DataBase[patient_ID][5])
												print("patient room number : ",Pateints_DataBase[patient_ID][6])
												print("patient is in "+Pateints_DataBase[patient_ID][0]+" department")
												print("patient is followed by doctor : "+Pateints_DataBase[patient_ID][1])
											except :
												print("Patient ID should be an integer number")
								
								elif Admin_choice == "3" :										#Admin mode --> Pateints Management --> Delete patient data
											try :		#To avoid non integer input
												patient_ID = int(input("Enter patient ID : "))
												while patient_ID not in Pateints_DataBase :
													patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
												Pateints_DataBase.pop(patient_ID)
												print("----------------------Patient data deleted successfully----------------------")
											except :
												print("Patient ID should be an integer number")
										
								elif Admin_choice == "4" :						 				#Admin mode --> Pateints Management --> Edit patient data
											try :		#To avoid non integer input
												patient_ID=int(input("Enter patient ID : "))
												while patient_ID not in Pateints_DataBase :
													patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
												while True :
													print("------------------------------------------")
													print("|To Edit pateint Department Enter 1 :    |")
													print("|To Edit Doctor following case Enter 2 : |")
													print("|To Edit pateint Name Enter 3 :          |")
													print("|To Edit pateint Age Enter 4 :           |")
													print("|To Edit pateint Gender Enter 5 :        |")
													print("|To Edit pateint Address Enter 6 :       |")
													print("|To Edit pateint RoomNumber Enter 7 :    |")
													print("|To be Back Enter B                      |")
													print("-----------------------------------------")
													Admin_choice = input("Enter your choice : ")
													Admin_choice = Admin_choice.upper()
													if Admin_choice == "1" :
														Pateints_DataBase[patient_ID][0]=input("\nEnter patient department : ")
														print("----------------------Patient Department edited successfully----------------------")
														
													elif Admin_choice == "2" :
														Pateints_DataBase[patient_ID][1]=input("\nEnter Doctor follouing case : ")
														print("----------------------Doctor follouing case edited successfully----------------------")
										
													elif Admin_choice == "3" :
														Pateints_DataBase[patient_ID][2]=input("\nEnter patient name : ")
														print("----------------------Patient name edited successfully----------------------")
													
													elif Admin_choice == "4" :
														Pateints_DataBase[patient_ID][3]=input("\nEnter patient Age : ")
														print("----------------------Patient age edited successfully----------------------")
												
													elif Admin_choice == "5" :
														Pateints_DataBase[patient_ID][4]=input("\nEnter patient gender : ")
														print("----------------------Patient address gender successfully----------------------")
														
													elif Admin_choice == "6" :
														Pateints_DataBase[patient_ID][5]=input("\nEnter patient address : ")
														print("----------------------Patient address edited successfully----------------------")
														
													elif Admin_choice == "7" :
														Pateints_DataBase[patient_ID][6]=input("\nEnter patient RoomNumber : ")
														print("----------------------Patient RoomNumber edited successfully----------------------")
												
													elif Admin_choice == "B" :
														break
														
													else :
														print("Please Enter a correct choice")
											except :
												print("Patient ID should be an integer number")
																				
								elif Admin_choice == "B" :										#Admin mode --> Pateints Management --> Back
											break
								
								else :
											print("Please enter a correct choice\n")
										elif AdminOptions == "2" :															#Admin mode --> Doctors Management
							print("-----------------------------------------")
							print("|To add new doctor Enter 1              |")
							print("|To display doctor Enter 2              |")
							print("|To delete doctor data Enter 3          |")
							print("|To edit doctor data Enter 4            |")
							print("|To be back enter B                     |")
							print("-----------------------------------------")
							Admin_choice = input ("Enter your choice : ")
							Admin_choice = Admin_choice.upper()
							
							if Admin_choice == "1" : 											#Admin mode --> Doctors Management --> Enter new doctor data
									try :		#To avoid non integer input
										Doctor_ID = int(input("Enter doctor ID : "))
										while Doctor_ID in Doctors_DataBase :			#if Admin entered used ID
											Doctor_ID = int(input("This ID is unavailable, please try another ID : "))
										
										Department=input("Enter Doctor department : ")
										Name      =input("Enter Doctor name       : ")
										Address   =input("Enter Doctor address    : ")
										Doctors_DataBase[Doctor_ID]=[[Department,Name,Address]]
										print("----------------------Doctor added successfully----------------------")
									except :
										print("Doctor ID should be an integer number")
								
							elif Admin_choice == "2" : 											#Admin mode --> Doctors Management --> Display doctor data
									try :		#To avoid non integer input
										Doctor_ID = int(input("Enter doctor ID : "))
										while Doctor_ID not in Doctors_DataBase :
											Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
										print("Doctor name    : ",Doctors_DataBase[Doctor_ID][0][1])
										print("Doctor address : ",Doctors_DataBase[Doctor_ID][0][2])
										print("Doctor is in "+Doctors_DataBase[Doctor_ID][0][0]+" department")
									except :
										print("Doctor ID should be an integer number")
							
							elif Admin_choice == "3" :											#Admin mode --> Doctors Management --> Delete doctor data
									try :		#To avoid non integer input
										Doctor_ID = int(input("Enter doctor ID : "))
										while Doctor_ID not in Doctors_DataBase :
											Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
										Doctors_DataBase.pop(Doctor_ID)
										print("/----------------------Doctor data deleted successfully----------------------/")
									except :
										print("Doctor ID should be an integer number")
											
