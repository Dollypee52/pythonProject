class Custom_Dict(dict):

    def _setitem_(self, key, value):
        return super()._setitem_(self, key, value)

    def _getitem_(self, key):
        return super()._getitem_(key)


my_dictionary = {'name': "Dolapo Tope", 'age': 20}
temp_file = open("my_dictionary.txt", mode="w")
print(my_dictionary, file=temp_file)
print(my_dictionary['age'], file=temp_file)
print(my_dictionary['name'], file=temp_file)
temp_file.close()

