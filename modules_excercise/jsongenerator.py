
### WRITE IMPORT STATEMENTS HERE
import json
from employee import details, employee_name, age, title

def create_dict(name, age, title):
    ### WRITE SOLUTION HERE
    employee_dict = {'first_name': name, 'age': int(age), 'title': title}
    return employee_dict
    
    raise NotImplementedError()

def write_json_to_file(json_obj, output_file):

    try:
        with open(output_file, "w") as newfile:
            newfile.write(json_obj)
    except:
        raise NotImplementedError()

def main():
    details()

    # Create dictionary
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))

    # Write out the json object to file
    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()