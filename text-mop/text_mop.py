def remove_whitespaces(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
        text = text.replace(" ", "")
        return text

if __name__ == '__main__':
    import sys
    import os

    file_name = sys.argv[1]
    # Get the file name from the environment variable
    file_name = os.environ.get('FILE_NAME', file_name)
    result = remove_whitespaces(file_name)
    print(result)