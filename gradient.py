x = [1,2,3,4]
y = [3,5,7,9]

a = 1
b = 2

for j in range(5):
    
    sum_a = 0
    sum_b = 0
    
    for i in range(4):
        y_pred = a*x[i] + b
        #err_a = 2*(y_pred-y[i])*x[i]
        #err_b = 2*(y_pred-y[i])
        
        err_a = (y_pred-y[i])*(y_pred-y[i])*x[i]
        err_b = (y_pred-y[i])*(y_pred-y[i])
        
        sum_a = sum_a + err_a
        sum_b = sum_b + err_b
        print("err_a : ",err_a," err_b : ",err_b,"\n")
        
    a_next = a - 0.2 * sum_a
    b_next = b - 0.2 * sum_b
        
    a = a_next
    b = b_next
        
    print("a : ",a," b : ",b,"\n")
    print("##########################\n")


