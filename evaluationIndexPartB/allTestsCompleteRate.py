import json

f = open('../test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

# 各类型题目完成率：eachTypeCompleteRate.json "test_each_type_complete_score"

resultDict = dict() # 返回的结果，里面有所有题目的完成率
completedNumber = 0
for key,value in data.items():
    for case in value["cases"]:
        if case["final_score"] == 100:
            completedNumber += 1
    resultDict[key] = min(completedNumber, 200)/200*100


fTestCompleteRate = open("allTestsCompleteRate.json", 'w')
fTestCompleteRate.write(json.dumps(resultDict, ensure_ascii=False, indent=4))
fTestCompleteRate.close()
f.close()
