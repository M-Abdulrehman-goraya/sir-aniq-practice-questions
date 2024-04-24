# class Phonebook:
#     def __init__(self):
#         self.record = {}
#     def insert(self,name,number):
#         self.record[name] = number
#     def showcontact(self):
#         for name , number in self.record.items():
#             print(f"Name : {name} : Number : {number}")
#     def searchcontact(self,name):
#         if name in self.record:
#             print(f"{name} found with contact number {self.record[name]}")
#     def del_contact(self,name):
#         if name in self.record:
#             del self.record[name]
# person = Phonebook()
# person.insert("Ali",3221676)
# person.insert("Kasim",3789322)
# person.showcontact()
# person.searchcontact("Ali")
# person.del_contact("Kasim")
# person.showcontact()
# class BaseSalary:
#     def __init__(self):
#         self.base_salary = 10000
#     def get_salary(self):
#         return self.base_salary
# class Science(BaseSalary):
#     def __init__(self):
#         super().__init__()
#         self.science = 3000
#     def salary(self):
#         return super().get_salary()+self.science
# class Maths(Science):
#     def __init__(self):
#         super().__init__()
#         self.maths = 3000
#     def salary(self):
#         return super().salary()+self.maths
# class Phy(Science):
#     def __init__(self):
#         super().__init__()
#         self.phy = 2000
#     def salary(self):
#         return super().salary()+self.phy
# t1 = Science()
# print(t1.salary())
# t2 = Maths()
# print(t2.salary())
# t3 = Phy()
# print(t3.salary())
# class Player:
#     def __init__(self,name,age,blood,city,country):
#         self.name = name
#         self.age = age
#         self.blood = blood
#         self.city = city
#         self.country = country
#     def show_details(self):
#         print(self.name,self.age,self.blood,self.city,self.country)
# class Batsman(Player):
#     def __init__(self, name, age, blood, city, country,totalRuns,battingStance):
#         super().__init__(name, age, blood, city, country)
#         self.totalRuns = totalRuns
#         self.battingStance = battingStance
#     def show_details(self):
#         return super().show_details() , self.totalRuns , self.battingStance
# class Bowler(Player):
#     def __init__(self, name, age, blood, city, country,totalWickets,bowlingArm):
#         super().__init__(name, age, blood, city, country)
#         self.totalWickets = totalWickets
#         self.bowlingArm = bowlingArm
#     def show_details(self):
#         return super().show_details() , self.totalWickets , self.bowlingArm
# class Allrounder(Batsman,Bowler):
#     # def __init__(self, name, age, blood, city, country, totalRuns, battingStance,totalWickets,bowlingArm):
#     #     Batsman.__init__(self,name, age, blood, city, country, totalRuns,battingStance)
#     #     Bowler.__init__(self,name, age, blood, city, country,totalWickets,bowlingArm)
#     def __init__(self, name, age, blood, city, country, totalRuns, battingStance, totalWickets, bowlingArm):
#         Batsman.__init__(self, name, age, blood, city, country, totalRuns, battingStance)
#         Bowler.__init__(self, name, age, blood, city, country, totalWickets, bowlingArm)

#     def show_details(self):
#         return super(Batsman).show_details() ,super(Bowler).show_details()
# player = Allrounder("Virat",34,"DK","Delhi","India","103432","Right Hand batter",33,"Right")
# player.show_details()
# class Player:
#     def __init__(self, name, age, blood_group, city, country):
#         self.name = name
#         self.age = age
#         self.blood_group = blood_group
#         self.city = city
#         self.country = country

# class Batsman(Player):
#     def __init__(self, name, age, blood_group, city, country, total_runs, batting_stance):
#         super().__init__(name, age, blood_group, city, country)
#         self.total_runs = total_runs
#         self.batting_stance = batting_stance

# class Bowler(Player):
#     def __init__(self, name, age, blood_group, city, country, total_wickets, bowling_arm):
#         super().__init__(name, age, blood_group, city, country)
#         self.total_wickets = total_wickets
#         self.bowling_arm = bowling_arm

# class Allrounder(Batsman, Bowler):
#     def __init__(self, name, age, blood_group, city, country, total_runs, batting_stance, total_wickets, bowling_arm):
#         Batsman.__init__(self, name, age, blood_group, city, country, total_runs, batting_stance)
#         Bowler.__init__(self, name, age, blood_group, city, country, total_wickets, bowling_arm)

# # Creating objects with appropriate values
# batsman1 = Batsman("Sachin", 48, "O+", "Mumbai", "India", 18426, "Right-handed")
# batsman2 = Batsman("Virat", 34, "A+", "Delhi", "India", 12169, "Right-handed")
# bowler1 = Bowler("Wasim", 50, "AB-", "Lahore", "Pakistan", 916, "Left-arm fast")
# allrounder1 = Allrounder("Shakib", 34, "B+", "Magura", "Bangladesh", 5000, "Left-handed", 300, "Left-arm spin")
# class MatrixMultiplier:
#     def __init__(self):
#         self.matrix_A = []
#         self.matrix_B = []
#         self.matrix_C = []

#     def get_matrix_size(self, matrix_name):
#         rows = int(input(f"Enter the number of rows for matrix {matrix_name}: "))
#         cols = int(input(f"Enter the number of columns for matrix {matrix_name}: "))
#         return rows, cols

#     def input_matrix_values(self, matrix, rows, cols):
#         print(f"Enter values for matrix ({rows}x{cols}):")
#         for i in range(rows):
#             row = []
#             for j in range(cols):
#                 value = int(input(f"Enter value for position ({i+1},{j+1}): "))
#                 row.append(value)
#             matrix.append(row)

#     def validate_matrices(self):
#         while True:
#             rows_A, cols_A = self.get_matrix_size('A')
#             rows_B, cols_B = self.get_matrix_size('B')

#             if cols_A != rows_B:
#                 print("Matrix multiplication rule violation! Column count of matrix A should be equal to row count of matrix B.")
#                 print("Please enter the sizes again.")
#             else:
#                 return rows_A, cols_A, cols_B

#     def multiply_matrices(self):
#         rows_A, cols_A, cols_B = self.validate_matrices()

#         self.input_matrix_values(self.matrix_A, rows_A, cols_A)
#         self.input_matrix_values(self.matrix_B, cols_A, cols_B)

#         # Initialize result matrix with zeros
#         self.matrix_C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

#         # Perform matrix multiplication
#         for i in range(rows_A):
#             for j in range(cols_B):
#                 for k in range(cols_A):
#                     self.matrix_C[i][j] += self.matrix_A[i][k] * self.matrix_B[k][j]

#     def display_result(self):
#         print("Matrix A:")
#         self.display_matrix(self.matrix_A)
#         print("Matrix B:")
#         self.display_matrix(self.matrix_B)
#         print("Product of Matrix A and Matrix B:")
#         self.display_matrix(self.matrix_C)

#     @staticmethod
#     def display_matrix(matrix):
#         for row in matrix:
#             print(row)


# # Example usage:
# matrix_multiplier = MatrixMultiplier()
# matrix_multiplier.multiply_matrices()
# # matrix_multiplier.display_result()
# class Matrix1:
#     def __init__(self,rows,coloums):
#         self.rows = rows
#         self.coloums = coloums     
#     def matrix_creation(self):
#         matrix1 = []
#         for i in range(self.rows):
#             row = []
#             for j in range(self.coloums):
#                 value = input(f"Enter value for ({i+1},{j+1})")
#                 row.append(value)
#             matrix1.append(row)
# class Matrix2:
#     def __init__(self,rows,coloums):
#         self.rows = rows
#         self.coloums = coloums     
#     def matrix_creation(self):
#         matrix2 = []
#         for i in range(self.rows):
#             row = []
#             for j in range(self.coloums):
#                 value = input(f"Enter value for ({i+1},{j+1})")
#                 row.append(value)
#             matrix2.append(row)
# rows_A = 3 
# cols_B = 3
# result_matrix = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
# print(result_matrix)