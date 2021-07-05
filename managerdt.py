import csv
import json


'''
json格式数文件的读取
'''
def load_jsondata(filename):
    f = open(filename,"r",encoding="utf-8")
    dict_data = json.load(f)
    # print(dict_data)
    f.close()
    return dict_data


'''
完成数据整合，返回整合后的数据列表对象
'''
def merge(dict_data):
    # 获取数据节点
    datanodes = dict_data['returndata']['datanodes']
    # 获取节点
    wdnodes  = dict_data['returndata']['wdnodes'][0]['nodes']

    # 获取wdnodes中编号和标签名，标签名中含有英文半角逗号，会对结果造成问题，需要转换为全角逗号
    yearInfo = [[node['code'],node['cname'].replace(',','，')] for node in wdnodes]
    dataInfo = [(node['wds'][0]['valuecode'],node['data']['strdata']) for  node in  datanodes]

    tmp_m = {}
    tmp_l = []
    key = ''
    for idx,node in enumerate(dataInfo):
        key = node[0]
        tmp_l.append(node[1])
        if(idx+1)%10 == 0:
            tmp_m[key] = tmp_l.copy()
            tmp_l.clear()
    for n in yearInfo:
        key = n[0]
        n.extend(tmp_m[key])
    return yearInfo


'''
列表对象保存为csv
'''
def save_csv_file(lst,filename):
    with open(filename,'w',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        for n in  lst:
            writer.writerow(n)

if __name__ == '__main__':

    # city_dict  = load_jsondata(filename="citydata.json")
    # rural_dict = load_jsondata(filename="ruraldata.json")
    # city_list = merge(city_dict)
    # rural_list = merge(rural_dict)
    # save_csv_file(city_list,"citydata.csv")
    # save_csv_file(rural_list,"ruraldata.csv")
    gdp_dict = load_jsondata("gdpdata.json")
    gdp_list = merge(gdp_dict)
    save_csv_file(gdp_list,"gdpdata.csv")
