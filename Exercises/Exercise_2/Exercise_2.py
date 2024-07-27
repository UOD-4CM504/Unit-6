import random


def rand_num_list_gen(num=100, lower=1, upper=50):
    rand_num_list = [random.randint(lower, upper) for _ in range(num)]
    return rand_num_list


def main():
    rand_num_list = rand_num_list_gen()
    dist = [0, 0, 0, 0, 0]
    lower = [1, 11, 21, 31, 41]
    upper = [10, 20, 30, 40, 50]

    for num in rand_num_list:
        if num < upper[0] + 1:
            dist[0] += 1
        elif num < upper[1] + 1:
            dist[1] += 1
        elif num < upper[2] + 1:
            dist[2] += 1
        elif num < upper[3] + 1:
            dist[3] += 1
        elif num < upper[4] + 1:
            dist[4] += 1


    for l, u, d in zip(lower, upper, dist):
        print(f"{l}..{u}: {d}")


def advanced_main():
    num_to_gen = input("Please enter the number of integers to generate from the range:\n")
    ranges = input("\nPlease enter the ranges in the following format: e.g. 1..10,11..20,21..30,31..40,41..50\n")
    ranges_list = ranges.split(",")
    rand_num_list = rand_num_list_gen(num=int(num_to_gen))
    lower = [int(s.split("..")[0]) for s in ranges_list]
    upper = [int(s.split("..")[1]) for s in ranges_list]
    dist = [0 for x in range(len(lower))]

    for num in rand_num_list:
        for i in range(len(lower)):
            if num > lower[i] - 1 and num < upper[i] + 1:
                dist[i] += 1

    print("\nThe count in the given ranges is:")
    for l, u, d in zip(lower, upper, dist):
        print(f"{l}..{u}: {d}")


if __name__ == "__main__":
    # main()
    advanced_main()