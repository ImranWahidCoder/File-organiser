import os
import shutil

# Create the type dictionary
types={
    "audio":[".mp3",".aa",".aax",".aiff",".alac",".voc",".wma"],
    "video":[".webm",".mkv",".flv",".gif",".wmv",".mp4",".m4p",".3gp"],
    "image":[".jpg",".jpeg",".png",".bmp",".webp",".svg"],
    "code":[".c",".cpp",".java",".py",".swift",".php",".asm",".js",".html",".htm",".css",".m",".r",".scala",".go"],
    "document":[".doc",".docx",".xls",".xlsx",".pdf",".ppt",".pptx",".txt",".ods",".json",".pages",".xml"],
    "compressed":[".zip",".rar"]
}

# function to provide the category of a file
def typeReader(types,content):
    extension=os.path.splitext(content)[1]
    for type in types.keys():
        for subCategory in types[type]:
            if subCategory==extension:
                return type
    return "others"

def organiser(path,remove_previous_copies):
    # If the organised directory is absent, create a new one
    if not os.path.isdir(path+"/Organised"):
        os.mkdir(path+"/Organised")
    
    # Get the content of the directory
    contents=os.listdir(path)
    
    # Iterate through the content and apply operation
    for content in contents:
        # Check if the content is a file or not
        if os.path.isfile(content) and len(os.path.splitext(content)[1])>1:

            # if the content is a file, find under which category it falls on
            category=typeReader(types,content)

            source=path+"/"+content
            destination=path+"/Organised/"+category
            # if the destination directory is not made, create it
            if not os.path.isdir(destination):
                os.mkdir(destination)
            
            # Copy the file to the destination
            shutil.copy(source,destination)

            # Remove the previous copies of the file if said
            if remove_previous_copies:
                os.remove(source)
            print(content," has been moved")
            


organiser(os.getcwd(),True)