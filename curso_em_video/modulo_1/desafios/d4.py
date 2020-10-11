str_a = 'Gleisson Neves'
str_number = '3'
int_a = -3
float_a = 3.14
bool_a  = False

print(type(str_a), type(int_a), type(float_a),type(bool_a))
print('String: "{0}", Int: {1}, float: {2}, boolean: {3}'.format(str_a, int_a, float_a, bool_a))
print("É número: {}, É número: {}, É Letra: {}, Está todo em letra maiúscula: {}, Está com letras maiúscula e minúscula: {}".format(str_number.isnumeric(), str_a.isnumeric(), str_a.isalpha(), str_a.isupper(), str_a.istitle()))
