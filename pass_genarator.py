import random
import string
def main():
    
    while True:
        
        try:
            
            lenn = int(input("\nEnter the lenght of pass : (forExit = 0)\n"));
           
            if lenn==0 :
                break
        
            data = string.digits+string.ascii_lowercase+string.ascii_uppercase+string.punctuation
            for x in range(lenn) :
                rand = random.randint(0,len(data)-1)
                print(data[rand],end = "")
        
        except ValueError :
            print("\n Plz Enter Valid number !\n ")
        
        
if __name__ == "__main__":
    main()

