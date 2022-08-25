def read_file(file_name):
    with open(file_name, "r") as file:
        data = file.read()
        return data
    
    raise NotImplementedError()

def read_file_into_list(file_name):
    with open(file_name, "r") as file:
        data = file.readlines()
        return data

    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    spfile = file_contents.split("\n")
    first_line = spfile[0]
    with open(output_filename, "w") as file:
        file.write(first_line)
    return output_filename

    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    with open(file_name, "r") as file:
        datas = file.readlines()
        lst = datas[1::2]

    return lst

    raise NotImplementedError()

def read_file_in_reverse(file_name):
    data = open(file_name, 'r')  
    first = data.readlines()
    nlst = first[::-1]
    return nlst
    
    raise NotImplementedError()


def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()