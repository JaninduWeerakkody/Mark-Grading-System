# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code soluton.
# Student ID: 20230797
# Date: 29.11.2023

from graphics import *

#Histogram

def histogram():  
    total_count=progress_count+trailer_count+retriever_count+excluded_count

    win = GraphWin("Histogram", 800, 800)
    win.setBackground("Mint Cream")

    heading = Text(Point(400, 30), 'Histogram results')
    heading.draw(win)
    heading.setTextColor("black")
    heading.setSize(28)
    heading.setStyle("bold")
    heading.setFace("helvetica")

    line1 = Line(Point(50,650), Point(750,650))
    line1.draw(win)

#Creating progress bar
    progress = Rectangle(Point(100,650), Point(240,650-(650*progress_count/total_count)))
    progress.draw(win)
    progress.setFill('Green')
    progress_num= Text(Point(170,640-(650*progress_count/total_count)),progress_count)
    progress_num.draw(win)
    progress_num.setSize(20)
    progress_name= Text(Point(170,670),'Progress')
    progress_name.draw(win)
    progress_name.setSize(20)

#Creating trailer bar
    trailer = Rectangle(Point(250,650), Point(390,650-(650*trailer_count/total_count)))
    trailer.draw(win)
    trailer.setFill('Blue')
    trailer_num= Text(Point(320,640-(650*trailer_count/total_count)),trailer_count)
    trailer_num.draw(win)
    trailer_num.setSize(20)
    trailer_name= Text(Point(320,670),'Trailer')
    trailer_name.draw(win)
    trailer_name.setSize(20)

#Creating retriever bar
    retriever = Rectangle(Point(400,650), Point(540,650-(650*retriever_count/total_count)))
    retriever.draw(win)
    retriever.setFill('Yellow')
    retriever_num= Text(Point(470,640-(650*retriever_count/total_count)),retriever_count)
    retriever_num.draw(win)
    retriever_num.setSize(20)
    retriever_name= Text(Point(470,670),'Retriever')
    retriever_name.draw(win)
    retriever_name.setSize(20)

#Creating excluded bar
    excluded = Rectangle(Point(550,650), Point(690,650-(650*excluded_count/total_count)))
    excluded.draw(win)
    excluded.setFill('Red')
    excluded_num= Text(Point(620,640-(650*excluded_count/total_count)),excluded_count)
    excluded_num.draw(win)
    excluded_num.setSize(20)
    excluded_name= Text(Point(620,670),'Excluded')
    excluded_name.draw(win)
    excluded_name.setSize(20)

    total_outcomes=Text(Point(170,700),str(total_count)+ ' outcomes in total')
    total_outcomes.draw(win)
    total_outcomes.setSize(25)

#Close the window by mouse click
    try:
        win.getMouse()
        win.close()
    except GraphicsError:
        pass

#Validation

progress_count=0
trailer_count=0
retriever_count=0
excluded_count=0
progression_type=0
l=[]

while True:
    while True:
        try:
            pass_credits=int(input('Please enter your credits at pass: '))
            if pass_credits not in {0,20,40,60,80,100,120}:
                print('Out of range')
                continue
        except ValueError:
            print("Integer required ")
        else:
            break

    while True:
        try:
            defer_credits=int(input('Please enter your credits at defer: '))
            if defer_credits not in {0,20,40,60,80,100,120}:
                print('Out of range')
                continue
        except ValueError:
            print("Integer required ")
        else:
            break

    while True:
        try:
            fail_credits=int(input('Please enter your credits at fail: '))
            if fail_credits not in {0,20,40,60,80,100,120}:
                print('Out of range')
                continue
        except ValueError:
            print("Integer required ")
        else:
            break

#Calculate results
    total = pass_credits + defer_credits + fail_credits
    if total==120:
        if pass_credits==120:
            print('Progress')
            progress_count = progress_count + 1
            progression_type='Progress'

        elif pass_credits==100:
            print('Progress (module trailer)')
            trailer_count = trailer_count + 1
            progression_type='Progress (module trailer)'

        elif fail_credits>=80:
            print('Exclude')
            excluded_count = excluded_count + 1
            progression_type='Exclude'
            
        else:
            print('Do not progress – module retriever')
            retriever_count = retriever_count + 1
            progression_type='Do not progress – module retriever'

#Store results and input data in a list
        l.append([progression_type,pass_credits,defer_credits,fail_credits])

#Multiple outcomes
        while True:
            print('Would you like to enter another set of data?')
            print('If you are a student enter q')
            multiple_students = input('Enter "y" for yes or "q" to quit and view results: ')
            if multiple_students!='y' and multiple_students!='q':
                print("wrong input")
                continue
            else:
                break
        if multiple_students == 'y':
            continue
        elif multiple_students == 'q':
            histogram() #call histogram
#part 2:
            print('Part 2: ')
            #show list with results and input data
            for i in range(len(l)):
                print(l[i][0],'-',l[i][1],',',l[i][2],',',l[i][3])
            #f=open('Progress data.txt','w')

#part 3:
            #write data in text file
            f = open('Progress data.txt', 'w')   #if you want to save data with previous data-replace 'w' with 'a'
            for i in range(len(l)):
                f.write(l[i][0]+' - '+str(l[i][1])+', '+str(l[i][2])+', '+str(l[i][3])+"\n")
            f.close()

            #read and print data from text file
            f=open('Progress data.txt','r')
            print("Part 3:")
            print(f.read())
            f.close()

            break       
    else:
        print('Total incorrect')
