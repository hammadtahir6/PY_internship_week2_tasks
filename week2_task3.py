#declare dif variable

string_variable= '1234'
int_variable = 789
float_variabl = 50.0
bool_var = True
complex_variable = 10 + 5j

#print org value and its type
print("_____original values and data types________")
print(f"string_variable: {string_variable} | type {type(string_variable)}")
print(f"int_variable: {int_variable} | type : {type(int_variable)}")
print(f"Float_variable: {float_variabl} | type: {type(float_variabl)}")
print(f"Bool_variable: {bool_var} | type: {type(bool_var)}")
print(f"Complex_variable: {bool_var} | type: {type(bool_var)}")
print("--------------------------------------------------------------------")

#conversion of variables to different types
#string to int
try:
    converted_string_variable = int(string_variable)
    print(f"string variable is converted to int: {converted_string_variable} | Type: {type(converted_string_variable)}")
except ValueError:
    print("this conversion is not possible")

#int to float 
converted_int = float(int_variable)
print(f"int is converted to float: {converted_int} | type: {type(converted_int)}")

#float to string
converted_float = str(float_variabl)
print(f"float is converted to string: {converted_float} | type: {type(converted_float)}")

#bool to int 
converted_bool = int(bool_var)
print(f"bool in converted to int: {converted_bool} | Type: {type(converted_bool)}")

#complex to string
converted_complex = str(complex_variable)
print(f"complex var is conveted to string: {converted_complex} | type: {type(converted_complex)}")