# Note : 1. lst_of_lifts is used for tracking the current location of the lifts and indices as lift numbers.
#        2. lift_movements is used for tracking all the movements of the lift as a list with respect to lift number.
from LiftSystem import LiftSystem
def main():
    lifts=[3,'G',6,12,10,11]
    for i in range(len(lifts)):
        if lifts[i]=='G':
            lifts[i]=0
    ls=LiftSystem(lst_of_lifts=lifts)
    while True:
        print("-"*50)
        s=input("Enter your floor number:")
        if s=='G':
            s=0
        elif not s.isnumeric(): # If there is an option for entering invalid string literal except 'G'
            print("Invalid !!!")  # Can break if its invalid string
            print("Please enter a valid floor number")
            continue
        s=int(s)
        if s>=0 and s<=12:
            nearest_lift_no=ls.get_nearest_position(s)
            print("Nearest lift number is:", nearest_lift_no)
            #ls.print()    # to print the lift movements and track the current lift position
        else:
            print("Please enter Valid number between 'G' to 12")  # Can break if its invalid number/floor
        exit=input("Do you want to exit y/n? ")
        if exit.lower()=='y':
            print("-----Exiting-----")
            break

if __name__=='__main__':
    main()
            
        
        
            
            
    