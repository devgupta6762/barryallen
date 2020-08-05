command=""
while command!="quit":
    command=input("> ")
    if command =="start":
        print('Car is started')
    elif command =="stop":
        print('Car is stopped')
    elif command =="help":
        print('''
        start- To start the car
        stop- To stop the car
        quit- To terminate the loop
        
        ''')
    elif command=="quit":
             break
    else:
        print('Sorry not acceptable')