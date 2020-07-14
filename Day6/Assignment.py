class Employee:
    
    raise_amount = 100000
    
    def __init__(self, l_name, f_name, salary, sales_data=[]):
        self.last_name = l_name
        self.first_name = f_name
        self.pay = salary
        self.email = f_name+"."+l_name+"@csueastbay.edu"
        self.sales = sales_data
    
    def maxSales(self):
        if len(self.sales) != 0:
            self.max_sales = max(self.sales)
        else:
            self.max_sales = []
            print("No sales record")
        
        
employee1 = Employee("Smith", "john", 2000000, [100,200,400,300]) 
employee2 = Employee("Smith", "john", 2000000)   

employee1.maxSales()

print(employee1.max_sales)
employee2.maxSales()
    

#Continue with the employ class definition from the snippet, please define a function that takes 
#the sales_data from an employee as input (variable numbers of sales_data), calculate the maximum sale, 
#and generate an attribute for this employee called “max_sale”.

#For example, if the employee has three sales: 200,400,300, this method will create an additional attribute
# for this employee called max_sale, and its value is going to be 400.
