import json
import requests

public = "{'method': 'customer.addCustomer', 'appKey': 'App-167766679947-23222', 'timestamp': '2023-03-02 16:34:35', 'version': '1.0'}".replace(
    "'", '"')
public = json.loads(public)
business = "{'dataList': [{'area': '宝安区', 'country': '中国', 'labelNames': '超级VIP客户', 'address': '广东省平县山亭胡街L座 340305', 'city': '深圳市', 'nickName': '自动化型号', 'contactName': '自动化客户7410', 'fullName': '可删除wPWoIVWaSmfrARPxkXbJ', 'industry': None, 'remark': None, 'customerNumber': 'VxSFoKGZOOIcuRLmgvXe', 'province': '广东省', 'phone': '15625657546', 'organizations': [{'organization': '自动化测试组织'}]}]}".replace(
    "'", '"')
business = business.replace("None", '""')
finaldata = json.loads(business)
for i, j in public.items():
    finaldata[i] = j
send = "[{'key': 'nickName', 'send': 1, 'dataList': 1, 'htmlType': 1, 'value': '自动化型号'}]".replace("'", '"')
if len(send) > 3:
  send = json.loads(send)
  for dic in send:
      if dic['dataList'] == 0:
          action = finaldata
      else:
          action = finaldata['dataList'][0]
      if dic['send'] == 0:
          del (action[dic['key']])
      elif dic['value'] != "":
          action[dic['key']] = dic['value']
finaldata['sign'] = "50585e9817d02094b1df58c398aad608"
url = 'https://lijing.dataserver.cn/es/open/api'
result = requests.post(url=url, json=finaldata)
print(finaldata)
aa = result.text
print(aa)