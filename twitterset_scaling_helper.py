import os
import bz2
import pickle 
import generate_dataset
from zipfile import ZipFile


# // joakim test code

s = generate_dataset

s

# // add support for uncompressed vs compressed

class DatasetScalingHelper():

    directory_out = None
    directory_in = None

    verbosity = False
    fn_format = "YYMMDD-HH_MM_SS--YYMMDD-HH_MM_SS.zip" # // AA: Deprecated
    format_fn_sep = "--" # // AA: Goes between time range (for file names)
    format_suffix_zip = ".zip"


    def __init__(self, _verbosity = True):
        self.verbosity = _verbosity


    def check_failsafe(self):
        if self.directory_in is None: self.print_warn("no input dir, aborting"); return False
        if self.directory_out is None: self.print_warn("no output dir, aborting"); return False

        return True


    def print_progress(self, _msg):
        print(f"progress: {_msg}") if self.verbosity else ...


    def print_warn(self, _msg):
        print(f"warn: {_msg}") if self.verbosity else ...


    def set_dir_output(self, _path):
   #     if not os.path.isdir(_path): self.print_warn("output dir: None. aborting"); return
   #     if _path[-1] is not "/": _path += "/"
        self.directory_out = _path


    def set_dir_input(self, _path):
   #     if not os.path.isdir(_path): self.print_warn("input dir: None. aborting"); return
   #    if _path[-1] is not "/": _path += "/"
        self.directory_in = _path


    def get_filenames_inin_dir(self):
        file_names = [item[2] for item in os.walk(self.directory_in)]
        undesirables = [".DS_Store"] # // might show up in certain OS. OSX is currently supported
        for x in undesirables:
            try:
                file_names[0].remove(x)
            except:
                pass  
        return file_names[0]


    def get_file_content(self, _file_name, _is_compressed=True):
        # // implement _is_compressed option (for non compressed alternatives)
        unzipped = bz2.BZ2File(_file_name).read()
        non_binary = pickle.loads(unzipped)
        return non_binary 


    def sort_tweetset_chronologically(self, _tweet_list):
        _tweet_list.sort(key=lambda tweet: tweet.created_at, reverse=False)
        self.print_progress("sorted tweet list")


    def reformat_tweet_datetime(self, _tweet):      
        dt_string = str(_tweet.created_at)
        dt_string = dt_string = dt_string[2:]
        dt_string = dt_string.replace("-", "")
        dt_string = dt_string.replace(" ", "-")
        dt_string = dt_string.replace(":", "_")
        return dt_string


    def save_data(self, _content, _path, _compression_enabled):
        if _compression_enabled:
            sfile = bz2.BZ2File(f"{_path}{self.format_suffix_zip}", 'w')
            pickle.dump(_content, sfile)
            sfile.close()
            self.print_progress(f"saved content to: {_path}{self.format_suffix_zip}")
        else:
            pickle_out = open(_path, "wb")
            pickle.dump(_content, pickle_out)
            pickle_out.close()
            self.print_progress(f"saved content to: {_path}")


    def merge_datasets_by_directory(self, _sortby_tweet_time=True):
        if not self.check_failsafe(): return
        # // AA: Might need another failsafe for invalid files?

        file_names = self.get_filenames_inin_dir()
        cache = []
        for name in file_names: cache.extend(self.get_file_content(f"{self.directory_in}{name}"))
        self.sort_tweetset_chronologically(cache)

        new_file_path = ""
        if _sortby_tweet_time:
            filename_start = self.reformat_tweet_datetime(cache[0])
            filename_end = self.reformat_tweet_datetime(cache[-1])
            new_file_path = f"{self.directory_out}{filename_start}{self.format_fn_sep}{filename_end}"
        else:
            # // AA: creates new filename by old filenames, not the same as time attached to tweets.
            filename_start = file_names[0].split(self.format_fn_sep)[0]
            filename_end = file_names[-1].split(self.format_fn_sep)[1]
            new_file_path = f"{self.directory_out}{filename_start}{self.format_fn_sep}{filename_end}", "csv"
            if self.format_suffix_zip in new_file_path:
                new_file_path = new_file_path.split(self.format_suffix_zip)[0]

        self.save_data(cache, new_file_path, True)


    def merge_datasets_by_time_range(self):
        pass


    # only filename support is by tweet time
    def split_dataset_by_obj_count(self, _divider):
        if not self.check_failsafe(): return

        file_names = self.get_filenames_inin_dir()
        # // AA: rethink, probably a hack
        if len(file_names) > 1: self.print_warn("trying to split several files. not allowed"); return
        if len(file_names) == 0: self.print_warn("trying to split zero files. not allowed"); return

        cache_continious = []
        for name in file_names: 
            cache_continious.extend(self.get_file_content(f"{self.directory_in}{name}"))
        self.sort_tweetset_chronologically(cache_continious)

        cache_split = []
        cache_split_current_portion = []
        cache_split_portion_size = int(len(cache_continious) / _divider)
        while len(cache_continious) > 0:
            cache_split_current_portion.append(cache_continious.pop(0))
            if len(cache_split_current_portion) >= cache_split_portion_size:
                copy = cache_split_current_portion.copy()
                cache_split.append(copy)
                cache_split_current_portion.clear()
            
        # // AA: resolution for uneven division: weak hack. Not spreading out evenly 
        # //        because that would shuffle timestamps
        if len(cache_split_current_portion) > 0:
            cache_split[-1].extend(cache_split_current_portion)

        for chunk in cache_split:
            filename_start = self.reformat_tweet_datetime(chunk[0])
            filename_end = self.reformat_tweet_datetime(chunk[-1])
            new_file_path = f"{self.directory_out}{filename_start}{self.format_fn_sep}{filename_end}"
            self.save_data(chunk, new_file_path, True)
        

    def split_datasets_by_time_range(self):
        pass


    

s = DatasetScalingHelper()
s.set_dir_input("../DataCollection/DC/")
s.set_dir_output("../DataCollection/DCMERGE/")
s.merge_datasets_by_directory(True)


# import zipfile
# from os import listdir
# from os.path import isfile, join
# directory = "../DataCollection/DCMERGE/"
# onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
# for o in onlyfiles:
#     if o.endswith(".zip"):
#         zip = zipfile.ZipFile(o, 'r')
#         zip.extractall(directory)
#         zip.close()            


#### // ZIPFILE


# dir_name = 'C:/Users/Joakim/Desktop/SkoleTing/Studio/Datacollection/DCMERGE'
# extension = ".zip"


# os.chdir(dir_name)                              # // change directory from working dir to dir with files

# for item in os.listdir(dir_name):               # // loop through items in dir
#     if item.endswith(extension):                # // check for ".zip" extension
#         file_name = os.path.abspath(item)       # // get full path of files
#         print("print", file_name)               # // print file name for dev sake
#         zip_ref = zipfile.ZipFile(file_name)    # // create zipfile object
#         zip_ref.extractall(dir_name)            # // extract file to dir
#         zip_ref.close()                         # // close file
#         os.remove(file_name)                    # // delete zipped file
# #file_name = dir_name + "/" + item



        
### // Check dir
# file_names = s.get_filenames_inin_dir()
# for x in file_names:
#    print(file_names)

#s.set_dir_input("../TestFolder_mergedFromDataColl")
#s.set_dir_output("../TestFolder2_splitFromTestFolder")
# s.split_dataset_by_obj_count(6)




print('terminating')