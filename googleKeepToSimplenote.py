
import json
import pandas
import os

class KeepToSimplenote:
    
    def __init__(self) -> None:
        pass
    
    def _transferTimeToText(self,timestamp):
        result_ms = pandas.to_datetime(timestamp,unit='us')
        return result_ms
    
    def _fileReader(self,filename:str):
        with open(filename) as user_file:
            file_contents = json.load(user_file)
        
        return file_contents
    
    def fileToString(self,filename:str):
        ALL_FILE_STRING = ""
        NEW_LINE = "\n"
        
        fileContextDict = self._fileReader(filename)
        
        the_title = fileContextDict["title"]
        
        try:
            the_text = fileContextDict["textContent"]
        except:
            the_text = "empty"
        time_created = self._transferTimeToText(fileContextDict["createdTimestampUsec"])
        time_edited = self._transferTimeToText(fileContextDict["userEditedTimestampUsec"])
        
        the_note_categories = ""
        
        #print all note categories
        try:
            for i in fileContextDict["labels"]:
                the_note_categories = the_note_categories + i["name"] + ";" 
        except:
            the_note_categories = "nolabels"
            
        ALL_FILE_STRING+=NEW_LINE+"---"
        ALL_FILE_STRING+=NEW_LINE+"notetitle::"+the_title
        ALL_FILE_STRING+=NEW_LINE+"timecreated::"+str(time_created)
        ALL_FILE_STRING+=NEW_LINE+"timeedited::"+str(time_edited)
        ALL_FILE_STRING+=NEW_LINE+"categories::"+the_note_categories
        ALL_FILE_STRING+=NEW_LINE+"---"
        ALL_FILE_STRING+=NEW_LINE
        ALL_FILE_STRING+=NEW_LINE+"##################"
        ALL_FILE_STRING+=NEW_LINE+the_title
        ALL_FILE_STRING+=NEW_LINE+"##################"
        ALL_FILE_STRING+=NEW_LINE
        ALL_FILE_STRING+=NEW_LINE+the_text
        
        return ALL_FILE_STRING,the_title
        
    def noteToFile(self,filename:str):
        filestring1 = self.fileToString(filename)
        
        fileName1 = filestring1[1] + ".txt"
        f = open(fileName1, 'wt', encoding='utf-8')
        f.write(filestring1[0])


def main():
    
    file1 = KeepToSimplenote()
    
    dir_list = os.listdir("keepNotes")
    note_counter = 0
    
    for i in dir_list:
        if i.endswith("json"):
            note_counter = note_counter + 1
            print(i)
            file1.noteToFile("keepNotes/"+i)
    
    # number of notes
    
    #check number of files created vs keepNotes
    newly_created_note_list = os.listdir(".")
    
    #number of created notes
    cr_note_counter = 0
    for i in newly_created_note_list:
        if i.endswith("txt"):
            cr_note_counter = cr_note_counter + 1
    
    # Created notes vs original notes
    print("original_keep_notes:",note_counter)
    print("created_notes:",cr_note_counter)
    print("missing notes",str(note_counter - cr_note_counter))
    
    
if __name__ == "__main__":
    main()