import json

class Variables:
    def __init__(self,variable_name):
        self.path = "D:\Study\Eighth Sem\DWBI\config\config.cfg"
        self.name = variable_name

    def get_variable(self):

        with open(self.path,"r") as file:
            file_content = json.loads(file.read())
            # print(file_content)
            return file_content[self.name]
        
# var = Variables("database")
# database_name = Variables("database").get_variable()


# database_name = Variables("database").get_variable()

# print(database_name)