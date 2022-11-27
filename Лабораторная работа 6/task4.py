import json

INPUT_FILE = "input_1.csv"


def csv_to_list_dict(file,new_line="\n",delimn = ",") -> list[dict]:

    with open(file) as f:
        data_list = f.readlines()
        answer_list=[]
        splited_list = [data_list[i].split(delimn) for i in range(len(data_list))]
        for elm in splited_list:
            elm[-1] = elm[-1].replace(new_line,"")
        for string in range(1,len(splited_list)):
            dict = {splited_list[0][col]:splited_list[string][col] for col in range(len(splited_list[0]))}
            answer_list.append(dict)

        return answer_list


#print(csv_to_list_dict(INPUT_FILE))
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
