# text-mop

Takes the name of a file that exists in the same location as the Dockerfile and print file text without spaces

## Run the thing

### Working path

From the root directory containing the Dockerfile
``` powershell
cd c:/python-text-utils/text-mop
```

### Build the docker image

``` powershell
docker build --build-arg FILE_NAME=text_file.txt -t textmop:01 .
```

### Run the docker container
``` powershell
docker run -it -v <absolute_path_to_directory_containing_text_file>:/app -e FILE_NAME=text_file.txt textmop:01
```