# bring in randomness cause we need it in our lives
import random

### Begin Dr. Forsyth Code. Do Not Modify ###

# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return vars


# set the maximum length of the list
max_length = 100

# set the maximum upper bound for the list
upper_bound = 1000

# generate a random lists of integers
nums = generate_random_int_list(max_length, upper_bound)

# create two variables to hold the final answers
num_evens = 0
num_odds = 0
### YOUR CODE BEGINS HERE ###

if nums:  # check if the list is not empty
    for i in nums:  # iterate/go through each number in the list to start checking
        if i % 2 == 0:  # check if the number is even by dividing it by 2 and checking if the remainder is 0
            num_evens += 1  # increment the even count
        else: # if the number is not even, meaninging the division by 2 has a remainder, then it is odd
            num_odds += 1  # increment the odd count 

print(f"Number of evens: {num_evens}")  # print the number of even numbers
print(f"Number of odds: {num_odds}")  # print the number of odd numbers