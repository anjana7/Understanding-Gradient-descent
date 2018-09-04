x = [1,2,3,4,5,6,7,8,9]
y = [3,5,7,9,11,13,15,17,19]

a = 1
b = 2

epoch = 1000
thres = 0.001

for j in range(epoch):
    
    sum_a = 0
    sum_b = 0
    
    error = 0
    
    for i in range(len(x)):
        y_pred = a*x[i] + b
        err_a = (y_pred-y[i])*x[i]
        err_b = (y_pred-y[i])
        
        sum_a = sum_a + err_a
        sum_b = sum_b + err_b
        
        error = error + (y_pred-y[i])*(y_pred-y[i])
        #print("err_a : ",err_a," err_b : ",err_b,"\n")
        
    a_next = a - 0.003 * sum_a
    b_next = b - 0.003 * sum_b
        
    a = a_next
    b = b_next
        
    print("a : ",a," b : ",b,"\n")
    print("##########################\n")
          
    if(error/len(x) < thres):
        j = epoch



