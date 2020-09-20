from os import path, chdir, mkdir

class SaveData():

    def __init__(self, file_name):
        self.target_file = file_name

        self.str_data = []
        self.bool_data = []
        self.int_data = []
        self.float_data = []

        self.str_len = 0
        self.bool_len = 0
        self.int_len = 0
        self.float_len = 0

    def fill_data(self, target):
        pass

    def get_data_list(self):
        return [self.str_data, self.bool_data, self.int_data, self.float_data]

class Data:

    def __init__(self, project_path=path.dirname(__file__)):
        self.home_dir = project_path
        self.data_dir = None
        self.bmap_dir = None
        self.font_dir = None
        self.save_dir = None

        self.save_slots = []
        self.current_slot = 0

        self.generate_directory()

    def generate_directory(self):
        try:
            # Creates folder named 'data' and registers the path in memory
            mkdir(path.join(self.home_dir, 'data'))
            self.data_dir = path.join(self.home_dir, 'data')

            # Creates folders inside 'data' and registers the path in memory
            mkdir(path.join(self.data_dir, 'bmap'))
            self.bmap_dir = path.join(self.data_dir, 'bmap')

            mkdir(path.join(self.data_dir, 'font'))
            self.font_dir = path.join(self.data_dir, 'font')

            mkdir(path.join(self.data_dir, 'save'))
            self.save_dir = path.join(self.data_dir, 'save')
        
        except FileExistsError:
            
            # If both Folders exist, the paths are registered in memory
            self.data_dir = path.join(self.home_dir, 'data')
            self.save_dir = path.join(self.data_dir, 'save')
            self.bmap_dir = path.join(self.data_dir, 'bmap')
            self.font_dir = path.join(self.data_dir, 'font')

    def get_dir(self, d):
        self.data_dir = path.join(self.home_dir, 'data')
        self.save_dir = path.join(self.data_dir, 'save')
        self.font_dir = path.join(self.data_dir, 'font')
        self.font_dir = path.join(self.data_dir, 'bmap')
        
        if d == "bmap":
            return self.bmap_dir

        if d == "font":
            return self.font_dir

    def add_slot(self, save):
        self.save_slots.append(save)

    def name_slot(self, index, name):
        self.save_slots[index] = name

    def save(self, target):
        chdir(self.save_dir)
        with open(path.join(self.save_slots[self.current_slot], target.save_data.target_file), 'w') as f:
            for t in target.save_data.get_data_list():
                for data in target.save_data.t:
                    f.write(str(target))
                    f.write("\n")
            f.close()
        chdir(self.home_dir)

    def load(self, target):
        chdir(self.save_dir)
        with open(path.join(self.save_slots[self.current_slot], target.save_data.target_file), 'r') as f:
            for data in target.str_data:
                target.save_data.str_data = str(f.readline().strip())
            for data in target.bool_data:
                target.save_data.bool_data = bool(f.readline().strip())
            for data in target.int_data:
                target.save_data.int_data = int(f.readline().strip())
            for data in target.float_data:
                target.save_data.float_data = float(f.readline().strip())
            f.close()
        chdir(self.home_dir)
