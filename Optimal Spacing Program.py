def main():
    # Let a be the number of counters available
    print("Hello Bro!")
    print("Loading....")
    print("Loaded..... Please Proceed!")
    layout = input("What kind of layout does our counters have? Linear or Circular? ").strip().lower()
    total_counters = int(input("Enter the total number of counters in the bank: "))

    # We'll start the counters from 1 to total counters. We store these counters in a list
    unfilled_counters = list(range(1, total_counters + 1))

    # Firstly, the list of occupied will be empty because no seats have been packed.
    filled_counters = []
    
    # This loop will help us to take care of user-inputs.
    while True:
        next_customer = input("Do we have a next customer? (yes/no): ").strip().lower()
        """
        If we have next customer, we'll call our assign_best_counter function to return the best seat
        Then, we'll add the value returned by assign_best_counter function to filled_counters list
        Also, we'll remove the same value from our unfilled_counters because now it's been taken!
        """

        if next_customer == 'yes':
            next_seat = assign_best_counterc(unfilled_counters, filled_counters, layout)
            print(f"Assign the next customer to seat number {next_seat}.")
            filled_counters.append(next_seat)
            unfilled_counters.remove(next_seat)

        # Now, next part will deal with updating our filled and unfilled list
        # Because when any customer would leave any counter, the counter that was filled is now unfilled
        # Here if all counters are unfilled, we should not ask the question "Any recently emptied seats?"
        # So, I set a condition to check if we even have any filled seats yet!
        if len(filled_counters) != 0:
            seat_change = input("Has any seat been unoccupied recently? (yes/no): ").strip().lower()
            if seat_change == 'yes':
                if filled_counters:
                    invalid_attempts = 0
                    already_vacant_attempts = 0

                    # this code will empty seats
                    while invalid_attempts < 2 and already_vacant_attempts < 3:
                        try:
                            released_seat = int(input("Which seat number was unoccupied? "))
                            if released_seat < 1 or released_seat > total_counters:
                                invalid_attempts += 1
                                print(f"Please enter a valid seat number between 1 and {total_counters}.")
                                if invalid_attempts == 2:
                                    print("Too many invalid attempts. Moving on to the next customer.")
                                    break
                                # what if? so lets prompt for input again without incrementing already_vacant_attempts
                                continue   

                            if released_seat in filled_counters:
                                filled_counters.remove(released_seat)
                                unfilled_counters.append(released_seat)
                                unfilled_counters.sort()  # Keep the list sorted
                                break  
                            else:
                                already_vacant_attempts += 1
                                print("Check again! That place was not occupied at all!")
                        except ValueError:
                            invalid_attempts += 1
                            print("Invalid Input. The seat number is numeric!")

                    if already_vacant_attempts == 3:
                        print("Too many attempts with already vacant seats. Moving on to the next customer.")
                else:
                    print("We don't have any occupied places yet.")

def assign_best_counterc(unfilled_counters, filled_counters, layout):
    if len(filled_counters) == 0:
        # as we have no element in filled list
        # no seats are occupied. so lets return the first unoccupied seat, usually 1.
        return unfilled_counters[0]  

    max_distance = -1
    candidates = []  # List to hold counters with max minimum distance
    num_counters = max(unfilled_counters + filled_counters)

    # we will find all counters with the maximum minimum distance
    for counter in unfilled_counters:
        nearest_distance = float('inf')  # Start with a large number

        # let me find here the minimum distance to any occupied seat
        for oc in filled_counters:
            if layout == "linear":
                distance = abs(counter - oc)
                if distance < nearest_distance:
                    nearest_distance = distance
            else:
                distance = min(abs(counter - oc), num_counters - abs(counter - oc))
                if distance < nearest_distance:
                    nearest_distance = distance

        if nearest_distance > max_distance:
            max_distance = nearest_distance
            candidates = [counter]  
            # Start a new list of candidates. after all they are equally likely.
        elif nearest_distance == max_distance:
            # adding to the list of candidates with same max distances
            candidates.append(counter)  
            

    # What I do now is to choose among candidates based on the number of occupied neighbors
    return best_candidate(filled_counters, candidates)


# there could be case when we have multiple seats with their minimum distance to the 
# nearest occupied seats all equal as maximum? How will we select the best seat then
# we need to check both neighbouring counters or urinals. if one counter has only one neighbour
# and the other counter has two neighbour. the one with only one neighbor will be returned by
# this function. 

def best_candidate(filled_counters, candidates):
    best = None
    best_score = float('inf')  # Inf because we want to declare a variable but do not want it to be the final value as a part of else statement 
    
    for candidate in candidates:
        score = 0
        
        # Check the left and right neighbors
        if candidate - 1 in filled_counters:
            score += 1
        if candidate + 1 in filled_counters:
            score += 1
        
        # Update the best candidate based on the score
        if score < best_score:
            best_score = score
            best = candidate
    
    return best

main()
