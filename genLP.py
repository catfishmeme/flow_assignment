import sys


def print_aux(X,Y,Z):
     aux = ""
     for i in range(1,X+1):
          for k in range(1,Y+1):
               for j in range(1,Z+1):
                    aux += "u{0}{1} + v{1}{2} - x{0}{1}{2} = 0\n".format(i,k,j)
                    
     print(aux,end="")
     
     
def print_demand(X,Y,Z):
     '''prints demand constraints'''
     demand = ""
     for i in range(1,X+1):
          for j in range(1,Z+1):
               mysum1 = mysum2 = mysum3 = ""
               for k in range(1,Y+1):
                    mysum1 += "w{}{}{} +".format(i,k,j)
                    mysum2 += "w{0}{1}{2} x{0}{1}{2} +".format(i,k,j)
                    mysum3 += "x{}{}{} +".format(i,k,j)
                    
               
               mysum1 = mysum1[:-1] + "= "
               mysum2 = mysum2[:-1] + "= "
               mysum3 = mysum3[:-1] + "= "
               
               mysum1 += "3"
               mysum2 += str(i + j)
               mysum3 += str(i + j)
               
               demand += mysum1 + "\n" + mysum2 + "\n" + mysum3+ "\n"
                         
                
              
     print(demand,end="")
     
     
def print_capp(X,Y,Z):
     capp = ""
     for i in range(1,X+1):
          for k in range(1,Y+1):
               capp += "u{0}{1} - c{0}{1} <= 0\n".format(i,k)
               capp += "u{0}{1} - c{0}{1} r <= 0\n".format(i,k)
               
               
     for k in range(1,Y+1):
          for j in range(1,Z+1):
               capp += "v{0}{1} - d{0}{1} <= 0\n".format(k,j)
               capp += "v{0}{1} - d{0}{1} r <= 0\n".format(k,j)
               
     print(capp,end="")
     
     
def print_integer(X,Y,Z):
     integer = ""
     for i in range(1,X+1):
          for k in range(1,Y+1):
               for j in range(1,Z+1):
                    integer += "w{}{}{}\n".format(i,k,j)
     print(integer,end="")
     
def print_nonneg(X,Y,Z):
     nonneg = ""
     for i in range(1,X+1):
          for k in range(1,Y+1):
               nonneg += "0 <= u{}{}\n".format(i,k)
               for j in range(1,Z+1):
                    
                    nonneg += "0 <= x{}{}{}\n".format(i,k,j)
                    
     for k in range(1,Y+1):
          for j in range(1,Z+1):
               nonneg += "0 <= v{}{}\n".format(k,j)
               
     nonneg += "0 <= r\n"
     
     print(nonneg,end="")


def main():
     (X,Y,Z) = sys.argv[1:4]
     X = int(X)
     Y = int(Y)
     Z = int(Z)
     
     print("X = {}, Y = {}, Z = {}".format(X,Y,Z))
     print("Minimize")
     print(" r")
     print("Subject to")
     print_aux(X,Y,Z)
     print_demand(X,Y,Z)
     print_capp(X,Y,Z)
     print("Bounds")
     print_nonneg(X,Y,Z)
     print("Integer")
     print_integer(X,Y,Z)
     print("End")
     
     
     
main()