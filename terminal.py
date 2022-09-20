def num_terminal(terminal,soma=0):
    if terminal==0:
        return soma
    else:
        return num_terminal(terminal-1,soma+terminal)      


def fatorial(n=4):
    if n==0:
        return 1
    else:
        return fatorial(n-1)*n  

if __name__ == "__main__":
    print(num_terminal(4))
    print(num_terminal(10))
    #print(num_terminal(8))
    #print(num_terminal(16))
    #print(fatorial())