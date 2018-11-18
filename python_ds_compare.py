import time
import uuid

"Initialize the attributes"

list_values = list()
set_values  = set()

"Setting up the total records on list and set"
TOTAL_ITERATION = 1000000

def main():

    """Creating for loop and storing all unique records in list
    Using uuid module to create a unique key - time based"""
    print("List and Set Compare started....")
    start_time = time.time()
    for i in range(TOTAL_ITERATION):
        uuid_str = str(uuid.uuid4())
        list_values.append(uuid_str)
    end_time = time.time()
    print("Total Time Taken to Store records in list: {}".format(end_time - start_time))

    "Creating for loop and storing all unique records in set"
    "Using uuid module to create a unique key - time based"
    start_time = time.time()
    for i in range(TOTAL_ITERATION):
        uuid_str = str(uuid.uuid4())
        set_values.add(uuid_str)
    end_time = time.time()
    print("Total Time Taken to Store records in set: {}".format(end_time - start_time))

    "Adding one value to find it"
    list_values.append("findme")
    set_values.add("findme")

    print("Total number of records on list:{}".format(len(list_values)))
    print("Total number of records on set:{}".format(len(set_values)))

    "Finding in List"
    start_time = time.time()
    print("findme" in list_values)
    end_time = time.time()
    print("Total Time taken to find one value in list:{}".format(end_time - start_time))

    "Finding in Set"
    start_time = time.time()
    print("findme" in set_values)
    end_time = time.time()
    print("Total Time taken to find one value in set:{}".format(end_time - start_time))

"Main bulitin variable"
if __name__ == '__main__':
    main()


