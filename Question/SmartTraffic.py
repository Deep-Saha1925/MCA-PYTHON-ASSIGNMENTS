emergency = input("Is there an emergency vehicle nearby?(yes/no): ")
pedestrians = input("Are pedestials currenly crossing?(yes/no): ")
traffic_green = input("Is the traffic light green?(yes/no): ")
heavy_rail = input("Is it raining heavily?(yes/no): ")
accident = input("Is there an accident reported ahead?(yes/no): ")
school = input("Is this a school zone?(yes/no): ")
rush_hour = input("Is it rush hour?(yes/no): ")

if emergency == "yes":
    print("All traffic stop, emergency vehicle ahead!!")

elif pedestrians == "yes" and traffic_green == "yes":
    print("All traffic stop, pedestrians ahead!!")

elif accident == "yes":
    print("Caution: Accident Ahead. Proceed Slowly.")

elif heavy_rail == "yes" and traffic_green == "no":
    print("Wait for Green Visibility Low.")
    
elif heavy_rail == "yes" and traffic_green == "yes":
    print("Proceed Slowly Wet Roads.")

elif school == "yes" and rush_hour == "yes":
    print("ExtraCaution: School Zone during Rush Hour.")
    
elif school == "yes":
    print("Drive Carefully - School Zone.")
    
elif traffic_green == "yes":
    print("you may go")
    
else:
    print("Stop and wait for green")