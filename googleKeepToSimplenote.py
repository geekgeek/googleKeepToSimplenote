
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
                the_note_categories = the_note_categories + i["name"] + ":::" 
        except:
            the_note_categories = "nolabels"
            
        ALL_FILE_STRING+=NEW_LINE+"##########"
        ALL_FILE_STRING+=NEW_LINE+the_title
        ALL_FILE_STRING+=NEW_LINE+"##########"
        ALL_FILE_STRING+=NEW_LINE+str(time_created)
        ALL_FILE_STRING+=NEW_LINE+str(time_edited)
        ALL_FILE_STRING+=NEW_LINE+"##########"
        ALL_FILE_STRING+=NEW_LINE+the_note_categories
        ALL_FILE_STRING+=NEW_LINE+"##########"
        ALL_FILE_STRING+=NEW_LINE+"##########"
        ALL_FILE_STRING+=NEW_LINE+"##########"
        ALL_FILE_STRING+=NEW_LINE+the_text
        ALL_FILE_STRING+=NEW_LINE+"##########"
        
        return ALL_FILE_STRING,the_title
        
    def noteToFile(self,filename:str):
        filestring1 = self.fileToString(filename)
        
        fileName1 = filestring1[1] + ".txt"
        f = open(fileName1, 'wt', encoding='utf-8')
        f.write(filestring1[0])


def main():
    
    file1 = KeepToSimplenote()
    
    dir_list = os.listdir("keepNotes")
    for i in dir_list:
        if i.endswith("json"):
            print(i)
            file1.noteToFile("keepNotes/"+i)
    
if __name__ == "__main__":
    main()