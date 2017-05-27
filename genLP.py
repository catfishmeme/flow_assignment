import sys


def print_aux(X,Y,Z):
     aux = ""
     for i in range(1,X+1):
          for k in range(1,Y+1):
               for j in range(1,Z+1):
                    aux += "u{0}{1} + v{1}{2} - x{0}{1}{2} = 0\n".format(i,k,j)
                    
     print(aux,end="")
     
     for k in range(1,Y+1):
          mysum = ""
          for i in range(1,X+1):
               mysum += "+ u{}{} ".format(i,k)
          for j in range(1,Z+1):
               mysum += "- v{}{} ".format(k,j)
               
          mysum += "= 0"
          print(mysum[2:])
     
     
def print_objective_constraints(X,Y,Z):
     for k in range(1,Y+1):
          con = "l - "
          for i in range(1,X+1):
               con += "u{}{} - ".format(i,k)
               
          con = con[:-2] + ">= 0"
          
          print(con)
     
def print_demand(X,Y,Z):
     '''prints demand constraints'''
     demand = ""
     for i in range(1,X+1):
          for j in range(1,Z+1):
               mysum =  ""
               for k in range(1,Y+1):
                    demand += "x{0}{1}{2} - {3}w{0}{1}{2} = 0\n".format(i,k,j,(i+j)/3)
                    mysum += "w{}{}{} + ".format(i,k,j)
                    
                    
               
               mysum = mysum[:-2] + "= "
               
               
               mysum += "3"
               
               
               demand += mysum + "\n"
                         
                
              
     print(demand,end="")
     
     
def print_capp(X,Y,Z):
     capp = ""
     for i in range(1,X+1):
          for k in range(1,Y+1):
               capp += "u{0}{1} - c{0}{1} <= 0\n".format(i,k)
               
               
               
     for k in range(1,Y+1):
          for j in range(1,Z+1):
               capp += "v{0}{1} - d{0}{1} <= 0\n".format(k,j)
               
               
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
               
     nonneg += "0 <= l\n"
     
     print(nonneg,end="")


def main():
     (X,Y,Z) = sys.argv[1:4]
     X = int(X)
     Y = int(Y)
     Z = int(Z)
     
     print("X = {}, Y = {}, Z = {}".format(X,Y,Z))
     print("Minimize")
     print(" l")
     print("Subject to")
     print_aux(X,Y,Z)
     print_objective_constraints(X,Y,Z)
     print_demand(X,Y,Z)
     print_capp(X,Y,Z)
     print("Bounds")
     print_nonneg(X,Y,Z)
     print("Integer")
     print_integer(X,Y,Z)
     print("End")
     
     
     
main()