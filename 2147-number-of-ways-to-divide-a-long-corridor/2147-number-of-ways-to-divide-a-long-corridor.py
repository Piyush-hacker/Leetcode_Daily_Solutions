class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # iterate through the list 
        # keep track of how many seats there are 
        # keep track of the flexibility of the barrier placement 
        # keep a running total of options 
        # return that total if there were enough seats 

        current_total = 1
        num_of_seats = 0 

        current_seats = 0 
        current_streak = 0 

        for i in range(len(corridor)): 

            if corridor[i] == "S": 
                num_of_seats += 1 

                if current_seats == 2: # start a new streak 
                    current_total *= current_streak + 1 
                    current_seats = 0
                    current_streak = 0

                current_seats += 1 

            # corridor[i] == "P" and current seats == 2
            elif current_seats == 2: 
                current_streak += 1

        # returns answer modulo 10^9 + 7
        if num_of_seats != 0 and num_of_seats % 2 == 0: 
            return current_total % (10 ** 9 + 7)
        return 0 
        

            