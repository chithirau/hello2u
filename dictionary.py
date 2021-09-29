import yaml
dictionary={"tomato":2,"potato":2}
print("vegetables:"+str(dictionary))
#result={dictionary.values()}
#print(result)
with open(r'C:\Users\Chithira\TASK3\file.yaml', 'w') as file:
    documents = yaml.dump(dictionary, file)