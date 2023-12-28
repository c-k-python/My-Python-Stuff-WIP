import os

def list_files(start_path):
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    
    if os.path.exists(folder_path):
        print("\nListing files and folders:")
        list_files(folder_path)
    else:
        print("Invalid folder path. Please provide a valid path.")

    # Add this line to prevent the console window from closing immediately
    input("Press Enter to exit...")
