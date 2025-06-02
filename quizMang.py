import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="quiz_comp")
mycursor = mydb.cursor()
while True:
    choice = int(input("enter your wish:"))
    if choice == 1:
        while True:
            sql = int(input("enter the index_no:"))
            sql1 = input("enter the ques_desc:")
            sql2 = input("enter the option a:")
            sql3 = input("enter the option b:")
            sql4 = input("enter the option c:")
            sql5 = input("enter the option d:")
            sql6 = input("the answer is:")
            sql_in = f"insert into questions111 values({sql},'{sql1}','{sql2}','{sql3}','{sql4}','{sql5}','{sql6}')"
            mycursor.execute(sql_in)
            mydb.commit()
            print("your request has been processed.Thank you for making us as a part of your project")
            select=int(input("1->enter record\n2->exit\enter ur choice"))
            if select==2:
                break
    if choice == 2:
        while True:
            sql6 = int(input("enter the participant reg_no:"))
            sql7 = input("enter the participant name:")
            sql8 = int(input("enter the age group:"))
            sql9 = input("enter the city:")
            sql10 = int(input("enter the no of appearances made:"))
            sql_int = f"insert into participants111 values({sql6},'{sql7}',{sql8},'{sql9}',{sql10})"
            mycursor.execute(sql_int)
            print("participants are all updated")
            mydb.commit()
            x=int(input('enter 1 more\enter 2 exit'))
            if x==2:
                break
    if choice==3:
        while True:
            a=int(input("enter the reg_no"))
            b=input("enter the participants name")
            c=int(input("enter the scores"))
            d=int(input("enter the total correct answer"))
            e=int(input("enter the incorrect answer"))
            f=int(input("enter the no_of_attempted_questions"))
            sql_insert='''insert into scores111 (participant_name, scores, total_correct, total_wrong, total_attempted)
                values (%s,%s,%s,%s,%s)'''
            val=(b,c,d,e,f)
            mycursor.execute(sql_insert,val)
            mydb.commit()
            y=int(input('enter for more 1 enter 2 to exit'))
            if y==2:
                break
    if choice == 4:
        while True:
            table = input("Enter the name of the table you want to display (questions111, participants111, scores111):")
            mycursor.execute(f"SELECT * FROM {table}")
            result = mycursor.fetchall()
            for row in result:
                print(row)
            z=int(input('enter 1 for more enter 2 to exit'))
            if z==2:
                break
