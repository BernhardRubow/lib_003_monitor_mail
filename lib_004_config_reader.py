import os, json

### classes #######################################################################################

class nvp_config_reader:

    @staticmethod
    def get_local_path(folder):
        current_path = os.path.dirname(os.path.abspath(__file__))
        desired_path = current_path + "//" + folder
        return desired_path


    @staticmethod
    def read_config_file(filename):
        """
        Reads and converts the json configurationfile to
        a accessible dictionary
        """
        filename = nvp_config_reader.get_local_path(filename)
        with open(filename) as fh:
            config_data = json.load(fh)
        return config_data