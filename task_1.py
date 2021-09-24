def transcribe(seq, i):
    if 'U' in seq or 'u' in seq:
        print('It is uracil in the sequence. Invalid alphabet, try again!')
        i = 1
        return seq, i
    seq = seq.replace('T', 'U')
    seq = seq.replace('t', 'u')
    i = 0
    return seq, i 
    
def complement():
    print(seq)

def reverse():
    print(seq)
    
def reverse_complement():
    print(seq)

def seq_check(seq, i):
    
    return i
    
func_dict = {"transcribe": transcribe, "complement": complement, "reverse": reverse, "reverse complement": reverse_complement}

while 1:
    com = input("Enter command: ")
    if com == "exit":
        print("Good bye")
        break
    i = 1
    if com in func_dict:
        while i:
            seq = input("Enter sequence: ")
            i = seq_check(seq, i)
            seq, i = func_dict[com](seq, i)
        print(seq)
    else:
        print("Unknown command. Try again or print 'exit'.")