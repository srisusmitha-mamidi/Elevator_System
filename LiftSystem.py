class LiftSystem:
    def __init__(self,lst_of_lifts):
        self.lst_of_lifts=lst_of_lifts   # Current position of the lifts 
        self.lift_movements={i+1:[lst_of_lifts[i]] for i in range(6)}
    def get_nearest_position(self,floor_number):
        nearest=13
        for i in range(len(self.lst_of_lifts)):
            position=abs(floor_number-self.lst_of_lifts[i])
            if position<nearest:
                nearest=min(position,nearest)
                idx=i+1
        if nearest!=0:
            self.lst_of_lifts[idx-1]=floor_number
            self.lift_movements[idx].append(floor_number)
        else:
            print("Lift is already in the same floor :)")
        return idx
    def print(self):     # to print the current position of lifts and lift movements
        print("Current position of lifts", self.lst_of_lifts)
        for i in self.lift_movements:
            print("--- Floor number:",i, "---")
            print("List of floors lift - ",i,"has taken",self.lift_movements[i])
        
        
            
            
        
            
            
            
    