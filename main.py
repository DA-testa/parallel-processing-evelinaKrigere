# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    beigu_t=[0]*n
    for i in range(m):
        min_t=min(beigu_t)
        threads_sk=beigu_t.index(min_t)
        output.append((threads_sk,min_t))

        beigu_t[threads_sk]+=data[i]

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    #n = 0
    #m = 0
    ievade=input()
    if "I"in ievade:
        n, m = map(int, input().split())
        data = list(map(int, input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for threads_sk, sakuma_t in result:
            print(threads_sk, sakuma_t)



if __name__ == "__main__":
    main()
