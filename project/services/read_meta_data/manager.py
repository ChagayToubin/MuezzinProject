from project.services.read_meta_data.read_file import ReadFile
class Manager:
    def __init__(self,KAFKA_URI,path_file):
        self.meta_data=ReadFile()
        self.path_file=path_file
    def app(self):
        self.meta_data.read_meta_data(self.path_file)

