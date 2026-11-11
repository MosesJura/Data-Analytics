#  Calculate the tip amount on a restaurant bill given the tip percentage
# Bill is $ 100

Bill = 100
tax = 0.2 # 20%
Tips = 0.15 # 15% 

tax = Bill * tax
Tips = Bill * Tips

 #Displayed output 

print(f'The tip on a ${Tips:.2f} restaurant bill is ${Bill:.2f}')