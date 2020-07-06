Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======= RESTART: C:\Users\joshm\Desktop\Listen Up\ListenUpPayPal1.1.py =======
Password: 
Traceback (most recent call last):
  File "C:\Users\joshm\Desktop\Listen Up\ListenUpPayPal1.1.py", line 174, in <module>
    run()
  File "C:\Users\joshm\Desktop\Listen Up\ListenUpPayPal1.1.py", line 141, in run
    password = input('Password: ').encode()
KeyboardInterrupt
>>> 'a'.startswith('abc')
False
>>> 'ax'.replace('a','b')
'bx'
>>> 
======= RESTART: C:\Users\joshm\Desktop\Listen Up\ListenUpPayPal1.1.py =======
Password: mountaindew
TylerNet file name: 0622PPLRECON.TXT
PayPal Authentication info file name: paypalauth.txt
Output file name: 0622outputb.txt
Error file name: 0622errorb.txt
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
1
0
1
1
1
1
1
0
1
0
0
0
1
0
1
0
1
0
1
0
1
0
0
0
0
0
1
0
1
0
1
0
1
0
1
0
0
0
0
0
0
0
0
1
0
0
0
1
0
1
1
1
1
0
0
0
0
0
0
0
0
0
1
0
1
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
0
1
0
1
0
0
0
0
0
0
0
0
0
0
0
1
0
1
0
1
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
0
0
0
0
0
1
0
1
0
1
0
1
0
1
0
0
1
1
0
0
0
0
0
0
0
0
0
0
0
1
0
1
0
1
0
1
0
0
0
0
0
1
0
1
0
1
0
1
Press enter to exit
>>> set('''701651	NOTFOUND
701663	NOTFOUND
701720	NOTFOUND
701721	NOTFOUND
701723	NOTFOUND
701724	NOTFOUND
701725	NOTFOUND
701726	NOTFOUND
701727	NOTFOUND
701728	NOTFOUND
E08249	NOTFOUND
L12010	NOTFOUND
701697	NOTFOUND
701705	NOTFOUND
701736	NOTFOUND
E08250	NOTFOUND
L12024	NOTFOUND
L12025	NOTFOUND
L12027	NOTFOUND
L12028	NOTFOUND
L12029	NOTFOUND
L12052	NOTFOUND
E08257	NOTFOUND
E08258	NOTFOUND
E08259	NOTFOUND
701737	NOTFOUND
701741	NOTFOUND
701742	NOTFOUND
701747	NOTFOUND
701748	NOTFOUND
A87464	NOTFOUND
132971	NOTFOUND
701755	NOTFOUND
701757	NOTFOUND
701758	NOTFOUND
701759	NOTFOUND
E08262	NOTFOUND
L12082	NOTFOUND'''.split('\n'))
{'701723\tNOTFOUND', 'E08257\tNOTFOUND', 'L12027\tNOTFOUND', 'E08262\tNOTFOUND', '701737\tNOTFOUND', '132971\tNOTFOUND', '701725\tNOTFOUND', 'L12024\tNOTFOUND', 'E08258\tNOTFOUND', '701759\tNOTFOUND', '701741\tNOTFOUND', 'A87464\tNOTFOUND', 'L12025\tNOTFOUND', '701663\tNOTFOUND', '701748\tNOTFOUND', '701697\tNOTFOUND', '701728\tNOTFOUND', '701757\tNOTFOUND', 'L12029\tNOTFOUND', '701724\tNOTFOUND', '701742\tNOTFOUND', '701727\tNOTFOUND', 'L12028\tNOTFOUND', 'E08259\tNOTFOUND', 'E08249\tNOTFOUND', '701651\tNOTFOUND', '701726\tNOTFOUND', 'L12010\tNOTFOUND', 'L12052\tNOTFOUND', 'L12082\tNOTFOUND', '701705\tNOTFOUND', '701736\tNOTFOUND', '701720\tNOTFOUND', '701758\tNOTFOUND', '701747\tNOTFOUND', '701755\tNOTFOUND', 'E08250\tNOTFOUND', '701721\tNOTFOUND'}
>>> access_tokens, expires_ats = get_access_tokens('mountaindew'.encode())
PayPal Authentication info file name: paypalauth.txt
>>> file_lines = get_file('TylerNet file name: ')
TylerNet file name: 0622PPLRECON.TXT
>>> tyler_data = [[line[sum(widths[:k]):sum(widths[:k+1])].strip() for k in range(len(widths))] for line in file_lines]
>>> tyler_data[2]
['', '', 'BG2P3FF105FF', '10019', '4355.00', '701663', '20062210:54']
>>> tyler_data[0]
['', '', '9KS30457BV192774', '94109', '4350.00', '701651', '20062209:35']
>>> tyler_data[1]
['', '', '9KS30457BV192774', '94109', '4350.00', '701651', '20062209:35']
>>> tyler_data[5]
['Paid on 2020-06-21T02:09:59.0000000', 'lcjd08@gmail.com', '76924478', '968181792', '1457.28', '701720', '20062209:50']
>>> line = tyler_data[5]
>>> transaction,is_best_case = get_best_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens,expires_ats)
0
0
>>> transaction,is_best_case = get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens[0])
0
>>> transaction,is_best_case = get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens[1])
0
>>> amt_dollars,time_string,email,zip_code,listing_id,entry_time_string,access_token=get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens[1])
0
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    amt_dollars,time_string,email,zip_code,listing_id,entry_time_string,access_token=get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens[1])
ValueError: not enough values to unpack (expected 7, got 2)
>>> amt_dollars,time_string,email,zip_code,listing_id,entry_time_string,access_token=line[4],line[0],line[1],line[3],line[2],line[6],access_tokens[1]
>>> headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}
>>> amt_cents = abs(round(float2(amt_dollars)*100))
>>> params = {
        'transaction_status':'S',
        'transaction_amount':'['+str(amt_cents-1)+' TO '+str(amt_cents+1)+']',
        'tansaction_currency':'USD',
        'start_date':string2iso(time_string,entry_time_string,-2),
        'end_date':string2iso(time_string,entry_time_string,+1),
        'fields':'transaction_info,payer_info,shipping_info,auction_info',
        'page_size':page_size
    }
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers=headers, params=params)
>>> response.json()
{'transaction_details': [], 'account_number': 'KZSHK9NUEKW6C', 'start_date': '2020-06-21T08:59:59+0000', 'end_date': '2020-06-21T09:14:59+0000', 'last_refreshed_datetime': '2020-06-30T15:59:59+0000', 'page': 1, 'total_items': 0, 'total_pages': 0, 'links': [{'href': 'https://api.paypal.com/v1/reporting/transactions?transaction_status=S&transaction_amount=%5B145727+TO+145729%5D&tansaction_currency=USD&start_date=2020-06-21T01%3A59%3A59-07%3A00&end_date=2020-06-21T02%3A14%3A59-07%3A00&fields=transaction_info%2Cpayer_info%2Cshipping_info%2Cauction_info&page_size=200&page=1', 'rel': 'self', 'method': 'GET'}]}
>>> headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[0]}
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers=headers, params=params)
>>> response.json()
{'transaction_details': [], 'account_number': 'VKBWUZP7PJ6TL', 'start_date': '2020-06-21T08:59:59+0000', 'end_date': '2020-06-21T09:14:59+0000', 'last_refreshed_datetime': '2020-06-30T15:59:59+0000', 'page': 1, 'total_items': 0, 'total_pages': 0, 'links': [{'href': 'https://api.paypal.com/v1/reporting/transactions?transaction_status=S&transaction_amount=%5B145727+TO+145729%5D&tansaction_currency=USD&start_date=2020-06-21T01%3A59%3A59-07%3A00&end_date=2020-06-21T02%3A14%3A59-07%3A00&fields=transaction_info%2Cpayer_info%2Cshipping_info%2Cauction_info&page_size=200&page=1', 'rel': 'self', 'method': 'GET'}]}
>>> params
{'transaction_status': 'S', 'transaction_amount': '[145727 TO 145729]', 'tansaction_currency': 'USD', 'start_date': '2020-06-21T01:59:59-07:00', 'end_date': '2020-06-21T02:14:59-07:00', 'fields': 'transaction_info,payer_info,shipping_info,auction_info', 'page_size': 200}
>>> set1={'701723\tNOTFOUND', 'E08257\tNOTFOUND', 'L12027\tNOTFOUND', 'E08262\tNOTFOUND', '701737\tNOTFOUND', '132971\tNOTFOUND', '701725\tNOTFOUND', 'L12024\tNOTFOUND', 'E08258\tNOTFOUND', '701759\tNOTFOUND', '701741\tNOTFOUND', 'A87464\tNOTFOUND', 'L12025\tNOTFOUND', '701663\tNOTFOUND', '701748\tNOTFOUND', '701697\tNOTFOUND', '701728\tNOTFOUND', '701757\tNOTFOUND', 'L12029\tNOTFOUND', '701724\tNOTFOUND', '701742\tNOTFOUND', '701727\tNOTFOUND', 'L12028\tNOTFOUND', 'E08259\tNOTFOUND', 'E08249\tNOTFOUND', '701651\tNOTFOUND', '701726\tNOTFOUND', 'L12010\tNOTFOUND', 'L12052\tNOTFOUND', 'L12082\tNOTFOUND', '701705\tNOTFOUND', '701736\tNOTFOUND', '701720\tNOTFOUND', '701758\tNOTFOUND', '701747\tNOTFOUND', '701755\tNOTFOUND', 'E08250\tNOTFOUND', '701721\tNOTFOUND'}
>>> setb=set('''701651	NOTFOUND
701663	NOTFOUND
701720	NOTFOUND
701721	NOTFOUND
701723	NOTFOUND
701724	NOTFOUND
701725	NOTFOUND
701726	NOTFOUND
701727	NOTFOUND
701728	NOTFOUND
E08244	NOTFOUND
E08248	NOTFOUND
E08249	NOTFOUND
L12006	NOTFOUND
L12010	NOTFOUND
701697	NOTFOUND
701705	NOTFOUND
701736	NOTFOUND
E08250	NOTFOUND
L12024	NOTFOUND
L12025	NOTFOUND
L12027	NOTFOUND
L12028	NOTFOUND
L12029	NOTFOUND
L12052	NOTFOUND
E08257	NOTFOUND
E08258	NOTFOUND
E08259	NOTFOUND
701737	NOTFOUND
701741	NOTFOUND
701742	NOTFOUND
701747	NOTFOUND
701748	NOTFOUND
A87464	NOTFOUND
132971	NOTFOUND
701755	NOTFOUND
701757	NOTFOUND
701758	NOTFOUND
701759	NOTFOUND
E08262	NOTFOUND
E08263	NOTFOUND
E08264	NOTFOUND
L12082	NOTFOUND'''.split('\n'))
>>> len(set1)
38
>>> len(setb)
43
>>> for k in set1:
	if not k in setb:
		print(k)

		
>>> for k in setb:
	if not k in set1:
		print(k)

		
E08244	NOTFOUND
L12006	NOTFOUND
E08264	NOTFOUND
E08263	NOTFOUND
E08248	NOTFOUND
>>> for k in setb:
	if not k in set1:
		print(k[:7],end='')

		
E08244	L12006	E08264	E08263	E08248	
>>> for j,line in enumerate(tyler_data):
	if sum([k.startwsith(line[5]) for k in set1]):
		print(j)

		
Traceback (most recent call last):
  File "<pyshell#40>", line 2, in <module>
    if sum([k.startwsith(line[5]) for k in set1]):
  File "<pyshell#40>", line 2, in <listcomp>
    if sum([k.startwsith(line[5]) for k in set1]):
AttributeError: 'str' object has no attribute 'startwsith'
>>> for j,line in enumerate(tyler_data):
	if sum([k.startswith(line[5]) for k in set1]):
		print(j)

		
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
56
72
73
74
75
91
92
93
94
95
98
99
100
101
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
140
141
142
143
144
145
146
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
189
190
191
192
208
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
237
238
239
240
>>> params
{'transaction_status': 'S', 'transaction_amount': '[145727 TO 145729]', 'tansaction_currency': 'USD', 'start_date': '2020-06-21T01:59:59-07:00', 'end_date': '2020-06-21T02:14:59-07:00', 'fields': 'transaction_info,payer_info,shipping_info,auction_info', 'page_size': 200}
>>> params={'transaction_status': 'S', 'transaction_amount': '[125727 TO 165729]', 'tansaction_currency': 'USD', 'start_date': '2020-06-21T01:59:59-07:00', 'end_date': '2020-06-21T02:14:59-07:00', 'fields': 'transaction_info,payer_info,shipping_info,auction_info', 'page_size': 200}
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers=headers, params=params)
>>> response.json()
{'transaction_details': [], 'account_number': 'VKBWUZP7PJ6TL', 'start_date': '2020-06-21T08:59:59+0000', 'end_date': '2020-06-21T09:14:59+0000', 'last_refreshed_datetime': '2020-06-30T15:59:59+0000', 'page': 1, 'total_items': 0, 'total_pages': 0, 'links': [{'href': 'https://api.paypal.com/v1/reporting/transactions?transaction_status=S&transaction_amount=%5B125727+TO+165729%5D&tansaction_currency=USD&start_date=2020-06-21T01%3A59%3A59-07%3A00&end_date=2020-06-21T02%3A14%3A59-07%3A00&fields=transaction_info%2Cpayer_info%2Cshipping_info%2Cauction_info&page_size=200&page=1', 'rel': 'self', 'method': 'GET'}]}
>>> headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[1]}
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers=headers, params=params)
>>> response.json()
{'transaction_details': [], 'account_number': 'KZSHK9NUEKW6C', 'start_date': '2020-06-21T08:59:59+0000', 'end_date': '2020-06-21T09:14:59+0000', 'last_refreshed_datetime': '2020-06-30T15:59:59+0000', 'page': 1, 'total_items': 0, 'total_pages': 0, 'links': [{'href': 'https://api.paypal.com/v1/reporting/transactions?transaction_status=S&transaction_amount=%5B125727+TO+165729%5D&tansaction_currency=USD&start_date=2020-06-21T01%3A59%3A59-07%3A00&end_date=2020-06-21T02%3A14%3A59-07%3A00&fields=transaction_info%2Cpayer_info%2Cshipping_info%2Cauction_info&page_size=200&page=1', 'rel': 'self', 'method': 'GET'}]}
>>> params={'transaction_status': 'S', 'tansaction_currency': 'USD', 'start_date': '2020-06-21T01:49:59-07:00', 'end_date': '2020-06-21T02:24:59-07:00', 'fields': 'transaction_info,payer_info,shipping_info,auction_info', 'page_size': 200}
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[0]}, params=params)
>>> response.json()['total_items']
2
>>> response.json()
{'transaction_details': [{'transaction_info': {'paypal_account_id': 'MFZ448TH6ZAT2', 'transaction_id': '7PR98115YX474032F', 'transaction_event_code': 'T0004', 'transaction_initiation_date': '2020-06-21T09:16:34+0000', 'transaction_updated_date': '2020-06-21T09:16:34+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '127.45'}, 'fee_amount': {'currency_code': 'USD', 'value': '-3.10'}, 'transaction_status': 'S', 'custom_field': 'EBAY_EMSCX00001034417767515_S:EMSCX00001034417767615_T', 'protection_eligibility': '01'}, 'payer_info': {'account_id': 'MFZ448TH6ZAT2', 'email_address': 'mr.waden@yahoo.com', 'address_status': 'Y', 'payer_status': 'Y', 'payer_name': {'given_name': 'Wade', 'surname': 'Niedermann', 'alternate_full_name': 'Wade Niedermann'}, 'country_code': 'US'}, 'shipping_info': {'name': 'Wade W Niedermann', 'method': '0', 'address': {'line1': '115 Sundance Trl', 'city': 'Capron', 'state': 'IL', 'country_code': 'US', 'postal_code': '61012-9590'}}, 'auction_info': {'auction_site': 'Ebay', 'auction_item_site': 'http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=283366998224', 'auction_buyer_id': 'waden01'}}, {'transaction_info': {'transaction_id': '4RW22138N0763962E', 'paypal_reference_id': '7PR98115YX474032F', 'paypal_reference_id_type': 'TXN', 'transaction_event_code': 'T0020', 'transaction_initiation_date': '2020-06-21T09:16:34+0000', 'transaction_updated_date': '2020-06-21T09:16:34+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '-7.50'}, 'transaction_status': 'S', 'custom_field': 'EBAY_EMSCX00001034417767515_S:EMSCX00001034417767615_T', 'protection_eligibility': '02'}, 'payer_info': {'address_status': 'N', 'payer_name': {}}, 'shipping_info': {'method': '0'}, 'auction_info': {'auction_site': 'Ebay', 'auction_item_site': 'http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=283366998224', 'auction_buyer_id': 'waden01'}}], 'account_number': 'VKBWUZP7PJ6TL', 'start_date': '2020-06-21T08:49:59+0000', 'end_date': '2020-06-21T09:24:59+0000', 'last_refreshed_datetime': '2020-06-30T15:59:59+0000', 'page': 1, 'total_items': 2, 'total_pages': 1, 'links': [{'href': 'https://api.paypal.com/v1/reporting/transactions?transaction_status=S&tansaction_currency=USD&start_date=2020-06-21T01%3A49%3A59-07%3A00&end_date=2020-06-21T02%3A24%3A59-07%3A00&fields=transaction_info%2Cpayer_info%2Cshipping_info%2Cauction_info&page_size=200&page=1', 'rel': 'self', 'method': 'GET'}]}
>>> line
['Paid on 2020-06-26T06:30:54.0000000', 'rich.danan12@gmail.com', '163865132345', '601695205', '636.44', 'L12090', '20062611:40']
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[1]}, params=params)
>>> response.json()['total_items']
0
>>> params={'transaction_status': 'S', 'tansaction_currency': 'USD', 'start_date': '2020-06-21T00:49:59-07:00', 'end_date': '2020-06-21T03:24:59-07:00', 'fields': 'transaction_info,payer_info,shipping_info,auction_info', 'page_size': 200}
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[1]}, params=params)
>>> response.json()['total_items']
0
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[0]}, params=params)
>>> response.json()['total_items']
2
>>> params={'transaction_status': 'S', 'transaction_amount': '[125727 TO 165729]', 'tansaction_currency': 'USD', 'start_date': '2020-05-21T01:59:59-07:00', 'end_date': '2020-07-21T02:14:59-07:00', 'fields': 'transaction_info,payer_info,shipping_info,auction_info', 'page_size': 200}
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[0]}, params=params)
>>> response.json()['total_items']
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    response.json()['total_items']
KeyError: 'total_items'
>>> response.json()
{'name': 'INVALID_REQUEST', 'message': 'Invalid request - see details.', 'debug_id': '8ce0b114869d3', 'details': [{'field': 'end_date', 'value': '2020-07-21T02:14:59-07:00', 'location': 'query', 'issue': 'Date range is greater than 31 days'}], 'links': []}
>>> params={'transaction_status': 'S', 'transaction_amount': '[125727 TO 165729]', 'tansaction_currency': 'USD', 'start_date': '2020-06-20T01:59:59-07:00', 'end_date': '2020-06-22T02:14:59-07:00', 'fields': 'transaction_info,payer_info,shipping_info,auction_info', 'page_size': 200}
>>> 
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[0]}, params=params)
>>> response.json()['total_items']
0
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[1]}, params=params)
>>> response.json()['total_items']
0
>>> params={'transaction_status': 'S', 'transaction_amount': '[120000 TO 160000]', 'tansaction_currency': 'USD', 'start_date': '2020-06-18T01:59:59-07:00', 'end_date': '2020-06-24T02:14:59-07:00', 'fields': 'transaction_info,payer_info,shipping_info,auction_info', 'page_size': 200}
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[0]}, params=params)
>>> response.json()['total_items']
5
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[1]}, params=params)
>>> response.json()['total_items']
4
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[0]}, params=params)
>>> response.json()
{'transaction_details': [{'transaction_info': {'paypal_account_id': 'JXXVCAUUJK7X8', 'transaction_id': '9VC28831HP0281022', 'transaction_event_code': 'T0007', 'transaction_initiation_date': '2020-06-19T14:17:01+0000', 'transaction_updated_date': '2020-06-19T14:17:01+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '1299.72'}, 'fee_amount': {'currency_code': 'USD', 'value': '-28.89'}, 'transaction_status': 'S', 'invoice_id': '121354', 'protection_eligibility': '01'}, 'payer_info': {'account_id': 'JXXVCAUUJK7X8', 'email_address': 'hamidoudia@gmail.com', 'phone_number': {'country_code': '1', 'national_number': '3033462258'}, 'address_status': 'Y', 'payer_status': 'N', 'payer_name': {'given_name': 'Hamidou', 'surname': 'Dia', 'alternate_full_name': 'Hamidou Dia'}, 'country_code': 'US', 'address': {'line1': '1391 Bladon ave.', 'city': 'Deltona', 'state': 'FL', 'country_code': 'US', 'postal_code': '32738'}}, 'shipping_info': {'name': 'Hamidou, Dia', 'address': {'line1': '575 South Gaylord Street', 'city': 'Denver', 'state': 'CO', 'country_code': 'US', 'postal_code': '80209'}}, 'auction_info': {}}, {'transaction_info': {'paypal_account_id': '5RBCWQH8TW3R4', 'transaction_id': '6HE07017WB1692805', 'paypal_reference_id': '09C27256UK9104051', 'paypal_reference_id_type': 'TXN', 'transaction_event_code': 'T0005', 'transaction_initiation_date': '2020-06-22T15:38:17+0000', 'transaction_updated_date': '2020-06-22T15:38:17+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '1457.28'}, 'fee_amount': {'currency_code': 'USD', 'value': '-32.36'}, 'transaction_status': 'S', 'invoice_id': '9554332660', 'protection_eligibility': '02', 'instrument_type': 'CREDITCARD', 'instrument_sub_type': 'M'}, 'payer_info': {'account_id': '5RBCWQH8TW3R4', 'address_status': 'Y', 'payer_status': 'N', 'payer_name': {'given_name': 'Garrett', 'surname': 'Goda', 'alternate_full_name': 'Garrett Goda'}, 'country_code': 'US'}, 'shipping_info': {'name': 'Garrett Goda', 'address': {'line1': '1090 Ala Napunani St. Apt. 404', 'city': 'Honolulu', 'state': 'HI', 'country_code': 'US', 'postal_code': '96818'}}, 'auction_info': {}}, {'transaction_info': {'paypal_account_id': '6XJTZ6XKY5BQL', 'transaction_id': '3W487768B3782210S', 'paypal_reference_id': '5L70778665540240V', 'paypal_reference_id_type': 'TXN', 'transaction_event_code': 'T0006', 'transaction_initiation_date': '2020-06-22T15:41:11+0000', 'transaction_updated_date': '2020-06-22T15:41:11+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '1487.84'}, 'fee_amount': {'currency_code': 'USD', 'value': '-33.03'}, 'sales_tax_amount': {'currency_code': 'USD', 'value': '88.84'}, 'transaction_status': 'S', 'invoice_id': '9554332664', 'protection_eligibility': '01'}, 'payer_info': {'account_id': '6XJTZ6XKY5BQL', 'email_address': 'Metropolis_488@hotmail.com', 'phone_number': {'country_code': '1', 'national_number': '4342490862'}, 'address_status': 'Y', 'payer_status': 'Y', 'payer_name': {'given_name': 'Matthew', 'surname': 'Steiner', 'alternate_full_name': 'Matthew Steiner'}, 'country_code': 'US', 'address': {'line1': '21 Brocketts Point Rd', 'city': 'Branford', 'state': 'CT', 'country_code': 'US', 'postal_code': '06405'}}, 'shipping_info': {'name': 'Matthew, Steiner', 'address': {'line1': '21 Brocketts Point Rd', 'city': 'Branford', 'state': 'CT', 'country_code': 'US', 'postal_code': '06405'}}, 'auction_info': {}}, {'transaction_info': {'paypal_account_id': '8CFCMV6TSDCC6', 'transaction_id': '5P914601XX9466815', 'paypal_reference_id': '4A586464W3656201N', 'paypal_reference_id_type': 'TXN', 'transaction_event_code': 'T1107', 'transaction_initiation_date': '2020-06-22T19:29:45+0000', 'transaction_updated_date': '2020-06-22T19:29:45+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '-1528.41'}, 'transaction_status': 'S', 'transaction_subject': 'Magnapan refund', 'transaction_note': 'Magnapan refund', 'invoice_id': '121356', 'protection_eligibility': '02'}, 'payer_info': {'account_id': '8CFCMV6TSDCC6', 'email_address': 'tim@hyperarts.com', 'phone_number': {'country_code': '1', 'national_number': '5103396084'}, 'address_status': 'N', 'payer_status': 'Y', 'payer_name': {'given_name': 'Timothy', 'surname': 'Ware', 'alternate_full_name': 'Timothy Ware'}, 'country_code': 'US', 'address': {'line1': '5918 N Dexter Ave', 'city': 'Tampa', 'state': 'FL', 'country_code': 'US', 'postal_code': '33604'}}, 'shipping_info': {'name': 'Timothy, Ware'}, 'auction_info': {}}, {'transaction_info': {'paypal_account_id': 'UG2B7FR9YER2L', 'transaction_id': '2W159783EW686303M', 'paypal_reference_id': '47Y263784Y125654S', 'paypal_reference_id_type': 'TXN', 'transaction_event_code': 'T0005', 'transaction_initiation_date': '2020-06-23T18:24:43+0000', 'transaction_updated_date': '2020-06-23T18:24:43+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '1260.45'}, 'fee_amount': {'currency_code': 'USD', 'value': '-28.03'}, 'transaction_status': 'S', 'invoice_id': '9554332669', 'protection_eligibility': '02', 'instrument_type': 'CREDITCARD', 'instrument_sub_type': 'M'}, 'payer_info': {'account_id': 'UG2B7FR9YER2L', 'address_status': 'Y', 'payer_status': 'N', 'payer_name': {'given_name': 'John', 'surname': 'MacKenzie', 'alternate_full_name': 'John MacKenzie'}, 'country_code': 'US'}, 'shipping_info': {'name': 'John  MacKenzie', 'address': {'line1': '1705 Buffalo Dancer Trail NE', 'city': 'Alburquerque', 'state': 'NM', 'country_code': 'US', 'postal_code': '87112'}}, 'auction_info': {}}], 'account_number': 'VKBWUZP7PJ6TL', 'start_date': '2020-06-18T08:59:59+0000', 'end_date': '2020-06-24T09:14:59+0000', 'last_refreshed_datetime': '2020-06-30T15:59:59+0000', 'page': 1, 'total_items': 5, 'total_pages': 1, 'links': [{'href': 'https://api.paypal.com/v1/reporting/transactions?transaction_status=S&transaction_amount=%5B120000+TO+160000%5D&tansaction_currency=USD&start_date=2020-06-18T01%3A59%3A59-07%3A00&end_date=2020-06-24T02%3A14%3A59-07%3A00&fields=transaction_info%2Cpayer_info%2Cshipping_info%2Cauction_info&page_size=200&page=1', 'rel': 'self', 'method': 'GET'}]}
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[1]}, params=params)
>>> response.json()
{'transaction_details': [{'transaction_info': {'paypal_account_id': 'JJP3YM4LBFUNS', 'transaction_id': '0L220366CB4960531', 'paypal_reference_id': '8MR755851T133735J', 'paypal_reference_id_type': 'TXN', 'transaction_event_code': 'T1107', 'transaction_initiation_date': '2020-06-18T12:44:07+0000', 'transaction_updated_date': '2020-06-18T12:44:07+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '-1327.06'}, 'transaction_status': 'S', 'custom_field': 'EBAY_EMSCX00001023443890117_S:EMSCX00001023443890217_T', 'protection_eligibility': '02'}, 'payer_info': {'account_id': 'JJP3YM4LBFUNS', 'email_address': 'hickman.jw@gmail.com', 'phone_number': {'country_code': '1', 'national_number': '2064279417'}, 'address_status': 'N', 'payer_status': 'Y', 'payer_name': {'given_name': 'Jason', 'surname': 'Hickman', 'alternate_full_name': 'Jason Hickman'}, 'country_code': 'US'}, 'shipping_info': {'name': 'Jason, Hickman', 'method': '0'}, 'auction_info': {}}, {'transaction_info': {'paypal_account_id': 'YVNVUW7JUMCSA', 'transaction_id': '10425064HC260970X', 'transaction_event_code': 'T0004', 'transaction_initiation_date': '2020-06-18T18:02:23+0000', 'transaction_updated_date': '2020-06-18T18:02:23+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '1595.35'}, 'fee_amount': {'currency_code': 'USD', 'value': '-35.40'}, 'transaction_status': 'S', 'custom_field': 'EBAY_EMSCX00001033497318615_S:EMSCX00001033497318715_T', 'protection_eligibility': '01'}, 'payer_info': {'account_id': 'YVNVUW7JUMCSA', 'email_address': 'mike.r.nich@gmail.com', 'address_status': 'Y', 'payer_status': 'Y', 'payer_name': {'given_name': 'Mike', 'surname': 'Nichols', 'alternate_full_name': 'Mike Nichols'}, 'country_code': 'US'}, 'shipping_info': {'name': 'Mike Nichols', 'method': '0', 'address': {'line1': '2618 W Viewmont Way W', 'city': 'Seattle', 'state': 'WA', 'country_code': 'US', 'postal_code': '98199-3019'}}, 'auction_info': {'auction_site': 'Ebay', 'auction_item_site': 'http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=163968508161', 'auction_buyer_id': 'drakan2'}}, {'transaction_info': {'paypal_account_id': 'VAYS964DG82AW', 'transaction_id': '5XK02081GH7296319', 'transaction_event_code': 'T0004', 'transaction_initiation_date': '2020-06-19T07:35:52+0000', 'transaction_updated_date': '2020-06-19T07:35:52+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '1380.19'}, 'fee_amount': {'currency_code': 'USD', 'value': '-30.66'}, 'transaction_status': 'S', 'custom_field': 'EBAY_EMSCX00001035006589713_S:EMSCX00001035006589813_T', 'protection_eligibility': '01'}, 'payer_info': {'account_id': 'VAYS964DG82AW', 'email_address': 'raymondteng@gmail.com', 'address_status': 'Y', 'payer_status': 'Y', 'payer_name': {'given_name': 'raymond', 'surname': 'teng', 'alternate_full_name': 'raymond teng'}, 'country_code': 'US'}, 'shipping_info': {'name': 'Raymond Teng', 'method': '0', 'address': {'line1': '6038 N Campbell Ave', 'city': 'Chicago', 'state': 'IL', 'country_code': 'US', 'postal_code': '60659-4107'}}, 'auction_info': {'auction_site': 'Ebay', 'auction_item_site': 'http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=164249217455', 'auction_buyer_id': 'rrrteng'}}, {'transaction_info': {'paypal_account_id': 'DUW6YG59XJ2LL', 'transaction_id': '57T6278989901861B', 'paypal_reference_id': '9NX127775R5146330', 'paypal_reference_id_type': 'TXN', 'transaction_event_code': 'T1107', 'transaction_initiation_date': '2020-06-23T13:27:28+0000', 'transaction_updated_date': '2020-06-23T13:27:28+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '-1272.00'}, 'transaction_status': 'S', 'custom_field': 'EBAY_EMSCX00001020625356418_S:EMSCX00001020625466618_T', 'protection_eligibility': '02'}, 'payer_info': {'account_id': 'DUW6YG59XJ2LL', 'email_address': 'locmarylandiphone@gmail.com', 'phone_number': {'country_code': '1', 'national_number': '6264560037'}, 'address_status': 'N', 'payer_status': 'Y', 'payer_name': {'given_name': 'loc', 'surname': 'le', 'alternate_full_name': 'loc le'}, 'country_code': 'US'}, 'shipping_info': {'name': 'loc, le', 'method': '0'}, 'auction_info': {}}], 'account_number': 'KZSHK9NUEKW6C', 'start_date': '2020-06-18T08:59:59+0000', 'end_date': '2020-06-24T09:14:59+0000', 'last_refreshed_datetime': '2020-06-30T15:59:59+0000', 'page': 1, 'total_items': 4, 'total_pages': 1, 'links': [{'href': 'https://api.paypal.com/v1/reporting/transactions?transaction_status=S&transaction_amount=%5B120000+TO+160000%5D&tansaction_currency=USD&start_date=2020-06-18T01%3A59%3A59-07%3A00&end_date=2020-06-24T02%3A14%3A59-07%3A00&fields=transaction_info%2Cpayer_info%2Cshipping_info%2Cauction_info&page_size=200&page=1', 'rel': 'self', 'method': 'GET'}]}
>>> params={'transaction_status': 'S', 'transaction_amount': '[14727 TO 145729]', 'tansaction_currency': 'USD', 'start_date': '2020-06-18T01:59:59-07:00', 'end_date': '2020-06-24T02:14:59-07:00', 'fields': 'transaction_info,payer_info,shipping_info,auction_info', 'page_size': 200}
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[0]}, params=params)
>>> response.json()

>>> response.json()['total_items']
21
>>> params={'transaction_status': 'S', 'transaction_amount': '[145727 TO 145729]', 'tansaction_currency': 'USD', 'start_date': '2020-06-18T01:59:59-07:00', 'end_date': '2020-06-24T02:14:59-07:00', 'fields': 'transaction_info,payer_info,shipping_info,auction_info', 'page_size': 200}
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[0]}, params=params)
>>> response.json()
{'transaction_details': [{'transaction_info': {'paypal_account_id': '5RBCWQH8TW3R4', 'transaction_id': '6HE07017WB1692805', 'paypal_reference_id': '09C27256UK9104051', 'paypal_reference_id_type': 'TXN', 'transaction_event_code': 'T0005', 'transaction_initiation_date': '2020-06-22T15:38:17+0000', 'transaction_updated_date': '2020-06-22T15:38:17+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '1457.28'}, 'fee_amount': {'currency_code': 'USD', 'value': '-32.36'}, 'transaction_status': 'S', 'invoice_id': '9554332660', 'protection_eligibility': '02', 'instrument_type': 'CREDITCARD', 'instrument_sub_type': 'M'}, 'payer_info': {'account_id': '5RBCWQH8TW3R4', 'address_status': 'Y', 'payer_status': 'N', 'payer_name': {'given_name': 'Garrett', 'surname': 'Goda', 'alternate_full_name': 'Garrett Goda'}, 'country_code': 'US'}, 'shipping_info': {'name': 'Garrett Goda', 'address': {'line1': '1090 Ala Napunani St. Apt. 404', 'city': 'Honolulu', 'state': 'HI', 'country_code': 'US', 'postal_code': '96818'}}, 'auction_info': {}}], 'account_number': 'VKBWUZP7PJ6TL', 'start_date': '2020-06-18T08:59:59+0000', 'end_date': '2020-06-24T09:14:59+0000', 'last_refreshed_datetime': '2020-06-30T15:59:59+0000', 'page': 1, 'total_items': 1, 'total_pages': 1, 'links': [{'href': 'https://api.paypal.com/v1/reporting/transactions?transaction_status=S&transaction_amount=%5B145727+TO+145729%5D&tansaction_currency=USD&start_date=2020-06-18T01%3A59%3A59-07%3A00&end_date=2020-06-24T02%3A14%3A59-07%3A00&fields=transaction_info%2Cpayer_info%2Cshipping_info%2Cauction_info&page_size=200&page=1', 'rel': 'self', 'method': 'GET'}]}
>>> params = {
        'transaction_status':'S',
        'transaction_amount':'['+str(amt_cents-1)+' TO '+str(amt_cents+1)+']',
        'tansaction_currency':'USD',
        'start_date':string2iso(time_string,entry_time_string,-2),
        'end_date':string2iso(time_string,entry_time_string,+1),
        'fields':'transaction_info,payer_info,shipping_info,auction_info',
        'page_size':page_size
    }
>>> params
{'transaction_status': 'S', 'transaction_amount': '[145727 TO 145729]', 'tansaction_currency': 'USD', 'start_date': '2020-06-21T01:59:59-07:00', 'end_date': '2020-06-21T02:14:59-07:00', 'fields': 'transaction_info,payer_info,shipping_info,auction_info', 'page_size': 200}
>>> params={'transaction_status': 'S', 'transaction_amount': '[145727 TO 145729]', 'tansaction_currency': 'USD', 'start_date': '2020-06-21T01:59:59-07:00', 'end_date': '2020-06-21T09:14:59-07:00', 'fields': 'transaction_info,payer_info,shipping_info,auction_info', 'page_size': 200}
>>> response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_tokens[0]}, params=params)
>>> response.json()
{'transaction_details': [], 'account_number': 'VKBWUZP7PJ6TL', 'start_date': '2020-06-21T08:59:59+0000', 'end_date': '2020-06-21T16:14:59+0000', 'last_refreshed_datetime': '2020-06-30T15:59:59+0000', 'page': 1, 'total_items': 0, 'total_pages': 0, 'links': [{'href': 'https://api.paypal.com/v1/reporting/transactions?transaction_status=S&transaction_amount=%5B145727+TO+145729%5D&tansaction_currency=USD&start_date=2020-06-21T01%3A59%3A59-07%3A00&end_date=2020-06-21T09%3A14%3A59-07%3A00&fields=transaction_info%2Cpayer_info%2Cshipping_info%2Cauction_info&page_size=200&page=1', 'rel': 'self', 'method': 'GET'}]}
>>> t={'transaction_details': [{'transaction_info': {'paypal_account_id': '5RBCWQH8TW3R4', 'transaction_id': '6HE07017WB1692805', 'paypal_reference_id': '09C27256UK9104051', 'paypal_reference_id_type': 'TXN', 'transaction_event_code': 'T0005', 'transaction_initiation_date': '2020-06-22T15:38:17+0000', 'transaction_updated_date': '2020-06-22T15:38:17+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '1457.28'}, 'fee_amount': {'currency_code': 'USD', 'value': '-32.36'}, 'transaction_status': 'S', 'invoice_id': '9554332660', 'protection_eligibility': '02', 'instrument_type': 'CREDITCARD', 'instrument_sub_type': 'M'}, 'payer_info': {'account_id': '5RBCWQH8TW3R4', 'address_status': 'Y', 'payer_status': 'N', 'payer_name': {'given_name': 'Garrett', 'surname': 'Goda', 'alternate_full_name': 'Garrett Goda'}, 'country_code': 'US'}, 'shipping_info': {'name': 'Garrett Goda', 'address': {'line1': '1090 Ala Napunani St. Apt. 404', 'city': 'Honolulu', 'state': 'HI', 'country_code': 'US', 'postal_code': '96818'}}, 'auction_info': {}}], 'account_number': 'VKBWUZP7PJ6TL', 'start_date': '2020-06-18T08:59:59+0000', 'end_date': '2020-06-24T09:14:59+0000', 'last_refreshed_datetime': '2020-06-30T15:59:59+0000', 'page': 1, 'total_items': 1, 'total_pages': 1, 'links': [{'href': 'https://api.paypal.com/v1/reporting/transactions?transaction_status=S&transaction_amount=%5B145727+TO+145729%5D&tansaction_currency=USD&start_date=2020-06-18T01%3A59%3A59-07%3A00&end_date=2020-06-24T02%3A14%3A59-07%3A00&fields=transaction_info%2Cpayer_info%2Cshipping_info%2Cauction_info&page_size=200&page=1', 'rel': 'self', 'method': 'GET'}]}
>>> transaction_detail=t['transaction_details'][0]
>>> transaction_detail['transaction_info']['transaction_amount']['value']
'1457.28'
>>> compare_zips(transaction_detail['shipping_info']['address']['postal_code'],zip_code)
True
>>> transaction_detail['auction_info']['auction_item_site']
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    transaction_detail['auction_info']['auction_item_site']
KeyError: 'auction_item_site'
>>> 'email_address' in transaction_detail['payer_info']
False
>>> img_array = [cv2.imread('C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\'+str(k).zfill(4)) for k in range(134)]
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    img_array = [cv2.imread('C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\'+str(k).zfill(4)) for k in range(134)]
  File "<pyshell#99>", line 1, in <listcomp>
    img_array = [cv2.imread('C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\'+str(k).zfill(4)) for k in range(134)]
NameError: name 'cv2' is not defined
>>> import cv2
>>> img_array = [cv2.imread('C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\'+str(k).zfill(4)) for k in range(134)]

>>> len(img_array)
134
>>> out = cv2.VideoWriter(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, (1920//2,1080//2))
>>> for i in range(len(img_array)):
    out.write(img_array[i])

    
>>> out.release()
>>> [img.shape for img in img_array]
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    [img.shape for img in img_array]
  File "<pyshell#107>", line 1, in <listcomp>
    [img.shape for img in img_array]
AttributeError: 'NoneType' object has no attribute 'shape'
>>> str(k).zfill(4)
'701721\tNOTFOUND'
>>> str(17).zfill
<built-in method zfill of str object at 0x04969840>
>>> str(17).zfill(4)
'0017'
>>> k
'701721\tNOTFOUND'
>>> img_array = [cv2.imread('C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\'+str(k).zfill(4)+'.png') for k in range(134)]
>>> set([img.shape for img in img_array])
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    set([img.shape for img in img_array])
  File "<pyshell#113>", line 1, in <listcomp>
    set([img.shape for img in img_array])
AttributeError: 'NoneType' object has no attribute 'shape'
>>> img=cv2.imread('C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\'+str(k).zfill(4)+'.png')
>>> img.shape
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    img.shape
AttributeError: 'NoneType' object has no attribute 'shape'
>>> 'C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\'+str(k).zfill(0)+'.png'
'C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\701721\tNOTFOUND.png'
>>> 'C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\'+str(0).zfill(4)+'.png'
'C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\0000.png'
>>> cv2.imread('C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\0000.png')
>>> img=cv2.imread(r'C:\Users\joshm\Documents\DiamondAge\Video3\0091.png')
>>> img
array([[[229, 229, 229],
        [229, 229, 229],
        [229, 229, 229],
        ...,
        [229, 229, 229],
        [230, 230, 230],
        [229, 229, 229]],

       [[229, 229, 229],
        [229, 229, 229],
        [229, 229, 229],
        ...,
        [228, 228, 228],
        [229, 229, 229],
        [228, 228, 228]],

       [[229, 229, 229],
        [229, 229, 229],
        [229, 229, 229],
        ...,
        [228, 228, 228],
        [229, 229, 229],
        [229, 229, 229]],

       ...,

       [[229, 229, 229],
        [229, 229, 229],
        [229, 229, 229],
        ...,
        [229, 229, 229],
        [229, 229, 229],
        [229, 229, 229]],

       [[229, 229, 229],
        [230, 230, 230],
        [229, 229, 229],
        ...,
        [230, 230, 230],
        [229, 229, 229],
        [229, 229, 229]],

       [[228, 228, 228],
        [229, 229, 229],
        [229, 229, 229],
        ...,
        [229, 229, 229],
        [230, 230, 230],
        [229, 229, 229]]], dtype=uint8)
>>> img_array = [cv2.imread('C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\'+str(k).zfill(4)+'.png') for k in range(1,134)]
>>> set([img.shape for img in img_array])
{(540, 960, 3)}
>>> out = cv2.VideoWriter(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, (540,960))
>>> for i in range(len(img_array)):
    out.write(img_array[i])

    
>>> out.release()
>>> out = cv2.VideoWriter(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, (540,960))
>>> for img in img_array:
    out.write(img)

    
>>> out
<VideoWriter 085C5190>
>>> out.release()
>>> out = cv2.VideoWriter(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3b.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, (540,960))
>>> for img in img_array:
    out.write(img)

    
>>> img_array[0].shape
(540, 960, 3)
>>> out.release()
>>> out = cv2.VideoWriter(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3b.avi',-1, 15, (540,960))
>>> r'C:\Users\joshm\Documents\DiamondAge\Video3\video3b.avi'
'C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\video3b.avi'
>>> for img in img_array:
    out.write(img)

    
>>> out.release()
>>> out = cv2.VideoWriter(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3.avi',-1, 15, (540,960))
>>> for img in img_array:
    out.write(img)

    
>>> out.release()
>>> from skvideo import io
>>> skvideo.io.vwrite(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3.mp4', images)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    skvideo.io.vwrite(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3.mp4', images)
NameError: name 'skvideo' is not defined
>>> io.vwrite(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3.mp4', images)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    io.vwrite(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3.mp4', images)
NameError: name 'images' is not defined
>>> io.vwrite(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3.mp4', img_array)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    io.vwrite(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3.mp4', img_array)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\skvideo\io\io.py", line 60, in vwrite
    assert _HAS_FFMPEG, "Cannot find installation of real FFmpeg (which comes with ffprobe)."
AssertionError: Cannot find installation of real FFmpeg (which comes with ffprobe).
>>> io.vwrite(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3.avi', img_array)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    io.vwrite(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3.avi', img_array)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\skvideo\io\io.py", line 60, in vwrite
    assert _HAS_FFMPEG, "Cannot find installation of real FFmpeg (which comes with ffprobe)."
AssertionError: Cannot find installation of real FFmpeg (which comes with ffprobe).
>>> out = cv2.VideoWriter(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3.avi',-1, 15, (540,960))
>>> out = cv2.VideoWriter(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3b.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, (540,960))
>>> for img in img_array:
    out.write(img)

    
>>> out.release()
>>> out = cv2.VideoWriter(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3b.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, (960,540))
>>> for img in img_array:
    out.write(img)

    
>>> out.release()
>>> img_array = [cv2.imread('C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\'+str(k).zfill(4)+'.png') for k in range(137)]
>>> out = cv2.VideoWriter(r'C:\Users\joshm\Documents\DiamondAge\Video3b\video3b.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, (960,540))
>>> for img in img_array:
    out.write(img)

    
>>> out.release()
>>> img_array = [cv2.imread('C:\\Users\\joshm\\Documents\\DiamondAge\\Video3\\'+str(k).zfill(4)+'.png') for k in range(142)]
>>> out = cv2.VideoWriter(r'C:\Users\joshm\Documents\DiamondAge\Video3b\video3c.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, (960,540))
>>> for img in img_array:
    out.write(img)

    
>>> out.release()
>>> out = cv2.VideoWriter(r'C:\Users\joshm\Documents\DiamondAge\Video3\video3c.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, (960,540))
>>> for img in img_array:
    out.write(img)

    
>>> out.release()
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER')
214 0 0 r 214
214 1 0 r 214
214 2 0 r 214
214 3 0 r 214
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    compile_function('EULER')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 634, in compile_function
    print_founds()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 677, in print_founds
    next_var = order.index(symbol2.symbol)+symbol2.offset
ValueError: 'F' is not in list
>>> order = ['E','Q','varr','F','f','n','N']
>>> compile_function('EULER')
214 0 0 r 214
214 1 0 r 214
214 2 0 r 214
214 3 0 r 214
214 f f l 218l
215 0 0 r 215
215 1 0 r 215
215 2 0 r 215
215 3 0 r 215
215 f f l 219l
222 0 2 r 306r
222 1 3 r 307r
222 2 2 r 222
222 3 3 r 222
222 f f l 322l
223 0 2 r 306r
223 1 3 r 307r
223 2 2 r 223
223 3 3 r 223
223 f f l 323l
230 0 0 r 230
230 1 0 r 230
230 2 0 r 230
230 3 0 r 230
230 f f r 338r
231 0 0 r 231
231 1 0 r 231
231 2 0 r 231
231 3 0 r 231
231 f f r 339r
238 0 0 r 238
238 1 1 r 238
238 2 0 r 238
238 3 1 r 238
238 N N l 242l
239 0 1 r 239
239 1 0 r 238
239 2 1 r 239
239 3 0 r 238
239 N * l 242l
246 0 0 r 246
246 1 1 l 218l
246 N N l 408l
254 0 0 r 254
254 1 1 r 254
254 2 0 r 254
254 3 1 r 254
254 E E l 258l
255 0 1 r 254
255 1 0 r 255
255 2 1 r 254
255 3 0 r 255
255 E * * halt
262 0 2 l 266l
262 1 3 l 267l
262 2 2 r 262
262 3 3 r 262
262 E E l 282l
263 0 2 l 266l
263 1 3 l 267l
263 2 2 r 263
263 3 3 r 263
263 E E l 283l
270 0 2 r 258r
270 1 2 r 258r
270 2 2 r 270
270 3 3 r 270
270 N N * 282*
271 0 3 r 259r
271 1 3 r 259r
271 2 2 r 271
271 3 3 r 271
271 N N * 283*
286 0 0 r 286
286 1 1 r 286
286 2 0 r 286
286 3 1 r 286
286 E E l 290l
287 0 0 r 287
287 1 1 r 287
287 2 0 r 287
287 3 1 r 287
287 E E l 291l
294 0 0 r 294
294 1 1 r 294
294 2 0 r 294
294 3 1 r 294
294 N N l 210l
295 0 0 r 295
295 1 1 r 295
295 2 0 r 295
295 3 1 r 295
295 N N l 211l
310 0 2 l 218l
310 1 2 l 218l
310 2 2 r 310
310 3 3 r 310
310 n n l 322l
311 0 3 l 219l
311 1 3 l 219l
311 2 2 r 311
311 3 3 r 311
311 n n l 323l
326 0 0 r 326
326 1 1 r 326
326 2 0 r 326
326 3 1 r 326
326 f f * 330*
327 0 0 r 327
327 1 1 r 327
327 2 0 r 327
327 3 1 r 327
327 f f * 331*
334 0 0 r 334
334 1 1 r 334
334 2 0 r 334
334 3 1 r 334
334 n n l 226l
335 0 0 r 335
335 1 1 r 335
335 2 0 r 335
335 3 1 r 335
335 n n l 227l
342 0 2 l 346l
342 1 3 l 368l
342 2 2 r 342
342 3 3 r 342
342 N N l 360l
343 0 2 l 346l
343 1 3 l 368l
343 2 2 r 343
343 3 3 r 343
343 N N l 361l
350 0 0 r 350
350 1 0 r 351
350 2 0 r 350
350 3 0 r 351
350 n * * 338*
351 0 1 r 350
351 1 1 r 351
351 2 1 r 350
351 3 1 r 351
351 n * * 353*
356 0 2 r 356
356 1 3 l 361l
356 2 2 r 356
356 3 3 r 356
356 N N l 360l
357 0 2 r 356
357 1 3 l 361l
357 2 2 r 357
357 3 3 r 357
357 N N l 361l
364 0 0 r 364
364 1 1 r 364
364 2 0 r 364
364 3 1 r 364
364 N N l 234l
365 0 0 r 365
365 1 1 r 365
365 2 0 r 365
365 3 1 r 365
365 N N * halt
372 0 2 l 376l
372 1 3 l 377l
372 2 2 r 372
372 3 3 r 372
372 n * l 392l
373 0 2 l 377l
373 1 3 l 378l
373 2 2 r 373
373 3 3 r 373
373 n n l 393l
380 0 2 r 368r
380 1 3 r 368r
380 2 2 r 380
380 3 3 r 380
380 f f * 392*
381 0 3 r 368r
381 1 2 r 369r
381 2 2 r 381
381 3 3 r 381
381 f f * 393*
382 0 2 r 369r
382 1 3 r 369r
382 2 2 r 382
382 3 3 r 382
382 f f * 392*
396 0 0 r 396
396 1 1 r 396
396 2 0 r 396
396 3 1 r 396
396 n n l 400l
397 0 0 r 397
397 1 1 r 397
397 2 0 r 397
397 3 1 r 397
397 n n l 401l
404 0 0 r 404
404 1 1 r 404
404 2 0 r 404
404 3 1 r 404
404 f f * 346*
405 0 0 r 405
405 1 1 r 405
405 2 0 r 405
405 3 1 r 405
405 f f r 361r
412 0 0 r 412
412 1 0 r 412
412 2 0 r 412
412 3 0 r 412
412 F F l 416l
420 0 0 r 420
420 1 0 r 421
420 2 0 r 420
420 3 0 r 421
420 F * * 438*
421 0 1 r 420
421 1 1 r 421
421 2 1 r 420
421 3 1 r 421
421 F * * 439*
426 0 3 r 470r
426 1 3 r 470r
426 2 2 l 426
426 3 3 l 426
426 Q Q * 430*
427 0 2 r 416r
427 1 2 r 416r
427 2 2 l 427
427 3 3 l 427
427 Q * * 430*
434 0 0 r 434
434 1 1 r 434
434 2 0 r 434
434 3 1 r 434
434 r r l 510l
442 0 2 r 446r
442 1 3 r 447r
442 2 2 l 442
442 3 3 l 442
442 r r * 454*
443 0 2 r 446r
443 1 3 r 447r
443 2 2 l 443
443 3 3 l 443
443 r r * 455*
450 0 2 l 438l
450 1 3 l 455l
450 2 2 l 450
450 3 3 l 450
450 F F l 454l
451 0 2 l 454l
451 1 3 l 438l
451 2 2 l 451
451 3 3 l 451
451 F F l 455l
458 0 0 r 458
458 1 1 r 458
458 2 0 r 458
458 3 1 r 458
458 F F * 462*
459 0 0 r 459
459 1 1 r 459
459 2 0 r 459
459 3 1 r 459
459 F F * 463*
466 0 0 r 466
466 1 1 r 466
466 2 0 r 466
466 3 1 r 466
466 f f l 422l
467 0 0 r 467
467 1 1 r 467
467 2 0 r 467
467 3 1 r 467
467 f f l 423l
474 0 2 l 478l
474 1 3 l 479l
474 2 2 r 474
474 3 3 r 474
474 f f l 494l
475 0 2 l 479l
475 1 3 l 479l
475 2 2 r 475
475 3 3 r 475
475 f f l 494l
482 0 2 r 470r
482 1 3 r 471r
482 2 2 r 482
482 3 3 r 482
482 F F * 494*
483 0 3 r 470r
483 1 2 r 470r
483 2 2 r 483
483 3 3 r 483
483 F F * 494*
498 0 0 r 498
498 1 1 r 498
498 2 0 r 498
498 3 1 r 498
498 f f l 502l
506 0 0 r 506
506 1 1 r 506
506 2 0 r 506
506 3 1 r 506
506 F F l 416l
514 0 2 l 518l
514 1 3 l 519l
514 2 2 r 514
514 3 3 r 514
514 r * l 534l
515 0 2 l 519l
515 1 3 l 520l
515 2 2 r 515
515 3 3 r 515
515 r r l 534l
522 0 2 r 510r
522 1 3 r 510r
522 2 2 r 522
522 3 3 r 522
522 Q Q * 534*
523 0 3 r 510r
523 1 2 r 511r
523 2 2 r 523
523 3 3 r 523
523 Q Q * 534*
524 0 2 r 511r
524 1 3 r 511r
524 2 2 r 524
524 3 3 r 524
524 Q Q * 534*
538 0 0 r 538
538 1 1 r 538
538 2 0 r 538
538 3 1 r 538
538 r r l 542l
546 0 0 r 546
546 1 1 r 546
546 2 0 r 546
546 3 1 r 546
546 Q Q r 250r
258l N * r 262
258l * * l *
258r N * r 262
258r * * r *
218l F * r 222
218l * * l *
219l F * r 223
219l * * l *
306r f * r 310
306r * * r *
307r f * r 311
307r * * r *
322l F * r 326
322l * * l *
323l F * r 327
323l * * l *
338r n * r 342
338r * * r *
338* n * r 342
338* * * * *
339r n * r 343
339r * * r *
242l n * r 246
242l * * l *
408l r * r 412
408l * * l *
266l n * r 270
266l * * l *
267l n * r 271
267l * * l *
282l N * r 286
282l * * l *
282* N * r 286
282* * * * *
283l N * r 287
283l * * l *
283* N * r 287
283* * * * *
259r N * r 263
259r * * r *
290l n * r 294
290l * * l *
291l n * r 295
291l * * l *
210l F * r 214
210l * * l *
211l F * r 215
211l * * l *
330* f * r 334
330* * * * *
331* f * r 335
331* * * * *
226l F * r 230
226l * * l *
227l F * r 231
227l * * l *
346l f * r 350
346l * * l *
346* f * r 350
346* * * * *
368l f * r 372
368l * * l *
368r f * r 372
368r * * r *
360l n * r 364
360l * * l *
361l n * r 365
361l * * l *
361r n * r 365
361r * * r *
353* n * r 357
353* * * * *
234l n * r 239
234l * * l *
376l F * r 380
376l * * l *
377l F * r 381
377l * * l *
392l f * r 396
392l * * l *
392* f * r 396
392* * * * *
378l F * r 382
378l * * l *
393l f * r 397
393l * * l *
393* f * r 397
393* * * * *
369r f * r 373
369r * * r *
400l F * r 404
400l * * l *
401l F * r 405
401l * * l *
416l r * r 421
416l * * l *
416r r * r 421
416r * * r *
438l F * l 442
438l * * l *
438* F * l 442
438* * * * *
439* F * l 443
439* * * * *
470r F * r 474
470r * * r *
430* Q * r 434
430* * * * *
510l Q * r 514
510l * * l *
510r Q * r 514
510r * * r *
446r f * l 450
446r * * r *
447r f * l 451
447r * * r *
454l r * r 458
454l * * l *
454* r * r 458
454* * * * *
455l r * r 459
455l * * l *
455* r * r 459
455* * * * *
462* F * r 466
462* * * * *
463* F * r 467
463* * * * *
422l r * l 426
422l * * l *
423l r * l 427
423l * * l *
478l r * r 482
478l * * l *
479l r * r 483
479l * * l *
494l F * r 498
494l * * l *
494* F * r 498
494* * * * *
471r F * r 475
471r * * r *
502l r * r 506
502l * * l *
518l E * r 522
518l * * l *
519l E * r 523
519l * * l *
534l Q * r 538
534l * * l *
534* Q * r 538
534* * * * *
520l E * r 524
520l * * l *
511r Q * r 515
511r * * r *
542l E * r 546
542l * * l *
250r N * r 255
250r * * r *
>>> len(used_states)
135
>>> 135-17
118
>>> quasis[0]
End(is_start=True, next_quasis=[258])
>>> directions[258]
{'l', 'r'}
>>> order
['E', 'Q', 'varr', 'F', 'f', 'n', 'N']
>>> for sym in order:
	print(sym[-1]+'0'*8,end='')

	
E00000000Q00000000r00000000F00000000f00000000n00000000N00000000
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> order=['E', 'Q', 'varr', 'F', 'f', 'n', 'N']
>>> compile_function('EULER')
215 0 0 r 215
215 1 0 r 215
215 2 0 r 215
215 3 0 r 215
215 f f l 219l
216 0 0 r 216
216 1 0 r 216
216 2 0 r 216
216 3 0 r 216
216 f f l 220l
223 0 2 r 307r
223 1 3 r 308r
223 2 2 r 223
223 3 3 r 223
223 f f l 323l
224 0 2 r 307r
224 1 3 r 308r
224 2 2 r 224
224 3 3 r 224
224 f f l 324l
231 0 0 r 231
231 1 0 r 231
231 2 0 r 231
231 3 0 r 231
231 f f r 339r
232 0 0 r 232
232 1 0 r 232
232 2 0 r 232
232 3 0 r 232
232 f f r 340r
239 0 0 r 239
239 1 1 r 239
239 2 0 r 239
239 3 1 r 239
239 N N l 243l
240 0 1 r 240
240 1 0 r 239
240 2 1 r 240
240 3 0 r 239
240 N * l 243l
247 0 0 r 247
247 1 1 l 219l
247 N N l 409l
255 0 0 r 255
255 1 1 r 255
255 2 0 r 255
255 3 1 r 255
255 E E l 259l
256 0 1 r 255
256 1 0 r 256
256 2 1 r 255
256 3 0 r 256
256 E * * halt
263 0 2 l 267l
263 1 3 l 268l
263 2 2 r 263
263 3 3 r 263
263 E E l 283l
264 0 2 l 267l
264 1 3 l 268l
264 2 2 r 264
264 3 3 r 264
264 E E l 284l
271 0 2 r 259r
271 1 2 r 259r
271 2 2 r 271
271 3 3 r 271
271 N N * 283*
272 0 3 r 260r
272 1 3 r 260r
272 2 2 r 272
272 3 3 r 272
272 N N * 284*
287 0 0 r 287
287 1 1 r 287
287 2 0 r 287
287 3 1 r 287
287 E E l 291l
288 0 0 r 288
288 1 1 r 288
288 2 0 r 288
288 3 1 r 288
288 E E l 292l
295 0 0 r 295
295 1 1 r 295
295 2 0 r 295
295 3 1 r 295
295 N N l 211l
296 0 0 r 296
296 1 1 r 296
296 2 0 r 296
296 3 1 r 296
296 N N l 212l
311 0 2 l 219l
311 1 2 l 219l
311 2 2 r 311
311 3 3 r 311
311 n n l 323l
312 0 3 l 220l
312 1 3 l 220l
312 2 2 r 312
312 3 3 r 312
312 n n l 324l
327 0 0 r 327
327 1 1 r 327
327 2 0 r 327
327 3 1 r 327
327 f f * 331*
328 0 0 r 328
328 1 1 r 328
328 2 0 r 328
328 3 1 r 328
328 f f * 332*
335 0 0 r 335
335 1 1 r 335
335 2 0 r 335
335 3 1 r 335
335 n n l 227l
336 0 0 r 336
336 1 1 r 336
336 2 0 r 336
336 3 1 r 336
336 n n l 228l
343 0 2 l 347l
343 1 3 l 369l
343 2 2 r 343
343 3 3 r 343
343 N N l 361l
344 0 2 l 347l
344 1 3 l 369l
344 2 2 r 344
344 3 3 r 344
344 N N l 362l
351 0 0 r 351
351 1 0 r 352
351 2 0 r 351
351 3 0 r 352
351 n n * 339*
352 0 1 r 351
352 1 1 r 352
352 2 1 r 351
352 3 1 r 352
352 n n * 354*
357 0 2 r 357
357 1 3 l 362l
357 2 2 r 357
357 3 3 r 357
357 N N l 361l
358 0 2 r 357
358 1 3 l 362l
358 2 2 r 358
358 3 3 r 358
358 N N l 362l
365 0 0 r 365
365 1 1 r 365
365 2 0 r 365
365 3 1 r 365
365 N N l 235l
366 0 0 r 366
366 1 1 r 366
366 2 0 r 366
366 3 1 r 366
366 N N * halt
373 0 2 l 377l
373 1 3 l 378l
373 2 2 r 373
373 3 3 r 373
373 n n l 393l
374 0 2 l 378l
374 1 3 l 379l
374 2 2 r 374
374 3 3 r 374
374 n n l 394l
381 0 2 r 369r
381 1 3 r 369r
381 2 2 r 381
381 3 3 r 381
381 f f * 393*
382 0 3 r 369r
382 1 2 r 370r
382 2 2 r 382
382 3 3 r 382
382 f f * 394*
383 0 2 r 370r
383 1 3 r 370r
383 2 2 r 383
383 3 3 r 383
383 f f * 393*
397 0 0 r 397
397 1 1 r 397
397 2 0 r 397
397 3 1 r 397
397 n n l 401l
398 0 0 r 398
398 1 1 r 398
398 2 0 r 398
398 3 1 r 398
398 n n l 402l
405 0 0 r 405
405 1 1 r 405
405 2 0 r 405
405 3 1 r 405
405 f f * 347*
406 0 0 r 406
406 1 1 r 406
406 2 0 r 406
406 3 1 r 406
406 f f r 362r
413 0 0 r 413
413 1 0 r 413
413 2 0 r 413
413 3 0 r 413
413 F F l 417l
421 0 0 r 421
421 1 0 r 422
421 2 0 r 421
421 3 0 r 422
421 F F * 439*
422 0 1 r 421
422 1 1 r 422
422 2 1 r 421
422 3 1 r 422
422 F F * 440*
427 0 3 r 471r
427 1 3 r 471r
427 2 2 l 427
427 3 3 l 427
427 Q Q * 431*
428 0 2 r 417r
428 1 2 r 417r
428 2 2 l 428
428 3 3 l 428
428 Q * * 431*
435 0 0 r 435
435 1 1 r 435
435 2 0 r 435
435 3 1 r 435
435 r r l 511l
443 0 2 r 447r
443 1 3 r 448r
443 2 2 l 443
443 3 3 l 443
443 r r * 455*
444 0 2 r 447r
444 1 3 r 448r
444 2 2 l 444
444 3 3 l 444
444 r r * 456*
451 0 2 l 439l
451 1 3 l 456l
451 2 2 l 451
451 3 3 l 451
451 F F l 455l
452 0 2 l 455l
452 1 3 l 439l
452 2 2 l 452
452 3 3 l 452
452 F F l 456l
459 0 0 r 459
459 1 1 r 459
459 2 0 r 459
459 3 1 r 459
459 F F * 463*
460 0 0 r 460
460 1 1 r 460
460 2 0 r 460
460 3 1 r 460
460 F F * 464*
467 0 0 r 467
467 1 1 r 467
467 2 0 r 467
467 3 1 r 467
467 f f l 423l
468 0 0 r 468
468 1 1 r 468
468 2 0 r 468
468 3 1 r 468
468 f f l 424l
475 0 2 l 479l
475 1 3 l 480l
475 2 2 r 475
475 3 3 r 475
475 f f l 495l
476 0 2 l 480l
476 1 3 l 480l
476 2 2 r 476
476 3 3 r 476
476 f f l 495l
483 0 2 r 471r
483 1 3 r 472r
483 2 2 r 483
483 3 3 r 483
483 F F * 495*
484 0 3 r 471r
484 1 2 r 471r
484 2 2 r 484
484 3 3 r 484
484 F F * 495*
499 0 0 r 499
499 1 1 r 499
499 2 0 r 499
499 3 1 r 499
499 f f l 503l
507 0 0 r 507
507 1 1 r 507
507 2 0 r 507
507 3 1 r 507
507 F F l 417l
515 0 2 l 519l
515 1 3 l 520l
515 2 2 r 515
515 3 3 r 515
515 r * l 535l
516 0 2 l 520l
516 1 3 l 521l
516 2 2 r 516
516 3 3 r 516
516 r r l 535l
523 0 2 r 511r
523 1 3 r 511r
523 2 2 r 523
523 3 3 r 523
523 Q Q * 535*
524 0 3 r 511r
524 1 2 r 512r
524 2 2 r 524
524 3 3 r 524
524 Q Q * 535*
525 0 2 r 512r
525 1 3 r 512r
525 2 2 r 525
525 3 3 r 525
525 Q Q * 535*
539 0 0 r 539
539 1 1 r 539
539 2 0 r 539
539 3 1 r 539
539 r r l 543l
547 0 0 r 547
547 1 1 r 547
547 2 0 r 547
547 3 1 r 547
547 Q Q r 251r
259r N * r 263
259r * * r *
259l N * r 263
259l * * l *
219l F * r 223
219l * * l *
220l F * r 224
220l * * l *
307r f * r 311
307r * * r *
308r f * r 312
308r * * r *
323l F * r 327
323l * * l *
324l F * r 328
324l * * l *
339* n * r 343
339* * * * *
339r n * r 343
339r * * r *
340r n * r 344
340r * * r *
243l n * r 247
243l * * l *
409l r * r 413
409l * * l *
267l n * r 271
267l * * l *
268l n * r 272
268l * * l *
283* N * r 287
283* * * * *
283l N * r 287
283l * * l *
284* N * r 288
284* * * * *
284l N * r 288
284l * * l *
260r N * r 264
260r * * r *
291l n * r 295
291l * * l *
292l n * r 296
292l * * l *
211l F * r 215
211l * * l *
212l F * r 216
212l * * l *
331* f * r 335
331* * * * *
332* f * r 336
332* * * * *
227l F * r 231
227l * * l *
228l F * r 232
228l * * l *
347* f * r 351
347* * * * *
347l f * r 351
347l * * l *
369r f * r 373
369r * * r *
369l f * r 373
369l * * l *
361l n * r 365
361l * * l *
362r n * r 366
362r * * r *
362l n * r 366
362l * * l *
354* n * r 358
354* * * * *
235l n * r 240
235l * * l *
377l F * r 381
377l * * l *
378l F * r 382
378l * * l *
393* f * r 397
393* * * * *
393l f * r 397
393l * * l *
379l F * r 383
379l * * l *
394* f * r 398
394* * * * *
394l f * r 398
394l * * l *
370r f * r 374
370r * * r *
401l F * r 405
401l * * l *
402l F * r 406
402l * * l *
417r r * r 422
417r * * r *
417l r * r 422
417l * * l *
439* F * l 443
439* * * * *
439l F * l 443
439l * * l *
440* F * l 444
440* * * * *
471r F * r 475
471r * * r *
431* Q * r 435
431* * * * *
511r Q * r 515
511r * * r *
511l Q * r 515
511l * * l *
447r f * l 451
447r * * r *
448r f * l 452
448r * * r *
455* r * r 459
455* * * * *
455l r * r 459
455l * * l *
456* r * r 460
456* * * * *
456l r * r 460
456l * * l *
463* F * r 467
463* * * * *
464* F * r 468
464* * * * *
423l r * l 427
423l * * l *
424l r * l 428
424l * * l *
479l r * r 483
479l * * l *
480l r * r 484
480l * * l *
495* F * r 499
495* * * * *
495l F * r 499
495l * * l *
472r F * r 476
472r * * r *
503l r * r 507
503l * * l *
519l E * r 523
519l * * l *
520l E * r 524
520l * * l *
535* Q * r 539
535* * * * *
535l Q * r 539
535l * * l *
521l E * r 525
521l * * l *
512r Q * r 516
512r * * r *
543l E * r 547
543l * * l *
251r N * r 256
251r * * r *
>>> quasis[0]
End(is_start=True, next_quasis=[259])
>>> directions[259]
{'r', 'l'}
>>> len(used_states)
135
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> order=['E', 'Q', 'varr', 'F', 'f', 'n', 'N']
>>> compile_function('EULER')
215 0 0 r 215
215 1 0 r 215
215 2 0 r 215
215 3 0 r 215
215 f f l 219l
216 0 0 r 216
216 1 0 r 216
216 2 0 r 216
216 3 0 r 216
216 f f l 220l
223 0 2 r 307r
223 1 3 r 308r
223 2 2 r 223
223 3 3 r 223
223 f f l 323l
224 0 2 r 307r
224 1 3 r 308r
224 2 2 r 224
224 3 3 r 224
224 f f l 324l
231 0 0 r 231
231 1 0 r 231
231 2 0 r 231
231 3 0 r 231
231 f f r 339r
232 0 0 r 232
232 1 0 r 232
232 2 0 r 232
232 3 0 r 232
232 f f r 340r
239 0 0 r 239
239 1 1 r 239
239 2 0 r 239
239 3 1 r 239
239 N N l 243l
240 0 1 r 240
240 1 0 r 239
240 2 1 r 240
240 3 0 r 239
240 N * l 243l
247 0 0 r 247
247 1 1 l 219l
247 N N l 409l
255 0 0 r 255
255 1 1 r 255
255 2 0 r 255
255 3 1 r 255
255 E E l 259l
256 0 1 r 255
256 1 0 r 256
256 2 1 r 255
256 3 0 r 256
256 E * * halt
263 0 2 l 267l
263 1 3 l 268l
263 2 2 r 263
263 3 3 r 263
263 E E l 283l
264 0 2 l 267l
264 1 3 l 268l
264 2 2 r 264
264 3 3 r 264
264 E E l 284l
271 0 2 r 259r
271 1 2 r 259r
271 2 2 r 271
271 3 3 r 271
271 N N * 283*
272 0 3 r 260r
272 1 3 r 260r
272 2 2 r 272
272 3 3 r 272
272 N N * 284*
287 0 0 r 287
287 1 1 r 287
287 2 0 r 287
287 3 1 r 287
287 E E l 291l
288 0 0 r 288
288 1 1 r 288
288 2 0 r 288
288 3 1 r 288
288 E E l 292l
295 0 0 r 295
295 1 1 r 295
295 2 0 r 295
295 3 1 r 295
295 N N l 211l
296 0 0 r 296
296 1 1 r 296
296 2 0 r 296
296 3 1 r 296
296 N N l 212l
311 0 2 l 219l
311 1 2 l 219l
311 2 2 r 311
311 3 3 r 311
311 n n l 323l
312 0 3 l 220l
312 1 3 l 220l
312 2 2 r 312
312 3 3 r 312
312 n n l 324l
327 0 0 r 327
327 1 1 r 327
327 2 0 r 327
327 3 1 r 327
327 f f * 331*
328 0 0 r 328
328 1 1 r 328
328 2 0 r 328
328 3 1 r 328
328 f f * 332*
335 0 0 r 335
335 1 1 r 335
335 2 0 r 335
335 3 1 r 335
335 n n l 227l
336 0 0 r 336
336 1 1 r 336
336 2 0 r 336
336 3 1 r 336
336 n n l 228l
343 0 2 l 347l
343 1 3 l 369l
343 2 2 r 343
343 3 3 r 343
343 N N l 361l
344 0 2 l 347l
344 1 3 l 369l
344 2 2 r 344
344 3 3 r 344
344 N N l 362l
351 0 0 r 351
351 1 0 r 352
351 2 0 r 351
351 3 0 r 352
351 n * * 339*
352 0 1 r 351
352 1 1 r 352
352 2 1 r 351
352 3 1 r 352
352 n * * 354*
357 0 2 r 357
357 1 3 l 362l
357 2 2 r 357
357 3 3 r 357
357 N N l 361l
358 0 2 r 357
358 1 3 l 362l
358 2 2 r 358
358 3 3 r 358
358 N N l 362l
365 0 0 r 365
365 1 1 r 365
365 2 0 r 365
365 3 1 r 365
365 N N l 235l
366 0 0 r 366
366 1 1 r 366
366 2 0 r 366
366 3 1 r 366
366 N N * halt
373 0 2 l 377l
373 1 3 l 378l
373 2 2 r 373
373 3 3 r 373
373 n * l 393l
374 0 2 l 378l
374 1 3 l 379l
374 2 2 r 374
374 3 3 r 374
374 n * l 394l
381 0 2 r 369r
381 1 3 r 369r
381 2 2 r 381
381 3 3 r 381
381 f f * 393*
382 0 3 r 369r
382 1 2 r 370r
382 2 2 r 382
382 3 3 r 382
382 f f * 394*
383 0 2 r 370r
383 1 3 r 370r
383 2 2 r 383
383 3 3 r 383
383 f f * 393*
397 0 0 r 397
397 1 1 r 397
397 2 0 r 397
397 3 1 r 397
397 n n l 401l
398 0 0 r 398
398 1 1 r 398
398 2 0 r 398
398 3 1 r 398
398 n n l 402l
405 0 0 r 405
405 1 1 r 405
405 2 0 r 405
405 3 1 r 405
405 f f * 347*
406 0 0 r 406
406 1 1 r 406
406 2 0 r 406
406 3 1 r 406
406 f f r 362r
413 0 0 r 413
413 1 0 r 413
413 2 0 r 413
413 3 0 r 413
413 F F l 417l
421 0 0 r 421
421 1 0 r 422
421 2 0 r 421
421 3 0 r 422
421 F * * 439*
422 0 1 r 421
422 1 1 r 422
422 2 1 r 421
422 3 1 r 422
422 F F * 440*
427 0 3 r 471r
427 1 3 r 471r
427 2 2 l 427
427 3 3 l 427
427 Q Q * 431*
428 0 2 r 417r
428 1 2 r 417r
428 2 2 l 428
428 3 3 l 428
428 Q * * 431*
435 0 0 r 435
435 1 1 r 435
435 2 0 r 435
435 3 1 r 435
435 r r l 511l
443 0 2 r 447r
443 1 3 r 448r
443 2 2 l 443
443 3 3 l 443
443 r r * 455*
444 0 2 r 447r
444 1 3 r 448r
444 2 2 l 444
444 3 3 l 444
444 r r * 456*
451 0 2 l 439l
451 1 3 l 456l
451 2 2 l 451
451 3 3 l 451
451 F * l 455l
452 0 2 l 455l
452 1 3 l 439l
452 2 2 l 452
452 3 3 l 452
452 F * l 456l
459 0 0 r 459
459 1 1 r 459
459 2 0 r 459
459 3 1 r 459
459 F F * 463*
460 0 0 r 460
460 1 1 r 460
460 2 0 r 460
460 3 1 r 460
460 F F * 464*
467 0 0 r 467
467 1 1 r 467
467 2 0 r 467
467 3 1 r 467
467 f f l 423l
468 0 0 r 468
468 1 1 r 468
468 2 0 r 468
468 3 1 r 468
468 f f l 424l
475 0 2 l 479l
475 1 3 l 480l
475 2 2 r 475
475 3 3 r 475
475 f f l 495l
476 0 2 l 480l
476 1 3 l 480l
476 2 2 r 476
476 3 3 r 476
476 f f l 495l
483 0 2 r 471r
483 1 3 r 472r
483 2 2 r 483
483 3 3 r 483
483 F F * 495*
484 0 3 r 471r
484 1 2 r 471r
484 2 2 r 484
484 3 3 r 484
484 F F * 495*
499 0 0 r 499
499 1 1 r 499
499 2 0 r 499
499 3 1 r 499
499 f f l 503l
507 0 0 r 507
507 1 1 r 507
507 2 0 r 507
507 3 1 r 507
507 F F l 417l
515 0 2 l 519l
515 1 3 l 520l
515 2 2 r 515
515 3 3 r 515
515 r r l 535l
516 0 2 l 520l
516 1 3 l 521l
516 2 2 r 516
516 3 3 r 516
516 r r l 535l
523 0 2 r 511r
523 1 3 r 511r
523 2 2 r 523
523 3 3 r 523
523 Q Q * 535*
524 0 3 r 511r
524 1 2 r 512r
524 2 2 r 524
524 3 3 r 524
524 Q Q * 535*
525 0 2 r 512r
525 1 3 r 512r
525 2 2 r 525
525 3 3 r 525
525 Q Q * 535*
539 0 0 r 539
539 1 1 r 539
539 2 0 r 539
539 3 1 r 539
539 r r l 543l
547 0 0 r 547
547 1 1 r 547
547 2 0 r 547
547 3 1 r 547
547 Q Q r 251r
259l N * r 263
259l * * l *
259r N * r 263
259r * * r *
219l F * r 223
219l * * l *
220l F * r 224
220l * * l *
307r f * r 311
307r * * r *
308r f * r 312
308r * * r *
323l F * r 327
323l * * l *
324l F * r 328
324l * * l *
339* n * r 343
339* * * * *
339r n * r 343
339r * * r *
340r n * r 344
340r * * r *
243l n * r 247
243l * * l *
409l r * r 413
409l * * l *
267l n * r 271
267l * * l *
268l n * r 272
268l * * l *
283* N * r 287
283* * * * *
283l N * r 287
283l * * l *
284* N * r 288
284* * * * *
284l N * r 288
284l * * l *
260r N * r 264
260r * * r *
291l n * r 295
291l * * l *
292l n * r 296
292l * * l *
211l F * r 215
211l * * l *
212l F * r 216
212l * * l *
331* f * r 335
331* * * * *
332* f * r 336
332* * * * *
227l F * r 231
227l * * l *
228l F * r 232
228l * * l *
347* f * r 351
347* * * * *
347l f * r 351
347l * * l *
369l f * r 373
369l * * l *
369r f * r 373
369r * * r *
361l n * r 365
361l * * l *
362l n * r 366
362l * * l *
362r n * r 366
362r * * r *
354* n * r 358
354* * * * *
235l n * r 240
235l * * l *
377l F * r 381
377l * * l *
378l F * r 382
378l * * l *
393* f * r 397
393* * * * *
393l f * r 397
393l * * l *
379l F * r 383
379l * * l *
394* f * r 398
394* * * * *
394l f * r 398
394l * * l *
370r f * r 374
370r * * r *
401l F * r 405
401l * * l *
402l F * r 406
402l * * l *
417l r * r 422
417l * * l *
417r r * r 422
417r * * r *
439* F * l 443
439* * * * *
439l F * l 443
439l * * l *
440* F * l 444
440* * * * *
471r F * r 475
471r * * r *
431* Q * r 435
431* * * * *
511l Q * r 515
511l * * l *
511r Q * r 515
511r * * r *
447r f * l 451
447r * * r *
448r f * l 452
448r * * r *
455* r * r 459
455* * * * *
455l r * r 459
455l * * l *
456* r * r 460
456* * * * *
456l r * r 460
456l * * l *
463* F * r 467
463* * * * *
464* F * r 468
464* * * * *
423l r * l 427
423l * * l *
424l r * l 428
424l * * l *
479l r * r 483
479l * * l *
480l r * r 484
480l * * l *
495* F * r 499
495* * * * *
495l F * r 499
495l * * l *
472r F * r 476
472r * * r *
503l r * r 507
503l * * l *
519l E * r 523
519l * * l *
520l E * r 524
520l * * l *
535* Q * r 539
535* * * * *
535l Q * r 539
535l * * l *
521l E * r 525
521l * * l *
512r Q * r 516
512r * * r *
543l E * r 547
543l * * l *
251r N * r 256
251r * * r *
>>> quasis[0]
End(is_start=True, next_quasis=[259])
>>> '\n'.join([(k,quasis[k]) for k in range(len(quasis))])
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    '\n'.join([(k,quasis[k]) for k in range(len(quasis))])
TypeError: sequence item 0: expected str instance, tuple found
>>> '\n'.join([str(k,quasis[k]) for k in range(len(quasis))])
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    '\n'.join([str(k,quasis[k]) for k in range(len(quasis))])
  File "<pyshell#194>", line 1, in <listcomp>
    '\n'.join([str(k,quasis[k]) for k in range(len(quasis))])
TypeError: str() argument 2 must be str, not End
>>> '\n'.join([str((k,quasis[k])) for k in range(len(quasis))])

>>> print('\n'.join([str((k,quasis[k])) for k in range(len(quasis))]))

>>> 283 in used_states
True
>>> 284 in used_states
True
>>> quasis[128]
Step(instruction=5, is_found=True, variable='F', next_quasis=[147, 147], direction=None)
>>> quasis[5]
Instruction(STORE, vard=F, next_quasis=[147, 147])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> order=['E', 'Q', 'varr', 'F', 'f', 'n', 'N']
>>> compile_function('EULER')
215 0 0 r 215
215 1 0 r 215
215 2 0 r 215
215 Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    compile_function('EULER')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 634, in compile_function
    print_founds()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 699, in print_founds
    str(transition[2])+('' if step2.is_found else direction) if type(quasis[transition[2]])==State else 'halt')
KeyboardInterrupt
>>> print('\n'.join([str((k,quasis[k])) for k in range(len(quasis))]))

>>> instruction=quasis[5]
>>> use_temp = instruction.loadto=='TEMP'
>>> use_temp
True
>>> instruction.read
False
>>> if command=='LOAD':
        transitions={'0':['0', acc if use_temp else 0],'1':['1', acc if use_temp else 1]}
    elif command=='STORE':        
        transitions={'0':['0' if use_temp else str(acc), acc],'1':['1' if use_temp else str(acc), acc]}
        
SyntaxError: unindent does not match any outer indentation level
>>> if command=='LOAD':
        transitions={'0':['0', acc if use_temp else 0],'1':['1', acc if use_temp else 1]}
elif command=='STORE':
        transitions={'0':['0' if use_temp else str(acc), acc],'1':['1' if use_temp else str(acc), acc]}

        
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    if command=='LOAD':
NameError: name 'command' is not defined
>>> command=instruction.command
>>> if command=='LOAD':
        transitions={'0':['0', acc if use_temp else 0],'1':['1', acc if use_temp else 1]}
elif command=='STORE':
        transitions={'0':['0' if use_temp else str(acc), acc],'1':['1' if use_temp else str(acc), acc]}

        
Traceback (most recent call last):
  File "<pyshell#213>", line 4, in <module>
    transitions={'0':['0' if use_temp else str(acc), acc],'1':['1' if use_temp else str(acc), acc]}
NameError: name 'acc' is not defined
>>> acc=0
>>> if command=='LOAD':
        transitions={'0':['0', acc if use_temp else 0],'1':['1', acc if use_temp else 1]}
elif command=='STORE':
        transitions={'0':['0' if use_temp else str(acc), acc],'1':['1' if use_temp else str(acc), acc]}

        
>>> if transitions:
        for symbol in transitions:
            if instruction.read:
                transitions[symbol][0] += '\''
            transitions[symbol] += [step.next_quasis[0]]
        transitions.update(
            {'0\'':['0\'',acc,n_step],'1\'':['1\'',acc,n_step],
            Symbol(step.variable,1-instruction.big):[None,acc,step.next_quasis[1]]})

        
Traceback (most recent call last):
  File "<pyshell#218>", line 5, in <module>
    transitions[symbol] += [step.next_quasis[0]]
NameError: name 'step' is not defined
>>> step = quasis[128]
>>> if transitions:
        for symbol in transitions:
            if instruction.read:
                transitions[symbol][0] += '\''
            transitions[symbol] += [step.next_quasis[0]]
        transitions.update(
            {'0\'':['0\'',acc,n_step],'1\'':['1\'',acc,n_step],
            Symbol(step.variable,1-instruction.big):[None,acc,step.next_quasis[1]]})

        
Traceback (most recent call last):
  File "<pyshell#221>", line 7, in <module>
    {'0\'':['0\'',acc,n_step],'1\'':['1\'',acc,n_step],
NameError: name 'n_step' is not defined
>>> n_step=128
     
>>> if transitions:
        for symbol in transitions:
            if instruction.read:
                transitions[symbol][0] += '\''
            transitions[symbol] += [step.next_quasis[0]]
        transitions.update(
            {'0\'':['0\'',acc,n_step],'1\'':['1\'',acc,n_step],
            Symbol(step.variable,1-instruction.big):[None,acc,step.next_quasis[1]]})

     
>>> transitions
     
{'0': ['0', 0, 147, 147], '1': ['1', 0, 147, 147], "0'": ["0'", 0, 128], "1'": ["1'", 0, 128], Sym('F'+1): [None, 0, 147]}
>>> quasis[5].read
     
False
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER')
     
State(step=128, acc=0, transitions={'0': ['0', 0, 147], '1': ['1', 0, 147], "0'": ["0'", 0, 128], "1'": ["1'", 0, 128], Sym('F'+1): [None, 0, 147]}, direction=1) State(step=128, acc=1, transitions={'0': ['0', 1, 147], '1': ['1', 1, 147], "0'": ["0'", 1, 128], "1'": ["1'", 1, 128], Sym('F'+1): [None, 1, 147]}, direction=1)
State(step=128, acc=0, transitions={'0': ['1', 0, 147], '1': ['1', 0, 147], "0'": ["0'", 0, 128], "1'": ["1'", 0, 128], Sym('F'+1): [None, 0, 147]}, direction=1) State(step=128, acc=1, transitions={'0': ['1', 1, 147], '1': ['1', 1, 147], "0'": ["0'", 1, 128], "1'": ["1'", 1, 128], Sym('F'+1): [None, 1, 147]}, direction=1)
State(step=128, acc=0, transitions={'0': ['1', 0, 299], '1': ['1', 0, 299], "0'": ["0'", 0, 223], "1'": ["1'", 0, 223], Sym('F'+1): [None, 0, 299]}, direction=1) State(step=128, acc=1, transitions={'0': ['1', 1, 300], '1': ['1', 1, 300], "0'": ["0'", 1, 224], "1'": ["1'", 1, 224], Sym('F'+1): [None, 1, 300]}, direction=1)
State(step=128, acc=0, transitions={'0': ["0'", 0, 307], '1': ["1'", 1, 308], "0'": ["0'", 0, 223], "1'": ["1'", 0, 223], Sym('F'+1): [None, 0, 323]}, direction=1) State(step=128, acc=1, transitions={'0': ["0'", 0, 307], '1': ["1'", 1, 308], "0'": ["0'", 1, 224], "1'": ["1'", 1, 224], Sym('F'+1): [None, 1, 324]}, direction=1)
State(step=128, acc=0, transitions={'0': ["0'", 0, 307], '1': ["1'", 1, 308], "0'": ["0'", 0, 223], "1'": ["1'", 0, 223], Sym('F'+1): [Sym('F'+1), 0, 323]}, direction=1) State(step=128, acc=1, transitions={'0': ["0'", 0, 307], '1': ["1'", 1, 308], "0'": ["0'", 1, 224], "1'": ["1'", 1, 224], Sym('F'+1): [Sym('F'+1), 1, 324]}, direction=1)
215 0 0 r 215
215 1 0 r 215
215 2 0 r 215
215 3 0 r 215
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    compile_function('EULER')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 639, in compile_function
    print_founds()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 682, in print_founds
    next_var = order.index(symbol2.symbol)+symbol2.offset
ValueError: 'F' is not in list
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER')
     
>>> quasi = quasis[223]
     
>>> )))
    
SyntaxError: invalid syntax
>>> quasi
State(step=128, acc=0, transitions={'0': ['1', 0, 299], '1': ['1', 0, 299], "0'": ["0'", 0, 223], "1'": ["1'", 0, 223], Sym('F'+1): [None, 0, 299]}, direction=1)
>>> step = quasis[quasi.step]
>>> instruction = quasis[step.instruction]
>>> command = instruction.command
>>> step.is_found and command in ['LOAD','STORE']
True
>>> symbol = '0'
>>> quasi2 = quasis[quasi.transitions[symbol][2]]
>>> quasi2
State(step=147, acc=0, transitions={Sym('F'+0): [None, 0, 303]}, direction=None)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER')
Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    compile_function('EULER')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 627, in compile_function
    skip_searches()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 556, in skip_searches
    quasi.transitions[symbol] = quasi3.transitions[quasi.transitions[symbol][0]]
KeyError: None
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> ValueError: 'F' is not in list
SyntaxError: invalid syntax
>>> order = ['E','Q','varr','F','f','n','N']
>>> compile_function('EULER')
215 0 0 r 215
215 1 0 r 215
215 2 0 r 215
215 3 0 r 215
215 f f l 219l
216 0 0 r 216
216 1 0 r 216
216 2 0 r 216
216 3 0 r 216
216 f f l 220l
223 0 3 r 308r
223 1 3 r 308r
223 2 2 r 223
223 3 3 r 223
223 f f l 323l
224 0 3 r 308r
224 1 3 r 308r
224 2 2 r 224
224 3 3 r 224
224 f f l 324l
231 0 0 r 231
231 1 0 r 231
231 2 0 r 231
231 3 0 r 231
231 f f r 339r
232 0 0 r 232
232 1 0 r 232
232 2 0 r 232
232 3 0 r 232
232 f f r 340r
239 0 0 r 239
239 1 1 r 239
239 2 0 r 239
239 3 1 r 239
239 N N l 243l
240 0 1 r 240
240 1 0 r 239
240 2 1 r 240
240 3 0 r 239
240 N N l 243l
247 0 0 r 247
247 1 1 l 299l
247 N N l 409l
255 0 0 r 255
255 1 1 r 255
255 2 0 r 255
255 3 1 r 255
255 E E l 259l
256 0 1 r 255
256 1 0 r 256
256 2 1 r 255
256 3 0 r 256
256 E E * halt
263 0 2 l 267l
263 1 3 l 268l
263 2 2 r 263
263 3 3 r 263
263 E E l 283l
264 0 2 l 267l
264 1 3 l 268l
264 2 2 r 264
264 3 3 r 264
264 E E l 284l
271 0 2 r 259r
271 1 2 r 259r
271 2 2 r 271
271 3 3 r 271
271 N N * 283*
272 0 3 r 260r
272 1 3 r 260r
272 2 2 r 272
272 3 3 r 272
272 N N * 284*
287 0 0 r 287
287 1 1 r 287
287 2 0 r 287
287 3 1 r 287
287 E E l 291l
288 0 0 r 288
288 1 1 r 288
288 2 0 r 288
288 3 1 r 288
288 E E l 292l
295 0 0 r 295
295 1 1 r 295
295 2 0 r 295
295 3 1 r 295
295 N N l 211l
296 0 0 r 296
296 1 1 r 296
296 2 0 r 296
296 3 1 r 296
296 N N l 212l
303 0 2 r 307r
303 1 3 r 308r
303 2 2 r 303
303 3 3 r 303
303 f f l 323l
304 0 2 r 307r
304 1 3 r 308r
304 2 2 r 304
304 3 3 r 304
304 f f l 324l
311 0 2 l 299l
311 1 2 l 299l
311 2 2 r 311
311 3 3 r 311
311 n n l 323l
312 0 3 l 300l
312 1 3 l 300l
312 2 2 r 312
312 3 3 r 312
312 n n l 324l
327 0 0 r 327
327 1 1 r 327
327 2 0 r 327
327 3 1 r 327
327 f f * 331*
328 0 0 r 328
328 1 1 r 328
328 2 0 r 328
328 3 1 r 328
328 f f * 332*
335 0 0 r 335
335 1 1 r 335
335 2 0 r 335
335 3 1 r 335
335 n n l 227l
336 0 0 r 336
336 1 1 r 336
336 2 0 r 336
336 3 1 r 336
336 n n l 228l
343 0 2 l 347l
343 1 3 l 369l
343 2 2 r 343
343 3 3 r 343
343 N N l 361l
344 0 2 l 347l
344 1 3 l 369l
344 2 2 r 344
344 3 3 r 344
344 N N l 362l
351 0 0 r 351
351 1 0 r 352
351 2 0 r 351
351 3 0 r 352
351 n n * 339*
352 0 1 r 351
352 1 1 r 352
352 2 1 r 351
352 3 1 r 352
352 n * * 354*
357 0 2 r 357
357 1 3 l 362l
357 2 2 r 357
357 3 3 r 357
357 N N l 361l
358 0 2 r 357
358 1 3 l 362l
358 2 2 r 358
358 3 3 r 358
358 N N l 362l
365 0 0 r 365
365 1 1 r 365
365 2 0 r 365
365 3 1 r 365
365 N N l 235l
366 0 0 r 366
366 1 1 r 366
366 2 0 r 366
366 3 1 r 366
366 N N * halt
373 0 2 l 377l
373 1 3 l 378l
373 2 2 r 373
373 3 3 r 373
373 n * l 393l
374 0 2 l 378l
374 1 3 l 379l
374 2 2 r 374
374 3 3 r 374
374 n * l 394l
381 0 2 r 369r
381 1 3 r 369r
381 2 2 r 381
381 3 3 r 381
381 f * * 393*
382 0 3 r 369r
382 1 2 r 370r
382 2 2 r 382
382 3 3 r 382
382 f * * 394*
383 0 2 r 370r
383 1 3 r 370r
383 2 2 r 383
383 3 3 r 383
383 f * * 393*
397 0 0 r 397
397 1 1 r 397
397 2 0 r 397
397 3 1 r 397
397 n n l 401l
398 0 0 r 398
398 1 1 r 398
398 2 0 r 398
398 3 1 r 398
398 n n l 402l
405 0 0 r 405
405 1 1 r 405
405 2 0 r 405
405 3 1 r 405
405 f f * 347*
406 0 0 r 406
406 1 1 r 406
406 2 0 r 406
406 3 1 r 406
406 f f r 362r
413 0 0 r 413
413 1 0 r 413
413 2 0 r 413
413 3 0 r 413
413 F F l 417l
421 0 0 r 421
421 1 0 r 422
421 2 0 r 421
421 3 0 r 422
421 F F * 439*
422 0 1 r 421
422 1 1 r 422
422 2 1 r 421
422 3 1 r 422
422 F F * 440*
427 0 3 r 471r
427 1 3 r 471r
427 2 2 l 427
427 3 3 l 427
427 Q Q * 431*
428 0 2 r 417r
428 1 2 r 417r
428 2 2 l 428
428 3 3 l 428
428 Q Q * 431*
435 0 0 r 435
435 1 1 r 435
435 2 0 r 435
435 3 1 r 435
435 r r l 511l
443 0 2 r 447r
443 1 3 r 448r
443 2 2 l 443
443 3 3 l 443
443 r r * 455*
444 0 2 r 447r
444 1 3 r 448r
444 2 2 l 444
444 3 3 l 444
444 r r * 456*
451 0 2 l 439l
451 1 3 l 456l
451 2 2 l 451
451 3 3 l 451
451 F F l 455l
452 0 2 l 455l
452 1 3 l 439l
452 2 2 l 452
452 3 3 l 452
452 F F l 456l
459 0 0 r 459
459 1 1 r 459
459 2 0 r 459
459 3 1 r 459
459 F F * 463*
460 0 0 r 460
460 1 1 r 460
460 2 0 r 460
460 3 1 r 460
460 F F * 464*
467 0 0 r 467
467 1 1 r 467
467 2 0 r 467
467 3 1 r 467
467 f f l 423l
468 0 0 r 468
468 1 1 r 468
468 2 0 r 468
468 3 1 r 468
468 f f l 424l
475 0 2 l 479l
475 1 3 l 480l
475 2 2 r 475
475 3 3 r 475
475 f * l 495l
476 0 2 l 480l
476 1 3 l 480l
476 2 2 r 476
476 3 3 r 476
476 f * l 495l
483 0 2 r 471r
483 1 3 r 472r
483 2 2 r 483
483 3 3 r 483
483 F F * 495*
484 0 3 r 471r
484 1 2 r 471r
484 2 2 r 484
484 3 3 r 484
484 F F * 495*
499 0 0 r 499
499 1 1 r 499
499 2 0 r 499
499 3 1 r 499
499 f f l 503l
507 0 0 r 507
507 1 1 r 507
507 2 0 r 507
507 3 1 r 507
507 F F l 417l
515 0 2 l 519l
515 1 3 l 520l
515 2 2 r 515
515 3 3 r 515
515 r r l 535l
516 0 2 l 520l
516 1 3 l 521l
516 2 2 r 516
516 3 3 r 516
516 r r l 535l
523 0 2 r 511r
523 1 3 r 511r
523 2 2 r 523
523 3 3 r 523
523 Q Q * 535*
524 0 3 r 511r
524 1 2 r 512r
524 2 2 r 524
524 3 3 r 524
524 Q Q * 535*
525 0 2 r 512r
525 1 3 r 512r
525 2 2 r 525
525 3 3 r 525
525 Q Q * 535*
539 0 0 r 539
539 1 1 r 539
539 2 0 r 539
539 3 1 r 539
539 r r l 543l
547 0 0 r 547
547 1 1 r 547
547 2 0 r 547
547 3 1 r 547
547 Q Q r 251r
259r N * r 263
259r * * r *
259l N * r 263
259l * * l *
219l F * r 223
219l * * l *
220l F * r 224
220l * * l *
308r f * r 312
308r * * r *
323l F * r 327
323l * * l *
324l F * r 328
324l * * l *
339* n * r 343
339* * * * *
339r n * r 343
339r * * r *
340r n * r 344
340r * * r *
243l n * r 247
243l * * l *
299l F * r 303
299l * * l *
409l r * r 413
409l * * l *
267l n * r 271
267l * * l *
268l n * r 272
268l * * l *
283* N * r 287
283* * * * *
283l N * r 287
283l * * l *
284* N * r 288
284* * * * *
284l N * r 288
284l * * l *
260r N * r 264
260r * * r *
291l n * r 295
291l * * l *
292l n * r 296
292l * * l *
211l F * r 215
211l * * l *
212l F * r 216
212l * * l *
307r f * r 311
307r * * r *
300l F * r 304
300l * * l *
331* f * r 335
331* * * * *
332* f * r 336
332* * * * *
227l F * r 231
227l * * l *
228l F * r 232
228l * * l *
347* f * r 351
347* * * * *
347l f * r 351
347l * * l *
369r f * r 373
369r * * r *
369l f * r 373
369l * * l *
361l n * r 365
361l * * l *
362r n * r 366
362r * * r *
362l n * r 366
362l * * l *
354* n * r 358
354* * * * *
235l n * r 240
235l * * l *
377l F * r 381
377l * * l *
378l F * r 382
378l * * l *
393* f * r 397
393* * * * *
393l f * r 397
393l * * l *
379l F * r 383
379l * * l *
394* f * r 398
394* * * * *
394l f * r 398
394l * * l *
370r f * r 374
370r * * r *
401l F * r 405
401l * * l *
402l F * r 406
402l * * l *
417r r * r 422
417r * * r *
417l r * r 422
417l * * l *
439* F * l 443
439* * * * *
439l F * l 443
439l * * l *
440* F * l 444
440* * * * *
471r F * r 475
471r * * r *
431* Q * r 435
431* * * * *
511r Q * r 515
511r * * r *
511l Q * r 515
511l * * l *
447r f * l 451
447r * * r *
448r f * l 452
448r * * r *
455* r * r 459
455* * * * *
455l r * r 459
455l * * l *
456* r * r 460
456* * * * *
456l r * r 460
456l * * l *
463* F * r 467
463* * * * *
464* F * r 468
464* * * * *
423l r * l 427
423l * * l *
424l r * l 428
424l * * l *
479l r * r 483
479l * * l *
480l r * r 484
480l * * l *
495* F * r 499
495* * * * *
495l F * r 499
495l * * l *
472r F * r 476
472r * * r *
503l r * r 507
503l * * l *
519l E * r 523
519l * * l *
520l E * r 524
520l * * l *
535* Q * r 539
535* * * * *
535l Q * r 539
535l * * l *
521l E * r 525
521l * * l *
512r Q * r 516
512r * * r *
543l E * r 547
543l * * l *
251r N * r 256
251r * * r *
>>> len(used_states)
139
>>> quasis[0]
End(is_start=True, next_quasis=[259])
>>> directions[259]
{'r', 'l'}
>>> print('\n'.join([str((k,quasis[k])) for k in range(len(quasis))]))

>>> 295 in used_states
True
>>> 296 in used_states
True
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> order = ['E','Q','varr','F','f','n','N']
>>> compile_function('EULER')
216 0 0 r 216
216 1 0 r 216
216 2 0 r 216
216 3 0 r 216
216 f f l 220l
217 0 0 r 217
217 1 0 r 217
217 2 0 r 217
217 3 0 r 217
217 f f l 221l
224 0 3 r 309r
224 1 3 r 309r
224 2 2 r 224
224 3 3 r 224
224 f f l 324l
225 0 3 r 309r
225 1 3 r 309r
225 2 2 r 225
225 3 3 r 225
225 f f l 325l
232 0 0 r 232
232 1 0 r 232
232 2 0 r 232
232 3 0 r 232
232 f f r 340r
233 0 0 r 233
233 1 0 r 233
233 2 0 r 233
233 3 0 r 233
233 f f r 341r
240 0 0 r 240
240 1 1 r 240
240 2 0 r 240
240 3 1 r 240
240 N N l 244l
241 0 1 r 241
241 1 0 r 240
241 2 1 r 241
241 3 0 r 240
241 N * l 244l
248 0 0 r 248
248 1 1 l 300l
248 N N l 410l
256 0 0 r 256
256 1 1 r 256
256 2 0 r 256
256 3 1 r 256
256 E E l 260l
257 0 1 r 256
257 1 0 r 257
257 2 1 r 256
257 3 0 r 257
257 E * * halt
264 0 2 l 268l
264 1 3 l 269l
264 2 2 r 264
264 3 3 r 264
264 E E l 284l
265 0 2 l 268l
265 1 3 l 269l
265 2 2 r 265
265 3 3 r 265
265 E E l 285l
272 0 2 r 260r
272 1 2 r 260r
272 2 2 r 272
272 3 3 r 272
272 N N * 284*
273 0 3 r 261r
273 1 3 r 261r
273 2 2 r 273
273 3 3 r 273
273 N N * 285*
288 0 0 r 288
288 1 1 r 288
288 2 0 r 288
288 3 1 r 288
288 E E l 292l
289 0 0 r 289
289 1 1 r 289
289 2 0 r 289
289 3 1 r 289
289 E E l 293l
296 0 0 r 296
296 1 1 r 296
296 2 0 r 296
296 3 1 r 296
296 N N l 212l
297 0 0 r 297
297 1 1 r 297
297 2 0 r 297
297 3 1 r 297
297 N N l 213l
304 0 2 r 308r
304 1 3 r 309r
304 2 2 r 304
304 3 3 r 304
304 f f l 324l
305 0 2 r 308r
305 1 3 r 309r
305 2 2 r 305
305 3 3 r 305
305 f f l 325l
312 0 2 l 300l
312 1 2 l 300l
312 2 2 r 312
312 3 3 r 312
312 n n l 324l
313 0 3 l 301l
313 1 3 l 301l
313 2 2 r 313
313 3 3 r 313
313 n n l 325l
328 0 0 r 328
328 1 1 r 328
328 2 0 r 328
328 3 1 r 328
328 f f * 332*
329 0 0 r 329
329 1 1 r 329
329 2 0 r 329
329 3 1 r 329
329 f f * 333*
336 0 0 r 336
336 1 1 r 336
336 2 0 r 336
336 3 1 r 336
336 n n l 228l
337 0 0 r 337
337 1 1 r 337
337 2 0 r 337
337 3 1 r 337
337 n n l 229l
344 0 2 l 348l
344 1 3 l 370l
344 2 2 r 344
344 3 3 r 344
344 N N l 362l
345 0 2 l 348l
345 1 3 l 370l
345 2 2 r 345
345 3 3 r 345
345 N N l 363l
352 0 0 r 352
352 1 0 r 353
352 2 0 r 352
352 3 0 r 353
352 n * * 340*
353 0 1 r 352
353 1 1 r 353
353 2 1 r 352
353 3 1 r 353
353 n * * 354*
358 0 2 r 358
358 1 3 l 363l
358 2 2 r 358
358 3 3 r 358
358 N N l 362l
366 0 0 r 366
366 1 1 r 366
366 2 0 r 366
366 3 1 r 366
366 N N l 236l
367 0 0 r 367
367 1 1 r 367
367 2 0 r 367
367 3 1 r 367
367 N N * halt
374 0 2 l 378l
374 1 3 l 379l
374 2 2 r 374
374 3 3 r 374
374 n * l 394l
375 0 2 l 379l
375 1 3 l 380l
375 2 2 r 375
375 3 3 r 375
375 n n l 395l
382 0 2 r 370r
382 1 3 r 370r
382 2 2 r 382
382 3 3 r 382
382 f f * 394*
383 0 3 r 370r
383 1 2 r 371r
383 2 2 r 383
383 3 3 r 383
383 f f * 395*
384 0 2 r 371r
384 1 3 r 371r
384 2 2 r 384
384 3 3 r 384
384 f f * 394*
398 0 0 r 398
398 1 1 r 398
398 2 0 r 398
398 3 1 r 398
398 n n l 402l
399 0 0 r 399
399 1 1 r 399
399 2 0 r 399
399 3 1 r 399
399 n n l 403l
406 0 0 r 406
406 1 1 r 406
406 2 0 r 406
406 3 1 r 406
406 f f * 348*
407 0 0 r 407
407 1 1 r 407
407 2 0 r 407
407 3 1 r 407
407 f f r 363r
414 0 0 r 414
414 1 0 r 414
414 2 0 r 414
414 3 0 r 414
414 F F l 418l
422 0 0 r 422
422 1 0 r 423
422 2 0 r 422
422 3 0 r 423
422 F F * 440*
423 0 1 r 422
423 1 1 r 423
423 2 1 r 422
423 3 1 r 423
423 F * * 441*
428 0 3 r 472r
428 1 3 r 472r
428 2 2 l 428
428 3 3 l 428
428 Q Q * 432*
429 0 2 r 418r
429 1 2 r 418r
429 2 2 l 429
429 3 3 l 429
429 Q * * 432*
436 0 0 r 436
436 1 1 r 436
436 2 0 r 436
436 3 1 r 436
436 r r l 512l
444 0 2 r 448r
444 1 3 r 449r
444 2 2 l 444
444 3 3 l 444
444 r r * 456*
445 0 2 r 448r
445 1 3 r 449r
445 2 2 l 445
445 3 3 l 445
445 r r * 457*
452 0 2 l 440l
452 1 3 l 457l
452 2 2 l 452
452 3 3 l 452
452 F F l 456l
453 0 2 l 456l
453 1 3 l 440l
453 2 2 l 453
453 3 3 l 453
453 F F l 457l
460 0 0 r 460
460 1 1 r 460
460 2 0 r 460
460 3 1 r 460
460 F F * 464*
461 0 0 r 461
461 1 1 r 461
461 2 0 r 461
461 3 1 r 461
461 F F * 465*
468 0 0 r 468
468 1 1 r 468
468 2 0 r 468
468 3 1 r 468
468 f f l 424l
469 0 0 r 469
469 1 1 r 469
469 2 0 r 469
469 3 1 r 469
469 f f l 425l
476 0 2 l 480l
476 1 3 l 481l
476 2 2 r 476
476 3 3 r 476
476 f f l 496l
477 0 2 l 481l
477 1 3 l 481l
477 2 2 r 477
477 3 3 r 477
477 f f l 496l
484 0 2 r 472r
484 1 3 r 473r
484 2 2 r 484
484 3 3 r 484
484 F F * 496*
485 0 3 r 472r
485 1 2 r 472r
485 2 2 r 485
485 3 3 r 485
485 F F * 496*
500 0 0 r 500
500 1 1 r 500
500 2 0 r 500
500 3 1 r 500
500 f f l 504l
508 0 0 r 508
508 1 1 r 508
508 2 0 r 508
508 3 1 r 508
508 F F l 418l
516 0 2 l 520l
516 1 3 l 521l
516 2 2 r 516
516 3 3 r 516
516 r * l 536l
517 0 2 l 521l
517 1 3 l 522l
517 2 2 r 517
517 3 3 r 517
517 r * l 536l
524 0 2 r 512r
524 1 3 r 512r
524 2 2 r 524
524 3 3 r 524
524 Q * * 536*
525 0 3 r 512r
525 1 2 r 513r
525 2 2 r 525
525 3 3 r 525
525 Q * * 536*
526 0 2 r 513r
526 1 3 r 513r
526 2 2 r 526
526 3 3 r 526
526 Q * * 536*
540 0 0 r 540
540 1 1 r 540
540 2 0 r 540
540 3 1 r 540
540 r r l 544l
548 0 0 r 548
548 1 1 r 548
548 2 0 r 548
548 3 1 r 548
548 Q Q r 252r
260r N * r 264
260r * * r *
260l N * r 264
260l * * l *
220l F * r 224
220l * * l *
221l F * r 225
221l * * l *
309r f * r 313
309r * * r *
324l F * r 328
324l * * l *
325l F * r 329
325l * * l *
340r n * r 344
340r * * r *
340* n * r 344
340* * * * *
341r n * r 345
341r * * r *
244l n * r 248
244l * * l *
300l F * r 304
300l * * l *
410l r * r 414
410l * * l *
268l n * r 272
268l * * l *
269l n * r 273
269l * * l *
284l N * r 288
284l * * l *
284* N * r 288
284* * * * *
285l N * r 289
285l * * l *
285* N * r 289
285* * * * *
261r N * r 265
261r * * r *
292l n * r 296
292l * * l *
293l n * r 297
293l * * l *
212l F * r 216
212l * * l *
213l F * r 217
213l * * l *
308r f * r 312
308r * * r *
301l F * r 305
301l * * l *
332* f * r 336
332* * * * *
333* f * r 337
333* * * * *
228l F * r 232
228l * * l *
229l F * r 233
229l * * l *
348l f * r 352
348l * * l *
348* f * r 352
348* * * * *
370l f * r 374
370l * * l *
370r f * r 374
370r * * r *
362l n * r 366
362l * * l *
363l n * r 367
363l * * l *
363r n * r 367
363r * * r *
354* n * r 358
354* * * * *
236l n * r 241
236l * * l *
378l F * r 382
378l * * l *
379l F * r 383
379l * * l *
394l f * r 398
394l * * l *
394* f * r 398
394* * * * *
380l F * r 384
380l * * l *
395l f * r 399
395l * * l *
395* f * r 399
395* * * * *
371r f * r 375
371r * * r *
402l F * r 406
402l * * l *
403l F * r 407
403l * * l *
418l r * r 423
418l * * l *
418r r * r 423
418r * * r *
440l F * l 444
440l * * l *
440* F * l 444
440* * * * *
441* F * l 445
441* * * * *
472r F * r 476
472r * * r *
432* Q * r 436
432* * * * *
512l Q * r 516
512l * * l *
512r Q * r 516
512r * * r *
448r f * l 452
448r * * r *
449r f * l 453
449r * * r *
456l r * r 460
456l * * l *
456* r * r 460
456* * * * *
457l r * r 461
457l * * l *
457* r * r 461
457* * * * *
464* F * r 468
464* * * * *
465* F * r 469
465* * * * *
424l r * l 428
424l * * l *
425l r * l 429
425l * * l *
480l r * r 484
480l * * l *
481l r * r 485
481l * * l *
496l F * r 500
496l * * l *
496* F * r 500
496* * * * *
473r F * r 477
473r * * r *
504l r * r 508
504l * * l *
520l E * r 524
520l * * l *
521l E * r 525
521l * * l *
536l Q * r 540
536l * * l *
536* Q * r 540
536* * * * *
522l E * r 526
522l * * l *
513r Q * r 517
513r * * r *
544l E * r 548
544l * * l *
252r N * r 257
252r * * r *
>>> {type(quasi) for quasi in quasis}
{<class '__main__.FunctionCall'>, <class 'NoneType'>, <class '__main__.State'>, <class '__main__.End'>, <class '__main__.Step'>, <class '__main__.Instruction'>}
>>> {None,FunctionCall,Instruction,Step,State,End}
{<class '__main__.FunctionCall'>, <class '__main__.State'>, <class '__main__.End'>, <class '__main__.Step'>, None, <class '__main__.Instruction'>}
>>> {type(None),FunctionCall,Instruction,Step,State,End}
{<class '__main__.FunctionCall'>, <class 'NoneType'>, <class '__main__.State'>, <class '__main__.End'>, <class '__main__.Step'>, <class '__main__.Instruction'>}
>>> len(used_states)
138
>>> quasis[0]
End(is_start=True, next_quasis=[260])
>>> ''.join([sym+'0'*13 for sym in order])
'E0000000000000Q0000000000000varr0000000000000F0000000000000f0000000000000n0000000000000N0000000000000'
>>> def squares():
	for k in range(2,100):
		yield k*k

		
>>> squares()
<generator object squares at 0x03CD9070>
>>> squares()[0]
Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    squares()[0]
TypeError: 'generator' object is not subscriptable
>>> list(squares)[0]
Traceback (most recent call last):
  File "<pyshell#263>", line 1, in <module>
    list(squares)[0]
TypeError: 'function' object is not iterable
>>> list(squares())[0]
4
>>> squares().close()
>>> list(squares())[0]
4
>>> next(squares())
4
>>> squares().next()
Traceback (most recent call last):
  File "<pyshell#268>", line 1, in <module>
    squares().next()
AttributeError: 'generator' object has no attribute 'next'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis = []
>>> function = LineParser.line.parse('TEST').value
>>> functions

>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
Traceback (most recent call last):
  File "<pyshell#275>", line 2, in <module>
    more_ends = remove_ends()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 343, in remove_ends
    for k,_,next_quasi in get_quasis_from(quasi,[FunctionCall,End]):
TypeError: cannot unpack non-iterable NoneType object
>>> def get_quasis_from(quasi,types=[FunctionCall,Instruction,State,End]):
    global quasis
    if type(quasi)==State and quasi.transitions:
        for symbol,transition in quasi.transitions.items():
            yield symbol,transition,quasis[transition[2]]
    elif type(quasi) in [FunctionCall,Instruction,End]:
        if quasi.next_quasis:
            for k,next_quasi in enumerate(quasi.next_quasis):
                yield k,next_quasi,quasis[next_quasi]
        else:
            yield 0,None,None

            
>>> while more_ends:
        more_ends = remove_ends()

        
Traceback (most recent call last):
  File "<pyshell#279>", line 2, in <module>
    more_ends = remove_ends()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 344, in remove_ends
    for k,_,next_quasi in get_quasis_from(quasi,[FunctionCall,End]):
TypeError: 'NoneType' object does not support item assignment
>>> len(quasis)
35
>>> _
35
>>> for _,quasi in get_quasis():
        for something in get_quasis_from(quasi,[FunctionCall,End]):
		print(something)
		
SyntaxError: inconsistent use of tabs and spaces in indentation
for _,quasi in get_quasis():
        for something in get_quasis_from(quasi,[FunctionCall,End]):
		print(something)
>>> for _,quasi in get_quasis():
	for something in get_quasis_from(quasi,[FunctionCall,End]):
		print(something)

		
(0, 1, FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[4]))
(0, 4, End(is_start=True, next_quasis=[6]))
(0, 3, End(is_start=False, next_quasis=None))
(1, 3, End(is_start=False, next_quasis=None))
(0, None, None)
(0, 6, Instruction(LOADNEXT, vard=A, next_quasis=[7, 19]))
(0, 7, Instruction(BRANCH, next_quasis=[12, 9, 9, 9]))
(1, 19, Instruction(UNREAD, vard=A, next_quasis=[20]))
(0, 12, Instruction(SLLs, vard=B, next_quasis=[13]))
(1, 9, FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[21]))
(2, 9, FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[21]))
(3, 9, FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[21]))
(0, 21, End(is_start=True, next_quasis=[22]))
(0, 12, Instruction(SLLs, vard=B, next_quasis=[13]))
(1, 19, Instruction(UNREAD, vard=A, next_quasis=[20]))
(2, 12, Instruction(SLLs, vard=B, next_quasis=[13]))
(3, 12, Instruction(SLLs, vard=B, next_quasis=[13]))
(0, 13, Instruction(BRANCH, next_quasis=[6, 15, 15, 15]))
(0, 6, Instruction(LOADNEXT, vard=A, next_quasis=[7, 19]))
(1, 15, Instruction(LOADI, next_quasis=[16]))
(2, 15, Instruction(LOADI, next_quasis=[16]))
(3, 15, Instruction(LOADI, next_quasis=[16]))
(0, 16, Instruction(LOADNEXT, vard=A, next_quasis=[17, 19]))
(0, 17, Instruction(BRANCH, next_quasis=[15, 19, 19, 19]))
(1, 19, Instruction(UNREAD, vard=A, next_quasis=[20]))
(0, 15, Instruction(LOADI, next_quasis=[16]))
(1, 19, Instruction(UNREAD, vard=A, next_quasis=[20]))
(2, 19, Instruction(UNREAD, vard=A, next_quasis=[20]))
(3, 19, Instruction(UNREAD, vard=A, next_quasis=[20]))
(0, 20, End(is_start=False, next_quasis=[2]))
(0, 2, Instruction(STORE, vard=S, next_quasis=[3, 3]))
(0, 22, Instruction(LOADI, next_quasis=[24]))
(0, 24, Instruction(LOADNEXT, vard=B, next_quasis=[25, 32]))
(0, 25, Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26]))
(1, 32, Instruction(UNREAD, vard=B, next_quasis=[33]))
(0, 26, Instruction(LOAD, vard=D, next_quasis=[27, 32]))
(0, 27, Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[28]))
(1, 32, Instruction(UNREAD, vard=B, next_quasis=[33]))
(0, 28, Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[29]))
(0, 29, Instruction(STORENEXT, vard=D, next_quasis=[30, 32]))
(0, 30, Instruction(JUMP, next_quasis=[24]))
(1, 32, Instruction(UNREAD, vard=B, next_quasis=[33]))
(0, 24, Instruction(LOADNEXT, vard=B, next_quasis=[25, 32]))
(0, 33, Instruction(UNREAD, vard=D, next_quasis=[34]))
(0, 34, End(is_start=False, next_quasis=[10]))
(0, 10, Instruction(BRANCH, next_quasis=[12, 19, 12, 12]))
>>> _ = None
>>> _,_ = None,None
>>> functions[0].lines
[End(is_start=True, next_quasis=[1]), FunctionCall(command='LOADI', args=[0, 'ACC'], next_quasis=[3]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'], next_quasis=[4, 11]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}], next_quasis=[5]), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'], next_quasis=[6, 11]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}], next_quasis=[7]), FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}], next_quasis=[8]), FunctionCall(command='STORENEXT', args=['vard', 'TEMP'], next_quasis=[9, 11]), FunctionCall(command='JUMP', args=['start'], next_quasis=[3]), Label(name='oob'), FunctionCall(command='UNREAD', args=['var0'], next_quasis=[12]), FunctionCall(command='UNREAD', args=['var1'], next_quasis=[13]), FunctionCall(command='UNREAD', args=['vard'], next_quasis=[14]), End(is_start=False, next_quasis=[])]
>>> quasis = []
>>> function = LineParser.line.parse('TEST').value
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[1])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[4])
2 Instruction(STORE, vard=S, next_quasis=[3, 3])
3 End(is_start=False, next_quasis=None)
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 9, 9, 9])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[21])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
14 None
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
18 None
19 Instruction(UNREAD, vard=A, next_quasis=[20])
20 End(is_start=False, next_quasis=[2])
21 End(is_start=True, next_quasis=[22])
22 Instruction(LOADI, next_quasis=[24])
23 None
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[28])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[29])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
31 None
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[34])
34 End(is_start=False, next_quasis=[10])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
Traceback (most recent call last):
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 55, in <module>
    @dataclass
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\dataclasses.py", line 966, in dataclass
    return wrap(_cls)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\dataclasses.py", line 958, in wrap
    return _process_class(cls, init, repr, eq, order, unsafe_hash, frozen)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\dataclasses.py", line 809, in _process_class
    for name, type in cls_annotations.items()]
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\dataclasses.py", line 809, in <listcomp>
    for name, type in cls_annotations.items()]
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\dataclasses.py", line 702, in _get_field
    raise ValueError(f'mutable default {type(f.default)} for field '
ValueError: mutable default <class 'list'> for field next_quasis is not allowed: use default_factory
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis = []
		     
>>> function = LineParser.line.parse('TEST').value
		     
>>> )))
SyntaxError: invalid syntax
>>> function.next_quasis [None]
Traceback (most recent call last):
  File "<pyshell#298>", line 1, in <module>
    function.next_quasis [None]
TypeError: 'NoneType' object is not subscriptable
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[1])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[4])
2 Instruction(STORE, vard=S, next_quasis=[3, 3])
3 End(is_start=False, next_quasis=[None])
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 9, 9, 9])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[21])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
14 None
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
18 None
19 Instruction(UNREAD, vard=A, next_quasis=[20])
20 End(is_start=False, next_quasis=[2])
21 End(is_start=True, next_quasis=[22])
22 Instruction(LOADI, next_quasis=[24])
23 None
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[28])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[29])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
31 None
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[34])
34 End(is_start=False, next_quasis=[10])
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
Traceback (most recent call last):
  File "<pyshell#305>", line 2, in <module>
    more_ends = remove_ends()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 344, in remove_ends
    for k,_,next_quasi in get_quasis_from(quasi,[FunctionCall,End]):
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 336, in get_quasis_from
    yield k,next_quasi,quasis[next_quasi]
TypeError: list indices must be integers or slices, not NoneType
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function.next_quasis = [None]
Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    function.next_quasis = [None]
NameError: name 'function' is not defined
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
Traceback (most recent call last):
  File "<pyshell#313>", line 2, in <module>
    more_ends = remove_ends()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 344, in remove_ends
    for k,_,next_quasi in get_quasis_from(quasi,[FunctionCall,End]):
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 336, in get_quasis_from
    yield k,next_quasi,quasis[next_quasi]
TypeError: list indices must be integers or slices, not NoneType
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
Traceback (most recent call last):
  File "<pyshell#319>", line 2, in <module>
    more_ends = remove_ends()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 344, in remove_ends
    for k,_,next_quasi in get_quasis_from(quasi,[FunctionCall,End]):
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 336, in get_quasis_from
    yield k,next_quasi,quasis[next_quasi]
KeyboardInterrupt
>>> remove_ends()
True
>>> remove_ends()
True
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('TEST').value
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
Traceback (most recent call last):
  File "<pyshell#326>", line 2, in <module>
    more_ends = remove_ends()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 343, in remove_ends
    _,quasi.next_quasis[k],_ = next(get_quasis_from(quasi))
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 328, in get_quasis_from
    def get_quasis_from(quasi,types=[FunctionCall,Instruction,State,End]):
KeyboardInterrupt
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[1])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[4])
2 Instruction(STORE, vard=S, next_quasis=[3, 3])
3 End(is_start=False, next_quasis=None)
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 7])
7 Instruction(BRANCH, next_quasis=[12, 12, 12, 12])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[21])
10 Instruction(BRANCH, next_quasis=[12, 12, 12, 12])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 6, 6, 6])
14 None
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 17])
17 Instruction(BRANCH, next_quasis=[15, 15, 15, 15])
18 None
19 Instruction(UNREAD, vard=A, next_quasis=[20])
20 End(is_start=False, next_quasis=[2])
21 End(is_start=True, next_quasis=[22])
22 Instruction(LOADI, next_quasis=[24])
23 None
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 25])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 27])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[28])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[29])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 30])
30 Instruction(JUMP, next_quasis=[24])
31 None
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[34])
34 End(is_start=False, next_quasis=[10])
>>> quasi = quasis[2]
>>> for k,_,next_quasi in get_quasis_from(quasi,[FunctionCall,End]):
	print('hi')

	
hi
hi
>>> def remove_ends():
    global quasis
    altered = False
    for _,quasi in get_quasis():
        for k,_,next_quasi in get_quasis_from(quasi,[FunctionCall,End]):
            _,quasi.next_quasis[k],_ = next(get_quasis_from(next_quasi))
            altered = True
    return altered

>>> remove_ends()
Traceback (most recent call last):
  File "<pyshell#335>", line 1, in <module>
    remove_ends()
  File "<pyshell#334>", line 6, in remove_ends
    _,quasi.next_quasis[k],_ = next(get_quasis_from(next_quasi))
StopIteration
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('TEST').value
>>> evaluate_function_call(function)
>>> remove_ends()
Traceback (most recent call last):
  File "<pyshell#338>", line 1, in <module>
    remove_ends()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 345, in remove_ends
    _,next_k,_ = next(get_quasis_from(next_quasi))
StopIteration
>>> def remove_ends():
    global quasis
    altered = False
    for _,quasi in get_quasis():
        for k,_,next_quasi in get_quasis_from(quasi,[FunctionCall,End]):
            _,next_k,_ = next(get_quasis_from(next_quasi))
            if next_k!=quasi.next_quasis[k]:
                quasi.next_quasis[k] = k
                altered = True
    return altered

>>> remove_ends()
Traceback (most recent call last):
  File "<pyshell#341>", line 1, in <module>
    remove_ends()
  File "<pyshell#340>", line 6, in remove_ends
    _,next_k,_ = next(get_quasis_from(next_quasi))
StopIteration
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[0])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[0])
2 Instruction(STORE, vard=S, next_quasis=[0, 1])
3 End(is_start=False, next_quasis=None)
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 9, 9, 9])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[21])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
14 None
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
18 None
19 Instruction(UNREAD, vard=A, next_quasis=[20])
20 End(is_start=False, next_quasis=[2])
21 End(is_start=True, next_quasis=[22])
22 Instruction(LOADI, next_quasis=[24])
23 None
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[28])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[29])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
31 None
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[34])
34 End(is_start=False, next_quasis=[10])
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[1])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[4])
2 Instruction(STORE, vard=S, next_quasis=[3, 3])
3 End(is_start=False, next_quasis=None)
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 9, 9, 9])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[21])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
14 None
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
18 None
19 Instruction(UNREAD, vard=A, next_quasis=[20])
20 End(is_start=False, next_quasis=[2])
21 End(is_start=True, next_quasis=[22])
22 Instruction(LOADI, next_quasis=[24])
23 None
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[28])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[29])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
31 None
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[34])
34 End(is_start=False, next_quasis=[10])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> evaluate_function_call(function)
>>> remove_ends()
Traceback (most recent call last):
  File "<pyshell#352>", line 1, in <module>
    remove_ends()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 343, in remove_ends
    _,next_k,_ = next(get_quasis_from(next_quasi))
StopIteration
>>> def get_quasis_from(quasi,types=[FunctionCall,Instruction,State,End]):
    global quasis
    if type(quasi)==State and quasi.transitions:
        for symbol,transition in quasi.transitions.items():
            yield symbol,transition,quasis[transition[2]]
    elif type(quasi) in [FunctionCall,Instruction,End]:
        for k,next_quasi in enumerate(quasi.next_quasis):
            yield k,next_quasi,(quasis[next_quasi] if next_quasi else None)

            
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[0])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[0])
2 Instruction(STORE, vard=S, next_quasis=[3, 3])
3 End(is_start=False, next_quasis=None)
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 9, 9, 9])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[21])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
14 None
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
18 NoneTraceback (most recent call last):
  File "<pyshell#356>", line 2, in <module>
    print(k,quasi)
KeyboardInterrupt
>>> get_quasis_from(quasis[0])
<generator object get_quasis_from at 0x03747D30>
>>> next(get_quasis_from(quasis[0]))
(0, 0, None)
>>> next(get_quasis_from(quasis[1]))
(0, 0, None)
>>> next(get_quasis_from(quasis[3]))
Traceback (most recent call last):
  File "<pyshell#360>", line 1, in <module>
    next(get_quasis_from(quasis[3]))
  File "<pyshell#354>", line 7, in get_quasis_from
    for k,next_quasi in enumerate(quasi.next_quasis):
TypeError: 'NoneType' object is not iterable
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[0])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[0])
2 Instruction(STORE, vard=S, next_quasis=[3, 3])
3 End(is_start=False, next_quasis=None)
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 9, 9, 9])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[21])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
14 None
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
18 None
19 Instruction(UNREAD, vard=A, next_quasis=[20])
20 End(is_start=False, next_quasis=[2])
21 End(is_start=True, next_quasis=[22])
22 Instruction(LOADI, next_quasis=[24])
23 None
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[28])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[29])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
31 None
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[34])
34 End(is_start=False, next_quasis=[10])
>>> next(get_quasis_from(quasis[2]))
(0, 3, End(is_start=False, next_quasis=None))
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> evaluate_function_call(function)
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> remove_ends()
Traceback (most recent call last):
  File "<pyshell#371>", line 1, in <module>
    remove_ends()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 343, in remove_ends
    if next_k!=quasi.next_quasis[k]:
StopIteration
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[0])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[0])
2 Instruction(STORE, vard=S, next_quasis=[0, 1])
3 End(is_start=False, next_quasis=[None])
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 9, 9, 9])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[21])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
14 None
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
18 None
19 Instruction(UNREAD, vard=A, next_quasis=[20])
20 End(is_start=False, next_quasis=[2])
21 End(is_start=True, next_quasis=[22])
22 Instruction(LOADI, next_quasis=[24])
23 None
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[28])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[29])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
31 None
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[34])
34 End(is_start=False, next_quasis=[10])
>>> quasis=[]
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[1])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[4])
2 Instruction(STORE, vard=S, next_quasis=[3, 3])
3 End(is_start=False, next_quasis=[None])
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 9, 9, 9])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[21])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
14 None
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
18 None
19 Instruction(UNREAD, vard=A, next_quasis=[20])
20 End(is_start=False, next_quasis=[2])
21 End(is_start=True, next_quasis=[22])
22 Instruction(LOADI, next_quasis=[24])
23 None
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[28])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[29])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
31 None
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[34])
34 End(is_start=False, next_quasis=[10])
>>> next(get_quasis_from(quasis[1])]
SyntaxError: invalid syntax
>>> next(get_quasis_from(quasis[1]))
(0, 4, End(is_start=True, next_quasis=[6]))
>>> quasi = quasis[0]
>>> for k,_,next_quasi in get_quasis_from(quasi,[FunctionCall,End]):
	print(k,next_quasi)

	
0 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[4])
>>> _,next_k,_ = next(get_quasis_from(next_quasi))
>>> next_k
4
>>> next_k!=quasi.next_quasis[k]
True
>>> 
KeyboardInterrupt
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> remove_ends()
Traceback (most recent call last):
  File "<pyshell#391>", line 1, in <module>
    remove_ends()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 342, in remove_ends
    _,next_k,_ = next(get_quasis_from(next_quasi))
StopIteration
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[4])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[6])
2 Instruction(STORE, vard=S, next_quasis=[None, None])
3 End(is_start=False, next_quasis=[None])
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 9, 9, 9])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[21])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
14 None
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
18 None
19 Instruction(UNREAD, vard=A, next_quasis=[20])
20 End(is_start=False, next_quasis=[2])
21 End(is_start=True, next_quasis=[22])
22 Instruction(LOADI, next_quasis=[24])
23 None
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[28])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[29])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
31 None
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[34])
34 End(is_start=False, next_quasis=[10])
>>> remove_ends()
Traceback (most recent call last):
  File "<pyshell#394>", line 1, in <module>
    remove_ends()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 342, in remove_ends
    _,next_k,_ = next(get_quasis_from(next_quasi))
StopIteration
>>> for _,quasi in get_quasis():
        for k,_,next_quasi in get_quasis_from(quasi,[FunctionCall,End]):
	    print(k,next_quasi)
            _,next_k,_ = next(get_quasis_from(next_quasi))
            
SyntaxError: inconsistent use of tabs and spaces in indentation
for _,quasi in get_quasis():
        for k,_,next_quasi in get_quasis_from(quasi,[FunctionCall,End]):
	    print(k,next_quasi)
            _,next_k,_ = next(get_quasis_from(next_quasi))
>>> for _,quasi in get_quasis():
	for k,_,next_quasi in get_quasis_from(quasi,[FunctionCall,End]):
		print(k,next_quasi)
		_,next_k,_ = next(get_quasis_from(next_quasi))

		
0 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
0 Instruction(BRANCH, next_quasis=[12, 9, 9, 9])
0 None
Traceback (most recent call last):
  File "<pyshell#397>", line 4, in <module>
    _,next_k,_ = next(get_quasis_from(next_quasi))
StopIteration
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> remove_ends()
True
>>> remove_ends()
True
>>> remove_ends()
True
>>> remove_ends()
True
>>> remove_ends()
True
>>> remove_ends()
False
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[6])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[6])
2 Instruction(STORE, vard=S, next_quasis=[None, None])
3 End(is_start=False, next_quasis=[None])
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[6, None])
7 Instruction(BRANCH, next_quasis=[6, 30, 30, 30])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[30])
10 Instruction(BRANCH, next_quasis=[6, None, 6, 6])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[6])
13 Instruction(BRANCH, next_quasis=[6, 17, 17, 17])
14 None
15 Instruction(LOADI, next_quasis=[17])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, None])
17 Instruction(BRANCH, next_quasis=[17, None, None, None])
18 None
19 Instruction(UNREAD, vard=A, next_quasis=[None])
20 End(is_start=False, next_quasis=[None])
21 End(is_start=True, next_quasis=[30])
22 Instruction(LOADI, next_quasis=[30])
23 None
24 Instruction(LOADNEXT, vard=B, next_quasis=[30, 6])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[30])
26 Instruction(LOAD, vard=D, next_quasis=[30, 6])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[30])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[30])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 6])
30 Instruction(JUMP, next_quasis=[30])
31 None
32 Instruction(UNREAD, vard=B, next_quasis=[6])
33 Instruction(UNREAD, vard=D, next_quasis=[6])
34 End(is_start=False, next_quasis=[6])
>>> try:
	a = 1/0
except:
	print('hi')

	
hi
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> remove_ends()
True
>>> remove_ends()
True
>>> remove_ends()
False
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[6])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[6])
2 Instruction(STORE, vard=S, next_quasis=[3, 3])
3 End(is_start=False, next_quasis=[None])
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 22, 22, 22])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[22])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
14 None
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
18 None
19 Instruction(UNREAD, vard=A, next_quasis=[2])
20 End(is_start=False, next_quasis=[2])
21 End(is_start=True, next_quasis=[22])
22 Instruction(LOADI, next_quasis=[24])
23 None
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[28])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[29])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
31 None
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[10])
34 End(is_start=False, next_quasis=[10])
>>> instruction2states()
Traceback (most recent call last):
  File "<pyshell#427>", line 1, in <module>
    instruction2states()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 501, in instruction2states
    quasis.append(State(instruction=k,acc=acc,transitions=transitions,direction=direction))
TypeError: __init__() got an unexpected keyword argument 'instruction'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
>>> instructions2states()
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[6])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[6])
2 Instruction(STORE, vard=S, next_quasis=[3, 3])
3 End(is_start=False, next_quasis=[None])
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 22, 22, 22])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[22])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
14 None
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
18 None
19 Instruction(UNREAD, vard=A, next_quasis=[2])
20 End(is_start=False, next_quasis=[2])
21 End(is_start=True, next_quasis=[22])
22 Instruction(LOADI, next_quasis=[24])
23 None
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[28])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[29])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
31 None
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[10])
34 End(is_start=False, next_quasis=[10])
35 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 2], "1'": ["1'", 0, 2], Sym('S'+1): [None, 0, 3]}, direction=1)
36 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 2], "1'": ["1'", 1, 2], Sym('S'+1): [None, 1, 3]}, direction=1)
37 State(instruction=2, acc=2, transitions={'0': ['2', 2, 3], '1': ['2', 2, 3], "0'": ["0'", 2, 2], "1'": ["1'", 2, 2], Sym('S'+1): [None, 2, 3]}, direction=1)
38 State(instruction=2, acc=3, transitions={'0': ['3', 3, 3], '1': ['3', 3, 3], "0'": ["0'", 3, 2], "1'": ["1'", 3, 2], Sym('S'+1): [None, 3, 3]}, direction=1)
39 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 7], '1': ["1'", 1, 7], "0'": ["0'", 0, 6], "1'": ["1'", 0, 6], Sym('A'+1): [None, 0, 19]}, direction=1)
40 State(instruction=6, acc=1, transitions={'0': ["0'", 0, 7], '1': ["1'", 1, 7], "0'": ["0'", 1, 6], "1'": ["1'", 1, 6], Sym('A'+1): [None, 1, 19]}, direction=1)
41 State(instruction=6, acc=2, transitions={'0': ["0'", 0, 7], '1': ["1'", 1, 7], "0'": ["0'", 2, 6], "1'": ["1'", 2, 6], Sym('A'+1): [None, 2, 19]}, direction=1)
42 State(instruction=6, acc=3, transitions={'0': ["0'", 0, 7], '1': ["1'", 1, 7], "0'": ["0'", 3, 6], "1'": ["1'", 3, 6], Sym('A'+1): [None, 3, 19]}, direction=1)
43 State(instruction=12, acc=0, transitions={'0': ['0', 0, 12], '1': ['0', 1, 12], "0'": ['0', 0, 12], "1'": ['0', 1, 12], Sym('B'+1): [None, 0, 13]}, direction=1)
44 State(instruction=12, acc=1, transitions={'0': ['1', 0, 12], '1': ['1', 1, 12], "0'": ['1', 0, 12], "1'": ['1', 1, 12], Sym('B'+1): [None, 1, 13]}, direction=1)
45 State(instruction=12, acc=2, transitions=None, direction=None)
46 State(instruction=12, acc=3, transitions=None, direction=None)
47 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 17], '1': ["1'", 1, 17], "0'": ["0'", 0, 16], "1'": ["1'", 0, 16], Sym('A'+1): [None, 0, 19]}, direction=1)
48 State(instruction=16, acc=1, transitions={'0': ["0'", 0, 17], '1': ["1'", 1, 17], "0'": ["0'", 1, 16], "1'": ["1'", 1, 16], Sym('A'+1): [None, 1, 19]}, direction=1)
49 State(instruction=16, acc=2, transitions={'0': ["0'", 0, 17], '1': ["1'", 1, 17], "0'": ["0'", 2, 16], "1'": ["1'", 2, 16], Sym('A'+1): [None, 2, 19]}, direction=1)
50 State(instruction=16, acc=3, transitions={'0': ["0'", 0, 17], '1': ["1'", 1, 17], "0'": ["0'", 3, 16], "1'": ["1'", 3, 16], Sym('A'+1): [None, 3, 19]}, direction=1)
51 State(instruction=19, acc=0, transitions={'0': ['0', 0, 19], '1': ['1', 0, 19], "0'": ['0', 0, 19], "1'": ['1', 0, 19], Sym('A'+1): [None, 0, 2]}, direction=1)
52 State(instruction=19, acc=1, transitions={'0': ['0', 1, 19], '1': ['1', 1, 19], "0'": ['0', 1, 19], "1'": ['1', 1, 19], Sym('A'+1): [None, 1, 2]}, direction=1)
53 State(instruction=19, acc=2, transitions={'0': ['0', 2, 19], '1': ['1', 2, 19], "0'": ['0', 2, 19], "1'": ['1', 2, 19], Sym('A'+1): [None, 2, 2]}, direction=1)
54 State(instruction=19, acc=3, transitions={'0': ['0', 3, 19], '1': ['1', 3, 19], "0'": ['0', 3, 19], "1'": ['1', 3, 19], Sym('A'+1): [None, 3, 2]}, direction=1)
55 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 25], '1': ["1'", 0, 25], "0'": ["0'", 0, 24], "1'": ["1'", 0, 24], Sym('B'+1): [None, 0, 32]}, direction=1)
56 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 25], '1': ["1'", 1, 25], "0'": ["0'", 1, 24], "1'": ["1'", 1, 24], Sym('B'+1): [None, 1, 32]}, direction=1)
57 State(instruction=24, acc=2, transitions={'0': ["0'", 2, 25], '1': ["1'", 2, 25], "0'": ["0'", 2, 24], "1'": ["1'", 2, 24], Sym('B'+1): [None, 2, 32]}, direction=1)
58 State(instruction=24, acc=3, transitions={'0': ["0'", 3, 25], '1': ["1'", 3, 25], "0'": ["0'", 3, 24], "1'": ["1'", 3, 24], Sym('B'+1): [None, 3, 32]}, direction=1)
59 State(instruction=26, acc=0, transitions={'0': ['0', 0, 27], '1': ['1', 0, 27], "0'": ["0'", 0, 26], "1'": ["1'", 0, 26], Sym('D'+1): [None, 0, 32]}, direction=1)
60 State(instruction=26, acc=1, transitions={'0': ['0', 1, 27], '1': ['1', 1, 27], "0'": ["0'", 1, 26], "1'": ["1'", 1, 26], Sym('D'+1): [None, 1, 32]}, direction=1)
61 State(instruction=26, acc=2, transitions={'0': ['0', 2, 27], '1': ['1', 2, 27], "0'": ["0'", 2, 26], "1'": ["1'", 2, 26], Sym('D'+1): [None, 2, 32]}, direction=1)
62 State(instruction=26, acc=3, transitions={'0': ['0', 3, 27], '1': ['1', 3, 27], "0'": ["0'", 3, 26], "1'": ["1'", 3, 26], Sym('D'+1): [None, 3, 32]}, direction=1)
63 State(instruction=29, acc=0, transitions={'0': ["0'", 0, 30], '1': ["1'", 0, 30], "0'": ["0'", 0, 29], "1'": ["1'", 0, 29], Sym('D'+1): [None, 0, 32]}, direction=1)
64 State(instruction=29, acc=1, transitions={'0': ["0'", 1, 30], '1': ["1'", 1, 30], "0'": ["0'", 1, 29], "1'": ["1'", 1, 29], Sym('D'+1): [None, 1, 32]}, direction=1)
65 State(instruction=29, acc=2, transitions={'0': ["0'", 2, 30], '1': ["1'", 2, 30], "0'": ["0'", 2, 29], "1'": ["1'", 2, 29], Sym('D'+1): [None, 2, 32]}, direction=1)
66 State(instruction=29, acc=3, transitions={'0': ["0'", 3, 30], '1': ["1'", 3, 30], "0'": ["0'", 3, 29], "1'": ["1'", 3, 29], Sym('D'+1): [None, 3, 32]}, direction=1)
67 State(instruction=32, acc=0, transitions={'0': ['0', 0, 32], '1': ['1', 0, 32], "0'": ['0', 0, 32], "1'": ['1', 0, 32], Sym('B'+1): [None, 0, 33]}, direction=1)
68 State(instruction=32, acc=1, transitions={'0': ['0', 1, 32], '1': ['1', 1, 32], "0'": ['0', 1, 32], "1'": ['1', 1, 32], Sym('B'+1): [None, 1, 33]}, direction=1)
69 State(instruction=32, acc=2, transitions={'0': ['0', 2, 32], '1': ['1', 2, 32], "0'": ['0', 2, 32], "1'": ['1', 2, 32], Sym('B'+1): [None, 2, 33]}, direction=1)
70 State(instruction=32, acc=3, transitions={'0': ['0', 3, 32], '1': ['1', 3, 32], "0'": ['0', 3, 32], "1'": ['1', 3, 32], Sym('B'+1): [None, 3, 33]}, direction=1)
71 State(instruction=33, acc=0, transitions={'0': ['0', 0, 33], '1': ['1', 0, 33], "0'": ['0', 0, 33], "1'": ['1', 0, 33], Sym('D'+1): [None, 0, 10]}, direction=1)
72 State(instruction=33, acc=1, transitions={'0': ['0', 1, 33], '1': ['1', 1, 33], "0'": ['0', 1, 33], "1'": ['1', 1, 33], Sym('D'+1): [None, 1, 10]}, direction=1)
73 State(instruction=33, acc=2, transitions={'0': ['0', 2, 33], '1': ['1', 2, 33], "0'": ['0', 2, 33], "1'": ['1', 2, 33], Sym('D'+1): [None, 2, 10]}, direction=1)
74 State(instruction=33, acc=3, transitions={'0': ['0', 3, 33], '1': ['1', 3, 33], "0'": ['0', 3, 33], "1'": ['1', 3, 33], Sym('D'+1): [None, 3, 10]}, direction=1)
>>> def apply_posts():
    global quasis
    altered = False
    for state in get_quasis([State]):
        instr = quasis[state.instruction]
        for symbol,transition,instr = get_quasis_from(state,[Instruction])
            k = 0
            if instr.command=='JUMP':
                altered = True
            elif instr.command=='BRANCH':
                k = transition[1]
                altered = True
            elif instr.command=='LOADI' and instr.loadto=='ACC':
                transition[1] = instr.imm
                altered = True
            elif instr.command=='MAP':
                size = validate_maps(instr.map_)
                if size==(2,1):
                    assert instruction.command=='LOAD' and instruction.loadto=='TEMP'
                    if (transition[1],int(symbol)) in instr.map_:
                        transition[1] = instr.map_[(transition[1],int(symbol))][0]
                    altered = True
                elif size==(1,1):
                    if (transition[1],) in instr.map_:
                        transition[1] = instr.map_[(transition[1],)][0]             
                    altered = True
            transition[2] = instr.next_quasis[k]               
    return altered
SyntaxError: invalid syntax
>>> 
>>> def apply_posts():
    global quasis
    altered = False
    for state in get_quasis([State]):
        instr = quasis[state.instruction]
        for symbol,transition,instr in get_quasis_from(state,[Instruction]):
            k = 0
            if instr.command=='JUMP':
                altered = True
            elif instr.command=='BRANCH':
                k = transition[1]
                altered = True
            elif instr.command=='LOADI' and instr.loadto=='ACC':
                transition[1] = instr.imm
                altered = True
            elif instr.command=='MAP':
                size = validate_maps(instr.map_)
                if size==(2,1):
                    assert instruction.command=='LOAD' and instruction.loadto=='TEMP'
                    if (transition[1],int(symbol)) in instr.map_:
                        transition[1] = instr.map_[(transition[1],int(symbol))][0]
                    altered = True
                elif size==(1,1):
                    if (transition[1],) in instr.map_:
                        transition[1] = instr.map_[(transition[1],)][0]
                    altered = True
            transition[2] = instr.next_quasis[k]
    return altered

>>> more_posts = True
>>> while more_posts:
	more_posts = apply_posts()

	
Traceback (most recent call last):
  File "<pyshell#446>", line 2, in <module>
    more_posts = apply_posts()
  File "<pyshell#441>", line 5, in apply_posts
    instr = quasis[state.instruction]
AttributeError: 'tuple' object has no attribute 'instruction'
>>> def apply_posts():
    global quasis
    altered = False
    for _,state in get_quasis([State]):
        instr = quasis[state.instruction]
        for symbol,transition,instr in get_quasis_from(state,[Instruction]):
            k = 0
            if instr.command=='JUMP':
                altered = True
            elif instr.command=='BRANCH':
                k = transition[1]
                altered = True
            elif instr.command=='LOADI' and instr.loadto=='ACC':
                transition[1] = instr.imm
                altered = True
            elif instr.command=='MAP':
                size = validate_maps(instr.map_)
                if size==(2,1):
                    assert instruction.command=='LOAD' and instruction.loadto=='TEMP'
                    if (transition[1],int(symbol)) in instr.map_:
                        transition[1] = instr.map_[(transition[1],int(symbol))][0]
                    altered = True
                elif size==(1,1):
                    if (transition[1],) in instr.map_:
                        transition[1] = instr.map_[(transition[1],)][0]
                    altered = True
            transition[2] = instr.next_quasis[k]
    return altered

>>> while more_posts:
	more_posts = apply_posts()

	
Traceback (most recent call last):
  File "<pyshell#450>", line 2, in <module>
    more_posts = apply_posts()
  File "<pyshell#448>", line 6, in apply_posts
    for symbol,transition,instr in get_quasis_from(state,[Instruction]):
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 331, in get_quasis_from
    for symbol,transition in quasi.transitions.items():
AttributeError: 'NoneType' object has no attribute 'items'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
>>> instructions2states()
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[6])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[6])
2 Instruction(STORE, vard=S, next_quasis=[3, 3])
3 End(is_start=False, next_quasis=[None])
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 22, 22, 22])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[22])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
14 None
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
18 None
19 Instruction(UNREAD, vard=A, next_quasis=[2])
20 End(is_start=False, next_quasis=[2])
21 End(is_start=True, next_quasis=[22])
22 Instruction(LOADI, next_quasis=[24])
23 None
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[28])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[29])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
31 None
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[10])
34 End(is_start=False, next_quasis=[10])
35 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 2], "1'": ["1'", 0, 2], Sym('S'+1): [None, 0, 3]}, direction=1)
36 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 2], "1'": ["1'", 1, 2], Sym('S'+1): [None, 1, 3]}, direction=1)
37 State(instruction=2, acc=2, transitions={'0': ['2', 2, 3], '1': ['2', 2, 3], "0'": ["0'", 2, 2], "1'": ["1'", 2, 2], Sym('S'+1): [None, 2, 3]}, direction=1)
38 State(instruction=2, acc=3, transitions={'0': ['3', 3, 3], '1': ['3', 3, 3], "0'": ["0'", 3, 2], "1'": ["1'", 3, 2], Sym('S'+1): [None, 3, 3]}, direction=1)
39 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 7], '1': ["1'", 1, 7], "0'": ["0'", 0, 6], "1'": ["1'", 0, 6], Sym('A'+1): [None, 0, 19]}, direction=1)
40 State(instruction=6, acc=1, transitions={'0': ["0'", 0, 7], '1': ["1'", 1, 7], "0'": ["0'", 1, 6], "1'": ["1'", 1, 6], Sym('A'+1): [None, 1, 19]}, direction=1)
41 State(instruction=6, acc=2, transitions={'0': ["0'", 0, 7], '1': ["1'", 1, 7], "0'": ["0'", 2, 6], "1'": ["1'", 2, 6], Sym('A'+1): [None, 2, 19]}, direction=1)
42 State(instruction=6, acc=3, transitions={'0': ["0'", 0, 7], '1': ["1'", 1, 7], "0'": ["0'", 3, 6], "1'": ["1'", 3, 6], Sym('A'+1): [None, 3, 19]}, direction=1)
43 State(instruction=12, acc=0, transitions={'0': ['0', 0, 12], '1': ['0', 1, 12], "0'": ['0', 0, 12], "1'": ['0', 1, 12], Sym('B'+1): [None, 0, 13]}, direction=1)
44 State(instruction=12, acc=1, transitions={'0': ['1', 0, 12], '1': ['1', 1, 12], "0'": ['1', 0, 12], "1'": ['1', 1, 12], Sym('B'+1): [None, 1, 13]}, direction=1)
45 State(instruction=12, acc=2, transitions=None, direction=None)
46 State(instruction=12, acc=3, transitions=None, direction=None)
47 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 17], '1': ["1'", 1, 17], "0'": ["0'", 0, 16], "1'": ["1'", 0, 16], Sym('A'+1): [None, 0, 19]}, direction=1)
48 State(instruction=16, acc=1, transitions={'0': ["0'", 0, 17], '1': ["1'", 1, 17], "0'": ["0'", 1, 16], "1'": ["1'", 1, 16], Sym('A'+1): [None, 1, 19]}, direction=1)
49 State(instruction=16, acc=2, transitions={'0': ["0'", 0, 17], '1': ["1'", 1, 17], "0'": ["0'", 2, 16], "1'": ["1'", 2, 16], Sym('A'+1): [None, 2, 19]}, direction=1)
50 State(instruction=16, acc=3, transitions={'0': ["0'", 0, 17], '1': ["1'", 1, 17], "0'": ["0'", 3, 16], "1'": ["1'", 3, 16], Sym('A'+1): [None, 3, 19]}, direction=1)
51 State(instruction=19, acc=0, transitions={'0': ['0', 0, 19], '1': ['1', 0, 19], "0'": ['0', 0, 19], "1'": ['1', 0, 19], Sym('A'+1): [None, 0, 2]}, direction=1)
52 State(instruction=19, acc=1, transitions={'0': ['0', 1, 19], '1': ['1', 1, 19], "0'": ['0', 1, 19], "1'": ['1', 1, 19], Sym('A'+1): [None, 1, 2]}, direction=1)
53 State(instruction=19, acc=2, transitions={'0': ['0', 2, 19], '1': ['1', 2, 19], "0'": ['0', 2, 19], "1'": ['1', 2, 19], Sym('A'+1): [None, 2, 2]}, direction=1)
54 State(instruction=19, acc=3, transitions={'0': ['0', 3, 19], '1': ['1', 3, 19], "0'": ['0', 3, 19], "1'": ['1', 3, 19], Sym('A'+1): [None, 3, 2]}, direction=1)
55 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 25], '1': ["1'", 0, 25], "0'": ["0'", 0, 24], "1'": ["1'", 0, 24], Sym('B'+1): [None, 0, 32]}, direction=1)
56 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 25], '1': ["1'", 1, 25], "0'": ["0'", 1, 24], "1'": ["1'", 1, 24], Sym('B'+1): [None, 1, 32]}, direction=1)
57 State(instruction=24, acc=2, transitions={'0': ["0'", 2, 25], '1': ["1'", 2, 25], "0'": ["0'", 2, 24], "1'": ["1'", 2, 24], Sym('B'+1): [None, 2, 32]}, direction=1)
58 State(instruction=24, acc=3, transitions={'0': ["0'", 3, 25], '1': ["1'", 3, 25], "0'": ["0'", 3, 24], "1'": ["1'", 3, 24], Sym('B'+1): [None, 3, 32]}, direction=1)
59 State(instruction=26, acc=0, transitions={'0': ['0', 0, 27], '1': ['1', 0, 27], "0'": ["0'", 0, 26], "1'": ["1'", 0, 26], Sym('D'+1): [None, 0, 32]}, direction=1)
60 State(instruction=26, acc=1, transitions={'0': ['0', 1, 27], '1': ['1', 1, 27], "0'": ["0'", 1, 26], "1'": ["1'", 1, 26], Sym('D'+1): [None, 1, 32]}, direction=1)
61 State(instruction=26, acc=2, transitions={'0': ['0', 2, 27], '1': ['1', 2, 27], "0'": ["0'", 2, 26], "1'": ["1'", 2, 26], Sym('D'+1): [None, 2, 32]}, direction=1)
62 State(instruction=26, acc=3, transitions={'0': ['0', 3, 27], '1': ['1', 3, 27], "0'": ["0'", 3, 26], "1'": ["1'", 3, 26], Sym('D'+1): [None, 3, 32]}, direction=1)
63 State(instruction=29, acc=0, transitions={'0': ["0'", 0, 30], '1': ["1'", 0, 30], "0'": ["0'", 0, 29], "1'": ["1'", 0, 29], Sym('D'+1): [None, 0, 32]}, direction=1)
64 State(instruction=29, acc=1, transitions={'0': ["0'", 1, 30], '1': ["1'", 1, 30], "0'": ["0'", 1, 29], "1'": ["1'", 1, 29], Sym('D'+1): [None, 1, 32]}, direction=1)
65 State(instruction=29, acc=2, transitions={'0': ["0'", 2, 30], '1': ["1'", 2, 30], "0'": ["0'", 2, 29], "1'": ["1'", 2, 29], Sym('D'+1): [None, 2, 32]}, direction=1)
66 State(instruction=29, acc=3, transitions={'0': ["0'", 3, 30], '1': ["1'", 3, 30], "0'": ["0'", 3, 29], "1'": ["1'", 3, 29], Sym('D'+1): [None, 3, 32]}, direction=1)
67 State(instruction=32, acc=0, transitions={'0': ['0', 0, 32], '1': ['1', 0, 32], "0'": ['0', 0, 32], "1'": ['1', 0, 32], Sym('B'+1): [None, 0, 33]}, direction=1)
68 State(instruction=32, acc=1, transitions={'0': ['0', 1, 32], '1': ['1', 1, 32], "0'": ['0', 1, 32], "1'": ['1', 1, 32], Sym('B'+1): [None, 1, 33]}, direction=1)
69 State(instruction=32, acc=2, transitions={'0': ['0', 2, 32], '1': ['1', 2, 32], "0'": ['0', 2, 32], "1'": ['1', 2, 32], Sym('B'+1): [None, 2, 33]}, direction=1)
70 State(instruction=32, acc=3, transitions={'0': ['0', 3, 32], '1': ['1', 3, 32], "0'": ['0', 3, 32], "1'": ['1', 3, 32], Sym('B'+1): [None, 3, 33]}, direction=1)
71 State(instruction=33, acc=0, transitions={'0': ['0', 0, 33], '1': ['1', 0, 33], "0'": ['0', 0, 33], "1'": ['1', 0, 33], Sym('D'+1): [None, 0, 10]}, direction=1)
72 State(instruction=33, acc=1, transitions={'0': ['0', 1, 33], '1': ['1', 1, 33], "0'": ['0', 1, 33], "1'": ['1', 1, 33], Sym('D'+1): [None, 1, 10]}, direction=1)
73 State(instruction=33, acc=2, transitions={'0': ['0', 2, 33], '1': ['1', 2, 33], "0'": ['0', 2, 33], "1'": ['1', 2, 33], Sym('D'+1): [None, 2, 10]}, direction=1)
74 State(instruction=33, acc=3, transitions={'0': ['0', 3, 33], '1': ['1', 3, 33], "0'": ['0', 3, 33], "1'": ['1', 3, 33], Sym('D'+1): [None, 3, 10]}, direction=1)
>>> more_posts = True
>>> while more_posts:
	more_posts = apply_posts()

	
Traceback (most recent call last):
  File "<pyshell#463>", line 2, in <module>
    more_posts = apply_posts()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 551, in apply_posts
    _,instr = quasis[state.instruction]
AttributeError: 'tuple' object has no attribute 'instruction'
>>> def apply_posts():
    global quasis
    altered = False
    for _,state in get_quasis([State]):
        instr = quasis[state.instruction]
        for symbol,transition,instr in get_quasis_from(state,[Instruction]):
            k = 0
            if instr.command=='JUMP':
                altered = True
            elif instr.command=='BRANCH':
                k = transition[1]
                altered = True
            elif instr.command=='LOADI' and instr.loadto=='ACC':
                transition[1] = instr.imm
                altered = True
            elif instr.command=='MAP':
                size = validate_maps(instr.map_)
                if size==(2,1):
                    assert instruction.command=='LOAD' and instruction.loadto=='TEMP'
                    if (transition[1],int(symbol)) in instr.map_:
                        transition[1] = instr.map_[(transition[1],int(symbol))][0]
                    altered = True
                elif size==(1,1):
                    if (transition[1],) in instr.map_:
                        transition[1] = instr.map_[(transition[1],)][0]             
                    altered = True
            transition[2] = instr.next_quasis[k]               
    return altered

>>> while more_posts:
	more_posts = apply_posts()

	
Traceback (most recent call last):
  File "<pyshell#467>", line 2, in <module>
    more_posts = apply_posts()
  File "<pyshell#465>", line 19, in apply_posts
    assert instruction.command=='LOAD' and instruction.loadto=='TEMP'
NameError: name 'instruction' is not defined
>>> def apply_posts():
    global quasis
    altered = False
    for _,state in get_quasis([State]):
        instr = quasis[state.instruction]
        for symbol,transition,instr in get_quasis_from(state,[Instruction]):
            k = 0
            if instr.command=='JUMP':
                altered = True
            elif instr.command=='BRANCH':
                k = transition[1]
                altered = True
            elif instr.command=='LOADI' and instr.loadto=='ACC':
                transition[1] = instr.imm
                altered = True
            elif instr.command=='MAP':
                size = validate_maps(instr.map_)
                if size==(2,1):
                    assert instr.command=='LOAD' and instr.loadto=='TEMP'
                    if (transition[1],int(symbol)) in instr.map_:
                        transition[1] = instr.map_[(transition[1],int(symbol))][0]
                    altered = True
                elif size==(1,1):
                    if (transition[1],) in instr.map_:
                        transition[1] = instr.map_[(transition[1],)][0]             
                    altered = True
            transition[2] = instr.next_quasis[k]               
    return altered

>>> while more_posts:
	more_posts = apply_posts()

	
Traceback (most recent call last):
  File "<pyshell#471>", line 2, in <module>
    more_posts = apply_posts()
  File "<pyshell#469>", line 19, in apply_posts
    assert instr.command=='LOAD' and instr.loadto=='TEMP'
AssertionError
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[6])
1 FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[6])
2 Instruction(STORE, vard=S, next_quasis=[3, 3])
3 End(is_start=False, next_quasis=[None])
4 End(is_start=True, next_quasis=[6])
5 None
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 22, 22, 22])
8 None
9 FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[22])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
11 None
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
14 None
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
18 None
19 Instruction(UNREAD, vard=A, next_quasis=[2])
20 End(is_start=False, next_quasis=[2])
21 End(is_start=True, next_quasis=[22])
22 Instruction(LOADI, next_quasis=[24])
23 None
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[28])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[29])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
31 None
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[10])
34 End(is_start=False, next_quasis=[10])
35 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 3], "1'": ["1'", 0, 3], Sym('S'+1): [None, 0, 3]}, direction=1)
36 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 3], "1'": ["1'", 1, 3], Sym('S'+1): [None, 1, 3]}, direction=1)
37 State(instruction=2, acc=2, transitions={'0': ['2', 2, 3], '1': ['2', 2, 3], "0'": ["0'", 2, 3], "1'": ["1'", 2, 3], Sym('S'+1): [None, 2, 3]}, direction=1)
38 State(instruction=2, acc=3, transitions={'0': ['3', 3, 3], '1': ['3', 3, 3], "0'": ["0'", 3, 3], "1'": ["1'", 3, 3], Sym('S'+1): [None, 3, 3]}, direction=1)
39 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 13], '1': ["1'", 0, 24], "0'": ["0'", 0, 12], "1'": ["1'", 0, 12], Sym('A'+1): [None, 0, 3]}, direction=1)
40 State(instruction=6, acc=1, transitions={'0': ["0'", 0, 13], '1': ["1'", 0, 24], "0'": ["0'", 1, 22], "1'": ["1'", 1, 22], Sym('A'+1): [None, 1, 3]}, direction=1)
41 State(instruction=6, acc=2, transitions={'0': ["0'", 0, 13], '1': ["1'", 0, 24], "0'": ["0'", 2, 22], "1'": ["1'", 2, 22], Sym('A'+1): [None, 2, 3]}, direction=1)
42 State(instruction=6, acc=3, transitions={'0': ["0'", 0, 13], '1': ["1'", 0, 24], "0'": ["0'", 3, 22], "1'": ["1'", 3, 22], Sym('A'+1): [None, 3, 3]}, direction=1)
43 State(instruction=12, acc=0, transitions={'0': ['0', 0, 12], '1': ['0', 0, 17], "0'": ['0', 0, 12], "1'": ['0', 0, 17], Sym('B'+1): [None, 0, 7]}, direction=1)
44 State(instruction=12, acc=1, transitions={'0': ['1', 0, 12], '1': ['1', 0, 17], "0'": ['1', 0, 12], "1'": ['1', 0, 17], Sym('B'+1): [None, 0, 16]}, direction=1)
45 State(instruction=12, acc=2, transitions=None, direction=None)
46 State(instruction=12, acc=3, transitions=None, direction=None)
47 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 2], "0'": ["0'", 0, 15], "1'": ["1'", 0, 15], Sym('A'+1): [None, 0, 3]}, direction=1)
48 State(instruction=16, acc=1, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 2], "0'": ["0'", 1, 19], "1'": ["1'", 1, 19], Sym('A'+1): [None, 1, 3]}, direction=1)
49 State(instruction=16, acc=2, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 2], "0'": ["0'", 2, 19], "1'": ["1'", 2, 19], Sym('A'+1): [None, 2, 3]}, direction=1)
50 State(instruction=16, acc=3, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 2], "0'": ["0'", 3, 19], "1'": ["1'", 3, 19], Sym('A'+1): [None, 3, 3]}, direction=1)
51 State(instruction=19, acc=0, transitions={'0': ['0', 0, 3], '1': ['1', 0, 3], "0'": ['0', 0, 3], "1'": ['1', 0, 3], Sym('A'+1): [None, 0, 3]}, direction=1)
52 State(instruction=19, acc=1, transitions={'0': ['0', 1, 3], '1': ['1', 1, 3], "0'": ['0', 1, 3], "1'": ['1', 1, 3], Sym('A'+1): [None, 1, 3]}, direction=1)
53 State(instruction=19, acc=2, transitions={'0': ['0', 2, 3], '1': ['1', 2, 3], "0'": ['0', 2, 3], "1'": ['1', 2, 3], Sym('A'+1): [None, 2, 3]}, direction=1)
54 State(instruction=19, acc=3, transitions={'0': ['0', 3, 3], '1': ['1', 3, 3], "0'": ['0', 3, 3], "1'": ['1', 3, 3], Sym('A'+1): [None, 3, 3]}, direction=1)
55 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 25], '1': ["1'", 0, 25], "0'": ["0'", 0, 24], "1'": ["1'", 0, 24], Sym('B'+1): [None, 0, 32]}, direction=1)
56 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 25], '1': ["1'", 1, 25], "0'": ["0'", 1, 24], "1'": ["1'", 1, 24], Sym('B'+1): [None, 1, 32]}, direction=1)
57 State(instruction=24, acc=2, transitions={'0': ["0'", 2, 25], '1': ["1'", 2, 25], "0'": ["0'", 2, 24], "1'": ["1'", 2, 24], Sym('B'+1): [None, 2, 32]}, direction=1)
58 State(instruction=24, acc=3, transitions={'0': ["0'", 3, 25], '1': ["1'", 3, 25], "0'": ["0'", 3, 24], "1'": ["1'", 3, 24], Sym('B'+1): [None, 3, 32]}, direction=1)
59 State(instruction=26, acc=0, transitions={'0': ['0', 0, 27], '1': ['1', 0, 27], "0'": ["0'", 0, 26], "1'": ["1'", 0, 26], Sym('D'+1): [None, 0, 32]}, direction=1)
60 State(instruction=26, acc=1, transitions={'0': ['0', 1, 27], '1': ['1', 1, 27], "0'": ["0'", 1, 26], "1'": ["1'", 1, 26], Sym('D'+1): [None, 1, 32]}, direction=1)
61 State(instruction=26, acc=2, transitions={'0': ['0', 2, 27], '1': ['1', 2, 27], "0'": ["0'", 2, 26], "1'": ["1'", 2, 26], Sym('D'+1): [None, 2, 32]}, direction=1)
62 State(instruction=26, acc=3, transitions={'0': ['0', 3, 27], '1': ['1', 3, 27], "0'": ["0'", 3, 26], "1'": ["1'", 3, 26], Sym('D'+1): [None, 3, 32]}, direction=1)
63 State(instruction=29, acc=0, transitions={'0': ["0'", 0, 30], '1': ["1'", 0, 30], "0'": ["0'", 0, 29], "1'": ["1'", 0, 29], Sym('D'+1): [None, 0, 32]}, direction=1)
64 State(instruction=29, acc=1, transitions={'0': ["0'", 1, 30], '1': ["1'", 1, 30], "0'": ["0'", 1, 29], "1'": ["1'", 1, 29], Sym('D'+1): [None, 1, 32]}, direction=1)
65 State(instruction=29, acc=2, transitions={'0': ["0'", 2, 30], '1': ["1'", 2, 30], "0'": ["0'", 2, 29], "1'": ["1'", 2, 29], Sym('D'+1): [None, 2, 32]}, direction=1)
66 State(instruction=29, acc=3, transitions={'0': ["0'", 3, 30], '1': ["1'", 3, 30], "0'": ["0'", 3, 29], "1'": ["1'", 3, 29], Sym('D'+1): [None, 3, 32]}, direction=1)
67 State(instruction=32, acc=0, transitions={'0': ['0', 0, 32], '1': ['1', 0, 32], "0'": ['0', 0, 32], "1'": ['1', 0, 32], Sym('B'+1): [None, 0, 33]}, direction=1)
68 State(instruction=32, acc=1, transitions={'0': ['0', 1, 32], '1': ['1', 1, 32], "0'": ['0', 1, 32], "1'": ['1', 1, 32], Sym('B'+1): [None, 1, 33]}, direction=1)
69 State(instruction=32, acc=2, transitions={'0': ['0', 2, 32], '1': ['1', 2, 32], "0'": ['0', 2, 32], "1'": ['1', 2, 32], Sym('B'+1): [None, 2, 33]}, direction=1)
70 State(instruction=32, acc=3, transitions={'0': ['0', 3, 32], '1': ['1', 3, 32], "0'": ['0', 3, 32], "1'": ['1', 3, 32], Sym('B'+1): [None, 3, 33]}, direction=1)
71 State(instruction=33, acc=0, transitions={'0': ['0', 0, 33], '1': ['1', 0, 33], "0'": ['0', 0, 33], "1'": ['1', 0, 33], Sym('D'+1): [None, 0, 10]}, direction=1)
72 State(instruction=33, acc=1, transitions={'0': ['0', 1, 33], '1': ['1', 1, 33], "0'": ['0', 1, 33], "1'": ['1', 1, 33], Sym('D'+1): [None, 1, 10]}, direction=1)
73 State(instruction=33, acc=2, transitions={'0': ['0', 2, 33], '1': ['1', 2, 33], "0'": ['0', 2, 33], "1'": ['1', 2, 33], Sym('D'+1): [None, 2, 10]}, direction=1)
74 State(instruction=33, acc=3, transitions={'0': ['0', 3, 33], '1': ['1', 3, 33], "0'": ['0', 3, 33], "1'": ['1', 3, 33], Sym('D'+1): [None, 3, 10]}, direction=1)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
>>> instructions2states()
>>> more_posts
Traceback (most recent call last):
  File "<pyshell#482>", line 1, in <module>
    more_posts
NameError: name 'more_posts' is not defined
>>> more_posts = True
>>> while more_posts:
	more_posts = apply_posts()

	
Traceback (most recent call last):
  File "<pyshell#486>", line 2, in <module>
    more_posts = apply_posts()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 566, in apply_posts
    if (transition[1],int(symbol)) in next_instr.map_:
ValueError: invalid literal for int() with base 10: "0'"
>>> for k,quasi in get_quasis([State]):
	print(k,quasi)

	
35 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 3], "1'": ["1'", 0, 3], Sym('S'+1): [None, 0, 3]}, direction=1)
36 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 3], "1'": ["1'", 1, 3], Sym('S'+1): [None, 1, 3]}, direction=1)
37 State(instruction=2, acc=2, transitions={'0': ['2', 2, 3], '1': ['2', 2, 3], "0'": ["0'", 2, 3], "1'": ["1'", 2, 3], Sym('S'+1): [None, 2, 3]}, direction=1)
38 State(instruction=2, acc=3, transitions={'0': ['3', 3, 3], '1': ['3', 3, 3], "0'": ["0'", 3, 3], "1'": ["1'", 3, 3], Sym('S'+1): [None, 3, 3]}, direction=1)
39 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 13], '1': ["1'", 0, 24], "0'": ["0'", 0, 12], "1'": ["1'", 0, 12], Sym('A'+1): [None, 0, 3]}, direction=1)
40 State(instruction=6, acc=1, transitions={'0': ["0'", 0, 13], '1': ["1'", 0, 24], "0'": ["0'", 1, 22], "1'": ["1'", 1, 22], Sym('A'+1): [None, 1, 3]}, direction=1)
41 State(instruction=6, acc=2, transitions={'0': ["0'", 0, 13], '1': ["1'", 0, 24], "0'": ["0'", 2, 22], "1'": ["1'", 2, 22], Sym('A'+1): [None, 2, 3]}, direction=1)
42 State(instruction=6, acc=3, transitions={'0': ["0'", 0, 13], '1': ["1'", 0, 24], "0'": ["0'", 3, 22], "1'": ["1'", 3, 22], Sym('A'+1): [None, 3, 3]}, direction=1)
43 State(instruction=12, acc=0, transitions={'0': ['0', 0, 12], '1': ['0', 0, 17], "0'": ['0', 0, 12], "1'": ['0', 0, 17], Sym('B'+1): [None, 0, 7]}, direction=1)
44 State(instruction=12, acc=1, transitions={'0': ['1', 0, 12], '1': ['1', 0, 17], "0'": ['1', 0, 12], "1'": ['1', 0, 17], Sym('B'+1): [None, 0, 16]}, direction=1)
45 State(instruction=12, acc=2, transitions=None, direction=None)
46 State(instruction=12, acc=3, transitions=None, direction=None)
47 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 2], "0'": ["0'", 0, 15], "1'": ["1'", 0, 15], Sym('A'+1): [None, 0, 3]}, direction=1)
48 State(instruction=16, acc=1, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 2], "0'": ["0'", 1, 19], "1'": ["1'", 1, 19], Sym('A'+1): [None, 1, 3]}, direction=1)
49 State(instruction=16, acc=2, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 2], "0'": ["0'", 2, 19], "1'": ["1'", 2, 19], Sym('A'+1): [None, 2, 3]}, direction=1)
50 State(instruction=16, acc=3, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 2], "0'": ["0'", 3, 19], "1'": ["1'", 3, 19], Sym('A'+1): [None, 3, 3]}, direction=1)
51 State(instruction=19, acc=0, transitions={'0': ['0', 0, 3], '1': ['1', 0, 3], "0'": ['0', 0, 3], "1'": ['1', 0, 3], Sym('A'+1): [None, 0, 3]}, direction=1)
52 State(instruction=19, acc=1, transitions={'0': ['0', 1, 3], '1': ['1', 1, 3], "0'": ['0', 1, 3], "1'": ['1', 1, 3], Sym('A'+1): [None, 1, 3]}, direction=1)
53 State(instruction=19, acc=2, transitions={'0': ['0', 2, 3], '1': ['1', 2, 3], "0'": ['0', 2, 3], "1'": ['1', 2, 3], Sym('A'+1): [None, 2, 3]}, direction=1)
54 State(instruction=19, acc=3, transitions={'0': ['0', 3, 3], '1': ['1', 3, 3], "0'": ['0', 3, 3], "1'": ['1', 3, 3], Sym('A'+1): [None, 3, 3]}, direction=1)
55 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 27], '1': ["1'", 1, 27], "0'": ["0'", 0, 25], "1'": ["1'", 0, 25], Sym('B'+1): [None, 0, 33]}, direction=1)
56 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 26], '1': ["1'", 2, 26], "0'": ["0'", 1, 25], "1'": ["1'", 1, 25], Sym('B'+1): [None, 1, 33]}, direction=1)
57 State(instruction=24, acc=2, transitions={'0': ["0'", 2, 26], '1': ["1'", 2, 26], "0'": ["0'", 2, 25], "1'": ["1'", 2, 25], Sym('B'+1): [None, 2, 33]}, direction=1)
58 State(instruction=24, acc=3, transitions={'0': ["0'", 3, 26], '1': ["1'", 3, 26], "0'": ["0'", 3, 25], "1'": ["1'", 3, 25], Sym('B'+1): [None, 3, 33]}, direction=1)
59 State(instruction=26, acc=0, transitions={'0': ['0', 0, 28], '1': ['1', 1, 28], "0'": ["0'", 0, 27], "1'": ["1'", 0, 27], Sym('D'+1): [None, 0, 33]}, direction=1)
60 State(instruction=26, acc=1, transitions={'0': ['0', 1, 28], '1': ['1', 2, 28], "0'": ["0'", 1, 27], "1'": ["1'", 1, 27], Sym('D'+1): [None, 1, 33]}, direction=1)
61 State(instruction=26, acc=2, transitions={'0': ['0', 2, 28], '1': ['1', 3, 28], "0'": ["0'", 2, 27], "1'": ["1'", 2, 27], Sym('D'+1): [None, 2, 33]}, direction=1)
62 State(instruction=26, acc=3, transitions={'0': ['0', 3, 28], '1': ['1', 3, 28], "0'": ["0'", 3, 27], "1'": ["1'", 3, 27], Sym('D'+1): [None, 3, 33]}, direction=1)
63 State(instruction=29, acc=0, transitions={'0': ["0'", 0, 24], '1': ["1'", 0, 24], "0'": ["0'", 0, 30], "1'": ["1'", 0, 30], Sym('D'+1): [None, 0, 33]}, direction=1)
64 State(instruction=29, acc=1, transitions={'0': ["0'", 1, 24], '1': ["1'", 1, 24], "0'": ["0'", 1, 30], "1'": ["1'", 1, 30], Sym('D'+1): [None, 1, 33]}, direction=1)
65 State(instruction=29, acc=2, transitions={'0': ["0'", 2, 24], '1': ["1'", 2, 24], "0'": ["0'", 2, 30], "1'": ["1'", 2, 30], Sym('D'+1): [None, 2, 33]}, direction=1)
66 State(instruction=29, acc=3, transitions={'0': ["0'", 3, 24], '1': ["1'", 3, 24], "0'": ["0'", 3, 30], "1'": ["1'", 3, 30], Sym('D'+1): [None, 3, 33]}, direction=1)
67 State(instruction=32, acc=0, transitions={'0': ['0', 0, 33], '1': ['1', 0, 33], "0'": ['0', 0, 33], "1'": ['1', 0, 33], Sym('B'+1): [None, 0, 10]}, direction=1)
68 State(instruction=32, acc=1, transitions={'0': ['0', 1, 33], '1': ['1', 1, 33], "0'": ['0', 1, 33], "1'": ['1', 1, 33], Sym('B'+1): [None, 1, 10]}, direction=1)
69 State(instruction=32, acc=2, transitions={'0': ['0', 2, 33], '1': ['1', 2, 33], "0'": ['0', 2, 33], "1'": ['1', 2, 33], Sym('B'+1): [None, 2, 10]}, direction=1)
70 State(instruction=32, acc=3, transitions={'0': ['0', 3, 33], '1': ['1', 3, 33], "0'": ['0', 3, 33], "1'": ['1', 3, 33], Sym('B'+1): [None, 3, 10]}, direction=1)
71 State(instruction=33, acc=0, transitions={'0': ['0', 0, 10], '1': ['1', 0, 10], "0'": ['0', 0, 10], "1'": ['1', 0, 10], Sym('D'+1): [None, 0, 12]}, direction=1)
72 State(instruction=33, acc=1, transitions={'0': ['0', 1, 10], '1': ['1', 1, 10], "0'": ['0', 1, 10], "1'": ['1', 1, 10], Sym('D'+1): [None, 1, 19]}, direction=1)
73 State(instruction=33, acc=2, transitions={'0': ['0', 2, 10], '1': ['1', 2, 10], "0'": ['0', 2, 10], "1'": ['1', 2, 10], Sym('D'+1): [None, 2, 12]}, direction=1)
74 State(instruction=33, acc=3, transitions={'0': ['0', 3, 10], '1': ['1', 3, 10], "0'": ['0', 3, 10], "1'": ['1', 3, 10], Sym('D'+1): [None, 3, 12]}, direction=1)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
>>> instructions2states()
>>> more_posts = True
>>> while more_posts:
	more_posts = apply_posts()

	
Traceback (most recent call last):
  File "<pyshell#499>", line 2, in <module>
    more_posts = apply_posts()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 566, in apply_posts
    if (transition[1],int(symbol)) in next_instr.map_:
ValueError: invalid literal for int() with base 10: "0'"
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
>>> instructions2states()
>>> for k,quasi in get_quasis([State]):
	print(k,quasi)

	
35 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 2], "1'": ["1'", 0, 2], Sym('S'+1): [None, 0, 3]}, direction=1)
36 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 2], "1'": ["1'", 1, 2], Sym('S'+1): [None, 1, 3]}, direction=1)
37 State(instruction=2, acc=2, transitions={'0': ['2', 2, 3], '1': ['2', 2, 3], "0'": ["0'", 2, 2], "1'": ["1'", 2, 2], Sym('S'+1): [None, 2, 3]}, direction=1)
38 State(instruction=2, acc=3, transitions={'0': ['3', 3, 3], '1': ['3', 3, 3], "0'": ["0'", 3, 2], "1'": ["1'", 3, 2], Sym('S'+1): [None, 3, 3]}, direction=1)
39 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 7], '1': ["1'", 1, 7], "0'": ["0'", 0, 6], "1'": ["1'", 0, 6], Sym('A'+1): [None, 0, 19]}, direction=1)
40 State(instruction=6, acc=1, transitions={'0': ["0'", 0, 7], '1': ["1'", 1, 7], "0'": ["0'", 1, 6], "1'": ["1'", 1, 6], Sym('A'+1): [None, 1, 19]}, direction=1)
41 State(instruction=6, acc=2, transitions={'0': ["0'", 0, 7], '1': ["1'", 1, 7], "0'": ["0'", 2, 6], "1'": ["1'", 2, 6], Sym('A'+1): [None, 2, 19]}, direction=1)
42 State(instruction=6, acc=3, transitions={'0': ["0'", 0, 7], '1': ["1'", 1, 7], "0'": ["0'", 3, 6], "1'": ["1'", 3, 6], Sym('A'+1): [None, 3, 19]}, direction=1)
43 State(instruction=12, acc=0, transitions={'0': ['0', 0, 12], '1': ['0', 1, 12], "0'": ['0', 0, 12], "1'": ['0', 1, 12], Sym('B'+1): [None, 0, 13]}, direction=1)
44 State(instruction=12, acc=1, transitions={'0': ['1', 0, 12], '1': ['1', 1, 12], "0'": ['1', 0, 12], "1'": ['1', 1, 12], Sym('B'+1): [None, 1, 13]}, direction=1)
45 State(instruction=12, acc=2, transitions=None, direction=None)
46 State(instruction=12, acc=3, transitions=None, direction=None)
47 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 17], '1': ["1'", 1, 17], "0'": ["0'", 0, 16], "1'": ["1'", 0, 16], Sym('A'+1): [None, 0, 19]}, direction=1)
48 State(instruction=16, acc=1, transitions={'0': ["0'", 0, 17], '1': ["1'", 1, 17], "0'": ["0'", 1, 16], "1'": ["1'", 1, 16], Sym('A'+1): [None, 1, 19]}, direction=1)
49 State(instruction=16, acc=2, transitions={'0': ["0'", 0, 17], '1': ["1'", 1, 17], "0'": ["0'", 2, 16], "1'": ["1'", 2, 16], Sym('A'+1): [None, 2, 19]}, direction=1)
50 State(instruction=16, acc=3, transitions={'0': ["0'", 0, 17], '1': ["1'", 1, 17], "0'": ["0'", 3, 16], "1'": ["1'", 3, 16], Sym('A'+1): [None, 3, 19]}, direction=1)
51 State(instruction=19, acc=0, transitions={'0': ['0', 0, 19], '1': ['1', 0, 19], "0'": ['0', 0, 19], "1'": ['1', 0, 19], Sym('A'+1): [None, 0, 2]}, direction=1)
52 State(instruction=19, acc=1, transitions={'0': ['0', 1, 19], '1': ['1', 1, 19], "0'": ['0', 1, 19], "1'": ['1', 1, 19], Sym('A'+1): [None, 1, 2]}, direction=1)
53 State(instruction=19, acc=2, transitions={'0': ['0', 2, 19], '1': ['1', 2, 19], "0'": ['0', 2, 19], "1'": ['1', 2, 19], Sym('A'+1): [None, 2, 2]}, direction=1)
54 State(instruction=19, acc=3, transitions={'0': ['0', 3, 19], '1': ['1', 3, 19], "0'": ['0', 3, 19], "1'": ['1', 3, 19], Sym('A'+1): [None, 3, 2]}, direction=1)
55 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 25], '1': ["1'", 0, 25], "0'": ["0'", 0, 24], "1'": ["1'", 0, 24], Sym('B'+1): [None, 0, 32]}, direction=1)
56 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 25], '1': ["1'", 1, 25], "0'": ["0'", 1, 24], "1'": ["1'", 1, 24], Sym('B'+1): [None, 1, 32]}, direction=1)
57 State(instruction=24, acc=2, transitions={'0': ["0'", 2, 25], '1': ["1'", 2, 25], "0'": ["0'", 2, 24], "1'": ["1'", 2, 24], Sym('B'+1): [None, 2, 32]}, direction=1)
58 State(instruction=24, acc=3, transitions={'0': ["0'", 3, 25], '1': ["1'", 3, 25], "0'": ["0'", 3, 24], "1'": ["1'", 3, 24], Sym('B'+1): [None, 3, 32]}, direction=1)
59 State(instruction=26, acc=0, transitions={'0': ['0', 0, 27], '1': ['1', 0, 27], "0'": ["0'", 0, 26], "1'": ["1'", 0, 26], Sym('D'+1): [None, 0, 32]}, direction=1)
60 State(instruction=26, acc=1, transitions={'0': ['0', 1, 27], '1': ['1', 1, 27], "0'": ["0'", 1, 26], "1'": ["1'", 1, 26], Sym('D'+1): [None, 1, 32]}, direction=1)
61 State(instruction=26, acc=2, transitions={'0': ['0', 2, 27], '1': ['1', 2, 27], "0'": ["0'", 2, 26], "1'": ["1'", 2, 26], Sym('D'+1): [None, 2, 32]}, direction=1)
62 State(instruction=26, acc=3, transitions={'0': ['0', 3, 27], '1': ['1', 3, 27], "0'": ["0'", 3, 26], "1'": ["1'", 3, 26], Sym('D'+1): [None, 3, 32]}, direction=1)
63 State(instruction=29, acc=0, transitions={'0': ["0'", 0, 30], '1': ["1'", 0, 30], "0'": ["0'", 0, 29], "1'": ["1'", 0, 29], Sym('D'+1): [None, 0, 32]}, direction=1)
64 State(instruction=29, acc=1, transitions={'0': ["0'", 1, 30], '1': ["1'", 1, 30], "0'": ["0'", 1, 29], "1'": ["1'", 1, 29], Sym('D'+1): [None, 1, 32]}, direction=1)
65 State(instruction=29, acc=2, transitions={'0': ["0'", 2, 30], '1': ["1'", 2, 30], "0'": ["0'", 2, 29], "1'": ["1'", 2, 29], Sym('D'+1): [None, 2, 32]}, direction=1)
66 State(instruction=29, acc=3, transitions={'0': ["0'", 3, 30], '1': ["1'", 3, 30], "0'": ["0'", 3, 29], "1'": ["1'", 3, 29], Sym('D'+1): [None, 3, 32]}, direction=1)
67 State(instruction=32, acc=0, transitions={'0': ['0', 0, 32], '1': ['1', 0, 32], "0'": ['0', 0, 32], "1'": ['1', 0, 32], Sym('B'+1): [None, 0, 33]}, direction=1)
68 State(instruction=32, acc=1, transitions={'0': ['0', 1, 32], '1': ['1', 1, 32], "0'": ['0', 1, 32], "1'": ['1', 1, 32], Sym('B'+1): [None, 1, 33]}, direction=1)
69 State(instruction=32, acc=2, transitions={'0': ['0', 2, 32], '1': ['1', 2, 32], "0'": ['0', 2, 32], "1'": ['1', 2, 32], Sym('B'+1): [None, 2, 33]}, direction=1)
70 State(instruction=32, acc=3, transitions={'0': ['0', 3, 32], '1': ['1', 3, 32], "0'": ['0', 3, 32], "1'": ['1', 3, 32], Sym('B'+1): [None, 3, 33]}, direction=1)
71 State(instruction=33, acc=0, transitions={'0': ['0', 0, 33], '1': ['1', 0, 33], "0'": ['0', 0, 33], "1'": ['1', 0, 33], Sym('D'+1): [None, 0, 10]}, direction=1)
72 State(instruction=33, acc=1, transitions={'0': ['0', 1, 33], '1': ['1', 1, 33], "0'": ['0', 1, 33], "1'": ['1', 1, 33], Sym('D'+1): [None, 1, 10]}, direction=1)
73 State(instruction=33, acc=2, transitions={'0': ['0', 2, 33], '1': ['1', 2, 33], "0'": ['0', 2, 33], "1'": ['1', 2, 33], Sym('D'+1): [None, 2, 10]}, direction=1)
74 State(instruction=33, acc=3, transitions={'0': ['0', 3, 33], '1': ['1', 3, 33], "0'": ['0', 3, 33], "1'": ['1', 3, 33], Sym('D'+1): [None, 3, 10]}, direction=1)
>>> apply_posts()
True
>>> for k,quasi in get_quasis([State]):
	print(k,quasi)

	
35 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 2], "1'": ["1'", 0, 2], Sym('S'+1): [None, 0, 3]}, direction=1)
36 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 2], "1'": ["1'", 1, 2], Sym('S'+1): [None, 1, 3]}, direction=1)
37 State(instruction=2, acc=2, transitions={'0': ['2', 2, 3], '1': ['2', 2, 3], "0'": ["0'", 2, 2], "1'": ["1'", 2, 2], Sym('S'+1): [None, 2, 3]}, direction=1)
38 State(instruction=2, acc=3, transitions={'0': ['3', 3, 3], '1': ['3', 3, 3], "0'": ["0'", 3, 2], "1'": ["1'", 3, 2], Sym('S'+1): [None, 3, 3]}, direction=1)
39 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 12], '1': ["1'", 1, 22], "0'": ["0'", 0, 7], "1'": ["1'", 0, 7], Sym('A'+1): [None, 0, 2]}, direction=1)
40 State(instruction=6, acc=1, transitions={'0': ["0'", 0, 12], '1': ["1'", 1, 22], "0'": ["0'", 1, 7], "1'": ["1'", 1, 7], Sym('A'+1): [None, 1, 2]}, direction=1)
41 State(instruction=6, acc=2, transitions={'0': ["0'", 0, 12], '1': ["1'", 1, 22], "0'": ["0'", 2, 7], "1'": ["1'", 2, 7], Sym('A'+1): [None, 2, 2]}, direction=1)
42 State(instruction=6, acc=3, transitions={'0': ["0'", 0, 12], '1': ["1'", 1, 22], "0'": ["0'", 3, 7], "1'": ["1'", 3, 7], Sym('A'+1): [None, 3, 2]}, direction=1)
43 State(instruction=12, acc=0, transitions={'0': ['0', 0, 6], '1': ['0', 1, 15], "0'": ['0', 0, 6], "1'": ['0', 1, 15], Sym('B'+1): [None, 0, 6]}, direction=1)
44 State(instruction=12, acc=1, transitions={'0': ['1', 0, 6], '1': ['1', 1, 15], "0'": ['1', 0, 6], "1'": ['1', 1, 15], Sym('B'+1): [None, 1, 15]}, direction=1)
45 State(instruction=12, acc=2, transitions=None, direction=None)
46 State(instruction=12, acc=3, transitions=None, direction=None)
47 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 15], '1': ["1'", 1, 19], "0'": ["0'", 0, 17], "1'": ["1'", 0, 17], Sym('A'+1): [None, 0, 2]}, direction=1)
48 State(instruction=16, acc=1, transitions={'0': ["0'", 0, 15], '1': ["1'", 1, 19], "0'": ["0'", 1, 17], "1'": ["1'", 1, 17], Sym('A'+1): [None, 1, 2]}, direction=1)
49 State(instruction=16, acc=2, transitions={'0': ["0'", 0, 15], '1': ["1'", 1, 19], "0'": ["0'", 2, 17], "1'": ["1'", 2, 17], Sym('A'+1): [None, 2, 2]}, direction=1)
50 State(instruction=16, acc=3, transitions={'0': ["0'", 0, 15], '1': ["1'", 1, 19], "0'": ["0'", 3, 17], "1'": ["1'", 3, 17], Sym('A'+1): [None, 3, 2]}, direction=1)
51 State(instruction=19, acc=0, transitions={'0': ['0', 0, 2], '1': ['1', 0, 2], "0'": ['0', 0, 2], "1'": ['1', 0, 2], Sym('A'+1): [None, 0, 3]}, direction=1)
52 State(instruction=19, acc=1, transitions={'0': ['0', 1, 2], '1': ['1', 1, 2], "0'": ['0', 1, 2], "1'": ['1', 1, 2], Sym('A'+1): [None, 1, 3]}, direction=1)
53 State(instruction=19, acc=2, transitions={'0': ['0', 2, 2], '1': ['1', 2, 2], "0'": ['0', 2, 2], "1'": ['1', 2, 2], Sym('A'+1): [None, 2, 3]}, direction=1)
54 State(instruction=19, acc=3, transitions={'0': ['0', 3, 2], '1': ['1', 3, 2], "0'": ['0', 3, 2], "1'": ['1', 3, 2], Sym('A'+1): [None, 3, 3]}, direction=1)
55 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 26], '1': ["1'", 1, 26], "0'": ["0'", 0, 25], "1'": ["1'", 0, 25], Sym('B'+1): [None, 0, 33]}, direction=1)
56 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 26], '1': ["1'", 2, 26], "0'": ["0'", 1, 25], "1'": ["1'", 1, 25], Sym('B'+1): [None, 1, 33]}, direction=1)
57 State(instruction=24, acc=2, transitions={'0': ["0'", 2, 26], '1': ["1'", 2, 26], "0'": ["0'", 2, 25], "1'": ["1'", 2, 25], Sym('B'+1): [None, 2, 33]}, direction=1)
58 State(instruction=24, acc=3, transitions={'0': ["0'", 3, 26], '1': ["1'", 3, 26], "0'": ["0'", 3, 25], "1'": ["1'", 3, 25], Sym('B'+1): [None, 3, 33]}, direction=1)
59 State(instruction=26, acc=0, transitions={'0': ['0', 0, 28], '1': ['1', 1, 28], "0'": ["0'", 0, 27], "1'": ["1'", 0, 27], Sym('D'+1): [None, 0, 33]}, direction=1)
60 State(instruction=26, acc=1, transitions={'0': ['0', 1, 28], '1': ['1', 2, 28], "0'": ["0'", 1, 27], "1'": ["1'", 1, 27], Sym('D'+1): [None, 1, 33]}, direction=1)
61 State(instruction=26, acc=2, transitions={'0': ['0', 2, 28], '1': ['1', 3, 28], "0'": ["0'", 2, 27], "1'": ["1'", 2, 27], Sym('D'+1): [None, 2, 33]}, direction=1)
62 State(instruction=26, acc=3, transitions={'0': ['0', 3, 28], '1': ['1', 3, 28], "0'": ["0'", 3, 27], "1'": ["1'", 3, 27], Sym('D'+1): [None, 3, 33]}, direction=1)
63 State(instruction=29, acc=0, transitions={'0': ["0'", 0, 24], '1': ["1'", 0, 24], "0'": ["0'", 0, 30], "1'": ["1'", 0, 30], Sym('D'+1): [None, 0, 33]}, direction=1)
64 State(instruction=29, acc=1, transitions={'0': ["0'", 1, 24], '1': ["1'", 1, 24], "0'": ["0'", 1, 30], "1'": ["1'", 1, 30], Sym('D'+1): [None, 1, 33]}, direction=1)
65 State(instruction=29, acc=2, transitions={'0': ["0'", 2, 24], '1': ["1'", 2, 24], "0'": ["0'", 2, 30], "1'": ["1'", 2, 30], Sym('D'+1): [None, 2, 33]}, direction=1)
66 State(instruction=29, acc=3, transitions={'0': ["0'", 3, 24], '1': ["1'", 3, 24], "0'": ["0'", 3, 30], "1'": ["1'", 3, 30], Sym('D'+1): [None, 3, 33]}, direction=1)
67 State(instruction=32, acc=0, transitions={'0': ['0', 0, 33], '1': ['1', 0, 33], "0'": ['0', 0, 33], "1'": ['1', 0, 33], Sym('B'+1): [None, 0, 10]}, direction=1)
68 State(instruction=32, acc=1, transitions={'0': ['0', 1, 33], '1': ['1', 1, 33], "0'": ['0', 1, 33], "1'": ['1', 1, 33], Sym('B'+1): [None, 1, 10]}, direction=1)
69 State(instruction=32, acc=2, transitions={'0': ['0', 2, 33], '1': ['1', 2, 33], "0'": ['0', 2, 33], "1'": ['1', 2, 33], Sym('B'+1): [None, 2, 10]}, direction=1)
70 State(instruction=32, acc=3, transitions={'0': ['0', 3, 33], '1': ['1', 3, 33], "0'": ['0', 3, 33], "1'": ['1', 3, 33], Sym('B'+1): [None, 3, 10]}, direction=1)
71 State(instruction=33, acc=0, transitions={'0': ['0', 0, 10], '1': ['1', 0, 10], "0'": ['0', 0, 10], "1'": ['1', 0, 10], Sym('D'+1): [None, 0, 12]}, direction=1)
72 State(instruction=33, acc=1, transitions={'0': ['0', 1, 10], '1': ['1', 1, 10], "0'": ['0', 1, 10], "1'": ['1', 1, 10], Sym('D'+1): [None, 1, 19]}, direction=1)
73 State(instruction=33, acc=2, transitions={'0': ['0', 2, 10], '1': ['1', 2, 10], "0'": ['0', 2, 10], "1'": ['1', 2, 10], Sym('D'+1): [None, 2, 12]}, direction=1)
74 State(instruction=33, acc=3, transitions={'0': ['0', 3, 10], '1': ['1', 3, 10], "0'": ['0', 3, 10], "1'": ['1', 3, 10], Sym('D'+1): [None, 3, 12]}, direction=1)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> function.next_quasis = [None]
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
>>> more_posts = True
>>> while more_posts:
	more_posts = apply_posts()

	
>>> for k,quasi in get_quasis([State]):
	print(k,quasi)

	
>>> len(quasis)
35
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
>>> instructions2states()
>>> more_posts = True
>>> while more_posts:
	more_posts = apply_posts()

	
Traceback (most recent call last):
  File "<pyshell#537>", line 2, in <module>
    more_posts = apply_posts()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 573, in apply_posts
    if state_change:
UnboundLocalError: local variable 'state_change' referenced before assignment
>>> def apply_posts():
    global quasis
    altered = False
    for _,state in get_quasis([State]):
        instruction = quasis[state.instruction]
        for symbol,transition,next_instr in get_quasis_from(state,[Instruction]):
            state_change = -1
            if next_instr.command=='JUMP':
                state_change = 0
            elif next_instr.command=='BRANCH':
                state_change = transition[1]
            elif next_instr.command=='LOADI' and next_instr.loadto=='ACC':
                transition[1] = next_instr.imm
                state_change = 0
            elif next_instr.command=='MAP':
                size = validate_maps(next_instr.map_)
                if size==(2,1):
                    assert instruction.command=='LOAD' and instruction.loadto=='TEMP'
                    if (transition[1],int(symbol)) in next_instr.map_:
                        transition[1] = next_instr.map_[(transition[1],int(symbol))][0]
                    state_change = 0
                elif size==(1,1):
                    if (transition[1],) in next_instr.map_:
                        transition[1] = next_instr.map_[(transition[1],)][0]             
                    state_change = 0
            if state_change>=0:
                transition[2] = next_instr.next_quasis[state_change]
                altered = True
    return altered

>>> apply_posts()
True
>>> apply_posts()
True
>>> apply_posts()
False
>>> for k,quasi in get_quasis([State]):
	print(k,quasi)

	
35 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 2], "1'": ["1'", 0, 2], Sym('S'+1): [None, 0, 3]}, direction=1)
36 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 2], "1'": ["1'", 1, 2], Sym('S'+1): [None, 1, 3]}, direction=1)
37 State(instruction=2, acc=2, transitions={'0': ['2', 2, 3], '1': ['2', 2, 3], "0'": ["0'", 2, 2], "1'": ["1'", 2, 2], Sym('S'+1): [None, 2, 3]}, direction=1)
38 State(instruction=2, acc=3, transitions={'0': ['3', 3, 3], '1': ['3', 3, 3], "0'": ["0'", 3, 2], "1'": ["1'", 3, 2], Sym('S'+1): [None, 3, 3]}, direction=1)
39 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 12], '1': ["1'", 0, 24], "0'": ["0'", 0, 6], "1'": ["1'", 0, 6], Sym('A'+1): [None, 0, 19]}, direction=1)
40 State(instruction=6, acc=1, transitions={'0': ["0'", 0, 12], '1': ["1'", 0, 24], "0'": ["0'", 1, 6], "1'": ["1'", 1, 6], Sym('A'+1): [None, 1, 19]}, direction=1)
41 State(instruction=6, acc=2, transitions={'0': ["0'", 0, 12], '1': ["1'", 0, 24], "0'": ["0'", 2, 6], "1'": ["1'", 2, 6], Sym('A'+1): [None, 2, 19]}, direction=1)
42 State(instruction=6, acc=3, transitions={'0': ["0'", 0, 12], '1': ["1'", 0, 24], "0'": ["0'", 3, 6], "1'": ["1'", 3, 6], Sym('A'+1): [None, 3, 19]}, direction=1)
43 State(instruction=12, acc=0, transitions={'0': ['0', 0, 12], '1': ['0', 1, 12], "0'": ['0', 0, 12], "1'": ['0', 1, 12], Sym('B'+1): [None, 0, 6]}, direction=1)
44 State(instruction=12, acc=1, transitions={'0': ['1', 0, 12], '1': ['1', 1, 12], "0'": ['1', 0, 12], "1'": ['1', 1, 12], Sym('B'+1): [None, 0, 16]}, direction=1)
45 State(instruction=12, acc=2, transitions=None, direction=None)
46 State(instruction=12, acc=3, transitions=None, direction=None)
47 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 19], "0'": ["0'", 0, 16], "1'": ["1'", 0, 16], Sym('A'+1): [None, 0, 19]}, direction=1)
48 State(instruction=16, acc=1, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 19], "0'": ["0'", 1, 16], "1'": ["1'", 1, 16], Sym('A'+1): [None, 1, 19]}, direction=1)
49 State(instruction=16, acc=2, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 19], "0'": ["0'", 2, 16], "1'": ["1'", 2, 16], Sym('A'+1): [None, 2, 19]}, direction=1)
50 State(instruction=16, acc=3, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 19], "0'": ["0'", 3, 16], "1'": ["1'", 3, 16], Sym('A'+1): [None, 3, 19]}, direction=1)
51 State(instruction=19, acc=0, transitions={'0': ['0', 0, 19], '1': ['1', 0, 19], "0'": ['0', 0, 19], "1'": ['1', 0, 19], Sym('A'+1): [None, 0, 2]}, direction=1)
52 State(instruction=19, acc=1, transitions={'0': ['0', 1, 19], '1': ['1', 1, 19], "0'": ['0', 1, 19], "1'": ['1', 1, 19], Sym('A'+1): [None, 1, 2]}, direction=1)
53 State(instruction=19, acc=2, transitions={'0': ['0', 2, 19], '1': ['1', 2, 19], "0'": ['0', 2, 19], "1'": ['1', 2, 19], Sym('A'+1): [None, 2, 2]}, direction=1)
54 State(instruction=19, acc=3, transitions={'0': ['0', 3, 19], '1': ['1', 3, 19], "0'": ['0', 3, 19], "1'": ['1', 3, 19], Sym('A'+1): [None, 3, 2]}, direction=1)
55 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 26], '1': ["1'", 1, 26], "0'": ["0'", 0, 24], "1'": ["1'", 0, 24], Sym('B'+1): [None, 0, 32]}, direction=1)
56 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 26], '1': ["1'", 2, 26], "0'": ["0'", 1, 24], "1'": ["1'", 1, 24], Sym('B'+1): [None, 1, 32]}, direction=1)
57 State(instruction=24, acc=2, transitions={'0': ["0'", 2, 26], '1': ["1'", 2, 26], "0'": ["0'", 2, 24], "1'": ["1'", 2, 24], Sym('B'+1): [None, 2, 32]}, direction=1)
58 State(instruction=24, acc=3, transitions={'0': ["0'", 3, 26], '1': ["1'", 3, 26], "0'": ["0'", 3, 24], "1'": ["1'", 3, 24], Sym('B'+1): [None, 3, 32]}, direction=1)
59 State(instruction=26, acc=0, transitions={'0': ['0', 0, 28], '1': ['1', 1, 28], "0'": ["0'", 0, 26], "1'": ["1'", 0, 26], Sym('D'+1): [None, 0, 32]}, direction=1)
60 State(instruction=26, acc=1, transitions={'0': ['0', 1, 28], '1': ['1', 2, 28], "0'": ["0'", 1, 26], "1'": ["1'", 1, 26], Sym('D'+1): [None, 1, 32]}, direction=1)
61 State(instruction=26, acc=2, transitions={'0': ['0', 2, 28], '1': ['1', 3, 28], "0'": ["0'", 2, 26], "1'": ["1'", 2, 26], Sym('D'+1): [None, 2, 32]}, direction=1)
62 State(instruction=26, acc=3, transitions={'0': ['0', 3, 28], '1': ['1', 3, 28], "0'": ["0'", 3, 26], "1'": ["1'", 3, 26], Sym('D'+1): [None, 3, 32]}, direction=1)
63 State(instruction=29, acc=0, transitions={'0': ["0'", 0, 24], '1': ["1'", 0, 24], "0'": ["0'", 0, 29], "1'": ["1'", 0, 29], Sym('D'+1): [None, 0, 32]}, direction=1)
64 State(instruction=29, acc=1, transitions={'0': ["0'", 1, 24], '1': ["1'", 1, 24], "0'": ["0'", 1, 29], "1'": ["1'", 1, 29], Sym('D'+1): [None, 1, 32]}, direction=1)
65 State(instruction=29, acc=2, transitions={'0': ["0'", 2, 24], '1': ["1'", 2, 24], "0'": ["0'", 2, 29], "1'": ["1'", 2, 29], Sym('D'+1): [None, 2, 32]}, direction=1)
66 State(instruction=29, acc=3, transitions={'0': ["0'", 3, 24], '1': ["1'", 3, 24], "0'": ["0'", 3, 29], "1'": ["1'", 3, 29], Sym('D'+1): [None, 3, 32]}, direction=1)
67 State(instruction=32, acc=0, transitions={'0': ['0', 0, 32], '1': ['1', 0, 32], "0'": ['0', 0, 32], "1'": ['1', 0, 32], Sym('B'+1): [None, 0, 33]}, direction=1)
68 State(instruction=32, acc=1, transitions={'0': ['0', 1, 32], '1': ['1', 1, 32], "0'": ['0', 1, 32], "1'": ['1', 1, 32], Sym('B'+1): [None, 1, 33]}, direction=1)
69 State(instruction=32, acc=2, transitions={'0': ['0', 2, 32], '1': ['1', 2, 32], "0'": ['0', 2, 32], "1'": ['1', 2, 32], Sym('B'+1): [None, 2, 33]}, direction=1)
70 State(instruction=32, acc=3, transitions={'0': ['0', 3, 32], '1': ['1', 3, 32], "0'": ['0', 3, 32], "1'": ['1', 3, 32], Sym('B'+1): [None, 3, 33]}, direction=1)
71 State(instruction=33, acc=0, transitions={'0': ['0', 0, 33], '1': ['1', 0, 33], "0'": ['0', 0, 33], "1'": ['1', 0, 33], Sym('D'+1): [None, 0, 12]}, direction=1)
72 State(instruction=33, acc=1, transitions={'0': ['0', 1, 33], '1': ['1', 1, 33], "0'": ['0', 1, 33], "1'": ['1', 1, 33], Sym('D'+1): [None, 1, 19]}, direction=1)
73 State(instruction=33, acc=2, transitions={'0': ['0', 2, 33], '1': ['1', 2, 33], "0'": ['0', 2, 33], "1'": ['1', 2, 33], Sym('D'+1): [None, 2, 12]}, direction=1)
74 State(instruction=33, acc=3, transitions={'0': ['0', 3, 33], '1': ['1', 3, 33], "0'": ['0', 3, 33], "1'": ['1', 3, 33], Sym('D'+1): [None, 3, 12]}, direction=1)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
>>> instructions2states()
>>> more_posts = True
>>> apply_posts()
True
>>> apply_pres()
Traceback (most recent call last):
  File "<pyshell#555>", line 1, in <module>
    apply_pres()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 629, in apply_pres
    replace_links(k,instr.next_quasis[0])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 483, in replace_links
    for symbol in quasi.transitions:
TypeError: 'NoneType' object is not iterable
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
>>> instructions2states()
>>> apply_posts()
True
>>> apply_pres()
Traceback (most recent call last):
  File "<pyshell#565>", line 1, in <module>
    apply_pres()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 630, in apply_pres
    quasi.next_quasis[0] = 0
NameError: name 'quasi' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
>>> instructions2states()
>>> apply_posts()
True
>>> apply_pres()
True
>>> apply_posts()
True
>>> apply_pres()
False
>>> apply_posts()
False
>>> for k,quasi in get_quasis([State]):
	print(k,quasi)

	
35 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 2], "1'": ["1'", 0, 2], Sym('S'+1): [None, 0, 3]}, direction=1)
36 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 2], "1'": ["1'", 1, 2], Sym('S'+1): [None, 1, 3]}, direction=1)
37 State(instruction=2, acc=2, transitions={'0': ['2', 2, 3], '1': ['2', 2, 3], "0'": ["0'", 2, 2], "1'": ["1'", 2, 2], Sym('S'+1): [None, 2, 3]}, direction=1)
38 State(instruction=2, acc=3, transitions={'0': ['3', 3, 3], '1': ['3', 3, 3], "0'": ["0'", 3, 2], "1'": ["1'", 3, 2], Sym('S'+1): [None, 3, 3]}, direction=1)
39 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 12], '1': ["1'", 0, 24], "0'": ["0'", 0, 6], "1'": ["1'", 0, 6], Sym('A'+1): [None, 0, 19]}, direction=1)
40 State(instruction=6, acc=1, transitions={'0': ["0'", 0, 12], '1': ["1'", 0, 24], "0'": ["0'", 1, 6], "1'": ["1'", 1, 6], Sym('A'+1): [None, 1, 19]}, direction=1)
41 State(instruction=6, acc=2, transitions={'0': ["0'", 0, 12], '1': ["1'", 0, 24], "0'": ["0'", 2, 6], "1'": ["1'", 2, 6], Sym('A'+1): [None, 2, 19]}, direction=1)
42 State(instruction=6, acc=3, transitions={'0': ["0'", 0, 12], '1': ["1'", 0, 24], "0'": ["0'", 3, 6], "1'": ["1'", 3, 6], Sym('A'+1): [None, 3, 19]}, direction=1)
43 State(instruction=12, acc=0, transitions={'0': ['0', 0, 12], '1': ['0', 1, 12], "0'": ['0', 0, 12], "1'": ['0', 1, 12], Sym('B'+1): [None, 0, 6]}, direction=1)
44 State(instruction=12, acc=1, transitions={'0': ['1', 0, 12], '1': ['1', 1, 12], "0'": ['1', 0, 12], "1'": ['1', 1, 12], Sym('B'+1): [None, 0, 16]}, direction=1)
45 State(instruction=12, acc=2, transitions={}, direction=None)
46 State(instruction=12, acc=3, transitions={}, direction=None)
47 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 19], "0'": ["0'", 0, 16], "1'": ["1'", 0, 16], Sym('A'+1): [None, 0, 19]}, direction=1)
48 State(instruction=16, acc=1, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 19], "0'": ["0'", 1, 16], "1'": ["1'", 1, 16], Sym('A'+1): [None, 1, 19]}, direction=1)
49 State(instruction=16, acc=2, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 19], "0'": ["0'", 2, 16], "1'": ["1'", 2, 16], Sym('A'+1): [None, 2, 19]}, direction=1)
50 State(instruction=16, acc=3, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 19], "0'": ["0'", 3, 16], "1'": ["1'", 3, 16], Sym('A'+1): [None, 3, 19]}, direction=1)
51 State(instruction=19, acc=0, transitions={'0': ['0', 0, 19], '1': ['1', 0, 19], "0'": ['0', 0, 19], "1'": ['1', 0, 19], Sym('A'+1): [None, 0, 2]}, direction=1)
52 State(instruction=19, acc=1, transitions={'0': ['0', 1, 19], '1': ['1', 1, 19], "0'": ['0', 1, 19], "1'": ['1', 1, 19], Sym('A'+1): [None, 1, 2]}, direction=1)
53 State(instruction=19, acc=2, transitions={'0': ['0', 2, 19], '1': ['1', 2, 19], "0'": ['0', 2, 19], "1'": ['1', 2, 19], Sym('A'+1): [None, 2, 2]}, direction=1)
54 State(instruction=19, acc=3, transitions={'0': ['0', 3, 19], '1': ['1', 3, 19], "0'": ['0', 3, 19], "1'": ['1', 3, 19], Sym('A'+1): [None, 3, 2]}, direction=1)
55 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 26], '1': ["1'", 1, 26], "0'": ["0'", 0, 24], "1'": ["1'", 0, 24], Sym('B'+1): [None, 0, 32]}, direction=1)
56 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 26], '1': ["1'", 2, 26], "0'": ["0'", 1, 24], "1'": ["1'", 1, 24], Sym('B'+1): [None, 1, 32]}, direction=1)
57 State(instruction=24, acc=2, transitions={'0': ["0'", 2, 26], '1': ["1'", 2, 26], "0'": ["0'", 2, 24], "1'": ["1'", 2, 24], Sym('B'+1): [None, 2, 32]}, direction=1)
58 State(instruction=24, acc=3, transitions={'0': ["0'", 3, 26], '1': ["1'", 3, 26], "0'": ["0'", 3, 24], "1'": ["1'", 3, 24], Sym('B'+1): [None, 3, 32]}, direction=1)
59 State(instruction=26, acc=0, transitions={'0': ['0', 0, 29], '1': ['1', 1, 29], "0'": ["0'", 0, 26], "1'": ["1'", 0, 26], Sym('D'+1): [None, 0, 32]}, direction=1)
60 State(instruction=26, acc=1, transitions={'0': ['0', 1, 29], '1': ['1', 2, 29], "0'": ["0'", 1, 26], "1'": ["1'", 1, 26], Sym('D'+1): [None, 1, 32]}, direction=1)
61 State(instruction=26, acc=2, transitions={'0': ['0', 2, 29], '1': ['1', 3, 29], "0'": ["0'", 2, 26], "1'": ["1'", 2, 26], Sym('D'+1): [None, 2, 32]}, direction=1)
62 State(instruction=26, acc=3, transitions={'0': ['0', 3, 29], '1': ['1', 3, 29], "0'": ["0'", 3, 26], "1'": ["1'", 3, 26], Sym('D'+1): [None, 3, 32]}, direction=1)
63 State(instruction=29, acc=0, transitions={'0': ["0'", 0, 24], '1': ["0'", 0, 24], "0'": ["0'", 0, 29], "1'": ["1'", 0, 29], Sym('D'+1): [None, 0, 32]}, direction=1)
64 State(instruction=29, acc=1, transitions={'0': ["1'", 0, 24], '1': ["1'", 0, 24], "0'": ["0'", 1, 29], "1'": ["1'", 1, 29], Sym('D'+1): [None, 1, 32]}, direction=1)
65 State(instruction=29, acc=2, transitions={'0': ["0'", 1, 24], '1': ["0'", 1, 24], "0'": ["0'", 2, 29], "1'": ["1'", 2, 29], Sym('D'+1): [None, 2, 32]}, direction=1)
66 State(instruction=29, acc=3, transitions={'0': ["1'", 1, 24], '1': ["1'", 1, 24], "0'": ["0'", 3, 29], "1'": ["1'", 3, 29], Sym('D'+1): [None, 3, 32]}, direction=1)
67 State(instruction=32, acc=0, transitions={'0': ['0', 0, 32], '1': ['1', 0, 32], "0'": ['0', 0, 32], "1'": ['1', 0, 32], Sym('B'+1): [None, 0, 33]}, direction=1)
68 State(instruction=32, acc=1, transitions={'0': ['0', 1, 32], '1': ['1', 1, 32], "0'": ['0', 1, 32], "1'": ['1', 1, 32], Sym('B'+1): [None, 1, 33]}, direction=1)
69 State(instruction=32, acc=2, transitions={'0': ['0', 2, 32], '1': ['1', 2, 32], "0'": ['0', 2, 32], "1'": ['1', 2, 32], Sym('B'+1): [None, 2, 33]}, direction=1)
70 State(instruction=32, acc=3, transitions={'0': ['0', 3, 32], '1': ['1', 3, 32], "0'": ['0', 3, 32], "1'": ['1', 3, 32], Sym('B'+1): [None, 3, 33]}, direction=1)
71 State(instruction=33, acc=0, transitions={'0': ['0', 0, 33], '1': ['1', 0, 33], "0'": ['0', 0, 33], "1'": ['1', 0, 33], Sym('D'+1): [None, 0, 12]}, direction=1)
72 State(instruction=33, acc=1, transitions={'0': ['0', 1, 33], '1': ['1', 1, 33], "0'": ['0', 1, 33], "1'": ['1', 1, 33], Sym('D'+1): [None, 1, 19]}, direction=1)
73 State(instruction=33, acc=2, transitions={'0': ['0', 2, 33], '1': ['1', 2, 33], "0'": ['0', 2, 33], "1'": ['1', 2, 33], Sym('D'+1): [None, 2, 12]}, direction=1)
74 State(instruction=33, acc=3, transitions={'0': ['0', 3, 33], '1': ['1', 3, 33], "0'": ['0', 3, 33], "1'": ['1', 3, 33], Sym('D'+1): [None, 3, 12]}, direction=1)
>>> quasis[29]
Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
>>> instructions2states()
>>> apply_posts()
True
>>> apply_pres()
True
>>> apply_posts()
True
>>> apply_pres()
False
>>> apply_posts()
False
>>> stitch_acc()
Traceback (most recent call last):
  File "<pyshell#595>", line 1, in <module>
    stitch_acc()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 685, in stitch_acc
    quasis[0].next_quasis[0] = find_state(0,quasis[0].next_quasis[0])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 668, in find_state
    if quasi.acc==acc and quasi.step==step:
NameError: name 'quasi' is not defined
>>> def find_state(acc,step):
    global quasis
    if type(quasis[step])==Instruction:
        for k,state in get_quasis([State]):
            if state.acc==acc and state.instruction==step:
                return k
    else:
        return step

>>> stitch_acc()
>>> for k,quasi in get_quasis([State]):
	print(k,quasi)

	
35 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 2], "1'": ["1'", 0, 2], Sym('S'+1): [None, 0, 3]}, direction=1)
36 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 2], "1'": ["1'", 1, 2], Sym('S'+1): [None, 1, 3]}, direction=1)
37 State(instruction=2, acc=2, transitions={'0': ['2', 2, 3], '1': ['2', 2, 3], "0'": ["0'", 2, 2], "1'": ["1'", 2, 2], Sym('S'+1): [None, 2, 3]}, direction=1)
38 State(instruction=2, acc=3, transitions={'0': ['3', 3, 3], '1': ['3', 3, 3], "0'": ["0'", 3, 2], "1'": ["1'", 3, 2], Sym('S'+1): [None, 3, 3]}, direction=1)
39 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 12], '1': ["1'", 0, 24], "0'": ["0'", 0, 6], "1'": ["1'", 0, 6], Sym('A'+1): [None, 0, 19]}, direction=1)
40 State(instruction=6, acc=1, transitions={'0': ["0'", 0, 12], '1': ["1'", 0, 24], "0'": ["0'", 1, 6], "1'": ["1'", 1, 6], Sym('A'+1): [None, 1, 19]}, direction=1)
41 State(instruction=6, acc=2, transitions={'0': ["0'", 0, 12], '1': ["1'", 0, 24], "0'": ["0'", 2, 6], "1'": ["1'", 2, 6], Sym('A'+1): [None, 2, 19]}, direction=1)
42 State(instruction=6, acc=3, transitions={'0': ["0'", 0, 12], '1': ["1'", 0, 24], "0'": ["0'", 3, 6], "1'": ["1'", 3, 6], Sym('A'+1): [None, 3, 19]}, direction=1)
43 State(instruction=12, acc=0, transitions={'0': ['0', 0, 12], '1': ['0', 1, 12], "0'": ['0', 0, 12], "1'": ['0', 1, 12], Sym('B'+1): [None, 0, 6]}, direction=1)
44 State(instruction=12, acc=1, transitions={'0': ['1', 0, 12], '1': ['1', 1, 12], "0'": ['1', 0, 12], "1'": ['1', 1, 12], Sym('B'+1): [None, 0, 16]}, direction=1)
45 State(instruction=12, acc=2, transitions={}, direction=None)
46 State(instruction=12, acc=3, transitions={}, direction=None)
47 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 19], "0'": ["0'", 0, 16], "1'": ["1'", 0, 16], Sym('A'+1): [None, 0, 19]}, direction=1)
48 State(instruction=16, acc=1, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 19], "0'": ["0'", 1, 16], "1'": ["1'", 1, 16], Sym('A'+1): [None, 1, 19]}, direction=1)
49 State(instruction=16, acc=2, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 19], "0'": ["0'", 2, 16], "1'": ["1'", 2, 16], Sym('A'+1): [None, 2, 19]}, direction=1)
50 State(instruction=16, acc=3, transitions={'0': ["0'", 0, 16], '1': ["1'", 1, 19], "0'": ["0'", 3, 16], "1'": ["1'", 3, 16], Sym('A'+1): [None, 3, 19]}, direction=1)
51 State(instruction=19, acc=0, transitions={'0': ['0', 0, 19], '1': ['1', 0, 19], "0'": ['0', 0, 19], "1'": ['1', 0, 19], Sym('A'+1): [None, 0, 2]}, direction=1)
52 State(instruction=19, acc=1, transitions={'0': ['0', 1, 19], '1': ['1', 1, 19], "0'": ['0', 1, 19], "1'": ['1', 1, 19], Sym('A'+1): [None, 1, 2]}, direction=1)
53 State(instruction=19, acc=2, transitions={'0': ['0', 2, 19], '1': ['1', 2, 19], "0'": ['0', 2, 19], "1'": ['1', 2, 19], Sym('A'+1): [None, 2, 2]}, direction=1)
54 State(instruction=19, acc=3, transitions={'0': ['0', 3, 19], '1': ['1', 3, 19], "0'": ['0', 3, 19], "1'": ['1', 3, 19], Sym('A'+1): [None, 3, 2]}, direction=1)
55 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 26], '1': ["1'", 1, 26], "0'": ["0'", 0, 24], "1'": ["1'", 0, 24], Sym('B'+1): [None, 0, 32]}, direction=1)
56 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 26], '1': ["1'", 2, 26], "0'": ["0'", 1, 24], "1'": ["1'", 1, 24], Sym('B'+1): [None, 1, 32]}, direction=1)
57 State(instruction=24, acc=2, transitions={'0': ["0'", 2, 26], '1': ["1'", 2, 26], "0'": ["0'", 2, 24], "1'": ["1'", 2, 24], Sym('B'+1): [None, 2, 32]}, direction=1)
58 State(instruction=24, acc=3, transitions={'0': ["0'", 3, 26], '1': ["1'", 3, 26], "0'": ["0'", 3, 24], "1'": ["1'", 3, 24], Sym('B'+1): [None, 3, 32]}, direction=1)
59 State(instruction=26, acc=0, transitions={'0': ['0', 0, 29], '1': ['1', 1, 29], "0'": ["0'", 0, 26], "1'": ["1'", 0, 26], Sym('D'+1): [None, 0, 32]}, direction=1)
60 State(instruction=26, acc=1, transitions={'0': ['0', 1, 29], '1': ['1', 2, 29], "0'": ["0'", 1, 26], "1'": ["1'", 1, 26], Sym('D'+1): [None, 1, 32]}, direction=1)
61 State(instruction=26, acc=2, transitions={'0': ['0', 2, 29], '1': ['1', 3, 29], "0'": ["0'", 2, 26], "1'": ["1'", 2, 26], Sym('D'+1): [None, 2, 32]}, direction=1)
62 State(instruction=26, acc=3, transitions={'0': ['0', 3, 29], '1': ['1', 3, 29], "0'": ["0'", 3, 26], "1'": ["1'", 3, 26], Sym('D'+1): [None, 3, 32]}, direction=1)
63 State(instruction=29, acc=0, transitions={'0': ["0'", 0, 24], '1': ["0'", 0, 24], "0'": ["0'", 0, 29], "1'": ["1'", 0, 29], Sym('D'+1): [None, 0, 32]}, direction=1)
64 State(instruction=29, acc=1, transitions={'0': ["1'", 0, 24], '1': ["1'", 0, 24], "0'": ["0'", 1, 29], "1'": ["1'", 1, 29], Sym('D'+1): [None, 1, 32]}, direction=1)
65 State(instruction=29, acc=2, transitions={'0': ["0'", 1, 24], '1': ["0'", 1, 24], "0'": ["0'", 2, 29], "1'": ["1'", 2, 29], Sym('D'+1): [None, 2, 32]}, direction=1)
66 State(instruction=29, acc=3, transitions={'0': ["1'", 1, 24], '1': ["1'", 1, 24], "0'": ["0'", 3, 29], "1'": ["1'", 3, 29], Sym('D'+1): [None, 3, 32]}, direction=1)
67 State(instruction=32, acc=0, transitions={'0': ['0', 0, 32], '1': ['1', 0, 32], "0'": ['0', 0, 32], "1'": ['1', 0, 32], Sym('B'+1): [None, 0, 33]}, direction=1)
68 State(instruction=32, acc=1, transitions={'0': ['0', 1, 32], '1': ['1', 1, 32], "0'": ['0', 1, 32], "1'": ['1', 1, 32], Sym('B'+1): [None, 1, 33]}, direction=1)
69 State(instruction=32, acc=2, transitions={'0': ['0', 2, 32], '1': ['1', 2, 32], "0'": ['0', 2, 32], "1'": ['1', 2, 32], Sym('B'+1): [None, 2, 33]}, direction=1)
70 State(instruction=32, acc=3, transitions={'0': ['0', 3, 32], '1': ['1', 3, 32], "0'": ['0', 3, 32], "1'": ['1', 3, 32], Sym('B'+1): [None, 3, 33]}, direction=1)
71 State(instruction=33, acc=0, transitions={'0': ['0', 0, 33], '1': ['1', 0, 33], "0'": ['0', 0, 33], "1'": ['1', 0, 33], Sym('D'+1): [None, 0, 12]}, direction=1)
72 State(instruction=33, acc=1, transitions={'0': ['0', 1, 33], '1': ['1', 1, 33], "0'": ['0', 1, 33], "1'": ['1', 1, 33], Sym('D'+1): [None, 1, 19]}, direction=1)
73 State(instruction=33, acc=2, transitions={'0': ['0', 2, 33], '1': ['1', 2, 33], "0'": ['0', 2, 33], "1'": ['1', 2, 33], Sym('D'+1): [None, 2, 12]}, direction=1)
74 State(instruction=33, acc=3, transitions={'0': ['0', 3, 33], '1': ['1', 3, 33], "0'": ['0', 3, 33], "1'": ['1', 3, 33], Sym('D'+1): [None, 3, 12]}, direction=1)
>>> quasis[0]
End(is_start=True, next_quasis=[39])
>>> quasis[2]
Instruction(STORE, vard=S, next_quasis=[3, 3])
>>> for k,quasi in get_quasis([Instruction]):
	print(k,quasi)

	
2 Instruction(STORE, vard=S, next_quasis=[3, 3])
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 22, 22, 22])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
19 Instruction(UNREAD, vard=A, next_quasis=[2])
22 Instruction(LOADI, next_quasis=[24])
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[29])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[0])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[10])
>>> def find_state(acc,step):
    global quasis
    if type(quasis[step])==Instruction:
        for k,state in get_states_of(step):
            if state.acc==acc:
                return k
    else:
        return step

>>> find_state(0,3)
3
>>> quasis[3]
End(is_start=False, next_quasis=[None])
>>> quasis[6]
Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
>>> acc,step=0,3
>>> type(quasis[step])==Instruction
False
>>> find_state(0,6)
39
>>> list(get_quasis_from(quasis[39],[Instruction]))
[('0', ["0'", 0, 12], Instruction(SLLs, vard=B, next_quasis=[13])), ('1', ["1'", 0, 24], Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])), ("0'", ["0'", 0, 6], Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])), ("1'", ["1'", 0, 6], Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])), (Sym('A'+1), [None, 0, 19], Instruction(UNREAD, vard=A, next_quasis=[2]))]
>>> for a,b,c in get_quasis_from(quasis[39],[Instruction]):
	print(a,b,c)

	
0 ["0'", 0, 12] Instruction(SLLs, vard=B, next_quasis=[13])
1 ["1'", 0, 24] Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
0' ["0'", 0, 6] Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
1' ["1'", 0, 6] Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
Sym('A'+1) [None, 0, 19] Instruction(UNREAD, vard=A, next_quasis=[2])
>>> for _,transition,_ in get_quasis_from(quasis[39],[Instruction]):
	print(transition)

	
["0'", 0, 12]
["1'", 0, 24]
["0'", 0, 6]
["1'", 0, 6]
[None, 0, 19]
>>> find_state(0,12)
43
>>> A = [[0,1],[2,3],[4,5]]
>>> def gen():
	for a in A:
		yield a

		
>>> for a in gen():
	a[1]+=7

	
>>> A
[[0, 8], [2, 10], [4, 12]]
>>> def stitch_acc():
    global quasis
    quasis[0].next_quasis[0] = find_state(0,quasis[0].next_quasis[0])
    for state in get_quasis([State]):
        for _,transition,_ in get_quasis_from(state,[Instruction]):
            print(transition[2],find_state(transition[1],transition[2]))
            transition[2] = find_state(transition[1],transition[2])

            
>>> stich_acc()
Traceback (most recent call last):
  File "<pyshell#631>", line 1, in <module>
    stich_acc()
NameError: name 'stich_acc' is not defined
>>> stitch_acc()
>>> for state in get_quasis([State]):
        for _,transition,_ in get_quasis_from(state,[Instruction]):
		print('Hi')
		
SyntaxError: inconsistent use of tabs and spaces in indentation
for state in get_quasis([State]):
        for _,transition,_ in get_quasis_from(state,[Instruction]):
		print('Hi')
>>> for state in get_quasis([State]):
	for _,transition,_ in get_quasis_from(state,[Instruction]):
		print('Hi')

		
>>> for state in get_quasis([State]):
	print('Hello')
	for _,transition,_ in get_quasis_from(state,[Instruction]):
		print('Hi')

		
Hello

Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Traceback (most recent call last):
  File "<pyshell#639>", line 2, in <module>
    print('Hello')
KeyboardInterrupt
>>> def stitch_acc():
    global quasis
    quasis[0].next_quasis[0] = find_state(0,quasis[0].next_quasis[0])
    for _,state in get_quasis([State]):
        for _,transition,_ in get_quasis_from(state,[Instruction]):
            print(transition[2],find_state(transition[1],transition[2]))
            transition[2] = find_state(transition[1],transition[2])

            
>>> stitch_acc()
2 35
2 35
2 36
2 36
2 37
2 37
2 38
2 38
12 43
24 55
6 39
6 39
19 51
12 43
24 55
6 40
6 40
19 52
12 43
24 55
6 41
6 41
19 53
12 43
24 55
6 42
6 42
19 54
12 43
12 44
6 39
12 43
12 44
16 47
16 47
19 52
16 47
16 47
19 51
16 47
19 52
16 48
16 48
19 52
16 47
19 52
16 49
16 49
19 53
16 47
19 52
16 50
16 50
19 54
19 51
19 51
19 51
19 51
2 35
19 52
19 52
19 52
19 52
2 36
19 53
19 53
19 53
19 53
2 37
19 54
19 54
19 54
19 54
2 38
26 59
26 60
24 55
24 55
32 67
26 60
26 61
24 56
24 56
32 68
26 61
26 61
24 57
24 57
32 69
26 62
26 62
24 58
24 58
32 70
29 63
29 64
26 59
26 59
32 67
29 64
29 65
26 60
26 60
32 68
29 65
29 66
26 61
26 61
32 69
29 66
29 66
26 62
26 62
32 70
24 55
24 55
29 63
29 63
32 67
24 55
24 55
29 64
29 64
32 68
24 56
24 56
29 65
29 65
32 69
24 56
24 56
29 66
29 66
32 70
32 67
32 67
32 67
32 67
33 71
32 68
32 68
32 68
32 68
33 72
32 69
32 69
32 69
32 69
33 73
32 70
32 70
32 70
32 70
33 74
33 71
33 71
33 71
33 71
12 43
33 72
33 72
33 72
33 72
19 52
33 73
33 73
33 73
33 73
12 45
33 74
33 74
33 74
33 74
12 46
>>> for k,quasi in get_quasis([State]):
	print(k,quasi)

	
35 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 35], "1'": ["1'", 0, 35], Sym('S'+1): [None, 0, 3]}, direction=1)
36 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 36], "1'": ["1'", 1, 36], Sym('S'+1): [None, 1, 3]}, direction=1)
37 State(instruction=2, acc=2, transitions={'0': ['2', 2, 3], '1': ['2', 2, 3], "0'": ["0'", 2, 37], "1'": ["1'", 2, 37], Sym('S'+1): [None, 2, 3]}, direction=1)
38 State(instruction=2, acc=3, transitions={'0': ['3', 3, 3], '1': ['3', 3, 3], "0'": ["0'", 3, 38], "1'": ["1'", 3, 38], Sym('S'+1): [None, 3, 3]}, direction=1)
39 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 43], '1': ["1'", 0, 55], "0'": ["0'", 0, 39], "1'": ["1'", 0, 39], Sym('A'+1): [None, 0, 51]}, direction=1)
40 State(instruction=6, acc=1, transitions={'0': ["0'", 0, 43], '1': ["1'", 0, 55], "0'": ["0'", 1, 40], "1'": ["1'", 1, 40], Sym('A'+1): [None, 1, 52]}, direction=1)
41 State(instruction=6, acc=2, transitions={'0': ["0'", 0, 43], '1': ["1'", 0, 55], "0'": ["0'", 2, 41], "1'": ["1'", 2, 41], Sym('A'+1): [None, 2, 53]}, direction=1)
42 State(instruction=6, acc=3, transitions={'0': ["0'", 0, 43], '1': ["1'", 0, 55], "0'": ["0'", 3, 42], "1'": ["1'", 3, 42], Sym('A'+1): [None, 3, 54]}, direction=1)
43 State(instruction=12, acc=0, transitions={'0': ['0', 0, 43], '1': ['0', 1, 44], "0'": ['0', 0, 43], "1'": ['0', 1, 44], Sym('B'+1): [None, 0, 39]}, direction=1)
44 State(instruction=12, acc=1, transitions={'0': ['1', 0, 43], '1': ['1', 1, 44], "0'": ['1', 0, 43], "1'": ['1', 1, 44], Sym('B'+1): [None, 0, 47]}, direction=1)
45 State(instruction=12, acc=2, transitions={}, direction=None)
46 State(instruction=12, acc=3, transitions={}, direction=None)
47 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 52], "0'": ["0'", 0, 47], "1'": ["1'", 0, 47], Sym('A'+1): [None, 0, 51]}, direction=1)
48 State(instruction=16, acc=1, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 52], "0'": ["0'", 1, 48], "1'": ["1'", 1, 48], Sym('A'+1): [None, 1, 52]}, direction=1)
49 State(instruction=16, acc=2, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 52], "0'": ["0'", 2, 49], "1'": ["1'", 2, 49], Sym('A'+1): [None, 2, 53]}, direction=1)
50 State(instruction=16, acc=3, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 52], "0'": ["0'", 3, 50], "1'": ["1'", 3, 50], Sym('A'+1): [None, 3, 54]}, direction=1)
51 State(instruction=19, acc=0, transitions={'0': ['0', 0, 51], '1': ['1', 0, 51], "0'": ['0', 0, 51], "1'": ['1', 0, 51], Sym('A'+1): [None, 0, 35]}, direction=1)
52 State(instruction=19, acc=1, transitions={'0': ['0', 1, 52], '1': ['1', 1, 52], "0'": ['0', 1, 52], "1'": ['1', 1, 52], Sym('A'+1): [None, 1, 36]}, direction=1)
53 State(instruction=19, acc=2, transitions={'0': ['0', 2, 53], '1': ['1', 2, 53], "0'": ['0', 2, 53], "1'": ['1', 2, 53], Sym('A'+1): [None, 2, 37]}, direction=1)
54 State(instruction=19, acc=3, transitions={'0': ['0', 3, 54], '1': ['1', 3, 54], "0'": ['0', 3, 54], "1'": ['1', 3, 54], Sym('A'+1): [None, 3, 38]}, direction=1)
55 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 59], '1': ["1'", 1, 60], "0'": ["0'", 0, 55], "1'": ["1'", 0, 55], Sym('B'+1): [None, 0, 67]}, direction=1)
56 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 60], '1': ["1'", 2, 61], "0'": ["0'", 1, 56], "1'": ["1'", 1, 56], Sym('B'+1): [None, 1, 68]}, direction=1)
57 State(instruction=24, acc=2, transitions={'0': ["0'", 2, 61], '1': ["1'", 2, 61], "0'": ["0'", 2, 57], "1'": ["1'", 2, 57], Sym('B'+1): [None, 2, 69]}, direction=1)
58 State(instruction=24, acc=3, transitions={'0': ["0'", 3, 62], '1': ["1'", 3, 62], "0'": ["0'", 3, 58], "1'": ["1'", 3, 58], Sym('B'+1): [None, 3, 70]}, direction=1)
59 State(instruction=26, acc=0, transitions={'0': ['0', 0, 63], '1': ['1', 1, 64], "0'": ["0'", 0, 59], "1'": ["1'", 0, 59], Sym('D'+1): [None, 0, 67]}, direction=1)
60 State(instruction=26, acc=1, transitions={'0': ['0', 1, 64], '1': ['1', 2, 65], "0'": ["0'", 1, 60], "1'": ["1'", 1, 60], Sym('D'+1): [None, 1, 68]}, direction=1)
61 State(instruction=26, acc=2, transitions={'0': ['0', 2, 65], '1': ['1', 3, 66], "0'": ["0'", 2, 61], "1'": ["1'", 2, 61], Sym('D'+1): [None, 2, 69]}, direction=1)
62 State(instruction=26, acc=3, transitions={'0': ['0', 3, 66], '1': ['1', 3, 66], "0'": ["0'", 3, 62], "1'": ["1'", 3, 62], Sym('D'+1): [None, 3, 70]}, direction=1)
63 State(instruction=29, acc=0, transitions={'0': ["0'", 0, 55], '1': ["0'", 0, 55], "0'": ["0'", 0, 63], "1'": ["1'", 0, 63], Sym('D'+1): [None, 0, 67]}, direction=1)
64 State(instruction=29, acc=1, transitions={'0': ["1'", 0, 55], '1': ["1'", 0, 55], "0'": ["0'", 1, 64], "1'": ["1'", 1, 64], Sym('D'+1): [None, 1, 68]}, direction=1)
65 State(instruction=29, acc=2, transitions={'0': ["0'", 1, 56], '1': ["0'", 1, 56], "0'": ["0'", 2, 65], "1'": ["1'", 2, 65], Sym('D'+1): [None, 2, 69]}, direction=1)
66 State(instruction=29, acc=3, transitions={'0': ["1'", 1, 56], '1': ["1'", 1, 56], "0'": ["0'", 3, 66], "1'": ["1'", 3, 66], Sym('D'+1): [None, 3, 70]}, direction=1)
67 State(instruction=32, acc=0, transitions={'0': ['0', 0, 67], '1': ['1', 0, 67], "0'": ['0', 0, 67], "1'": ['1', 0, 67], Sym('B'+1): [None, 0, 71]}, direction=1)
68 State(instruction=32, acc=1, transitions={'0': ['0', 1, 68], '1': ['1', 1, 68], "0'": ['0', 1, 68], "1'": ['1', 1, 68], Sym('B'+1): [None, 1, 72]}, direction=1)
69 State(instruction=32, acc=2, transitions={'0': ['0', 2, 69], '1': ['1', 2, 69], "0'": ['0', 2, 69], "1'": ['1', 2, 69], Sym('B'+1): [None, 2, 73]}, direction=1)
70 State(instruction=32, acc=3, transitions={'0': ['0', 3, 70], '1': ['1', 3, 70], "0'": ['0', 3, 70], "1'": ['1', 3, 70], Sym('B'+1): [None, 3, 74]}, direction=1)
71 State(instruction=33, acc=0, transitions={'0': ['0', 0, 71], '1': ['1', 0, 71], "0'": ['0', 0, 71], "1'": ['1', 0, 71], Sym('D'+1): [None, 0, 43]}, direction=1)
72 State(instruction=33, acc=1, transitions={'0': ['0', 1, 72], '1': ['1', 1, 72], "0'": ['0', 1, 72], "1'": ['1', 1, 72], Sym('D'+1): [None, 1, 52]}, direction=1)
73 State(instruction=33, acc=2, transitions={'0': ['0', 2, 73], '1': ['1', 2, 73], "0'": ['0', 2, 73], "1'": ['1', 2, 73], Sym('D'+1): [None, 2, 45]}, direction=1)
74 State(instruction=33, acc=3, transitions={'0': ['0', 3, 74], '1': ['1', 3, 74], "0'": ['0', 3, 74], "1'": ['1', 3, 74], Sym('D'+1): [None, 3, 46]}, direction=1)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasis=[]
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
>>> instructions2states()
>>> apply_posts()
True
>>> apply_pres()
True
>>> apply_posts()
True
>>> apply_pres()
False
>>> apply_posts()
False
>>> stitch_acc()
SyntaxError: multiple statements found while compiling a single statement
>>> function = LineParser.line.parse('TEST').value
>>> function.next_quasis = [None]
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
>>> instructions2states()
>>> apply_posts()
True
>>> apply_pres()
True
>>> apply_posts()
True
>>> apply_pres()
False
>>> apply_posts()
False
>>> stitch_acc()
>>> skip_searches()
Traceback (most recent call last):
  File "<pyshell#660>", line 1, in <module>
    skip_searches()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 665, in skip_searches
    instruction = quasis[state.instruction]
AttributeError: 'tuple' object has no attribute 'instruction'
>>> def skip_searches():
    global quasis
    altered = False
    for _,state in get_quasis([State]):
        instruction = quasis[state.instruction]
        command = instruction.command
        if command in ['LOAD','STORE'] and not instruction.read:
            for symbol,transition,next_state in get_quasis_from(state,[State]):
                next_instruction = quasis[next_state.instruction]
                if (instruction.vard==next_instruction.vard and                            
                        next_instruction.command in ['LOAD','STORE'] and
                        instruction.big==instruction2.big):
                    next_symbol = transition[1] if transition[1] else symbol
                    state.transitions[symbol] = next_state.transitions[next_symbol]
                    altered = True
    return altered

>>> skip_searches()
Traceback (most recent call last):
  File "<pyshell#663>", line 1, in <module>
    skip_searches()
  File "<pyshell#662>", line 12, in skip_searches
    instruction.big==instruction2.big):
NameError: name 'instruction2' is not defined
>>> def skip_searches():
    global quasis
    altered = False
    for _,state in get_quasis([State]):
        instruction = quasis[state.instruction]
        command = instruction.command
        if command in ['LOAD','STORE'] and not instruction.read:
            for symbol,transition,next_state in get_quasis_from(state,[State]):
                next_instruction = quasis[next_state.instruction]
                if (instruction.vard==next_instruction.vard and
                        next_instruction.command in ['LOAD','STORE'] and
                        instruction.big==next_instruction.big):
                    next_symbol = transition[1] if transition[1] else symbol
                    state.transitions[symbol] = next_state.transitions[next_symbol]
                    altered = True
    return altered

>>> skip_searches()
Traceback (most recent call last):
  File "<pyshell#666>", line 1, in <module>
    skip_searches()
  File "<pyshell#665>", line 14, in skip_searches
    state.transitions[symbol] = next_state.transitions[next_symbol]
KeyError: 1
>>> state
<module 'parsita.state' from 'C:\\Users\\joshm\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages\\parsita\\state.py'>
>>> next_state
Traceback (most recent call last):
  File "<pyshell#668>", line 1, in <module>
    next_state
NameError: name 'next_state' is not defined
>>> for _,state in get_quasis([State]):
        instruction = quasis[state.instruction]
        command = instruction.command
        if command in ['LOAD','STORE'] and not instruction.read:
            for symbol,transition,next_state in get_quasis_from(state,[State]):
                next_instruction = quasis[next_state.instruction]
                if (instruction.vard==next_instruction.vard and
                        next_instruction.command in ['LOAD','STORE'] and
                        instruction.big==next_instruction.big):
                    next_symbol = transition[1] if transition[1] else symbol
                    state.transitions[symbol] = next_state.transitions[next_symbol]
                    altered = True

                    
Traceback (most recent call last):
  File "<pyshell#670>", line 11, in <module>
    state.transitions[symbol] = next_state.transitions[next_symbol]
KeyError: 1
>>> state
State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 36], "1'": ["1'", 1, 36], Sym('S'+1): [None, 1, 3]}, direction=1)
>>> next_state
State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 36], "1'": ["1'", 1, 36], Sym('S'+1): [None, 1, 3]}, direction=1)
>>> def skip_searches():
    global quasis
    altered = False
    for _,state in get_quasis([State]):
        instruction = quasis[state.instruction]
        command = instruction.command
        if command in ['LOAD','STORE'] and not instruction.read:
            for symbol,transition,next_state in get_quasis_from(state,[State]):
                next_instruction = quasis[next_state.instruction]
                if (instruction.vard==next_instruction.vard and                            
                        next_instruction.command in ['LOAD','STORE'] and
                        instruction.big==instruction2.big):
                    next_symbol = transition[0] if transition[0] else symbol
                    state.transitions[symbol] = next_state.transitions[next_symbol]
                    altered = True
    return altered

>>> skip_searches()
Traceback (most recent call last):
  File "<pyshell#675>", line 1, in <module>
    skip_searches()
  File "<pyshell#674>", line 12, in skip_searches
    instruction.big==instruction2.big):
NameError: name 'instruction2' is not defined
>>> def skip_searches():
    global quasis
    altered = False
    for _,state in get_quasis([State]):
        instruction = quasis[state.instruction]
        command = instruction.command
        if command in ['LOAD','STORE'] and not instruction.read:
            for symbol,transition,next_state in get_quasis_from(state,[State]):
                next_instruction = quasis[next_state.instruction]
                if (instruction.vard==next_instruction.vard and                            
                        next_instruction.command in ['LOAD','STORE'] and
                        instruction.big==next_instruction.big):
                    next_symbol = transition[0] if transition[0] else symbol
                    state.transitions[symbol] = next_state.transitions[next_symbol]
                    altered = True
    return altered

>>> skip_searches()
True
>>> skip_searches()
True
>>> skip_searches()
True
>>> skip_searches()
True
>>> skip_searches()
True
>>> for k,quasi in get_quasis([State]):
	print(k,quasi)

	
35 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 35], "1'": ["1'", 0, 35], Sym('S'+1): [None, 0, 3]}, direction=1)
36 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 36], "1'": ["1'", 1, 36], Sym('S'+1): [None, 1, 3]}, direction=1)
37 State(instruction=2, acc=2, transitions={'0': ['2', 2, 3], '1': ['2', 2, 3], "0'": ["0'", 2, 37], "1'": ["1'", 2, 37], Sym('S'+1): [None, 2, 3]}, direction=1)
38 State(instruction=2, acc=3, transitions={'0': ['3', 3, 3], '1': ['3', 3, 3], "0'": ["0'", 3, 38], "1'": ["1'", 3, 38], Sym('S'+1): [None, 3, 3]}, direction=1)
39 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 43], '1': ["1'", 0, 55], "0'": ["0'", 0, 39], "1'": ["1'", 0, 39], Sym('A'+1): [None, 0, 51]}, direction=1)
40 State(instruction=6, acc=1, transitions={'0': ["0'", 0, 43], '1': ["1'", 0, 55], "0'": ["0'", 1, 40], "1'": ["1'", 1, 40], Sym('A'+1): [None, 1, 52]}, direction=1)
41 State(instruction=6, acc=2, transitions={'0': ["0'", 0, 43], '1': ["1'", 0, 55], "0'": ["0'", 2, 41], "1'": ["1'", 2, 41], Sym('A'+1): [None, 2, 53]}, direction=1)
42 State(instruction=6, acc=3, transitions={'0': ["0'", 0, 43], '1': ["1'", 0, 55], "0'": ["0'", 3, 42], "1'": ["1'", 3, 42], Sym('A'+1): [None, 3, 54]}, direction=1)
43 State(instruction=12, acc=0, transitions={'0': ['0', 0, 43], '1': ['0', 1, 44], "0'": ['0', 0, 43], "1'": ['0', 1, 44], Sym('B'+1): [None, 0, 39]}, direction=1)
44 State(instruction=12, acc=1, transitions={'0': ['1', 0, 43], '1': ['1', 1, 44], "0'": ['1', 0, 43], "1'": ['1', 1, 44], Sym('B'+1): [None, 0, 47]}, direction=1)
45 State(instruction=12, acc=2, transitions={}, direction=None)
46 State(instruction=12, acc=3, transitions={}, direction=None)
47 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 52], "0'": ["0'", 0, 47], "1'": ["1'", 0, 47], Sym('A'+1): [None, 0, 51]}, direction=1)
48 State(instruction=16, acc=1, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 52], "0'": ["0'", 1, 48], "1'": ["1'", 1, 48], Sym('A'+1): [None, 1, 52]}, direction=1)
49 State(instruction=16, acc=2, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 52], "0'": ["0'", 2, 49], "1'": ["1'", 2, 49], Sym('A'+1): [None, 2, 53]}, direction=1)
50 State(instruction=16, acc=3, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 52], "0'": ["0'", 3, 50], "1'": ["1'", 3, 50], Sym('A'+1): [None, 3, 54]}, direction=1)
51 State(instruction=19, acc=0, transitions={'0': ['0', 0, 51], '1': ['1', 0, 51], "0'": ['0', 0, 51], "1'": ['1', 0, 51], Sym('A'+1): [None, 0, 35]}, direction=1)
52 State(instruction=19, acc=1, transitions={'0': ['0', 1, 52], '1': ['1', 1, 52], "0'": ['0', 1, 52], "1'": ['1', 1, 52], Sym('A'+1): [None, 1, 36]}, direction=1)
53 State(instruction=19, acc=2, transitions={'0': ['0', 2, 53], '1': ['1', 2, 53], "0'": ['0', 2, 53], "1'": ['1', 2, 53], Sym('A'+1): [None, 2, 37]}, direction=1)
54 State(instruction=19, acc=3, transitions={'0': ['0', 3, 54], '1': ['1', 3, 54], "0'": ['0', 3, 54], "1'": ['1', 3, 54], Sym('A'+1): [None, 3, 38]}, direction=1)
55 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 59], '1': ["1'", 1, 60], "0'": ["0'", 0, 55], "1'": ["1'", 0, 55], Sym('B'+1): [None, 0, 67]}, direction=1)
56 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 60], '1': ["1'", 2, 61], "0'": ["0'", 1, 56], "1'": ["1'", 1, 56], Sym('B'+1): [None, 1, 68]}, direction=1)
57 State(instruction=24, acc=2, transitions={'0': ["0'", 2, 61], '1': ["1'", 2, 61], "0'": ["0'", 2, 57], "1'": ["1'", 2, 57], Sym('B'+1): [None, 2, 69]}, direction=1)
58 State(instruction=24, acc=3, transitions={'0': ["0'", 3, 62], '1': ["1'", 3, 62], "0'": ["0'", 3, 58], "1'": ["1'", 3, 58], Sym('B'+1): [None, 3, 70]}, direction=1)
59 State(instruction=26, acc=0, transitions={'0': ["0'", 0, 55], '1': ["1'", 0, 55], "0'": ["0'", 0, 59], "1'": ["1'", 0, 59], Sym('D'+1): [None, 0, 67]}, direction=1)
60 State(instruction=26, acc=1, transitions={'0': ["1'", 0, 55], '1': ["0'", 1, 56], "0'": ["0'", 1, 60], "1'": ["1'", 1, 60], Sym('D'+1): [None, 1, 68]}, direction=1)
61 State(instruction=26, acc=2, transitions={'0': ["0'", 1, 56], '1': ["1'", 1, 56], "0'": ["0'", 2, 61], "1'": ["1'", 2, 61], Sym('D'+1): [None, 2, 69]}, direction=1)
62 State(instruction=26, acc=3, transitions={'0': ["1'", 1, 56], '1': ["1'", 1, 56], "0'": ["0'", 3, 62], "1'": ["1'", 3, 62], Sym('D'+1): [None, 3, 70]}, direction=1)
63 State(instruction=29, acc=0, transitions={'0': ["0'", 0, 55], '1': ["0'", 0, 55], "0'": ["0'", 0, 63], "1'": ["1'", 0, 63], Sym('D'+1): [None, 0, 67]}, direction=1)
64 State(instruction=29, acc=1, transitions={'0': ["1'", 0, 55], '1': ["1'", 0, 55], "0'": ["0'", 1, 64], "1'": ["1'", 1, 64], Sym('D'+1): [None, 1, 68]}, direction=1)
65 State(instruction=29, acc=2, transitions={'0': ["0'", 1, 56], '1': ["0'", 1, 56], "0'": ["0'", 2, 65], "1'": ["1'", 2, 65], Sym('D'+1): [None, 2, 69]}, direction=1)
66 State(instruction=29, acc=3, transitions={'0': ["1'", 1, 56], '1': ["1'", 1, 56], "0'": ["0'", 3, 66], "1'": ["1'", 3, 66], Sym('D'+1): [None, 3, 70]}, direction=1)
67 State(instruction=32, acc=0, transitions={'0': ['0', 0, 67], '1': ['1', 0, 67], "0'": ['0', 0, 67], "1'": ['1', 0, 67], Sym('B'+1): [None, 0, 71]}, direction=1)
68 State(instruction=32, acc=1, transitions={'0': ['0', 1, 68], '1': ['1', 1, 68], "0'": ['0', 1, 68], "1'": ['1', 1, 68], Sym('B'+1): [None, 1, 72]}, direction=1)
69 State(instruction=32, acc=2, transitions={'0': ['0', 2, 69], '1': ['1', 2, 69], "0'": ['0', 2, 69], "1'": ['1', 2, 69], Sym('B'+1): [None, 2, 73]}, direction=1)
70 State(instruction=32, acc=3, transitions={'0': ['0', 3, 70], '1': ['1', 3, 70], "0'": ['0', 3, 70], "1'": ['1', 3, 70], Sym('B'+1): [None, 3, 74]}, direction=1)
71 State(instruction=33, acc=0, transitions={'0': ['0', 0, 71], '1': ['1', 0, 71], "0'": ['0', 0, 71], "1'": ['1', 0, 71], Sym('D'+1): [None, 0, 43]}, direction=1)
72 State(instruction=33, acc=1, transitions={'0': ['0', 1, 72], '1': ['1', 1, 72], "0'": ['0', 1, 72], "1'": ['1', 1, 72], Sym('D'+1): [None, 1, 52]}, direction=1)
73 State(instruction=33, acc=2, transitions={'0': ['0', 2, 73], '1': ['1', 2, 73], "0'": ['0', 2, 73], "1'": ['1', 2, 73], Sym('D'+1): [None, 2, 45]}, direction=1)
74 State(instruction=33, acc=3, transitions={'0': ['0', 3, 74], '1': ['1', 3, 74], "0'": ['0', 3, 74], "1'": ['1', 3, 74], Sym('D'+1): [None, 3, 46]}, direction=1)
>>> def skip_searches():
    global quasis
    altered = False
    for k,state in get_quasis([State]):
        instruction = quasis[state.instruction]
        command = instruction.command
        if command in ['LOAD','STORE'] and not instruction.read:
            for symbol,transition,next_state in get_quasis_from(state,[State]):
                next_instruction = quasis[next_state.instruction]
                if (instruction.vard==next_instruction.vard and                            
                        next_instruction.command in ['LOAD','STORE'] and
                        instruction.big==next_instruction.big):
                    next_symbol = transition[0] if transition[0] else symbol
                    state.transitions[symbol] = next_state.transitions[next_symbol]
                    altered = True
                    print(k,symbol)
    return altered

>>> skip_searches()
35 0'
35 1'
36 0'
36 1'
37 0'
37 1'
38 0'
38 1'
59 0'
59 1'
60 0'
60 1'
61 0'
61 1'
62 0'
62 1'
True
>>> def skip_searches():
    global quasis
    altered = False
    for k,state in get_quasis([State]):
        instruction = quasis[state.instruction]
        command = instruction.command
        if command in ['LOAD','STORE'] and not instruction.read:
            for symbol,transition,next_state in get_quasis_from(state,[State]):
                next_instruction = quasis[next_state.instruction]
                if (k!=transition[2] and
                        instruction.vard==next_instruction.vard and                            
                        next_instruction.command in ['LOAD','STORE'] and
                        instruction.big==next_instruction.big):
                    next_symbol = transition[0] if transition[0] else symbol
                    state.transitions[symbol] = next_state.transitions[next_symbol]
                    altered = True
                    print(k,symbol)
    return altered

>>> skip_searches()
False
>>> def merge_links():
    altered = False
    for k,state1 in get_quasis([State]):
        for j,state2 in get_quasis([State]):
            if j>k and equal_states(k,j):
                quasis[j]=None
                replace_links(j,k)
                altered = True
    return altered

>>> merge_links()
True
>>> merge_links()
True
>>> merge_links()
False
>>> for k,quasi in get_quasis([State]):
	print(k,quasi)

	
35 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 35], "1'": ["1'", 0, 35], Sym('S'+1): [None, 0, 3]}, direction=1)
36 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 36], "1'": ["1'", 1, 36], Sym('S'+1): [None, 1, 3]}, direction=1)
37 State(instruction=2, acc=2, transitions={'0': ['2', 2, 3], '1': ['2', 2, 3], "0'": ["0'", 2, 37], "1'": ["1'", 2, 37], Sym('S'+1): [None, 2, 3]}, direction=1)
38 State(instruction=2, acc=3, transitions={'0': ['3', 3, 3], '1': ['3', 3, 3], "0'": ["0'", 3, 38], "1'": ["1'", 3, 38], Sym('S'+1): [None, 3, 3]}, direction=1)
39 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 43], '1': ["1'", 0, 55], "0'": ["0'", 0, 39], "1'": ["1'", 0, 39], Sym('A'+1): [Sym('A'+1), 0, 51]}, direction=1)
40 State(instruction=6, acc=1, transitions={'0': ["0'", 0, 43], '1': ["1'", 0, 55], "0'": ["0'", 1, 40], "1'": ["1'", 1, 40], Sym('A'+1): [Sym('A'+1), 1, 52]}, direction=1)
41 State(instruction=6, acc=2, transitions={'0': ["0'", 0, 43], '1': ["1'", 0, 55], "0'": ["0'", 2, 41], "1'": ["1'", 2, 41], Sym('A'+1): [Sym('A'+1), 2, 53]}, direction=1)
42 State(instruction=6, acc=3, transitions={'0': ["0'", 0, 43], '1': ["1'", 0, 55], "0'": ["0'", 3, 42], "1'": ["1'", 3, 42], Sym('A'+1): [Sym('A'+1), 3, 54]}, direction=1)
43 State(instruction=12, acc=0, transitions={'0': ['0', 0, 43], '1': ['0', 1, 44], "0'": ['0', 0, 43], "1'": ['0', 1, 44], Sym('B'+1): [Sym('B'+1), 0, 39]}, direction=1)
44 State(instruction=12, acc=1, transitions={'0': ['1', 0, 43], '1': ['1', 1, 44], "0'": ['1', 0, 43], "1'": ['1', 1, 44], Sym('B'+1): [None, 0, 47]}, direction=1)
45 State(instruction=12, acc=2, transitions={}, direction=None)
47 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 52], "0'": ["0'", 0, 47], "1'": ["1'", 0, 47], Sym('A'+1): [Sym('A'+1), 0, 51]}, direction=1)
48 State(instruction=16, acc=1, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 52], "0'": ["0'", 1, 48], "1'": ["1'", 1, 48], Sym('A'+1): [Sym('A'+1), 1, 52]}, direction=1)
49 State(instruction=16, acc=2, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 52], "0'": ["0'", 2, 49], "1'": ["1'", 2, 49], Sym('A'+1): [Sym('A'+1), 2, 53]}, direction=1)
50 State(instruction=16, acc=3, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 52], "0'": ["0'", 3, 50], "1'": ["1'", 3, 50], Sym('A'+1): [Sym('A'+1), 3, 54]}, direction=1)
51 State(instruction=19, acc=0, transitions={'0': ['0', 0, 51], '1': ['1', 0, 51], "0'": ['0', 0, 51], "1'": ['1', 0, 51], Sym('A'+1): [Sym('A'+1), 0, 35]}, direction=1)
52 State(instruction=19, acc=1, transitions={'0': ['0', 1, 52], '1': ['1', 1, 52], "0'": ['0', 1, 52], "1'": ['1', 1, 52], Sym('A'+1): [Sym('A'+1), 1, 36]}, direction=1)
53 State(instruction=19, acc=2, transitions={'0': ['0', 2, 53], '1': ['1', 2, 53], "0'": ['0', 2, 53], "1'": ['1', 2, 53], Sym('A'+1): [Sym('A'+1), 2, 37]}, direction=1)
54 State(instruction=19, acc=3, transitions={'0': ['0', 3, 54], '1': ['1', 3, 54], "0'": ['0', 3, 54], "1'": ['1', 3, 54], Sym('A'+1): [Sym('A'+1), 3, 38]}, direction=1)
55 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 59], '1': ["1'", 1, 60], "0'": ["0'", 0, 55], "1'": ["1'", 0, 55], Sym('B'+1): [None, 0, 67]}, direction=1)
56 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 60], '1': ["1'", 2, 61], "0'": ["0'", 1, 56], "1'": ["1'", 1, 56], Sym('B'+1): [None, 1, 68]}, direction=1)
57 State(instruction=24, acc=2, transitions={'0': ["0'", 2, 61], '1': ["1'", 2, 61], "0'": ["0'", 2, 57], "1'": ["1'", 2, 57], Sym('B'+1): [None, 2, 69]}, direction=1)
58 State(instruction=24, acc=3, transitions={'0': ["0'", 3, 62], '1': ["1'", 3, 62], "0'": ["0'", 3, 58], "1'": ["1'", 3, 58], Sym('B'+1): [None, 3, 69]}, direction=1)
59 State(instruction=26, acc=0, transitions={'0': ["0'", 0, 55], '1': ["1'", 0, 55], "0'": ["0'", 0, 59], "1'": ["1'", 0, 59], Sym('D'+1): [Sym('D'+1), 0, 67]}, direction=1)
60 State(instruction=26, acc=1, transitions={'0': ["1'", 0, 55], '1': ["0'", 1, 56], "0'": ["0'", 1, 60], "1'": ["1'", 1, 60], Sym('D'+1): [Sym('D'+1), 1, 68]}, direction=1)
61 State(instruction=26, acc=2, transitions={'0': ["0'", 1, 56], '1': ["1'", 1, 56], "0'": ["0'", 2, 61], "1'": ["1'", 2, 61], Sym('D'+1): [Sym('D'+1), 2, 69]}, direction=1)
62 State(instruction=26, acc=3, transitions={'0': ["1'", 1, 56], '1': ["1'", 1, 56], "0'": ["0'", 3, 62], "1'": ["1'", 3, 62], Sym('D'+1): [Sym('D'+1), 3, 69]}, direction=1)
63 State(instruction=29, acc=0, transitions={'0': ["0'", 0, 55], '1': ["0'", 0, 55], "0'": ["0'", 0, 63], "1'": ["1'", 0, 63], Sym('D'+1): [Sym('D'+1), 0, 67]}, direction=1)
64 State(instruction=29, acc=1, transitions={'0': ["1'", 0, 55], '1': ["1'", 0, 55], "0'": ["0'", 1, 64], "1'": ["1'", 1, 64], Sym('D'+1): [Sym('D'+1), 1, 68]}, direction=1)
65 State(instruction=29, acc=2, transitions={'0': ["0'", 1, 56], '1': ["0'", 1, 56], "0'": ["0'", 2, 65], "1'": ["1'", 2, 65], Sym('D'+1): [Sym('D'+1), 2, 69]}, direction=1)
67 State(instruction=32, acc=0, transitions={'0': ['0', 0, 67], '1': ['1', 0, 67], "0'": ['0', 0, 67], "1'": ['1', 0, 67], Sym('B'+1): [Sym('B'+1), 0, 71]}, direction=1)
68 State(instruction=32, acc=1, transitions={'0': ['0', 1, 68], '1': ['1', 1, 68], "0'": ['0', 1, 68], "1'": ['1', 1, 68], Sym('B'+1): [Sym('B'+1), 1, 72]}, direction=1)
69 State(instruction=32, acc=2, transitions={'0': ['0', 2, 69], '1': ['1', 2, 69], "0'": ['0', 2, 69], "1'": ['1', 2, 69], Sym('B'+1): [Sym('B'+1), 2, 73]}, direction=1)
71 State(instruction=33, acc=0, transitions={'0': ['0', 0, 71], '1': ['1', 0, 71], "0'": ['0', 0, 71], "1'": ['1', 0, 71], Sym('D'+1): [Sym('D'+1), 0, 43]}, direction=1)
72 State(instruction=33, acc=1, transitions={'0': ['0', 1, 72], '1': ['1', 1, 72], "0'": ['0', 1, 72], "1'": ['1', 1, 72], Sym('D'+1): [Sym('D'+1), 1, 52]}, direction=1)
73 State(instruction=33, acc=2, transitions={'0': ['0', 2, 73], '1': ['1', 2, 73], "0'": ['0', 2, 73], "1'": ['1', 2, 73], Sym('D'+1): [Sym('D'+1), 2, 45]}, direction=1)
>>> for k,quasi in get_quasis([State]):
	print(k,str(quasi).replace(' ',''))

	
35 State(instruction=2,acc=0,transitions={'0':['0',0,3],'1':['0',0,3],"0'":["0'",0,35],"1'":["1'",0,35],Sym('S'+1):[None,0,3]},direction=1)
36 State(instruction=2,acc=1,transitions={'0':['1',1,3],'1':['1',1,3],"0'":["0'",1,36],"1'":["1'",1,36],Sym('S'+1):[None,1,3]},direction=1)
37 State(instruction=2,acc=2,transitions={'0':['2',2,3],'1':['2',2,3],"0'":["0'",2,37],"1'":["1'",2,37],Sym('S'+1):[None,2,3]},direction=1)
38 State(instruction=2,acc=3,transitions={'0':['3',3,3],'1':['3',3,3],"0'":["0'",3,38],"1'":["1'",3,38],Sym('S'+1):[None,3,3]},direction=1)
39 State(instruction=6,acc=0,transitions={'0':["0'",0,43],'1':["1'",0,55],"0'":["0'",0,39],"1'":["1'",0,39],Sym('A'+1):[Sym('A'+1),0,51]},direction=1)
40 State(instruction=6,acc=1,transitions={'0':["0'",0,43],'1':["1'",0,55],"0'":["0'",1,40],"1'":["1'",1,40],Sym('A'+1):[Sym('A'+1),1,52]},direction=1)
41 State(instruction=6,acc=2,transitions={'0':["0'",0,43],'1':["1'",0,55],"0'":["0'",2,41],"1'":["1'",2,41],Sym('A'+1):[Sym('A'+1),2,53]},direction=1)
42 State(instruction=6,acc=3,transitions={'0':["0'",0,43],'1':["1'",0,55],"0'":["0'",3,42],"1'":["1'",3,42],Sym('A'+1):[Sym('A'+1),3,54]},direction=1)
43 State(instruction=12,acc=0,transitions={'0':['0',0,43],'1':['0',1,44],"0'":['0',0,43],"1'":['0',1,44],Sym('B'+1):[Sym('B'+1),0,39]},direction=1)
44 State(instruction=12,acc=1,transitions={'0':['1',0,43],'1':['1',1,44],"0'":['1',0,43],"1'":['1',1,44],Sym('B'+1):[None,0,47]},direction=1)
45 State(instruction=12,acc=2,transitions={},direction=None)
47 State(instruction=16,acc=0,transitions={'0':["0'",0,47],'1':["1'",1,52],"0'":["0'",0,47],"1'":["1'",0,47],Sym('A'+1):[Sym('A'+1),0,51]},direction=1)
48 State(instruction=16,acc=1,transitions={'0':["0'",0,47],'1':["1'",1,52],"0'":["0'",1,48],"1'":["1'",1,48],Sym('A'+1):[Sym('A'+1),1,52]},direction=1)
49 State(instruction=16,acc=2,transitions={'0':["0'",0,47],'1':["1'",1,52],"0'":["0'",2,49],"1'":["1'",2,49],Sym('A'+1):[Sym('A'+1),2,53]},direction=1)
50 State(instruction=16,acc=3,transitions={'0':["0'",0,47],'1':["1'",1,52],"0'":["0'",3,50],"1'":["1'",3,50],Sym('A'+1):[Sym('A'+1),3,54]},direction=1)
51 State(instruction=19,acc=0,transitions={'0':['0',0,51],'1':['1',0,51],"0'":['0',0,51],"1'":['1',0,51],Sym('A'+1):[Sym('A'+1),0,35]},direction=1)
52 State(instruction=19,acc=1,transitions={'0':['0',1,52],'1':['1',1,52],"0'":['0',1,52],"1'":['1',1,52],Sym('A'+1):[Sym('A'+1),1,36]},direction=1)
53 State(instruction=19,acc=2,transitions={'0':['0',2,53],'1':['1',2,53],"0'":['0',2,53],"1'":['1',2,53],Sym('A'+1):[Sym('A'+1),2,37]},direction=1)
54 State(instruction=19,acc=3,transitions={'0':['0',3,54],'1':['1',3,54],"0'":['0',3,54],"1'":['1',3,54],Sym('A'+1):[Sym('A'+1),3,38]},direction=1)
55 State(instruction=24,acc=0,transitions={'0':["0'",0,59],'1':["1'",1,60],"0'":["0'",0,55],"1'":["1'",0,55],Sym('B'+1):[None,0,67]},direction=1)
56 State(instruction=24,acc=1,transitions={'0':["0'",1,60],'1':["1'",2,61],"0'":["0'",1,56],"1'":["1'",1,56],Sym('B'+1):[None,1,68]},direction=1)
57 State(instruction=24,acc=2,transitions={'0':["0'",2,61],'1':["1'",2,61],"0'":["0'",2,57],"1'":["1'",2,57],Sym('B'+1):[None,2,69]},direction=1)
58 State(instruction=24,acc=3,transitions={'0':["0'",3,62],'1':["1'",3,62],"0'":["0'",3,58],"1'":["1'",3,58],Sym('B'+1):[None,3,69]},direction=1)
59 State(instruction=26,acc=0,transitions={'0':["0'",0,55],'1':["1'",0,55],"0'":["0'",0,59],"1'":["1'",0,59],Sym('D'+1):[Sym('D'+1),0,67]},direction=1)
60 State(instruction=26,acc=1,transitions={'0':["1'",0,55],'1':["0'",1,56],"0'":["0'",1,60],"1'":["1'",1,60],Sym('D'+1):[Sym('D'+1),1,68]},direction=1)
61 State(instruction=26,acc=2,transitions={'0':["0'",1,56],'1':["1'",1,56],"0'":["0'",2,61],"1'":["1'",2,61],Sym('D'+1):[Sym('D'+1),2,69]},direction=1)
62 State(instruction=26,acc=3,transitions={'0':["1'",1,56],'1':["1'",1,56],"0'":["0'",3,62],"1'":["1'",3,62],Sym('D'+1):[Sym('D'+1),3,69]},direction=1)
63 State(instruction=29,acc=0,transitions={'0':["0'",0,55],'1':["0'",0,55],"0'":["0'",0,63],"1'":["1'",0,63],Sym('D'+1):[Sym('D'+1),0,67]},direction=1)
64 State(instruction=29,acc=1,transitions={'0':["1'",0,55],'1':["1'",0,55],"0'":["0'",1,64],"1'":["1'",1,64],Sym('D'+1):[Sym('D'+1),1,68]},direction=1)
65 State(instruction=29,acc=2,transitions={'0':["0'",1,56],'1':["0'",1,56],"0'":["0'",2,65],"1'":["1'",2,65],Sym('D'+1):[Sym('D'+1),2,69]},direction=1)
67 State(instruction=32,acc=0,transitions={'0':['0',0,67],'1':['1',0,67],"0'":['0',0,67],"1'":['1',0,67],Sym('B'+1):[Sym('B'+1),0,71]},direction=1)
68 State(instruction=32,acc=1,transitions={'0':['0',1,68],'1':['1',1,68],"0'":['0',1,68],"1'":['1',1,68],Sym('B'+1):[Sym('B'+1),1,72]},direction=1)
69 State(instruction=32,acc=2,transitions={'0':['0',2,69],'1':['1',2,69],"0'":['0',2,69],"1'":['1',2,69],Sym('B'+1):[Sym('B'+1),2,73]},direction=1)
71 State(instruction=33,acc=0,transitions={'0':['0',0,71],'1':['1',0,71],"0'":['0',0,71],"1'":['1',0,71],Sym('D'+1):[Sym('D'+1),0,43]},direction=1)
72 State(instruction=33,acc=1,transitions={'0':['0',1,72],'1':['1',1,72],"0'":['0',1,72],"1'":['1',1,72],Sym('D'+1):[Sym('D'+1),1,52]},direction=1)
73 State(instruction=33,acc=2,transitions={'0':['0',2,73],'1':['1',2,73],"0'":['0',2,73],"1'":['1',2,73],Sym('D'+1):[Sym('D'+1),2,45]},direction=1)
>>> used_states = {0}
>>> def find_successors(k):
    global quasis,used_states
    for something in get_quasis_from(quasis[k],[End,State]):
        j = something[1]
        if type(j)==list:
            j = j[2]
        if not j in used_states:
                used_states.add(j)
                find_successors(j)

                
>>> find_successors(0)
>>> used_states
{0, 3, 35, 36, 39, 43, 44, 45, 47, 51, 52, 55, 56, 59, 60, 61, 67, 68, 69, 71, 72, 73}
>>> for k in sorted(used_states):
	print(k,quasis[k])

	
0 End(is_start=True, next_quasis=[39])
3 End(is_start=False, next_quasis=[None])
35 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 35], "1'": ["1'", 0, 35], Sym('S'+1): [None, 0, 3]}, direction=1)
36 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 36], "1'": ["1'", 1, 36], Sym('S'+1): [None, 1, 3]}, direction=1)
39 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 43], '1': ["1'", 0, 55], "0'": ["0'", 0, 39], "1'": ["1'", 0, 39], Sym('A'+1): [Sym('A'+1), 0, 51]}, direction=1)
43 State(instruction=12, acc=0, transitions={'0': ['0', 0, 43], '1': ['0', 1, 44], "0'": ['0', 0, 43], "1'": ['0', 1, 44], Sym('B'+1): [Sym('B'+1), 0, 39]}, direction=1)
44 State(instruction=12, acc=1, transitions={'0': ['1', 0, 43], '1': ['1', 1, 44], "0'": ['1', 0, 43], "1'": ['1', 1, 44], Sym('B'+1): [None, 0, 47]}, direction=1)
45 State(instruction=12, acc=2, transitions={}, direction=None)
47 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 52], "0'": ["0'", 0, 47], "1'": ["1'", 0, 47], Sym('A'+1): [Sym('A'+1), 0, 51]}, direction=1)
51 State(instruction=19, acc=0, transitions={'0': ['0', 0, 51], '1': ['1', 0, 51], "0'": ['0', 0, 51], "1'": ['1', 0, 51], Sym('A'+1): [Sym('A'+1), 0, 35]}, direction=1)
52 State(instruction=19, acc=1, transitions={'0': ['0', 1, 52], '1': ['1', 1, 52], "0'": ['0', 1, 52], "1'": ['1', 1, 52], Sym('A'+1): [Sym('A'+1), 1, 36]}, direction=1)
55 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 59], '1': ["1'", 1, 60], "0'": ["0'", 0, 55], "1'": ["1'", 0, 55], Sym('B'+1): [None, 0, 67]}, direction=1)
56 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 60], '1': ["1'", 2, 61], "0'": ["0'", 1, 56], "1'": ["1'", 1, 56], Sym('B'+1): [None, 1, 68]}, direction=1)
59 State(instruction=26, acc=0, transitions={'0': ["0'", 0, 55], '1': ["1'", 0, 55], "0'": ["0'", 0, 59], "1'": ["1'", 0, 59], Sym('D'+1): [Sym('D'+1), 0, 67]}, direction=1)
60 State(instruction=26, acc=1, transitions={'0': ["1'", 0, 55], '1': ["0'", 1, 56], "0'": ["0'", 1, 60], "1'": ["1'", 1, 60], Sym('D'+1): [Sym('D'+1), 1, 68]}, direction=1)
61 State(instruction=26, acc=2, transitions={'0': ["0'", 1, 56], '1': ["1'", 1, 56], "0'": ["0'", 2, 61], "1'": ["1'", 2, 61], Sym('D'+1): [Sym('D'+1), 2, 69]}, direction=1)
67 State(instruction=32, acc=0, transitions={'0': ['0', 0, 67], '1': ['1', 0, 67], "0'": ['0', 0, 67], "1'": ['1', 0, 67], Sym('B'+1): [Sym('B'+1), 0, 71]}, direction=1)
68 State(instruction=32, acc=1, transitions={'0': ['0', 1, 68], '1': ['1', 1, 68], "0'": ['0', 1, 68], "1'": ['1', 1, 68], Sym('B'+1): [Sym('B'+1), 1, 72]}, direction=1)
69 State(instruction=32, acc=2, transitions={'0': ['0', 2, 69], '1': ['1', 2, 69], "0'": ['0', 2, 69], "1'": ['1', 2, 69], Sym('B'+1): [Sym('B'+1), 2, 73]}, direction=1)
71 State(instruction=33, acc=0, transitions={'0': ['0', 0, 71], '1': ['1', 0, 71], "0'": ['0', 0, 71], "1'": ['1', 0, 71], Sym('D'+1): [Sym('D'+1), 0, 43]}, direction=1)
72 State(instruction=33, acc=1, transitions={'0': ['0', 1, 72], '1': ['1', 1, 72], "0'": ['0', 1, 72], "1'": ['1', 1, 72], Sym('D'+1): [Sym('D'+1), 1, 52]}, direction=1)
73 State(instruction=33, acc=2, transitions={'0': ['0', 2, 73], '1': ['1', 2, 73], "0'": ['0', 2, 73], "1'": ['1', 2, 73], Sym('D'+1): [Sym('D'+1), 2, 45]}, direction=1)
>>> quasis[33]
Instruction(UNREAD, vard=D, next_quasis=[10])
>>> for k,quasi in get_quasis([Instruction]):
	print(k,quasi)

	
2 Instruction(STORE, vard=S, next_quasis=[3, 3])
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 22, 22, 22])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
19 Instruction(UNREAD, vard=A, next_quasis=[2])
22 Instruction(LOADI, next_quasis=[24])
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[29])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[0])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
32 Instruction(UNREAD, vard=B, next_quasis=[33])
33 Instruction(UNREAD, vard=D, next_quasis=[10])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
Traceback (most recent call last):
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 866, in <module>
    parse_files()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 260, in parse_files
    parsed_line = LineParser.line.parse(line).value
AttributeError: 'Failure' object has no attribute 'value'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> for k in sorted(used_states):
	print(k,quasis[k])

	
Traceback (most recent call last):
  File "<pyshell#712>", line 1, in <module>
    for k in sorted(used_states):
NameError: name 'used_states' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST')
60 0
60 1
61 0
61 1
62 0
62 1
63 0
63 1
0 End(is_start=True, next_quasis=[40])
3 End(is_start=False, next_quasis=[None])
36 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 36], "1'": ["1'", 0, 36], Sym('S'+1): [None, 0, 3]}, direction=1)
37 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 37], "1'": ["1'", 1, 37], Sym('S'+1): [None, 1, 3]}, direction=1)
40 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 44], '1': ["1'", 0, 56], "0'": ["0'", 0, 40], "1'": ["1'", 0, 40], Sym('A'+1): [Sym('A'+1), 0, 52]}, direction=1)
44 State(instruction=12, acc=0, transitions={'0': ['0', 0, 44], '1': ['0', 1, 45], "0'": ['0', 0, 44], "1'": ['0', 1, 45], Sym('B'+1): [None, 0, 40]}, direction=1)
45 State(instruction=12, acc=1, transitions={'0': ['1', 0, 44], '1': ['1', 1, 45], "0'": ['1', 0, 44], "1'": ['1', 1, 45], Sym('B'+1): [None, 0, 48]}, direction=1)
48 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 48], '1': ["1'", 1, 53], "0'": ["0'", 0, 48], "1'": ["1'", 0, 48], Sym('A'+1): [Sym('A'+1), 0, 52]}, direction=1)
52 State(instruction=19, acc=0, transitions={'0': ['0', 0, 52], '1': ['1', 0, 52], "0'": ['0', 0, 52], "1'": ['1', 0, 52], Sym('A'+1): [Sym('A'+1), 0, 36]}, direction=1)
53 State(instruction=19, acc=1, transitions={'0': ['0', 1, 53], '1': ['1', 1, 53], "0'": ['0', 1, 53], "1'": ['1', 1, 53], Sym('A'+1): [Sym('A'+1), 1, 37]}, direction=1)
56 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 60], '1': ["1'", 1, 61], "0'": ["0'", 0, 56], "1'": ["1'", 0, 56], Sym('B'+1): [None, 0, 68]}, direction=1)
57 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 61], '1': ["1'", 2, 62], "0'": ["0'", 1, 57], "1'": ["1'", 1, 57], Sym('B'+1): [None, 1, 69]}, direction=1)
60 State(instruction=26, acc=0, transitions={'0': ["0'", 0, 56], '1': ["1'", 0, 56], "0'": ["0'", 0, 60], "1'": ["1'", 0, 60], Sym('D'+1): [None, 0, 68]}, direction=1)
61 State(instruction=26, acc=1, transitions={'0': ["1'", 0, 56], '1': ["0'", 1, 57], "0'": ["0'", 1, 61], "1'": ["1'", 1, 61], Sym('D'+1): [None, 1, 69]}, direction=1)
62 State(instruction=26, acc=2, transitions={'0': ["0'", 1, 57], '1': ["1'", 1, 57], "0'": ["0'", 2, 62], "1'": ["1'", 2, 62], Sym('D'+1): [None, 1, 69]}, direction=1)
68 State(instruction=33, acc=0, transitions={'0': ['0', 0, 68], '1': ['1', 0, 68], "0'": ['0', 0, 68], "1'": ['1', 0, 68], Sym('B'+1): [Sym('B'+1), 0, 72]}, direction=1)
69 State(instruction=33, acc=1, transitions={'0': ['0', 1, 69], '1': ['1', 1, 69], "0'": ['0', 1, 69], "1'": ['1', 1, 69], Sym('B'+1): [Sym('B'+1), 1, 73]}, direction=1)
72 State(instruction=34, acc=0, transitions={'0': ['0', 0, 72], '1': ['1', 0, 72], "0'": ['0', 0, 72], "1'": ['1', 0, 72], Sym('D'+1): [Sym('D'+1), 0, 44]}, direction=1)
73 State(instruction=34, acc=1, transitions={'0': ['0', 1, 73], '1': ['1', 1, 73], "0'": ['0', 1, 73], "1'": ['1', 1, 73], Sym('D'+1): [Sym('D'+1), 1, 53]}, direction=1)
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Traceback (most recent call last):
  File "<frozen importlib._bootstrap>", line 900, in _find_spec
AttributeError: '_SixMetaPathImporter' object has no attribute 'find_spec'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 1, in <module>
    import requests
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\requests\__init__.py", line 43, in <module>
    import urllib3
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\__init__.py", line 7, in <module>
    from .connectionpool import HTTPConnectionPool, HTTPSConnectionPool, connection_from_url
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\connectionpool.py", line 11, in <module>
    from .exceptions import (
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\exceptions.py", line 2, in <module>
    from .packages.six.moves.http_client import IncompleteRead as httplib_IncompleteRead
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 963, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 902, in _find_spec
  File "<frozen importlib._bootstrap>", line 879, in _find_spec_legacy
  File "<frozen importlib._bootstrap>", line 449, in spec_from_loader
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\packages\six.py", line 212, in is_package
    return hasattr(self.__get_module(fullname), "__path__")
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\packages\six.py", line 116, in __getattr__
    _module = self._resolve()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\packages\six.py", line 113, in _resolve
    return _import_module(self.mod)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\packages\six.py", line 82, in _import_module
    __import__(name)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\http\client.py", line 71, in <module>
    import email.parser
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\email\parser.py", line 12, in <module>
    from email.feedparser import FeedParser, BytesFeedParser
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\email\feedparser.py", line 27, in <module>
    from email._policybase import compat32
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\email\_policybase.py", line 9, in <module>
    from email.utils import _has_surrogates
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\email\utils.py", line 30, in <module>
    import datetime
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 967, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 677, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 724, in exec_module
  File "<frozen importlib._bootstrap_external>", line 818, in get_code
  File "<frozen importlib._bootstrap_external>", line 916, in get_data
KeyboardInterrupt
>>> timedelta
  
Traceback (most recent call last):
  File "<pyshell#714>", line 1, in <module>
    timedelta
NameError: name 'timedelta' is not defined
>>> 
from datetime import datetime,timedelta
  

>>> timedelta
  
<class 'datetime.timedelta'>
>>> timedelta(weeks=1)
  
datetime.timedelta(days=7)
>>> datetime.timedelta(days=7).seconds
  
Traceback (most recent call last):
  File "<pyshell#718>", line 1, in <module>
    datetime.timedelta(days=7).seconds
AttributeError: type object 'datetime.datetime' has no attribute 'timedelta'
>>> datetime.timedelta(days=7).seconds()
  
Traceback (most recent call last):
  File "<pyshell#719>", line 1, in <module>
    datetime.timedelta(days=7).seconds()
AttributeError: type object 'datetime.datetime' has no attribute 'timedelta'
>>> timedelta(days=7).seconds()
  
Traceback (most recent call last):
  File "<pyshell#720>", line 1, in <module>
    timedelta(days=7).seconds()
TypeError: 'int' object is not callable
>>> timedelta(days=7).seconds
  
0
>>> timedelta(days=7).total_seconds
  
<built-in method total_seconds of datetime.timedelta object at 0x01513350>
>>> timedelta(days=7).total_seconds()
  
604800.0
>>> timedelta(days=-7).total_seconds()
  
-604800.0
>>> True/7
  
0.14285714285714285
>>> timedelta(days=1).total_seconds()
  
86400.0
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: 
Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 237, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 190, in run
    password = input('Password: ').encode()
KeyboardInterrupt
>>> file_lines = get_file('TylerNet file name: ')
  
TylerNet file name: 0622PPLRECON.TXT
>>> tyler_data = [[line[sum(widths[:k]):sum(widths[:k+1])].strip() for k in range(len(widths))] for line in file_lines]
  
>>> access_tokens, expires_ats = get_access_tokens(password)
  
Traceback (most recent call last):
  File "<pyshell#729>", line 1, in <module>
    access_tokens, expires_ats = get_access_tokens(password)
NameError: name 'password' is not defined
>>> access_tokens, expires_ats = get_access_tokens('mountaindew'.encode())
  
PayPal Authentication info file name: paypalauth.txt
>>> get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  
Traceback (most recent call last):
  File "<pyshell#731>", line 1, in <module>
    get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
NameError: name 'line' is not defined
>>> line = tyler_data[4]
  
>>> get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  
Traceback (most recent call last):
  File "<pyshell#733>", line 1, in <module>
    get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 45, in get_transaction_id
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}
UnboundLocalError: local variable 'access_token' referenced before assignment
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: 
Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 236, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 189, in run
    password = input('Password: ').encode()
KeyboardInterrupt
>>> file_lines = get_file('TylerNet file name: ')
  
TylerNet file name: 0622PPLRECON.TXT
>>> tyler_data = [[line[sum(widths[:k]):sum(widths[:k+1])].strip() for k in range(len(widths))] for line in file_lines]
  
>>> access_tokens, expires_ats = get_access_tokens('mountaindew'.encode())
  
PayPal Authentication info file name: paypalauth.txt
>>> line = tyler_data[4]
  
>>> get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  
1
0
Traceback (most recent call last):
  File "<pyshell#738>", line 1, in <module>
    get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 71, in get_transaction_id
    paypal_time = datetime.fromisoformat(transaction['transaction_info']['transaction_updated_date'])
ValueError: Invalid isoformat string: '2020-06-22T15:38:17+0000'
>>> datetime.fromisoformat('2020-06-22T15:38:17+0000')
  
Traceback (most recent call last):
  File "<pyshell#739>", line 1, in <module>
    datetime.fromisoformat('2020-06-22T15:38:17+0000')
ValueError: Invalid isoformat string: '2020-06-22T15:38:17+0000'
>>> datetime.fromisoformat('2020-06-22T15:38:17')
  
datetime.datetime(2020, 6, 22, 15, 38, 17)
>>> datetime.fromisoformat('2020-06-22T15:38:17+00:00')
  
datetime.datetime(2020, 6, 22, 15, 38, 17, tzinfo=datetime.timezone.utc)
>>> datetime.fromisoformat('2020-06-22T15:38:17+00')
  
Traceback (most recent call last):
  File "<pyshell#742>", line 1, in <module>
    datetime.fromisoformat('2020-06-22T15:38:17+00')
ValueError: Invalid isoformat string: '2020-06-22T15:38:17+00'
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: 
Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 236, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 189, in run
    password = input('Password: ').encode()
KeyboardInterrupt
>>> file_lines = get_file('TylerNet file name: ')
  
TylerNet file name: 0622PPLRECON.TXT
>>> tyler_data = [[line[sum(widths[:k]):sum(widths[:k+1])].strip() for k in range(len(widths))] for line in file_lines]
  
>>> access_tokens, expires_ats = get_access_tokens('mountaindew'.encode())
  
PayPal Authentication info file name: paypalauth.txt
>>> line = tyler_data[4]
  
>>> get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  
1
0
Traceback (most recent call last):
  File "<pyshell#747>", line 1, in <module>
    get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 73, in get_transaction_id
    'Time':(paypal_time-time).total_seconds(),
TypeError: can't subtract offset-naive and offset-aware datetimes
>>> strings2time(time_string,entry_time_string)
  
Traceback (most recent call last):
  File "<pyshell#748>", line 1, in <module>
    strings2time(time_string,entry_time_string)
NameError: name 'time_string' is not defined
>>> time_string,entry_time_string=line[0],line[6]
  
>>> strings2time(time_string,entry_time_string)
  
datetime.datetime(2020, 6, 21, 2, 9, 59)
>>> time = datetime.datetime(2020, 6, 21, 2, 9, 59)
  
Traceback (most recent call last):
  File "<pyshell#751>", line 1, in <module>
    time = datetime.datetime(2020, 6, 21, 2, 9, 59)
AttributeError: type object 'datetime.datetime' has no attribute 'datetime'
>>> time = strings2time(time_string,entry_time_string)
  
>>> time.astimezone('-07:00')
  
Traceback (most recent call last):
  File "<pyshell#753>", line 1, in <module>
    time.astimezone('-07:00')
TypeError: tzinfo argument must be None or of a tzinfo subclass, not type 'str'
>>> datetime.timezone.mdt
  
Traceback (most recent call last):
  File "<pyshell#754>", line 1, in <module>
    datetime.timezone.mdt
AttributeError: type object 'datetime.datetime' has no attribute 'timezone'
>>> from datetime import timezone
  
>>> timezone.mdt
  
Traceback (most recent call last):
  File "<pyshell#756>", line 1, in <module>
    timezone.mdt
AttributeError: type object 'datetime.timezone' has no attribute 'mdt'
>>> timezone.utcoffset(-7)
  
Traceback (most recent call last):
  File "<pyshell#757>", line 1, in <module>
    timezone.utcoffset(-7)
TypeError: descriptor 'utcoffset' requires a 'datetime.timezone' object but received a 'int'
>>> timezone.fromutc(-7)
  
Traceback (most recent call last):
  File "<pyshell#758>", line 1, in <module>
    timezone.fromutc(-7)
TypeError: descriptor 'fromutc' requires a 'datetime.timezone' object but received a 'int'
>>> time.astimezone(timezone(timedelta(hours=-7)))
  
datetime.datetime(2020, 6, 21, 1, 9, 59, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))
>>> time
  
datetime.datetime(2020, 6, 21, 2, 9, 59)
>>> time2=datetime(2020, 6, 21, 9, 19, 59)
  
>>> time.astimezone(timezone.utc)
  
datetime.datetime(2020, 6, 21, 8, 9, 59, tzinfo=datetime.timezone.utc)
>>> time.astimezone(timezone(timedelta(hours=-7)))
  
datetime.datetime(2020, 6, 21, 1, 9, 59, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))
>>> time2.astimezone(timezone.utc)
  
datetime.datetime(2020, 6, 21, 15, 19, 59, tzinfo=datetime.timezone.utc)
>>> time-time2
  
datetime.timedelta(days=-1, seconds=60600)
>>> time2-time
  
datetime.timedelta(seconds=25800)
>>> time.timezone
  
Traceback (most recent call last):
  File "<pyshell#767>", line 1, in <module>
    time.timezone
AttributeError: 'datetime.datetime' object has no attribute 'timezone'
>>> time.datetime.fromisoformat('2020-06-22T15:38:17',timezone=timedelta(hours=-7))
  
Traceback (most recent call last):
  File "<pyshell#768>", line 1, in <module>
    time.datetime.fromisoformat('2020-06-22T15:38:17',timezone=timedelta(hours=-7))
AttributeError: 'datetime.datetime' object has no attribute 'datetime'
>>> datetime.fromisoformat('2020-06-22T15:38:17',timezone=timedelta(hours=-7))
  
Traceback (most recent call last):
  File "<pyshell#769>", line 1, in <module>
    datetime.fromisoformat('2020-06-22T15:38:17',timezone=timedelta(hours=-7))
TypeError: fromisoformat() takes no keyword arguments
>>> time
  
datetime.datetime(2020, 6, 21, 2, 9, 59)
>>> time.timetz()
  
datetime.time(2, 9, 59)
>>> time = datetime.fromisoformat('2020-06-21T02:09:59.0000000')
  
Traceback (most recent call last):
  File "<pyshell#772>", line 1, in <module>
    time = datetime.fromisoformat('2020-06-21T02:09:59.0000000')
ValueError: Invalid isoformat string: '2020-06-21T02:09:59.0000000'
>>> time = datetime.fromisoformat('2020-06-21T02:09:59')
  
>>> time
  
datetime.datetime(2020, 6, 21, 2, 9, 59)
>>> time.replace(tzinfo=timezone(timedelta(hours=-7)))
  
datetime.datetime(2020, 6, 21, 2, 9, 59, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))
>>> time2 = datetime.fromisoformat('2020-06-21T09:20:00')
  
>>> time2.utcoffset()
  
>>> time2
  
datetime.datetime(2020, 6, 21, 9, 20)
>>> time2.astimezone(timezone.utc)
  
datetime.datetime(2020, 6, 21, 15, 20, tzinfo=datetime.timezone.utc)
>>> time2.reaplce(timezone=timezone.utc)
  
Traceback (most recent call last):
  File "<pyshell#780>", line 1, in <module>
    time2.reaplce(timezone=timezone.utc)
AttributeError: 'datetime.datetime' object has no attribute 'reaplce'
>>> time2.replace(timezone=timezone.utc)
  
Traceback (most recent call last):
  File "<pyshell#781>", line 1, in <module>
    time2.replace(timezone=timezone.utc)
TypeError: 'timezone' is an invalid keyword argument for replace()
>>> time2.replace(tzinfo=timezone.utc)
  
datetime.datetime(2020, 6, 21, 9, 20, tzinfo=datetime.timezone.utc)
>>> time
  
datetime.datetime(2020, 6, 21, 2, 9, 59)
>>> time-time2
  
datetime.timedelta(days=-1, seconds=60599)
>>> time2-time
  
datetime.timedelta(seconds=25801)
>>> 25801/3600
  
7.166944444444445
>>> time.astimezone(timezone.utc)-time2
  
Traceback (most recent call last):
  File "<pyshell#787>", line 1, in <module>
    time.astimezone(timezone.utc)-time2
TypeError: can't subtract offset-naive and offset-aware datetimes
>>> time
  
datetime.datetime(2020, 6, 21, 2, 9, 59)
>>> time2
  
datetime.datetime(2020, 6, 21, 9, 20)
>>> time2.replace(timezone=timezone.utc)
  
Traceback (most recent call last):
  File "<pyshell#790>", line 1, in <module>
    time2.replace(timezone=timezone.utc)
TypeError: 'timezone' is an invalid keyword argument for replace()
>>> time2.replace(tzinfo=timezone.utc)
  
datetime.datetime(2020, 6, 21, 9, 20, tzinfo=datetime.timezone.utc)
>>> time.replace(tzinfo=timezone(timedelta(hours=-7)))
  
datetime.datetime(2020, 6, 21, 2, 9, 59, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))
>>> time
  
datetime.datetime(2020, 6, 21, 2, 9, 59)
>>> time = time.replace(tzinfo=timezone(timedelta(hours=-7)))
  
>>> time2
  
datetime.datetime(2020, 6, 21, 9, 20)
>>> time2 = time2.replace(tzinfo=timezone.utc)
  
>>> time-time2
  
datetime.timedelta(days=-1, seconds=85799)
>>> (time-time2).total_seconds()
  
-601.0
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: 
Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 237, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 190, in run
    password = input('Password: ').encode()
KeyboardInterrupt
>>> file_lines = get_file('TylerNet file name: ')
  
TylerNet file name: 0622PPLRECON.TXT
>>> access_tokens, expires_ats = get_access_tokens('mountaindew'.encode())
  
PayPal Authentication info file name: paypalauth.txt
>>> line = tyler_data[5]
  
Traceback (most recent call last):
  File "<pyshell#801>", line 1, in <module>
    line = tyler_data[5]
NameError: name 'tyler_data' is not defined
>>> tyler_data = [[line[sum(widths[:k]):sum(widths[:k+1])].strip() for k in range(len(widths))] for line in file_lines]
  
>>> line = tyler_data[4]
  
>>> get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  
Traceback (most recent call last):
  File "<pyshell#804>", line 1, in <module>
    get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 65, in get_transaction_id
    print(response.json()['total_items'])
KeyError: 'total_items'
>>> time = datetime.fromisoformat('2020-06-21T02:09:59')
  
>>> time.replace(tzinfo=timezone(timedelta(hours=-7)))
  
datetime.datetime(2020, 6, 21, 2, 9, 59, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))
>>> time.isoformat()
  
'2020-06-21T02:09:59'
>>> amt_dollars,time_string,email,zip_code,listing_id,entry_time_string,access_tokens=line[4],line[0],line[1],line[3],line[2],line[6],access_tokens
  
>>>  amt_cents = abs(round(float2(amt_dollars)*100))
  
SyntaxError: unexpected indent
amt_cents = abs(round(float2(amt_dollars)*100))
>>> amt_cents = abs(round(float2(amt_dollars)*100))
  
>>> time = strings2time(time_string,entry_time_string)
  
>>> time
  
datetime.datetime(2020, 6, 21, 2, 9, 59, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))
>>> params = {
        'transaction_status':'S',
        'transaction_amount':'['+str(amt_cents-1)+' TO '+str(amt_cents+1)+']',
        'tansaction_currency':'USD',
        'start_date':(time+timedelta(weeks=-1)).isoformat()+'-07:00',
        'end_date':(time+timedelta(weeks=1)).isoformat()+'-07:00',
        'fields':'transaction_info,payer_info,shipping_info,auction_info',
        'page_size':page_size
    }
  
>>> params
  
{'transaction_status': 'S', 'transaction_amount': '[145727 TO 145729]', 'tansaction_currency': 'USD', 'start_date': '2020-06-14T02:09:59-07:00-07:00', 'end_date': '2020-06-28T02:09:59-07:00-07:00', 'fields': 'transaction_info,payer_info,shipping_info,auction_info', 'page_size': 200}
>>> time
  
datetime.datetime(2020, 6, 21, 2, 9, 59, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))
>>> time.isoformat()
  
'2020-06-21T02:09:59-07:00'
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: 
Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 237, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 190, in run
    password = input('Password: ').encode()
KeyboardInterrupt
>>> file_lines = get_file('TylerNet file name: ')
  
TylerNet file name: 0622PPLRECON.TXT
>>> access_tokens, expires_ats = get_access_tokens('mountaindew'.encode())
  
PayPal Authentication info file name: paypalauth.txt
>>> tyler_data = [[line[sum(widths[:k]):sum(widths[:k+1])].strip() for k in range(len(widths))] for line in file_lines]
  
>>> line = tyler_data[4]
  
>>> get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  
1
0
Traceback (most recent call last):
  File "<pyshell#821>", line 1, in <module>
    get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 75, in get_transaction_id
    'Email':transaction['payer_info']['email_address']==email,
KeyError: 'email_address'
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: 
Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 240, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 193, in run
    password = input('Password: ').encode()
KeyboardInterrupt
>>> file_lines = get_file('TylerNet file name: ')
  
TylerNet file name: 0622PPLRECON.TXT
>>> access_tokens, expires_ats = get_access_tokens('mountaindew'.encode())
  
PayPal Authentication info file name: paypalauth.txt

>>> tyler_data = [[line[sum(widths[:k]):sum(widths[:k+1])].strip() for k in range(len(widths))] for line in file_lines]
  
>>> line = tyler_data[4]
  
>>> get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  
1
0
Traceback (most recent call last):
  File "<pyshell#826>", line 1, in <module>
    get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 81, in get_transaction_id
    'Listing ID':(listing_id in transaction_detail['auction_info']['auction_item_site'])
NameError: name 'transaction_detail' is not defined
>>> def get_transaction_id(amt_dollars,time_string,email,zip_code,listing_id,entry_time_string,access_tokens):
    amt_cents = abs(round(float2(amt_dollars)*100))
    time = strings2time(time_string,entry_time_string)
    params = {
        'transaction_status':'S',
        'transaction_amount':'['+str(amt_cents-1)+' TO '+str(amt_cents+1)+']',
        'tansaction_currency':'USD',
        'start_date':(time+timedelta(weeks=-1)).isoformat(),
        'end_date':(time+timedelta(weeks=1)).isoformat(),
        'fields':'transaction_info,payer_info,shipping_info,auction_info',
        'page_size':page_size
    }
    transaction_details = []
    for access_token in access_tokens:
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}
        page_number = 1
        while True:
            params['page_number'] = page_number
            response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                    headers=headers, params=params)
            print(response.json()['total_items'])
            transaction_details += response.json()['transaction_details']
            if page_number>=response.json()['total_pages']:
                break
            else:
                page_number += 1
    for transaction in transaction_details:
        paypal_time = datetime.fromisoformat(transaction['transaction_info']['transaction_updated_date'][:-2]+':00')
        matches = {
            'Time':(paypal_time-time).total_seconds(),
            'Email':('email_address' in transaction['payer_info'] and
                     transaction['payer_info']['email_address']==email),
            'Name':('payer_name' in transaction['payer_info'] and
                    'surname' in transaction['payer_info']['payer_name'] and
                    transaction['payer_info']['payer_name']['surname']==email), #FILL THIS IN WITH THE CORRECT VARIABLE
            'Zip Code':compare_zips(transaction['shipping_info']['address']['postal_code'],zip_code),
            'Listing ID':(listing_id in transaction['auction_info']['auction_item_site'])
        }
        transaction['Joss Matches'] = matches
        transaction['Joss Score'] = (+ abs(matches['Time']/86400) - matches['Email']*7
                                     - matches['Name'] - matches['Zip Code'] - matches['Listing ID'])
    for k,transaction in enumerate(sorted(transaction_details, key=lambda transaction: transaction['Joss Score'])):
        print(k+1, matches)

            
>>> get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  
1
0
Traceback (most recent call last):
  File "<pyshell#828>", line 1, in <module>
    get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "<pyshell#827>", line 37, in get_transaction_id
    'Listing ID':(listing_id in transaction['auction_info']['auction_item_site'])
KeyError: 'auction_item_site'
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: 
Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 244, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 197, in run
    password = input('Password: ').encode()
KeyboardInterrupt
>>> file_lines = get_file('TylerNet file name: ')
  
TylerNet file name: 0622PPLRECON.TXT
>>> access_tokens, expires_ats = get_access_tokens('mountaindew'.encode())
  
PayPal Authentication info file name: paypalauth.txt
>>> tyler_data = [[line[sum(widths[:k]):sum(widths[:k+1])].strip() for k in range(len(widths))] for line in file_lines]
  
>>> line = tyler_data[4]
  
>>> get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  
1
0
Traceback (most recent call last):
  File "<pyshell#833>", line 1, in <module>
    get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 84, in get_transaction_id
    'Zip Code':compare_zips(safe_keys(transaction,'shipping_info','address','postal_code'),zip_code),
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 42, in compare_zips
    s1,s2 = s1.replace('-',''),s2.replace('-','')
AttributeError: 'NoneType' object has no attribute 'replace'
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: 
  file_lines = get_file('TylerNet file name: ')
TylerNet file name: File not found. Press any key to exit
Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 169, in get_file
    file = open(filename, 'rb' if password else 'r')
FileNotFoundError: [Errno 2] No such file or directory: "  file_lines = get_file('TylerNet file name: ')"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 246, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 201, in run
    file_lines = get_file('TylerNet file name: ')
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 171, in get_file
    input('File not found. Press any key to exit')
KeyboardInterrupt
>>> file_lines = get_file('TylerNet file name: ')
  
TylerNet file name: 0622PPLRECON.TXT
>>> access_tokens, expires_ats = get_access_tokens('mountaindew'.encode())
  
PayPal Authentication info file name: paypalauth.txt
>>> tyler_data = [[line[sum(widths[:k]):sum(widths[:k+1])].strip() for k in range(len(widths))] for line in file_lines]
  
>>> line = tyler_data[4]
  
>>> get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  
1
0
Traceback (most recent call last):
  File "<pyshell#838>", line 1, in <module>
    get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 87, in get_transaction_id
    'Listing ID':(listing_id in safe_keys(transaction,'auction_info','auction_item_site'))
TypeError: argument of type 'NoneType' is not iterable
>>> def safe_keys(dictionary,*keys):
    for key in keys:
        if key in dictionary:
            dictionary = dictionary[key]
        else:
            return ''

  
>>> get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  
1
0
1 {'Time': 109698.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
>>> def get_transaction_id(amt_dollars,time_string,email,zip_code,listing_id,entry_time_string,access_tokens):
    amt_cents = abs(round(float2(amt_dollars)*100))
    time = strings2time(time_string,entry_time_string)
    params = {
        'transaction_status':'S',
        'transaction_amount':'['+str(amt_cents-1)+' TO '+str(amt_cents+1)+']',
        'tansaction_currency':'USD',
        'start_date':(time+timedelta(weeks=-1)).isoformat(),
        'end_date':(time+timedelta(weeks=1)).isoformat(),
        'fields':'transaction_info,payer_info,shipping_info,auction_info',
        'page_size':page_size
    }
    transaction_details = []
    for access_token in access_tokens:
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}
        page_number = 1
        while True:
            params['page_number'] = page_number
            response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                    headers=headers, params=params)
            transaction_details += response.json()['transaction_details']
            if page_number>=response.json()['total_pages']:
                break
            else:
                page_number += 1
    for transaction in transaction_details:
        paypal_time = datetime.fromisoformat(transaction['transaction_info']['transaction_updated_date'][:-2]+':00')
        matches = {
            'Time':(paypal_time-time).total_seconds(),
            'Email':safe_keys(transaction,'payer_info','email_address')==email,
            'Name':safe_keys(transaction,'payer_info','payer_name','surname')==email, #FILL THIS IN WITH THE CORRECT VARIABLE
            'Zip Code':compare_zips(safe_keys(transaction,'shipping_info','address','postal_code'),zip_code),
            'Listing ID':(listing_id in safe_keys(transaction,'auction_info','auction_item_site'))
        }
        transaction['Joss Matches'] = matches
        transaction['Joss Score'] = (+ abs(matches['Time']/86400) - matches['Email']*7
                                     - matches['Name'] - matches['Zip Code'] - matches['Listing ID'])
    for k,transaction in enumerate(sorted(transaction_details, key=lambda transaction: transaction['Joss Score'])):
        print(k+1, matches)

  
>>> for line in tyler_data:
  get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)

  
1 {'Time': -528378.0, 'Email': True, 'Name': False, 'Zip Code': False, 'Listing ID': False}
1 {'Time': -528378.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
1 {'Time': 109698.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
1 {'Time': 109698.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
1 {'Time': 109698.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
1 {'Time': 37964.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
2 {'Time': 37964.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
Traceback (most recent call last):
  File "<pyshell#846>", line 2, in <module>
    get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "<pyshell#843>", line 20, in get_transaction_id
    headers=headers, params=params)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\requests\api.py", line 76, in get
    return request('get', url, params=params, **kwargs)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\requests\api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\requests\sessions.py", line 530, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\requests\sessions.py", line 643, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\requests\adapters.py", line 449, in send
    timeout=timeout
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\connectionpool.py", line 677, in urlopen
    chunked=chunked,
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\connectionpool.py", line 426, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\connectionpool.py", line 421, in _make_request
    httplib_response = conn.getresponse()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\http\client.py", line 1321, in getresponse
    response.begin()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\http\client.py", line 296, in begin
    version, status, reason = self._read_status()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\http\client.py", line 257, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\socket.py", line 589, in readinto
    return self._sock.recv_into(b)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\ssl.py", line 1052, in recv_into
    return self.read(nbytes, buffer)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\ssl.py", line 911, in read
    return self._sslobj.read(len, buffer)
KeyboardInterrupt
>>> done = set()
>>> for line in tyler_data:
	if not '\t'.join(line) in done:
		done.add('\t'.join(line))
		get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)

		
1 {'Time': -528378.0, 'Email': True, 'Name': False, 'Zip Code': False, 'Listing ID': False}
1 {'Time': -528378.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
1 {'Time': 109698.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
1 {'Time': 37964.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
2 {'Time': 37964.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
1 {'Time': 235252.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
1 {'Time': 141669.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
1 {'Time': 126257.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
1 {'Time': 249635.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
1 {'Time': 100381.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
1 {'Time': 104058.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}
Traceback (most recent call last):
  File "<pyshell#852>", line 4, in <module>
    get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "<pyshell#843>", line 33, in get_transaction_id
    'Listing ID':(listing_id in safe_keys(transaction,'auction_info','auction_item_site'))
TypeError: argument of type 'NoneType' is not iterable
>>> def safe_keys(dictionary,*keys):
    for key in keys:
        if key in dictionary:
            dictionary = dictionary[key]
        else:
            return ''
    return dictionary

>>> def get_transaction_id(amt_dollars,time_string,email,zip_code,listing_id,entry_time_string,access_tokens):
    amt_cents = abs(round(float2(amt_dollars)*100))
    time = strings2time(time_string,entry_time_string)
    params = {
        'transaction_status':'S',
        'transaction_amount':'['+str(amt_cents-1)+' TO '+str(amt_cents+1)+']',
        'tansaction_currency':'USD',
        'start_date':(time+timedelta(weeks=-1)).isoformat(),
        'end_date':(time+timedelta(weeks=1)).isoformat(),
        'fields':'transaction_info,payer_info,shipping_info,auction_info',
        'page_size':page_size
    }
    transaction_details = []
    for access_token in access_tokens:
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}
        page_number = 1
        while True:
            params['page_number'] = page_number
            response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                    headers=headers, params=params)
            transaction_details += response.json()['transaction_details']
            if page_number>=response.json()['total_pages']:
                break
            else:
                page_number += 1
    for transaction in transaction_details:
        paypal_time = datetime.fromisoformat(transaction['transaction_info']['transaction_updated_date'][:-2]+':00')
        matches = {
            'Time':(paypal_time-time).total_seconds(),
            'Email':safe_keys(transaction,'payer_info','email_address')==email,
            'Name':safe_keys(transaction,'payer_info','payer_name','surname')==email, #FILL THIS IN WITH THE CORRECT VARIABLE
            'Zip Code':compare_zips(safe_keys(transaction,'shipping_info','address','postal_code'),zip_code),
            'Listing ID':(listing_id in safe_keys(transaction,'auction_info','auction_item_site'))
        }
        transaction['Joss Matches'] = matches
        transaction['Joss Score'] = (+ abs(matches['Time']/86400) - matches['Email']*7
                                     - matches['Name'] - matches['Zip Code'] - matches['Listing ID'])
    for k,transaction in enumerate(sorted(transaction_details, key=lambda transaction: transaction['Joss Score'])):
        print(k+1, [item for item in matches.items() if item[1]])

        
>>> done = set()
>>> for line in tyler_data:
	if not '\t'.join(line) in done:
		done.add('\t'.join(line))
		get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)

		
1 [('Time', -528378.0), ('Email', True), ('Zip Code', True)]
1 [('Time', -528378.0), ('Zip Code', True)]
1 [('Time', 109698.0), ('Zip Code', True)]
1 [('Time', 37964.0), ('Email', True), ('Zip Code', True)]
2 [('Time', 37964.0), ('Email', True), ('Zip Code', True)]
1 [('Time', 235252.0), ('Zip Code', True)]
1 [('Time', 141669.0), ('Email', True), ('Zip Code', True)]
1 [('Time', 126257.0), ('Email', True), ('Zip Code', True)]
1 [('Time', 249635.0), ('Zip Code', True)]
1 [('Time', 100381.0), ('Zip Code', True)]
1 [('Time', 104058.0), ('Email', True), ('Zip Code', True)]
1 [('Time', -3.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -4.0), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', -4.0), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -4.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', -4.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -2.0), ('Email', True), ('Listing ID', True)]
1 [('Time', -6.0), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -6.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', 48161.0)]
2 [('Time', 48161.0)]
3 [('Time', 48161.0)]
1 [('Time', 48161.0)]
2 [('Time', 48161.0)]
3 [('Time', 48161.0)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -1.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', 259407.0), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', 259347.0), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -3.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', 16516.0), ('Listing ID', True)]
2 [('Time', 16516.0), ('Listing ID', True)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -1.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', -1.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -3.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -289319.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -11655.0), ('Email', True), ('Listing ID', True)]
1 [('Time', -11655.0), ('Listing ID', True)]
1 [('Time', -3640.0), ('Zip Code', True)]
1 [('Time', 2333.0), ('Zip Code', True)]
1 [('Time', 164370.0)]
2 [('Time', 164370.0)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -3.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -3753.0), ('Email', True), ('Listing ID', True)]
1 [('Time', -3813.0), ('Email', True), ('Listing ID', True)]
1 [('Time', -281887.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -281887.0), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -284287.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -284287.0), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -2.0), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -200018.0), ('Zip Code', True)]
1 [('Time', -200018.0), ('Email', True), ('Zip Code', True)]
1 [('Time', 443582.0)]
2 [('Time', 443582.0)]
1 [('Time', 443582.0)]
2 [('Time', 443582.0)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -304337.0), ('Listing ID', True)]
2 [('Time', -304337.0), ('Listing ID', True)]
1 [('Time', 11121.0), ('Zip Code', True)]
1 [('Time', 11121.0), ('Email', True), ('Zip Code', True)]
1 [('Time', 7309.0), ('Email', True), ('Zip Code', True)]
1 [('Time', 7309.0), ('Zip Code', True)]
1 [('Time', -263715.0), ('Email', True), ('Listing ID', True)]
1 [('Time', -263715.0), ('Listing ID', True)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -3.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -3.0), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -3.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -90589.0), ('Listing ID', True)]
1 [('Time', -10423.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -3526.0), ('Email', True)]
1 [('Time', 55822.0), ('Zip Code', True)]
1 [('Time', 55822.0), ('Zip Code', True)]
1 [('Time', 49117.0), ('Zip Code', True)]
1 [('Time', 600.0), ('Zip Code', True)]
1 [('Time', -5.0), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -5.0), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -5.0), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -5.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', 549713.0), ('Listing ID', True)]
2 [('Time', 549713.0), ('Listing ID', True)]
3 [('Time', 549713.0), ('Listing ID', True)]
4 [('Time', 549713.0), ('Listing ID', True)]
1 [('Time', -3.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
1 [('Time', -3.0), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', -3.0), ('Zip Code', True), ('Listing ID', True)]
>>> line = tyler_data[9]
>>> amt_dollars,time_string,email,zip_code,listing_id,entry_time_string,access_tokens=amt_dollars,time_string,email,zip_code,listing_id,entry_time_string,access_tokens
Traceback (most recent call last):
  File "<pyshell#861>", line 1, in <module>
    amt_dollars,time_string,email,zip_code,listing_id,entry_time_string,access_tokens=amt_dollars,time_string,email,zip_code,listing_id,entry_time_string,access_tokens
NameError: name 'amt_dollars' is not defined
>>> amt_dollars,time_string,email,zip_code,listing_id,entry_time_string,access_tokens=line[4],line[0],line[1],line[3],line[2],line[6],access_tokens
>>> amt_cents = abs(round(float2(amt_dollars)*100))
>>> time = strings2time(time_string,entry_time_string)
>>>  params = {
        'transaction_status':'S',
        'transaction_amount':'['+str(amt_cents-1)+' TO '+str(amt_cents+1)+']',
        'tansaction_currency':'USD',
        'start_date':(time+timedelta(weeks=-1)).isoformat(),
        'end_date':(time+timedelta(weeks=1)).isoformat(),
        'fields':'transaction_info,payer_info,shipping_info,auction_info',
        'page_size':page_size
    }
SyntaxError: unexpected indent
>>> params = {
       'transaction_status':'S',
       'transaction_amount':'['+str(amt_cents-1)+' TO '+str(amt_cents+1)+']',
       'tansaction_currency':'USD',
       'start_date':(time+timedelta(weeks=-1)).isoformat(),
       'end_date':(time+timedelta(weeks=1)).isoformat(),
       'fields':'transaction_info,payer_info,shipping_info,auction_info',
       'page_size':page_size
   }
>>> transaction_details = []
>>> for access_token in access_tokens:
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}
        page_number = 1
        while True:
            params['page_number'] = page_number
            response = requests.get('https://api.paypal.com/v1/reporting/transactions',
                                    headers=headers, params=params)
            transaction_details += response.json()['transaction_details']
            if page_number>=response.json()['total_pages']:
                break
            else:
                page_number += 1

                
>>> len(transaction_details)
2
>>> transaction_details[0]
{'transaction_info': {'paypal_account_id': 'XNAXREMW5WMTU', 'transaction_id': '91J95221S89730052', 'paypal_reference_id': '5U556201K1231693Y', 'paypal_reference_id_type': 'TXN', 'transaction_event_code': 'T0006', 'transaction_initiation_date': '2020-06-15T15:58:05+0000', 'transaction_updated_date': '2020-06-15T15:58:05+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '1487.84'}, 'fee_amount': {'currency_code': 'USD', 'value': '-33.03'}, 'sales_tax_amount': {'currency_code': 'USD', 'value': '88.84'}, 'transaction_status': 'S', 'invoice_id': '9554332648', 'protection_eligibility': '01'}, 'payer_info': {'account_id': 'XNAXREMW5WMTU', 'email_address': 'scillitoe.b@charter.net', 'address_status': 'Y', 'payer_status': 'N', 'payer_name': {'given_name': 'Robert', 'surname': 'Scillitoe', 'alternate_full_name': 'Robert Scillitoe'}, 'country_code': 'US'}, 'shipping_info': {'name': 'Robert, Scillitoe', 'address': {'line1': '18 Meredith Lane', 'city': 'New Milford', 'state': 'CT', 'country_code': 'US', 'postal_code': '06776'}}, 'auction_info': {}}
>>> transaction_details[1]
{'transaction_info': {'paypal_account_id': '6XJTZ6XKY5BQL', 'transaction_id': '3W487768B3782210S', 'paypal_reference_id': '5L70778665540240V', 'paypal_reference_id_type': 'TXN', 'transaction_event_code': 'T0006', 'transaction_initiation_date': '2020-06-22T15:41:11+0000', 'transaction_updated_date': '2020-06-22T15:41:11+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '1487.84'}, 'fee_amount': {'currency_code': 'USD', 'value': '-33.03'}, 'sales_tax_amount': {'currency_code': 'USD', 'value': '88.84'}, 'transaction_status': 'S', 'invoice_id': '9554332664', 'protection_eligibility': '01'}, 'payer_info': {'account_id': '6XJTZ6XKY5BQL', 'email_address': 'Metropolis_488@hotmail.com', 'phone_number': {'country_code': '1', 'national_number': '4342490862'}, 'address_status': 'Y', 'payer_status': 'Y', 'payer_name': {'given_name': 'Matthew', 'surname': 'Steiner', 'alternate_full_name': 'Matthew Steiner'}, 'country_code': 'US', 'address': {'line1': '21 Brocketts Point Rd', 'city': 'Branford', 'state': 'CT', 'country_code': 'US', 'postal_code': '06405'}}, 'shipping_info': {'name': 'Matthew, Steiner', 'address': {'line1': '21 Brocketts Point Rd', 'city': 'Branford', 'state': 'CT', 'country_code': 'US', 'postal_code': '06405'}}, 'auction_info': {}}
>>> for transaction in transaction_details:
        paypal_time = datetime.fromisoformat(transaction['transaction_info']['transaction_updated_date'][:-2]+':00')
        matches = {
            'Time':(paypal_time-time).total_seconds(),
            'Email':safe_keys(transaction,'payer_info','email_address')==email,
            'Name':safe_keys(transaction,'payer_info','payer_name','surname')==email, #FILL THIS IN WITH THE CORRECT VARIABLE
            'Zip Code':compare_zips(safe_keys(transaction,'shipping_info','address','postal_code'),zip_code),
            'Listing ID':(listing_id in safe_keys(transaction,'auction_info','auction_item_site'))
        }
        transaction['Joss Matches'] = matches
        transaction['Joss Score'] = (+ abs(matches['Time']/86400) - matches['Email']*7
                                     - matches['Name'] - matches['Zip Code'] - matches['Listing ID'])

        
>>> transaction_details[0]
{'transaction_info': {'paypal_account_id': 'XNAXREMW5WMTU', 'transaction_id': '91J95221S89730052', 'paypal_reference_id': '5U556201K1231693Y', 'paypal_reference_id_type': 'TXN', 'transaction_event_code': 'T0006', 'transaction_initiation_date': '2020-06-15T15:58:05+0000', 'transaction_updated_date': '2020-06-15T15:58:05+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '1487.84'}, 'fee_amount': {'currency_code': 'USD', 'value': '-33.03'}, 'sales_tax_amount': {'currency_code': 'USD', 'value': '88.84'}, 'transaction_status': 'S', 'invoice_id': '9554332648', 'protection_eligibility': '01'}, 'payer_info': {'account_id': 'XNAXREMW5WMTU', 'email_address': 'scillitoe.b@charter.net', 'address_status': 'Y', 'payer_status': 'N', 'payer_name': {'given_name': 'Robert', 'surname': 'Scillitoe', 'alternate_full_name': 'Robert Scillitoe'}, 'country_code': 'US'}, 'shipping_info': {'name': 'Robert, Scillitoe', 'address': {'line1': '18 Meredith Lane', 'city': 'New Milford', 'state': 'CT', 'country_code': 'US', 'postal_code': '06776'}}, 'auction_info': {}, 'Joss Matches': {'Time': -565822.0, 'Email': False, 'Name': False, 'Zip Code': False, 'Listing ID': False}, 'Joss Score': 6.548865740740741}
>>> transaction_details[1]
{'transaction_info': {'paypal_account_id': '6XJTZ6XKY5BQL', 'transaction_id': '3W487768B3782210S', 'paypal_reference_id': '5L70778665540240V', 'paypal_reference_id_type': 'TXN', 'transaction_event_code': 'T0006', 'transaction_initiation_date': '2020-06-22T15:41:11+0000', 'transaction_updated_date': '2020-06-22T15:41:11+0000', 'transaction_amount': {'currency_code': 'USD', 'value': '1487.84'}, 'fee_amount': {'currency_code': 'USD', 'value': '-33.03'}, 'sales_tax_amount': {'currency_code': 'USD', 'value': '88.84'}, 'transaction_status': 'S', 'invoice_id': '9554332664', 'protection_eligibility': '01'}, 'payer_info': {'account_id': '6XJTZ6XKY5BQL', 'email_address': 'Metropolis_488@hotmail.com', 'phone_number': {'country_code': '1', 'national_number': '4342490862'}, 'address_status': 'Y', 'payer_status': 'Y', 'payer_name': {'given_name': 'Matthew', 'surname': 'Steiner', 'alternate_full_name': 'Matthew Steiner'}, 'country_code': 'US', 'address': {'line1': '21 Brocketts Point Rd', 'city': 'Branford', 'state': 'CT', 'country_code': 'US', 'postal_code': '06405'}}, 'shipping_info': {'name': 'Matthew, Steiner', 'address': {'line1': '21 Brocketts Point Rd', 'city': 'Branford', 'state': 'CT', 'country_code': 'US', 'postal_code': '06405'}}, 'auction_info': {}, 'Joss Matches': {'Time': 37964.0, 'Email': True, 'Name': False, 'Zip Code': True, 'Listing ID': False}, 'Joss Score': -7.560601851851851}
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: mountaindew
TylerNet file name: 0622PPLRECON.TXT
PayPal Authentication info file name: paypalauth.txt

1 [('Time', -528378.0), ('Email', True), ('Zip Code', True)]

1 [('Time', -528378.0), ('Zip Code', True)]

1 [('Time', 109698.0), ('Zip Code', True)]

1 [('Time', 37964.0), ('Email', True), ('Zip Code', True)]
2 [('Time', -565822.0)]

1 [('Time', 235252.0), ('Zip Code', True)]

1 [('Time', 141669.0), ('Email', True), ('Zip Code', True)]

1 [('Time', 126257.0), ('Email', True), ('Zip Code', True)]

1 [('Time', 249635.0), ('Zip Code', True)]

1 [('Time', 100381.0), ('Zip Code', True)]

1 [('Time', 104058.0), ('Email', True), ('Zip Code', True)]

1 [('Time', -3.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -4.0), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', -247025.0), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -4.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', -247025.0), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -2.0), ('Email', True), ('Listing ID', True)]

1 [('Time', -6.0), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -6.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]


1 [('Time', -5.0), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', 14785.0)]
3 [('Time', 48161.0)]

1 [('Time', -5.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', 14785.0)]
3 [('Time', 48161.0)]

1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', 244499.0)]

1 [('Time', -1.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', 259407.0), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', 259347.0), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -3.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -3.0), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', 16516.0), ('Listing ID', True)]

1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -1.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', -16520.0), ('Listing ID', True)]

1 [('Time', -3.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -289319.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -11655.0), ('Email', True), ('Listing ID', True)]

1 [('Time', -11655.0), ('Listing ID', True)]


1 [('Time', -3640.0), ('Zip Code', True)]

1 [('Time', 2333.0), ('Zip Code', True)]

1 [('Time', -3505.0)]
2 [('Time', 164370.0)]

1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -3.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]





1 [('Time', -3753.0), ('Email', True), ('Listing ID', True)]

1 [('Time', -3813.0), ('Email', True), ('Listing ID', True)]




1 [('Time', -281887.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -281887.0), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -284287.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -284287.0), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -2.0), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]




1 [('Time', -200018.0), ('Zip Code', True)]

1 [('Time', -200018.0), ('Email', True), ('Zip Code', True)]

1 [('Time', -3.0), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', 443582.0)]

1 [('Time', -3.0), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', 443582.0)]

1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -59836.0), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', -304337.0), ('Listing ID', True)]

1 [('Time', 11121.0), ('Zip Code', True)]

1 [('Time', 11121.0), ('Email', True), ('Zip Code', True)]

1 [('Time', 7309.0), ('Email', True), ('Zip Code', True)]

1 [('Time', 7309.0), ('Zip Code', True)]

1 [('Time', -263715.0), ('Email', True), ('Listing ID', True)]

1 [('Time', -263715.0), ('Listing ID', True)]



1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]



1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -3.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -3.0), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -3.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -90589.0), ('Listing ID', True)]

1 [('Time', -10423.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -3526.0), ('Email', True)]

1 [('Time', 55822.0), ('Zip Code', True)]

1 [('Time', 55822.0), ('Zip Code', True)]

1 [('Time', 49117.0), ('Zip Code', True)]

1 [('Time', 600.0), ('Zip Code', True)]


1 [('Time', -5.0), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -5.0), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -5.0), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -5.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]



1 [('Time', -2.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -2.0), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', 331180.0), ('Listing ID', True)]
3 [('Time', 406391.0), ('Listing ID', True)]
4 [('Time', 549713.0), ('Listing ID', True)]

1 [('Time', -3.0), ('Email', True), ('Zip Code', True), ('Listing ID', True)]

1 [('Time', -3.0), ('Zip Code', True), ('Listing ID', True)]
2 [('Time', -589052.0), ('Listing ID', True)]

Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 247, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 242, in run
    out_file.close()
NameError: name 'out_file' is not defined
>>> timedelta(-589052.0)
datetime.timedelta(days=-589052)
>>> timedelta(seconds=-589052.0)
datetime.timedelta(days=-7, seconds=15748)
>>> timedelta(seconds=abs(-589052.0))
datetime.timedelta(days=6, seconds=70652)
>>> timedelta(seconds=abs(-589052.0)).hours
Traceback (most recent call last):
  File "<pyshell#880>", line 1, in <module>
    timedelta(seconds=abs(-589052.0)).hours
AttributeError: 'datetime.timedelta' object has no attribute 'hours'
>>> timedelta(seconds=abs(-589052.0)).hours()
Traceback (most recent call last):
  File "<pyshell#881>", line 1, in <module>
    timedelta(seconds=abs(-589052.0)).hours()
AttributeError: 'datetime.timedelta' object has no attribute 'hours'
>>> abs(-589052.0)
589052.0
>>> 589052.0//86400
6.0
>>> ((-10000)%34)
30
>>> def seconds2string(total):
    seconds = abs(total)
    days = seconds//86400
    hours = (seconds%86400)//3600
    mins = (seconds%3600)//60
    secs = (seconds%60)
    result = ''
    if days>0:
        result += str(days) + ' days,'
    if hours>0:
        result += str(hours) + ' hours,'
    if mins>0:
        result += str(mins) + ' mins,'
    if secds>0:
        result += str(secs) + ' secs '
    if total<0:
        return result + ' early, '
    else:
        return result + ' late, '

>>> seconds2string(100)
Traceback (most recent call last):
  File "<pyshell#887>", line 1, in <module>
    seconds2string(100)
  File "<pyshell#886>", line 14, in seconds2string
    if secds>0:
NameError: name 'secds' is not defined
>>> def seconds2string(total):
    seconds = abs(total)
    days = seconds//86400
    hours = (seconds%86400)//3600
    mins = (seconds%3600)//60
    secs = (seconds%60)
    result = ''
    if days>0:
        result += str(days) + ' days,'
    if hours>0:
        result += str(hours) + ' hours,'
    if mins>0:
        result += str(mins) + ' mins,'
    if secs>0:
        result += str(secs) + ' secs '
    if total<0:
        return result + ' early, '
    else:
        return result + ' late, '

>>> seconds2string(100)
'1 mins,40 secs  late, '
>>> seconds2string(1000)
'16 mins,40 secs  late, '
>>> seconds2string(10000)
'2 hours,46 mins,40 secs  late, '
>>> def seconds2string(total):
    seconds = abs(total)
    days = seconds//86400
    hours = (seconds%86400)//3600
    mins = (seconds%3600)//60
    secs = (seconds%60)
    result = ''
    if days>0:
        result += str(days) + ' days, '
    if hours>0:
        result += str(hours) + ' hours, '
    if mins>0:
        result += str(mins) + ' mins, '
    if secs>0:
        result += str(secs) + ' secs, '
    if total<0:
        return result[:-2] + ' early, '
    else:
        return result[:-2] + ' late, '

>>> seconds2string(10000)
'2 hours, 46 mins, 40 secs late, '
>>> seconds2string(10960)
'3 hours, 2 mins, 40 secs late, '
>>> seconds2string(9960)
'2 hours, 46 mins late, '
>>> seconds2string(996000)
'11 days, 12 hours, 40 mins late, '
>>> seconds2string(996000-50*60.5)
'11.0 days, 11.0 hours, 49.0 mins, 35.0 secs late, '
>>> seconds2string(996000-40*60.5)
'11.0 days, 11.0 hours, 59.0 mins, 40.0 secs late, '
>>> seconds2string(996000-39.5*60)
'11.0 days, 12.0 hours, 30.0 secs late, '
>>> 996000-39.5*60
993630.0
>>> total = 993630.0
>>> seconds = abs(total)
>>> seconds
993630.0
>>> days = seconds//86400
>>> days
11.0
>>> seconds//86400
11.0
>>> seconds/86400
11.500347222222222
>>> int(seconds/86400)
11
>>> def seconds2string(total):
    seconds = abs(total)
    days = int(seconds/86400)
    hours = int((seconds%86400)/3600)
    mins = int((seconds%3600)/60)
    secs = seconds%60
    result = ''
    if days>0:
        result += str(days) + ' days, '
    if hours>0:
        result += str(hours) + ' hours, '
    if mins>0:
        result += str(mins) + ' mins, '
    if secs>0:
        result += str(secs) + ' secs, '
    if total<0:
        return result[:-2] + ' early, '
    else:
        return result[:-2] + ' late, '

>>> seconds2string(996000-39.511*60)
'11 days, 12 hours, 29.339999999967404 secs late, '
>>> seconds2string(996000-39.51*60)
'11 days, 12 hours, 29.400000000023283 secs late, '
>>> %
SyntaxError: invalid syntax
>>> round(36.410005,2)
36.41
>>> print()

>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: mountaindew
TylerNet file name: 0622PPLRECON.TXT
PayPal Authentication info file name: paypalauth.txt

Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 268, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 242, in run
    get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 114, in get_transaction_id
    print(k+1, seconds2string(transaction['Joss Time']), 'matches:'+match_string if match_string else '')
TypeError: can only concatenate str (not "list") to str
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: mountaindew
TylerNet file name: 0622PPLRECON.TXT
PayPal Authentication info file name: paypalauth.txt

1 6 days, 2 hours, 46 mins, 18.0 secs early,  matches:Email, Zip Code

1 6 days, 2 hours, 46 mins, 18.0 secs early,  matches:Zip Code

1 1 days, 6 hours, 28 mins, 18.0 secs late,  matches:Zip Code

1 10 hours, 32 mins, 44.0 secs late,  matches:Email, Zip Code
2 6 days, 13 hours, 10 mins, 22.0 secs early,  

1 2 days, 17 hours, 20 mins, 52.0 secs late,  matches:Zip Code

1 1 days, 15 hours, 21 mins, 9.0 secs late,  matches:Email, Zip Code

1 1 days, 11 hours, 4 mins, 17.0 secs late,  matches:Email, Zip Code

1 2 days, 21 hours, 20 mins, 35.0 secs late,  matches:Zip Code

1 1 days, 3 hours, 53 mins, 1.0 secs late,  matches:Zip Code

1 1 days, 4 hours, 54 mins, 18.0 secs late,  matches:Email, Zip Code

1 3.0 secs early,  matches:Email, Zip Code, Listing ID

1 4.0 secs early,  matches:Zip Code, Listing ID
2 2 days, 20 hours, 37 mins, 5.0 secs early,  matches:Zip Code, Listing ID

1 4.0 secs early,  matches:Email, Zip Code, Listing ID
2 2 days, 20 hours, 37 mins, 5.0 secs early,  matches:Zip Code, Listing ID

1 2.0 secs early,  matches:Email, Zip Code, Listing ID

1 2.0 secs early,  matches:Email, Zip Code, Listing ID

1 2.0 secs early,  matches:Email, Listing ID

1 6.0 secs early,  matches:Zip Code, Listing ID

1 6.0 secs early,  matches:Email, Zip Code, Listing ID


1 5.0 secs early,  matches:Zip Code, Listing ID
2 4 hours, 6 mins, 25.0 secs late,  
3 13 hours, 22 mins, 41.0 secs late,  

1 5.0 secs early,  matches:Email, Zip Code, Listing ID
2 4 hours, 6 mins, 25.0 secs late,  
3 13 hours, 22 mins, 41.0 secs late,  

1 2.0 secs early,  matches:Email, Zip Code, Listing ID

1 2.0 secs early,  matches:Email, Zip Code, Listing ID
2 2 days, 19 hours, 54 mins, 59.0 secs late,  

1 1.0 secs early,  matches:Email, Zip Code, Listing ID

1 3 days, 3 mins, 27.0 secs late,  matches:Zip Code, Listing ID

1 3 days, 2 mins, 27.0 secs late,  matches:Zip Code, Listing ID

1 3.0 secs early,  matches:Email, Zip Code, Listing ID

1 3.0 secs early,  matches:Zip Code, Listing ID
2 4 hours, 35 mins, 16.0 secs late,  matches:Listing ID

1 2.0 secs early,  matches:Email, Zip Code, Listing ID

1 1.0 secs early,  matches:Email, Zip Code, Listing ID
2 4 hours, 35 mins, 20.0 secs early,  matches:Listing ID

1 3.0 secs early,  matches:Email, Zip Code, Listing ID

1 3 days, 8 hours, 21 mins, 59.0 secs early,  matches:Email, Zip Code, Listing ID

1 3 hours, 14 mins, 15.0 secs early,  matches:Email, Listing ID

1 3 hours, 14 mins, 15.0 secs early,  matches:Listing ID


Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 268, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 242, in run
    get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 94, in get_transaction_id
    headers=headers, params=params)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\requests\api.py", line 76, in get
    return request('get', url, params=params, **kwargs)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\requests\api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\requests\sessions.py", line 530, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\requests\sessions.py", line 643, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\requests\adapters.py", line 449, in send
    timeout=timeout
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\connectionpool.py", line 677, in urlopen
    chunked=chunked,
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\connectionpool.py", line 381, in _make_request
    self._validate_conn(conn)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\connectionpool.py", line 976, in _validate_conn
    conn.connect()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\connection.py", line 370, in connect
    ssl_context=context,
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\urllib3\util\ssl_.py", line 343, in ssl_wrap_socket
    context.load_verify_locations(ca_certs, ca_cert_dir, ca_cert_data)
KeyboardInterrupt
>>> [2] 6 days, 2 hours, 46 mins early,  Matches: Email, Zip Code
SyntaxError: invalid syntax
>>> 2 [6 days, 2 hours, 46 mins early,  Matches: Email, Zip Code]
SyntaxError: invalid syntax
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: 
Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 279, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 232, in run
    password = input('Password: ').encode()
KeyboardInterrupt
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: mountaindew
TylerNet file name: 0622PPLRECON.TXT
PayPal Authentication info file name: paypalauth.txt
Output file name: 0622output-in.txt
Error file name: 0622error-in.txt
Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 277, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 253, in run
    transaction = get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 120, in get_transaction_id
    prompt += '['+str(k+1)+'] '+seconds2string(transaction['Joss Time'])+('\tMatches: '+match_string if match_string else '')+'\n'
UnboundLocalError: local variable 'prompt' referenced before assignment
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: mountaindew
TylerNet file name: 0622PPLRECON.TXT
PayPal Authentication info file name: paypalauth.txt
Output file name: 0622output-in.txt
Error file name: 0622error-in.txt
Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 278, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 254, in run
    transaction = get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 121, in get_transaction_id
    prompt += '['+str(k+1)+'] '+seconds2string(transaction['Joss Time'])+('\tMatches: '+match_string if match_string else '')+'\n'
UnboundLocalError: local variable 'prompt' referenced before assignment
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: mountaindew
TylerNet file name: 0622PPLRECON.TXT
PayPal Authentication info file name: paypalauth.txt
Output file name: 0622output-in.txt
Error file name: 0622error-in.txt
[1] 6 days, 2 hours, 46 mins early, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1
Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 278, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 256, in run
    results[tyler_num] = (transaction['transaction_id'],
KeyError: 'transaction_id'
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: mountaindew
TylerNet file name: 0622PPLRECON.TXT
PayPal Authentication info file name: paypalauth.txt
Output file name: 0622output-in.txt
Error file name: 0622error-in.txt
[1] 6 days, 2 hours, 46 mins early, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1
[1] 6 days, 2 hours, 46 mins early, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1
[1] 1 days, 6 hours, 28 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1
[1] 10 hours, 32 mins late, 	Matches: Email, Zip Code
[2] 6 days, 13 hours, 10 mins early, 

Enter a number to select a match or 0 to mark as an error: 1
[1] 2 days, 17 hours, 20 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1
[1] 1 days, 15 hours, 21 mins late, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1
[1] 1 days, 11 hours, 4 mins late, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1
[1] 2 days, 21 hours, 20 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1
[1] 1 days, 3 hours, 53 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1
[1] 1 days, 4 hours, 54 mins late, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1
Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 278, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 254, in run
    transaction = get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 118, in get_transaction_id
    if abs(transaction['Joss Time'])<10*60 and (matches['Email'] or sum(matches)>=2):
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> matches
			  
Traceback (most recent call last):
  File "<pyshell#920>", line 1, in <module>
    matches
NameError: name 'matches' is not defined
>>> d = dict([('Email', True), ('Zip Code', True), ('Listing ID', True)])
			  
>>> d
			  
{'Email': True, 'Zip Code': True, 'Listing ID': True}
>>> d.values()
			  
dict_values([True, True, True])
>>> sum(d.values())
			  
3
>>> d = dict([('Email', True), ('Zip Code', True), ('Listing ID', True), ('Last Name', False)])
			  
>>> sum(d.values())
			  
3
>>> d
			  
{'Email': True, 'Zip Code': True, 'Listing ID': True, 'Last Name': False}
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: mountaindew
TylerNet file name: 0622PPLRECON.TXT
PayPal Authentication info file name: paypalauth.txt
Output file name: 0622output-in.txt
Error file name: 0622error-in.txt



[1] 6 days, 2 hours, 46 mins early, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 6 days, 2 hours, 46 mins early, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 1 days, 6 hours, 28 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 10 hours, 32 mins late, 	Matches: Email, Zip Code
[2] 6 days, 13 hours, 10 mins early, 

Enter a number to select a match or 0 to mark as an error: 1



[1] 2 days, 17 hours, 20 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 1 days, 15 hours, 21 mins late, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 1 days, 11 hours, 4 mins late, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 2 days, 21 hours, 20 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 1 days, 3 hours, 53 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 1 days, 4 hours, 54 mins late, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1
Traceback (most recent call last):
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 278, in <module>
    run()
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 254, in run
    transaction = get_transaction_id(line[4],line[0],line[1],line[3],line[2],line[6],access_tokens)
  File "C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py", line 118, in get_transaction_id
    if abs(transaction['Joss Time'])<10*60 and (matches['Email'] or sum(d.values())>=2):
NameError: name 'd' is not defined
>>> 
======= RESTART: C:/Users/joshm/Desktop/Listen Up/ListenUpPayPal1.2.py =======
Password: mountaindew
TylerNet file name: 0622PPLRECON.TXT
PayPal Authentication info file name: paypalauth.txt
Output file name: 0622output-in.txt
Error file name: 0622error-in.txt



[1] 6 days, 2 hours, 46 mins early, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 6 days, 2 hours, 46 mins early, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 1 days, 6 hours, 28 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 10 hours, 32 mins late, 	Matches: Email, Zip Code
[2] 6 days, 13 hours, 10 mins early, 

Enter a number to select a match or 0 to mark as an error: 1



[1] 2 days, 17 hours, 20 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 1 days, 15 hours, 21 mins late, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 1 days, 11 hours, 4 mins late, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 2 days, 21 hours, 20 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 1 days, 3 hours, 53 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 1 days, 4 hours, 54 mins late, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 3 days, 3 mins late, 	Matches: Zip Code, Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 3 days, 2 mins late, 	Matches: Zip Code, Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 3 days, 8 hours, 21 mins early, 	Matches: Email, Zip Code, Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 3 hours, 14 mins early, 	Matches: Email, Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 3 hours, 14 mins early, 	Matches: Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 1 hours early, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 38 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 58 mins early, 
[2] 1 days, 21 hours, 39 mins late, 

Enter a number to select a match or 0 to mark as an error: 1



[1] 1 hours, 2 mins early, 	Matches: Email, Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 1 hours, 3 mins early, 	Matches: Email, Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 3 days, 6 hours, 18 mins early, 	Matches: Email, Zip Code, Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 3 days, 6 hours, 18 mins early, 	Matches: Zip Code, Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 3 days, 6 hours, 58 mins early, 	Matches: Email, Zip Code, Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 3 days, 6 hours, 58 mins early, 	Matches: Zip Code, Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 2 days, 7 hours, 33 mins early, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 2 days, 7 hours, 33 mins early, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 16 hours, 37 mins early, 	Matches: Zip Code, Listing ID
[2] 3 days, 12 hours, 32 mins early, 	Matches: Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 3 hours, 5 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 3 hours, 5 mins late, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 2 hours, 1 mins late, 	Matches: Email, Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 2 hours, 1 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 3 days, 1 hours, 15 mins early, 	Matches: Email, Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 3 days, 1 hours, 15 mins early, 	Matches: Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 1 days, 1 hours, 9 mins early, 	Matches: Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 2 hours, 53 mins early, 	Matches: Email, Zip Code, Listing ID

Enter a number to select a match or 0 to mark as an error: 1



[1] 58 mins early, 	Matches: Email

Enter a number to select a match or 0 to mark as an error: 1



[1] 15 hours, 30 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 15 hours, 30 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 13 hours, 38 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1



[1] 10 mins late, 	Matches: Zip Code

Enter a number to select a match or 0 to mark as an error: 1
Press enter to exit
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
			  
Traceback (most recent call last):
  File "<pyshell#929>", line 1, in <module>
    compile_function('TEST',order=['D','A','B','S'])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 780, in compile_function
    states2rules(order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 815, in states2rules
    current_var = order.index(step.variable)
NameError: name 'step' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
			  
Traceback (most recent call last):
  File "<pyshell#930>", line 1, in <module>
    compile_function('TEST',order=['D','A','B','S'])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 780, in compile_function
    states2rules(order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 816, in states2rules
    if next_var<current_var:
NameError: name 'next_var' is not defined
>>> (1-(1))//1
			  
0
>>> (1-(1))//2
			  
0
>>> (1-(-1))//2
			  
1
>>> int(1<0)
			  
0
>>> int(-1<0)
			  
1
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
			  
Traceback (most recent call last):
  File "<pyshell#936>", line 1, in <module>
    compile_function('TEST',order=['D','A','B','S'])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 780, in compile_function
    states2rules(order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 824, in states2rules
    next_var = order.index(next_instruction.vard)+(next_instruction.direction<0)
AttributeError: 'Instruction' object has no attribute 'direction'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
			  
Traceback (most recent call last):
  File "<pyshell#937>", line 1, in <module>
    compile_function('TEST',order=['D','A','B','S'])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 780, in compile_function
    states2rules(order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 828, in states2rules
    transition[0].get_char(order),
AttributeError: 'str' object has no attribute 'get_char'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
			  
>>> directions
			  
{36: {'L'}, 37: {'L'}, 40: {'L', 'R'}, 44: {'L'}, 45: {'L'}, 48: {'L'}, 52: {'L', 'R'}, 53: {'L', 'R'}, 56: {'L'}, 57: {'L'}, 60: {'L', 'R'}, 61: {'L', 'R'}, 62: {'L', 'R'}, 68: {'L'}, 69: {'L'}, 72: {'L', 'R'}, 73: {'', 'L'}}
>>> len(rules)
			  
79
>>> for rule in rules.items():
	print(rule)

			  
(('36', "0'"), ('36L', "0'", 'L'))
(('36', "1'"), ('36L', "1'", 'L'))
(('37', "0'"), ('37L', "0'", 'L'))
(('37', "1'"), ('37L', "1'", 'L'))
(('40', '0'), ('40R', "0'", 'R'))
(('40', '1'), ('40R', "1'", 'R'))
(('40', "0'"), ('40', "0'", 'R'))
(('40', "1'"), ('40', "1'", 'R'))
(('40', 'B'), ('40L', 'B', 'L'))
(('44', '0'), ('44L', '0', 'L'))
(('44', '1'), ('44L', '0', 'L'))
(('44', "0'"), ('44L', '0', 'L'))
(('44', "1'"), ('44L', '0', 'L'))
(('44', 'S'), ('44L', 'None', 'L'))
(('45', '0'), ('45L', '1', 'L'))
(('45', '1'), ('45L', '1', 'L'))
(('45', "0'"), ('45L', '1', 'L'))
(('45', "1'"), ('45L', '1', 'L'))
(('45', 'S'), ('45L', 'None', 'L'))
(('48', '0'), ('48', "0'", 'R'))
(('48', '1'), ('48L', "1'", 'L'))
(('48', "0'"), ('48', "0'", 'R'))
(('48', "1'"), ('48', "1'", 'R'))
(('48', 'B'), ('48L', 'B', 'L'))
(('52', '0'), ('52L', '0', 'L'))
(('52', '1'), ('52L', '1', 'L'))
(('52', "0'"), ('52L', '0', 'L'))
(('52', "1'"), ('52L', '1', 'L'))
(('52', 'B'), ('52R', 'B', 'R'))
(('53', '0'), ('53L', '0', 'L'))
(('53', '1'), ('53L', '1', 'L'))
(('53', "0'"), ('53L', '0', 'L'))
(('53', "1'"), ('53L', '1', 'L'))
(('53', 'B'), ('53R', 'B', 'R'))
(('56', '0'), ('56L', "0'", 'L'))
(('56', '1'), ('56L', "1'", 'L'))
(('56', "0'"), ('56', "0'", 'R'))
(('56', "1'"), ('56', "1'", 'R'))
(('56', 'S'), ('56L', 'None', 'L'))
(('57', '0'), ('57L', "0'", 'L'))
(('57', '1'), ('57L', "1'", 'L'))
(('57', "0'"), ('57', "0'", 'R'))
(('57', "1'"), ('57', "1'", 'R'))
(('57', 'S'), ('57L', 'None', 'L'))
(('60', '0'), ('60R', "0'", 'R'))
(('60', '1'), ('60R', "1'", 'R'))
(('60', "0'"), ('60L', "0'", 'L'))
(('60', "1'"), ('60L', "1'", 'L'))
(('60', 'A'), ('60R', 'A', 'R'))
(('61', '0'), ('61R', "1'", 'R'))
(('61', '1'), ('61R', "0'", 'R'))
(('61', "0'"), ('61L', "0'", 'L'))
(('61', "1'"), ('61L', "1'", 'L'))
(('61', 'A'), ('61R', 'A', 'R'))
(('62', '0'), ('62R', "0'", 'R'))
(('62', '1'), ('62R', "1'", 'R'))
(('62', "0'"), ('62L', "0'", 'L'))
(('62', "1'"), ('62L', "1'", 'L'))
(('62', 'A'), ('62R', 'A', 'R'))
(('68', '0'), ('68L', '0', 'L'))
(('68', '1'), ('68L', '1', 'L'))
(('68', "0'"), ('68L', '0', 'L'))
(('68', "1'"), ('68L', '1', 'L'))
(('68', 'S'), ('68L', 'S', 'L'))
(('69', '0'), ('69L', '0', 'L'))
(('69', '1'), ('69L', '1', 'L'))
(('69', "0'"), ('69L', '0', 'L'))
(('69', "1'"), ('69L', '1', 'L'))
(('69', 'S'), ('69L', 'S', 'L'))
(('72', '0'), ('72L', '0', 'L'))
(('72', '1'), ('72L', '1', 'L'))
(('72', "0'"), ('72L', '0', 'L'))
(('72', "1'"), ('72L', '1', 'L'))
(('72', 'A'), ('72R', 'A', 'R'))
(('73', '0'), ('73L', '0', 'L'))
(('73', '1'), ('73L', '1', 'L'))
(('73', "0'"), ('73L', '0', 'L'))
(('73', "1'"), ('73L', '1', 'L'))
(('73', 'A'), ('73', 'A', 'R'))
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
			  
Traceback (most recent call last):
  File "<pyshell#945>", line 1, in <module>
    compile_function('TEST',order=['D','A','B','S'])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 780, in compile_function
    states2rules(order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 832, in states2rules
    command=='SEZ' and symbol=='1')/2
NameError: name 'command' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
>>> for rule in rules.items():
	print(rule)

	
(('36', "0'"), ('36', "0'", 'R'))
(('36', "1'"), ('36', "1'", 'R'))
(('37', "0'"), ('37', "0'", 'R'))
(('37', "1'"), ('37', "1'", 'R'))
(('40', '0'), ('40R', "0'", 'R'))
(('40', '1'), ('40R', "1'", 'R'))
(('40', "0'"), ('40', "0'", 'R'))
(('40', "1'"), ('40', "1'", 'R'))
(('40', 'B'), ('40L', 'B', 'L'))
(('44', '0'), ('44', '0', 'R'))
(('44', '1'), ('44', '0', 'R'))
(('44', "0'"), ('44', '0', 'R'))
(('44', "1'"), ('44', '0', 'R'))
(('44', 'S'), ('44L', 'S', 'L'))
(('45', '0'), ('45', '1', 'R'))
(('45', '1'), ('45', '1', 'R'))
(('45', "0'"), ('45', '1', 'R'))
(('45', "1'"), ('45', '1', 'R'))
(('45', 'S'), ('45L', 'S', 'L'))
(('48', '0'), ('48', "0'", 'R'))
(('48', '1'), ('48L', "1'", 'L'))
(('48', "0'"), ('48', "0'", 'R'))
(('48', "1'"), ('48', "1'", 'R'))
(('48', 'B'), ('48L', 'B', 'L'))
(('52', '0'), ('52', '0', 'R'))
(('52', '1'), ('52', '1', 'R'))
(('52', "0'"), ('52', '0', 'R'))
(('52', "1'"), ('52', '1', 'R'))
(('52', 'B'), ('52R', 'B', 'R'))
(('53', '0'), ('53', '0', 'R'))
(('53', '1'), ('53', '1', 'R'))
(('53', "0'"), ('53', '0', 'R'))
(('53', "1'"), ('53', '1', 'R'))
(('53', 'B'), ('53R', 'B', 'R'))
(('56', '0'), ('56L', "0'", 'L'))
(('56', '1'), ('56L', "1'", 'L'))
(('56', "0'"), ('56', "0'", 'R'))
(('56', "1'"), ('56', "1'", 'R'))
(('56', 'S'), ('56L', 'S', 'L'))
(('57', '0'), ('57L', "0'", 'L'))
(('57', '1'), ('57L', "1'", 'L'))
(('57', "0'"), ('57', "0'", 'R'))
(('57', "1'"), ('57', "1'", 'R'))
(('57', 'S'), ('57L', 'S', 'L'))
(('60', '0'), ('60R', "0'", 'R'))
(('60', '1'), ('60R', "1'", 'R'))
(('60', "0'"), ('60', "0'", 'R'))
(('60', "1'"), ('60', "1'", 'R'))
(('60', 'A'), ('60R', 'A', 'R'))
(('61', '0'), ('61R', "1'", 'R'))
(('61', '1'), ('61R', "0'", 'R'))
(('61', "0'"), ('61', "0'", 'R'))
(('61', "1'"), ('61', "1'", 'R'))
(('61', 'A'), ('61R', 'A', 'R'))
(('62', '0'), ('62R', "0'", 'R'))
(('62', '1'), ('62R', "1'", 'R'))
(('62', "0'"), ('62', "0'", 'R'))
(('62', "1'"), ('62', "1'", 'R'))
(('62', 'A'), ('62R', 'A', 'R'))
(('68', '0'), ('68', '0', 'R'))
(('68', '1'), ('68', '1', 'R'))
(('68', "0'"), ('68', '0', 'R'))
(('68', "1'"), ('68', '1', 'R'))
(('68', 'S'), ('68L', 'S', 'L'))
(('69', '0'), ('69', '0', 'R'))
(('69', '1'), ('69', '1', 'R'))
(('69', "0'"), ('69', '0', 'R'))
(('69', "1'"), ('69', '1', 'R'))
(('69', 'S'), ('69L', 'S', 'L'))
(('72', '0'), ('72', '0', 'R'))
(('72', '1'), ('72', '1', 'R'))
(('72', "0'"), ('72', '0', 'R'))
(('72', "1'"), ('72', '1', 'R'))
(('72', 'A'), ('72R', 'A', 'R'))
(('73', '0'), ('73', '0', 'R'))
(('73', '1'), ('73', '1', 'R'))
(('73', "0'"), ('73', '0', 'R'))
(('73', "1'"), ('73', '1', 'R'))
(('73', 'A'), ('73', 'A', 'R'))
>>> for k,instr in get_quasis([Instruction]):
	print(k,instr)

	
2 Instruction(STORE, vard=S, next_quasis=[3, 3])
6 Instruction(LOADNEXT, vard=A, next_quasis=[7, 19])
7 Instruction(BRANCH, next_quasis=[12, 22, 22, 22])
10 Instruction(BRANCH, next_quasis=[12, 19, 12, 12])
12 Instruction(SLLs, vard=B, next_quasis=[13])
13 Instruction(BRANCH, next_quasis=[6, 15, 15, 15])
15 Instruction(LOADI, next_quasis=[16])
16 Instruction(LOADNEXT, vard=A, next_quasis=[17, 19])
17 Instruction(BRANCH, next_quasis=[15, 19, 19, 19])
19 Instruction(UNREAD, vard=A, next_quasis=[2])
22 Instruction(LOADI, next_quasis=[24])
24 Instruction(LOADNEXT, vard=B, next_quasis=[25, 32])
25 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26])
26 Instruction(LOAD, vard=D, next_quasis=[27, 32])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[29])
28 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[0])
29 Instruction(STORENEXT, vard=D, next_quasis=[30, 32])
30 Instruction(JUMP, next_quasis=[24])
32 Instruction(MAP, map={(0,): (0,), (1,): (1,), (2,): (1,), (3,): (1,)}, next_quasis=[33])
33 Instruction(UNREAD, vard=B, next_quasis=[34])
34 Instruction(UNREAD, vard=D, next_quasis=[10])
>>> used_states
{0, 3, 36, 37, 40, 44, 45, 48, 52, 53, 56, 57, 60, 61, 62, 68, 69, 72, 73}
>>> quasis[0]
End(is_start=True, next_quasis=[40])
>>> quasis[40]
State(instruction=6, acc=0, transitions={'0': ["0'", 0, 44], '1': ["1'", 0, 56], "0'": ["0'", 0, 40], "1'": ["1'", 0, 40], Sym('A'+1): [Sym('A'+1), 0, 52]}, direction=1)
>>> for k in sorted(used_states):
	print(k,quasis[k])

	
0 End(is_start=True, next_quasis=[40])
3 End(is_start=False, next_quasis=[None])
36 State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 36], "1'": ["1'", 0, 36], Sym('S'+1): [Sym('S'+1), 0, 3]}, direction=1)
37 State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 37], "1'": ["1'", 1, 37], Sym('S'+1): [Sym('S'+1), 1, 3]}, direction=1)
40 State(instruction=6, acc=0, transitions={'0': ["0'", 0, 44], '1': ["1'", 0, 56], "0'": ["0'", 0, 40], "1'": ["1'", 0, 40], Sym('A'+1): [Sym('A'+1), 0, 52]}, direction=1)
44 State(instruction=12, acc=0, transitions={'0': ['0', 0, 44], '1': ['0', 1, 45], "0'": ['0', 0, 44], "1'": ['0', 1, 45], Sym('B'+1): [Sym('B'+1), 0, 40]}, direction=1)
45 State(instruction=12, acc=1, transitions={'0': ['1', 0, 44], '1': ['1', 1, 45], "0'": ['1', 0, 44], "1'": ['1', 1, 45], Sym('B'+1): [Sym('B'+1), 0, 48]}, direction=1)
48 State(instruction=16, acc=0, transitions={'0': ["0'", 0, 48], '1': ["1'", 1, 53], "0'": ["0'", 0, 48], "1'": ["1'", 0, 48], Sym('A'+1): [Sym('A'+1), 0, 52]}, direction=1)
52 State(instruction=19, acc=0, transitions={'0': ['0', 0, 52], '1': ['1', 0, 52], "0'": ['0', 0, 52], "1'": ['1', 0, 52], Sym('A'+1): [Sym('A'+1), 0, 36]}, direction=1)
53 State(instruction=19, acc=1, transitions={'0': ['0', 1, 53], '1': ['1', 1, 53], "0'": ['0', 1, 53], "1'": ['1', 1, 53], Sym('A'+1): [Sym('A'+1), 1, 37]}, direction=1)
56 State(instruction=24, acc=0, transitions={'0': ["0'", 0, 60], '1': ["1'", 1, 61], "0'": ["0'", 0, 56], "1'": ["1'", 0, 56], Sym('B'+1): [Sym('B'+1), 0, 68]}, direction=1)
57 State(instruction=24, acc=1, transitions={'0': ["0'", 1, 61], '1': ["1'", 2, 62], "0'": ["0'", 1, 57], "1'": ["1'", 1, 57], Sym('B'+1): [Sym('B'+1), 1, 69]}, direction=1)
60 State(instruction=26, acc=0, transitions={'0': ["0'", 0, 56], '1': ["1'", 0, 56], "0'": ["0'", 0, 60], "1'": ["1'", 0, 60], Sym('D'+1): [Sym('D'+1), 0, 68]}, direction=1)
61 State(instruction=26, acc=1, transitions={'0': ["1'", 0, 56], '1': ["0'", 1, 57], "0'": ["0'", 1, 61], "1'": ["1'", 1, 61], Sym('D'+1): [Sym('D'+1), 1, 69]}, direction=1)
62 State(instruction=26, acc=2, transitions={'0': ["0'", 1, 57], '1': ["1'", 1, 57], "0'": ["0'", 2, 62], "1'": ["1'", 2, 62], Sym('D'+1): [Sym('D'+1), 1, 69]}, direction=1)
68 State(instruction=33, acc=0, transitions={'0': ['0', 0, 68], '1': ['1', 0, 68], "0'": ['0', 0, 68], "1'": ['1', 0, 68], Sym('B'+1): [Sym('B'+1), 0, 72]}, direction=1)
69 State(instruction=33, acc=1, transitions={'0': ['0', 1, 69], '1': ['1', 1, 69], "0'": ['0', 1, 69], "1'": ['1', 1, 69], Sym('B'+1): [Sym('B'+1), 1, 73]}, direction=1)
72 State(instruction=34, acc=0, transitions={'0': ['0', 0, 72], '1': ['1', 0, 72], "0'": ['0', 0, 72], "1'": ['1', 0, 72], Sym('D'+1): [Sym('D'+1), 0, 44]}, direction=1)
73 State(instruction=34, acc=1, transitions={'0': ['0', 1, 73], '1': ['1', 1, 73], "0'": ['0', 1, 73], "1'": ['1', 1, 73], Sym('D'+1): [Sym('D'+1), 1, 53]}, direction=1)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
>>> for rule in rules.items():
	print(rule)

	
(('36', "0'"), ('36', "0'", 'R'))
(('36', "1'"), ('36', "1'", 'R'))
(('36', '0'), ('halt', '0', ''))
(('36', '1'), ('halt', '1', ''))
(('36', 'D'), ('halt', 'D', ''))
(('37', "0'"), ('37', "0'", 'R'))
(('37', "1'"), ('37', "1'", 'R'))
(('37', '0'), ('halt', '0', ''))
(('37', '1'), ('halt', '1', ''))
(('37', 'D'), ('halt', 'D', ''))
(('40', '0'), ('40R', "0'", 'R'))
(('40', '1'), ('40R', "1'", 'R'))
(('40', "0'"), ('40', "0'", 'R'))
(('40', "1'"), ('40', "1'", 'R'))
(('40', 'B'), ('40L', 'B', 'L'))
(('44', '0'), ('44', '0', 'R'))
(('44', '1'), ('44', '0', 'R'))
(('44', "0'"), ('44', '0', 'R'))
(('44', "1'"), ('44', '0', 'R'))
(('44', 'S'), ('44L', 'None', 'L'))
(('45', '0'), ('45', '1', 'R'))
(('45', '1'), ('45', '1', 'R'))
(('45', "0'"), ('45', '1', 'R'))
(('45', "1'"), ('45', '1', 'R'))
(('45', 'S'), ('45L', 'None', 'L'))
(('48', '0'), ('48', "0'", 'R'))
(('48', '1'), ('48L', "1'", 'L'))
(('48', "0'"), ('48', "0'", 'R'))
(('48', "1'"), ('48', "1'", 'R'))
(('48', 'B'), ('48L', 'B', 'L'))
(('52', '0'), ('52', '0', 'R'))
(('52', '1'), ('52', '1', 'R'))
(('52', "0'"), ('52', '0', 'R'))
(('52', "1'"), ('52', '1', 'R'))
(('52', 'B'), ('52R', 'B', 'R'))
(('53', '0'), ('53', '0', 'R'))
(('53', '1'), ('53', '1', 'R'))
(('53', "0'"), ('53', '0', 'R'))
(('53', "1'"), ('53', '1', 'R'))
(('53', 'B'), ('53R', 'B', 'R'))
(('56', '0'), ('56L', "0'", 'L'))
(('56', '1'), ('56L', "1'", 'L'))
(('56', "0'"), ('56', "0'", 'R'))
(('56', "1'"), ('56', "1'", 'R'))
(('56', 'S'), ('56L', 'None', 'L'))
(('57', '0'), ('57L', "0'", 'L'))
(('57', '1'), ('57L', "1'", 'L'))
(('57', "0'"), ('57', "0'", 'R'))
(('57', "1'"), ('57', "1'", 'R'))
(('57', 'S'), ('57L', 'None', 'L'))
(('60', '0'), ('60R', "0'", 'R'))
(('60', '1'), ('60R', "1'", 'R'))
(('60', "0'"), ('60', "0'", 'R'))
(('60', "1'"), ('60', "1'", 'R'))
(('60', 'A'), ('60R', 'A', 'R'))
(('61', '0'), ('61R', "1'", 'R'))
(('61', '1'), ('61R', "0'", 'R'))
(('61', "0'"), ('61', "0'", 'R'))
(('61', "1'"), ('61', "1'", 'R'))
(('61', 'A'), ('61R', 'A', 'R'))
(('62', '0'), ('62R', "0'", 'R'))
(('62', '1'), ('62R', "1'", 'R'))
(('62', "0'"), ('62', "0'", 'R'))
(('62', "1'"), ('62', "1'", 'R'))
(('62', 'A'), ('62R', 'A', 'R'))
(('68', '0'), ('68', '0', 'R'))
(('68', '1'), ('68', '1', 'R'))
(('68', "0'"), ('68', '0', 'R'))
(('68', "1'"), ('68', '1', 'R'))
(('68', 'S'), ('68L', 'S', 'L'))
(('69', '0'), ('69', '0', 'R'))
(('69', '1'), ('69', '1', 'R'))
(('69', "0'"), ('69', '0', 'R'))
(('69', "1'"), ('69', '1', 'R'))
(('69', 'S'), ('69L', 'S', 'L'))
(('72', '0'), ('72', '0', 'R'))
(('72', '1'), ('72', '1', 'R'))
(('72', "0'"), ('72', '0', 'R'))
(('72', "1'"), ('72', '1', 'R'))
(('72', 'A'), ('72R', 'A', 'R'))
(('73', '0'), ('73', '0', 'R'))
(('73', '1'), ('73', '1', 'R'))
(('73', "0'"), ('73', '0', 'R'))
(('73', "1'"), ('73', '1', 'R'))
(('73', 'A'), ('73', 'A', 'R'))
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
>>> for rule in rules.items():
	print(rule)

	
(('36', "0'"), ('36', "0'", 'R'))
(('36', "1'"), ('36', "1'", 'R'))
(('36', '0'), ('halt', '0', ''))
(('36', '1'), ('halt', '0', ''))
(('36', 'D'), ('halt', 'D', ''))
(('37', "0'"), ('37', "0'", 'R'))
(('37', "1'"), ('37', "1'", 'R'))
(('37', '0'), ('halt', '1', ''))
(('37', '1'), ('halt', '1', ''))
(('37', 'D'), ('halt', 'D', ''))
(('40', '0'), ('40R', "0'", 'R'))
(('40', '1'), ('40R', "1'", 'R'))
(('40', "0'"), ('40', "0'", 'R'))
(('40', "1'"), ('40', "1'", 'R'))
(('40', 'B'), ('40L', 'B', 'L'))
(('44', '0'), ('44', '0', 'R'))
(('44', '1'), ('44', '0', 'R'))
(('44', "0'"), ('44', '0', 'R'))
(('44', "1'"), ('44', '0', 'R'))
(('44', 'S'), ('44L', 'None', 'L'))
(('45', '0'), ('45', '1', 'R'))
(('45', '1'), ('45', '1', 'R'))
(('45', "0'"), ('45', '1', 'R'))
(('45', "1'"), ('45', '1', 'R'))
(('45', 'S'), ('45L', 'S', 'L'))
(('48', '0'), ('48', "0'", 'R'))
(('48', '1'), ('48L', "1'", 'L'))
(('48', "0'"), ('48', "0'", 'R'))
(('48', "1'"), ('48', "1'", 'R'))
(('48', 'B'), ('48L', 'B', 'L'))
(('52', '0'), ('52', '0', 'R'))
(('52', '1'), ('52', '1', 'R'))
(('52', "0'"), ('52', '0', 'R'))
(('52', "1'"), ('52', '1', 'R'))
(('52', 'B'), ('52R', 'B', 'R'))
(('53', '0'), ('53', '0', 'R'))
(('53', '1'), ('53', '1', 'R'))
(('53', "0'"), ('53', '0', 'R'))
(('53', "1'"), ('53', '1', 'R'))
(('53', 'B'), ('53R', 'B', 'R'))
(('56', '0'), ('56L', "0'", 'L'))
(('56', '1'), ('56L', "1'", 'L'))
(('56', "0'"), ('56', "0'", 'R'))
(('56', "1'"), ('56', "1'", 'R'))
(('56', 'S'), ('56L', 'S', 'L'))
(('57', '0'), ('57L', "0'", 'L'))
(('57', '1'), ('57L', "1'", 'L'))
(('57', "0'"), ('57', "0'", 'R'))
(('57', "1'"), ('57', "1'", 'R'))
(('57', 'S'), ('57L', 'S', 'L'))
(('60', '0'), ('60R', "0'", 'R'))
(('60', '1'), ('60R', "1'", 'R'))
(('60', "0'"), ('60', "0'", 'R'))
(('60', "1'"), ('60', "1'", 'R'))
(('60', 'A'), ('60R', 'A', 'R'))
(('61', '0'), ('61R', "1'", 'R'))
(('61', '1'), ('61R', "0'", 'R'))
(('61', "0'"), ('61', "0'", 'R'))
(('61', "1'"), ('61', "1'", 'R'))
(('61', 'A'), ('61R', 'A', 'R'))
(('62', '0'), ('62R', "0'", 'R'))
(('62', '1'), ('62R', "1'", 'R'))
(('62', "0'"), ('62', "0'", 'R'))
(('62', "1'"), ('62', "1'", 'R'))
(('62', 'A'), ('62R', 'A', 'R'))
(('68', '0'), ('68', '0', 'R'))
(('68', '1'), ('68', '1', 'R'))
(('68', "0'"), ('68', '0', 'R'))
(('68', "1'"), ('68', '1', 'R'))
(('68', 'S'), ('68L', 'S', 'L'))
(('69', '0'), ('69', '0', 'R'))
(('69', '1'), ('69', '1', 'R'))
(('69', "0'"), ('69', '0', 'R'))
(('69', "1'"), ('69', '1', 'R'))
(('69', 'S'), ('69L', 'S', 'L'))
(('72', '0'), ('72', '0', 'R'))
(('72', '1'), ('72', '1', 'R'))
(('72', "0'"), ('72', '0', 'R'))
(('72', "1'"), ('72', '1', 'R'))
(('72', 'A'), ('72R', 'A', 'R'))
(('73', '0'), ('73', '0', 'R'))
(('73', '1'), ('73', '1', 'R'))
(('73', "0'"), ('73', '0', 'R'))
(('73', "1'"), ('73', '1', 'R'))
(('73', 'A'), ('73', 'A', 'R'))
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
>>> for rule in rules.items():
	print(rule)

	
(('36', "0'"), ('36', "0'", 'R'))
(('36', "1'"), ('36', "1'", 'R'))
(('36', '0'), ('halt', '0', ''))
(('36', '1'), ('halt', '0', ''))
(('36', 'D'), ('halt', None, ''))
(('37', "0'"), ('37', "0'", 'R'))
(('37', "1'"), ('37', "1'", 'R'))
(('37', '0'), ('halt', '1', ''))
(('37', '1'), ('halt', '1', ''))
(('37', 'D'), ('halt', None, ''))
(('40', '0'), ('40R', "0'", 'R'))
(('40', '1'), ('40R', "1'", 'R'))
(('40', "0'"), ('40', "0'", 'R'))
(('40', "1'"), ('40', "1'", 'R'))
(('40', 'B'), ('40L', None, 'L'))
(('44', '0'), ('44', '0', 'R'))
(('44', '1'), ('44', '0', 'R'))
(('44', "0'"), ('44', '0', 'R'))
(('44', "1'"), ('44', '0', 'R'))
(('44', 'S'), ('44L', None, 'L'))
(('45', '0'), ('45', '1', 'R'))
(('45', '1'), ('45', '1', 'R'))
(('45', "0'"), ('45', '1', 'R'))
(('45', "1'"), ('45', '1', 'R'))
(('45', 'S'), ('45L', None, 'L'))
(('48', '0'), ('48', "0'", 'R'))
(('48', '1'), ('48L', "1'", 'L'))
(('48', "0'"), ('48', "0'", 'R'))
(('48', "1'"), ('48', "1'", 'R'))
(('48', 'B'), ('48L', None, 'L'))
(('52', '0'), ('52', '0', 'R'))
(('52', '1'), ('52', '1', 'R'))
(('52', "0'"), ('52', '0', 'R'))
(('52', "1'"), ('52', '1', 'R'))
(('52', 'B'), ('52R', None, 'R'))
(('53', '0'), ('53', '0', 'R'))
(('53', '1'), ('53', '1', 'R'))
(('53', "0'"), ('53', '0', 'R'))
(('53', "1'"), ('53', '1', 'R'))
(('53', 'B'), ('53R', None, 'R'))
(('56', '0'), ('56L', "0'", 'L'))
(('56', '1'), ('56L', "1'", 'L'))
(('56', "0'"), ('56', "0'", 'R'))
(('56', "1'"), ('56', "1'", 'R'))
(('56', 'S'), ('56L', None, 'L'))
(('57', '0'), ('57L', "0'", 'L'))
(('57', '1'), ('57L', "1'", 'L'))
(('57', "0'"), ('57', "0'", 'R'))
(('57', "1'"), ('57', "1'", 'R'))
(('57', 'S'), ('57L', None, 'L'))
(('60', '0'), ('60R', "0'", 'R'))
(('60', '1'), ('60R', "1'", 'R'))
(('60', "0'"), ('60', "0'", 'R'))
(('60', "1'"), ('60', "1'", 'R'))
(('60', 'A'), ('60R', None, 'R'))
(('61', '0'), ('61R', "1'", 'R'))
(('61', '1'), ('61R', "0'", 'R'))
(('61', "0'"), ('61', "0'", 'R'))
(('61', "1'"), ('61', "1'", 'R'))
(('61', 'A'), ('61R', None, 'R'))
(('62', '0'), ('62R', "0'", 'R'))
(('62', '1'), ('62R', "1'", 'R'))
(('62', "0'"), ('62', "0'", 'R'))
(('62', "1'"), ('62', "1'", 'R'))
(('62', 'A'), ('62R', None, 'R'))
(('68', '0'), ('68', '0', 'R'))
(('68', '1'), ('68', '1', 'R'))
(('68', "0'"), ('68', '0', 'R'))
(('68', "1'"), ('68', '1', 'R'))
(('68', 'S'), ('68L', None, 'L'))
(('69', '0'), ('69', '0', 'R'))
(('69', '1'), ('69', '1', 'R'))
(('69', "0'"), ('69', '0', 'R'))
(('69', "1'"), ('69', '1', 'R'))
(('69', 'S'), ('69L', None, 'L'))
(('72', '0'), ('72', '0', 'R'))
(('72', '1'), ('72', '1', 'R'))
(('72', "0'"), ('72', '0', 'R'))
(('72', "1'"), ('72', '1', 'R'))
(('72', 'A'), ('72R', None, 'R'))
(('73', '0'), ('73', '0', 'R'))
(('73', '1'), ('73', '1', 'R'))
(('73', "0'"), ('73', '0', 'R'))
(('73', "1'"), ('73', '1', 'R'))
(('73', 'A'), ('73', None, 'R'))
>>> directions
{36: {''}, 37: {''}, 40: {'R', 'L'}, 44: {'', 'L'}, 45: {'', 'L'}, 48: {'L'}, 52: {'', 'R'}, 53: {'', 'R'}, 56: {'L'}, 57: {'L'}, 60: {'', 'R'}, 61: {'', 'R'}, 62: {'', 'R'}, 68: {'', 'L'}, 69: {'', 'L'}, 72: {'', 'R'}, 73: {''}}
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
>>> directions
{36: {(3, '')}, 37: {(3, '')}, 40: {(2, 'R'), (1, 'L')}, 44: {(2, ''), (1, 'L')}, 45: {(2, ''), (1, 'L')}, 48: {(1, 'L')}, 52: {(3, 'R'), (1, '')}, 53: {(3, 'R'), (1, '')}, 56: {(0, 'L'), (2, 'L')}, 57: {(0, 'L'), (2, 'L')}, 60: {(2, 'R'), (0, '')}, 61: {(2, 'R'), (0, '')}, 62: {(2, 'R'), (0, '')}, 68: {(2, ''), (0, 'L')}, 69: {(2, ''), (0, 'L')}, 72: {(2, 'R'), (0, '')}, 73: {(1, ''), (0, '')}}
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
>>> directions
{36: {(3, ''), (3, 'R')}, 37: {(3, ''), (3, 'R')}, 44: {(2, ''), (2, 'R')}, 56: {(2, 'R')}, 52: {(1, ''), (1, 'L')}, 45: {(2, '')}, 40: {(1, 'L')}, 48: {(1, 'L')}, 53: {(1, ''), (1, 'L')}, 60: {(0, ''), (0, 'L')}, 61: {(0, ''), (0, 'L')}, 68: {(2, 'L'), (2, ''), (2, 'R')}, 62: {(0, ''), (0, 'L')}, 69: {(2, 'L'), (2, ''), (2, 'R')}, 57: {(2, 'R')}, 72: {(0, ''), (0, 'L')}, 73: {(0, ''), (0, 'L')}}
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
Traceback (most recent call last):
  File "<pyshell#972>", line 1, in <module>
    compile_function('TEST',order=['D','A','B','S'])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 781, in compile_function
    states2rules(order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 853, in states2rules
    rules[(str(k)+d,None)] = (str(k)+d,None,direction)
NameError: name 'd' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
>>> for rule0,rule1 in rules.items():
	print(rule0,rule1)

	
('36', "0'") ('36', "0'", 'R')
('36', "1'") ('36', "1'", 'R')
('36', '0') ('halt', '0', '')
('36', '1') ('halt', '0', '')
('36', 'D') ('halt', None, '')
('37', "0'") ('37', "0'", 'R')
('37', "1'") ('37', "1'", 'R')
('37', '0') ('halt', '1', '')
('37', '1') ('halt', '1', '')
('37', 'D') ('halt', None, '')
('40', '0') ('40R', "0'", 'R')
('40', '1') ('40R', "1'", 'R')
('40', "0'") ('40', "0'", 'R')
('40', "1'") ('40', "1'", 'R')
('40', 'B') ('40L', None, 'L')
('44', '0') ('44', '0', 'R')
('44', '1') ('44', '0', 'R')
('44', "0'") ('44', '0', 'R')
('44', "1'") ('44', '0', 'R')
('44', 'S') ('44L', None, 'L')
('45', '0') ('45', '1', 'R')
('45', '1') ('45', '1', 'R')
('45', "0'") ('45', '1', 'R')
('45', "1'") ('45', '1', 'R')
('45', 'S') ('45L', None, 'L')
('48', '0') ('48', "0'", 'R')
('48', '1') ('48L', "1'", 'L')
('48', "0'") ('48', "0'", 'R')
('48', "1'") ('48', "1'", 'R')
('48', 'B') ('48L', None, 'L')
('52', '0') ('52', '0', 'R')
('52', '1') ('52', '1', 'R')
('52', "0'") ('52', '0', 'R')
('52', "1'") ('52', '1', 'R')
('52', 'B') ('52R', None, 'R')
('53', '0') ('53', '0', 'R')
('53', '1') ('53', '1', 'R')
('53', "0'") ('53', '0', 'R')
('53', "1'") ('53', '1', 'R')
('53', 'B') ('53R', None, 'R')
('56', '0') ('56L', "0'", 'L')
('56', '1') ('56L', "1'", 'L')
('56', "0'") ('56', "0'", 'R')
('56', "1'") ('56', "1'", 'R')
('56', 'S') ('56L', None, 'L')
('57', '0') ('57L', "0'", 'L')
('57', '1') ('57L', "1'", 'L')
('57', "0'") ('57', "0'", 'R')
('57', "1'") ('57', "1'", 'R')
('57', 'S') ('57L', None, 'L')
('60', '0') ('60R', "0'", 'R')
('60', '1') ('60R', "1'", 'R')
('60', "0'") ('60', "0'", 'R')
('60', "1'") ('60', "1'", 'R')
('60', 'A') ('60R', None, 'R')
('61', '0') ('61R', "1'", 'R')
('61', '1') ('61R', "0'", 'R')
('61', "0'") ('61', "0'", 'R')
('61', "1'") ('61', "1'", 'R')
('61', 'A') ('61R', None, 'R')
('62', '0') ('62R', "0'", 'R')
('62', '1') ('62R', "1'", 'R')
('62', "0'") ('62', "0'", 'R')
('62', "1'") ('62', "1'", 'R')
('62', 'A') ('62R', None, 'R')
('68', '0') ('68', '0', 'R')
('68', '1') ('68', '1', 'R')
('68', "0'") ('68', '0', 'R')
('68', "1'") ('68', '1', 'R')
('68', 'S') ('68L', None, 'L')
('69', '0') ('69', '0', 'R')
('69', '1') ('69', '1', 'R')
('69', "0'") ('69', '0', 'R')
('69', "1'") ('69', '1', 'R')
('69', 'S') ('69L', None, 'L')
('72', '0') ('72', '0', 'R')
('72', '1') ('72', '1', 'R')
('72', "0'") ('72', '0', 'R')
('72', "1'") ('72', '1', 'R')
('72', 'A') ('72R', None, 'R')
('73', '0') ('73', '0', 'R')
('73', '1') ('73', '1', 'R')
('73', "0'") ('73', '0', 'R')
('73', "1'") ('73', '1', 'R')
('73', 'A') ('73', None, 'R')
('36R', None) ('36R', None, 'R')
('36R', 'S') ('36', None, 1)
('37R', None) ('37R', None, 'R')
('37R', 'S') ('37', None, 1)
('44R', None) ('44R', None, 'R')
('44R', 'B') ('44', None, 1)
('56R', None) ('56R', None, 'R')
('56R', 'B') ('56', None, 1)
('52L', None) ('52L', None, 'L')
('52L', 'A') ('52', None, 1)
('40L', None) ('40L', None, 'L')
('40L', 'A') ('40', None, 1)
('48L', None) ('48L', None, 'L')
('48L', 'A') ('48', None, 1)
('53L', None) ('53L', None, 'L')
('53L', 'A') ('53', None, 1)
('60L', None) ('60L', None, 'L')
('60L', 'D') ('60', None, 1)
('61L', None) ('61L', None, 'L')
('61L', 'D') ('61', None, 1)
('68R', None) ('68R', None, 'R')
('68R', 'B') ('68', None, 1)
('68L', None) ('68L', None, 'L')
('68L', 'B') ('68', None, 1)
('62L', None) ('62L', None, 'L')
('62L', 'D') ('62', None, 1)
('69R', None) ('69R', None, 'R')
('69R', 'B') ('69', None, 1)
('69L', None) ('69L', None, 'L')
('69L', 'B') ('69', None, 1)
('57R', None) ('57R', None, 'R')
('57R', 'B') ('57', None, 1)
('72L', None) ('72L', None, 'L')
('72L', 'D') ('72', None, 1)
('73L', None) ('73L', None, 'L')
('73L', 'D') ('73', None, 1)
>>> quasis[0]
End(is_start=True, next_quasis=[40])
>>> quasis[40]
State(instruction=6, acc=0, transitions={'0': ["0'", 0, 44], '1': ["1'", 0, 56], "0'": ["0'", 0, 40], "1'": ["1'", 0, 40], Sym('A'+1): [None, 0, 52]}, direction=1)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
Traceback (most recent call last):
  File "<pyshell#978>", line 1, in <module>
    compile_function('TEST',order=['D','A','B','S'])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 781, in compile_function
    states2rules(order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 823, in states2rules
    add_initial(order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 818, in add_initial
    directions[initial] = {(next_var,sign2char(next_var))}
NameError: name 'initial' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
>>> for rule0,rule1 in rules.items():
	print(rule0,rule1)

	
('36', "0'") ('36', "0'", 'R')
('36', "1'") ('36', "1'", 'R')
('36', '0') ('halt', '0', '')
('36', '1') ('halt', '0', '')
('36', 'D') ('halt', None, '')
('37', "0'") ('37', "0'", 'R')
('37', "1'") ('37', "1'", 'R')
('37', '0') ('halt', '1', '')
('37', '1') ('halt', '1', '')
('37', 'D') ('halt', None, '')
('40', '0') ('40R', "0'", 'R')
('40', '1') ('40R', "1'", 'R')
('40', "0'") ('40', "0'", 'R')
('40', "1'") ('40', "1'", 'R')
('40', 'B') ('40L', None, 'L')
('44', '0') ('44', '0', 'R')
('44', '1') ('44', '0', 'R')
('44', "0'") ('44', '0', 'R')
('44', "1'") ('44', '0', 'R')
('44', 'S') ('44L', None, 'L')
('45', '0') ('45', '1', 'R')
('45', '1') ('45', '1', 'R')
('45', "0'") ('45', '1', 'R')
('45', "1'") ('45', '1', 'R')
('45', 'S') ('45L', None, 'L')
('48', '0') ('48', "0'", 'R')
('48', '1') ('48L', "1'", 'L')
('48', "0'") ('48', "0'", 'R')
('48', "1'") ('48', "1'", 'R')
('48', 'B') ('48L', None, 'L')
('52', '0') ('52', '0', 'R')
('52', '1') ('52', '1', 'R')
('52', "0'") ('52', '0', 'R')
('52', "1'") ('52', '1', 'R')
('52', 'B') ('52R', None, 'R')
('53', '0') ('53', '0', 'R')
('53', '1') ('53', '1', 'R')
('53', "0'") ('53', '0', 'R')
('53', "1'") ('53', '1', 'R')
('53', 'B') ('53R', None, 'R')
('56', '0') ('56L', "0'", 'L')
('56', '1') ('56L', "1'", 'L')
('56', "0'") ('56', "0'", 'R')
('56', "1'") ('56', "1'", 'R')
('56', 'S') ('56L', None, 'L')
('57', '0') ('57L', "0'", 'L')
('57', '1') ('57L', "1'", 'L')
('57', "0'") ('57', "0'", 'R')
('57', "1'") ('57', "1'", 'R')
('57', 'S') ('57L', None, 'L')
('60', '0') ('60R', "0'", 'R')
('60', '1') ('60R', "1'", 'R')
('60', "0'") ('60', "0'", 'R')
('60', "1'") ('60', "1'", 'R')
('60', 'A') ('60R', None, 'R')
('61', '0') ('61R', "1'", 'R')
('61', '1') ('61R', "0'", 'R')
('61', "0'") ('61', "0'", 'R')
('61', "1'") ('61', "1'", 'R')
('61', 'A') ('61R', None, 'R')
('62', '0') ('62R', "0'", 'R')
('62', '1') ('62R', "1'", 'R')
('62', "0'") ('62', "0'", 'R')
('62', "1'") ('62', "1'", 'R')
('62', 'A') ('62R', None, 'R')
('68', '0') ('68', '0', 'R')
('68', '1') ('68', '1', 'R')
('68', "0'") ('68', '0', 'R')
('68', "1'") ('68', '1', 'R')
('68', 'S') ('68L', None, 'L')
('69', '0') ('69', '0', 'R')
('69', '1') ('69', '1', 'R')
('69', "0'") ('69', '0', 'R')
('69', "1'") ('69', '1', 'R')
('69', 'S') ('69L', None, 'L')
('72', '0') ('72', '0', 'R')
('72', '1') ('72', '1', 'R')
('72', "0'") ('72', '0', 'R')
('72', "1'") ('72', '1', 'R')
('72', 'A') ('72R', None, 'R')
('73', '0') ('73', '0', 'R')
('73', '1') ('73', '1', 'R')
('73', "0'") ('73', '0', 'R')
('73', "1'") ('73', '1', 'R')
('73', 'A') ('73', None, 'R')
('40R', None) ('40R', None, 'R')
('40R', 'A') ('40', None, 1)
('40L', None) ('40L', None, 'L')
('40L', 'A') ('40', None, 1)
('36R', None) ('36R', None, 'R')
('36R', 'S') ('36', None, 1)
('37R', None) ('37R', None, 'R')
('37R', 'S') ('37', None, 1)
('44R', None) ('44R', None, 'R')
('44R', 'B') ('44', None, 1)
('56R', None) ('56R', None, 'R')
('56R', 'B') ('56', None, 1)
('52L', None) ('52L', None, 'L')
('52L', 'A') ('52', None, 1)
('48L', None) ('48L', None, 'L')
('48L', 'A') ('48', None, 1)
('53L', None) ('53L', None, 'L')
('53L', 'A') ('53', None, 1)
('60L', None) ('60L', None, 'L')
('60L', 'D') ('60', None, 1)
('61L', None) ('61L', None, 'L')
('61L', 'D') ('61', None, 1)
('68L', None) ('68L', None, 'L')
('68L', 'B') ('68', None, 1)
('68R', None) ('68R', None, 'R')
('68R', 'B') ('68', None, 1)
('62L', None) ('62L', None, 'L')
('62L', 'D') ('62', None, 1)
('69L', None) ('69L', None, 'L')
('69L', 'B') ('69', None, 1)
('69R', None) ('69R', None, 'R')
('69R', 'B') ('69', None, 1)
('57R', None) ('57R', None, 'R')
('57R', 'B') ('57', None, 1)
('72L', None) ('72L', None, 'L')
('72L', 'D') ('72', None, 1)
('73L', None) ('73L', None, 'L')
('73L', 'D') ('73', None, 1)
>>> import itertools
>>> for perm in itertools.permutations('ABC'):
	print(perm)

	
('A', 'B', 'C')
('A', 'C', 'B')
('B', 'A', 'C')
('B', 'C', 'A')
('C', 'A', 'B')
('C', 'B', 'A')
>>> for perm in itertools.permutations('ABC'):
	print(''.join(perm))

	
ABC
ACB
BAC
BCA
CAB
CBA
>>> for perm in itertools.permutations('ABC'):
	s1 = ''.join(perm)
	for k in range(len(s1))
	
SyntaxError: invalid syntax
>>> for perm in itertools.permutations('ABC'):
	s1 = ''.join(perm)
	for k in range(len(s1)):
		for j in range(k+1,len(s1)):
	s2 = list(perm)
	
SyntaxError: expected an indented block
>>> for perm in itertools.permutations('ABC'):
	s1 = ''.join(perm)
	for k in range(len(s1)):
		for j in range(k+1,len(s1)):
			s2 = list(perm)
			s2[k],s2[j]=s2[j],s2[k]
			print(s1,''.join(s2))

			
ABC BAC
ABC CBA
ABC ACB
ACB CAB
ACB BCA
ACB ABC
BAC ABC
BAC CAB
BAC BCA
BCA CBA
BCA ACB
BCA BAC
CAB ACB
CAB BAC
CAB CBA
CBA BCA
CBA ABC
CBA CAB
>>> for perm in itertools.permutations('ABCD'):
	s1 = ''.join(perm)
	for k in range(len(s1)):
		for j in range(k+1,len(s1)):
			s2 = list(perm)
			s2[k],s2[j]=s2[j],s2[k]
			print(s1,''.join(s2))

			
ABCD BACD
ABCD CBAD
ABCD DBCA
ABCD ACBD
ABCD ADCB
ABCD ABDC
ABDC BADC
ABDC DBAC
ABDC CBDA
ABDC ADBC
ABDC ACDB
ABDC ABCD
ACBD CABD
ACBD BCAD
ACBD DCBA
ACBD ABCD
ACBD ADBC
ACBD ACDB
ACDB CADB
ACDB DCAB
ACDB BCDA
ACDB ADCB
ACDB ABDC
ACDB ACBD
ADBC DABC
ADBC BDAC
ADBC CDBA
ADBC ABDC
ADBC ACBD
ADBC ADCB
ADCB DACB
ADCB CDAB
ADCB BDCA
ADCB ACDB
ADCB ABCD
ADCB ADBC
BACD ABCD
BACD CABD
BACD DACB
BACD BCAD
BACD BDCA
BACD BADC
BADC ABDC
BADC DABC
BADC CADB
BADC BDAC
BADC BCDA
BADC BACD
BCAD CBAD
BCAD ACBD
BCAD DCAB
BCAD BACD
BCAD BDAC
BCAD BCDA
BCDA CBDA
BCDA DCBA
BCDA ACDB
BCDA BDCA
BCDA BADC
BCDA BCAD
BDAC DBAC
BDAC ADBC
BDAC CDAB
BDAC BADC
BDAC BCAD
BDAC BDCA
BDCA DBCA
BDCA CDBA
BDCA ADCB
BDCA BCDA
BDCA BACD
BDCA BDAC
CABD ACBD
CABD BACD
CABD DABC
CABD CBAD
CABD CDBA
CABD CADB
CADB ACDB
CADB DACB
CADB BADC
CADB CDAB
CADB CBDA
CADB CABD
CBAD BCAD
CBAD ABCD
CBAD DBAC
CBAD CABD
CBAD CDAB
CBAD CBDA
CBDA BCDA
CBDA DBCA
CBDA ABDC
CBDA CDBA
CBDA CADB
CBDA CBAD
CDAB DCAB
CDAB ADCB
CDAB BDAC
CDAB CADB
CDAB CBAD
CDAB CDBA
CDBA DCBA
CDBA BDCA
CDBA ADBC
CDBA CBDA
CDBA CABD
CDBA CDAB
DABC ADBC
DABC BADC
DABC CABD
DABC DBAC
DABC DCBA
DABC DACB
DACB ADCB
DACB CADB
DACB BACD
DACB DCAB
DACB DBCA
DACB DABC
DBAC BDAC
DBAC ABDC
DBAC CBAD
DBAC DABC
DBAC DCAB
DBAC DBCA
DBCA BDCA
DBCA CBDA
DBCA ABCD
DBCA DCBA
DBCA DACB
DBCA DBAC
DCAB CDAB
DCAB ACDB
DCAB BCAD
DCAB DACB
DCAB DBAC
DCAB DCBA
DCBA CDBA
DCBA BCDA
DCBA ACBD
DCBA DBCA
DCBA DABC
DCBA DCAB
>>> import networkx
Traceback (most recent call last):
  File "<pyshell#999>", line 1, in <module>
    import networkx
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\networkx\__init__.py", line 114, in <module>
    import networkx.generators
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\networkx\generators\__init__.py", line 13, in <module>
    from networkx.generators.geometric import *
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\networkx\generators\geometric.py", line 25, in <module>
    from scipy.spatial import cKDTree as KDTree
  File "C:\Users\joshm\AppData\Roaming\Python\Python37\site-packages\scipy\spatial\__init__.py", line 97, in <module>
    from ._spherical_voronoi import SphericalVoronoi
  File "C:\Users\joshm\AppData\Roaming\Python\Python37\site-packages\scipy\spatial\_spherical_voronoi.py", line 19, in <module>
    from scipy.spatial.distance import pdist
  File "C:\Users\joshm\AppData\Roaming\Python\Python37\site-packages\scipy\spatial\distance.py", line 123, in <module>
    from ..linalg import norm
  File "C:\Users\joshm\AppData\Roaming\Python\Python37\site-packages\scipy\linalg\__init__.py", line 191, in <module>
    from .basic import *
  File "C:\Users\joshm\AppData\Roaming\Python\Python37\site-packages\scipy\linalg\basic.py", line 15, in <module>
    from .decomp import _asarray_validated
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 967, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 677, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 724, in exec_module
  File "<frozen importlib._bootstrap_external>", line 818, in get_code
  File "<frozen importlib._bootstrap_external>", line 916, in get_data
KeyboardInterrupt
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
Traceback (most recent call last):
  File "<pyshell#1000>", line 1, in <module>
    compile_function('TEST',order=['D','A','B','S'])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 518, in compile_function
    more_pres = apply_pres()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 439, in apply_pres
    replace_links(k,instr.next_quasis[0])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 364, in replace_links
    if type(quasi) in [Instruction,Step,End] and quasi.next_quasis:
NameError: name 'Step' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
Traceback (most recent call last):
  File "<pyshell#1001>", line 1, in <module>
    compile_function('TEST',order=['D','A','B','S'])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 528, in compile_function
    states2rules(order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 579, in states2rules
    if not transition[2] in direction_table:  ########
NameError: name 'direction_table' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST',order=['D','A','B','S'])
>>> len(directions_table)
17
>>> directions_table
{36: [(Sym('S'+0.0), Sym('S'+0)), (Sym('S'+0.0), Sym('S'+0)), (Sym('A'+1), Sym('S'+0))], 37: [(Sym('S'+0.0), Sym('S'+0)), (Sym('S'+0.0), Sym('S'+0)), (Sym('A'+1), Sym('S'+0))], 44: [(Sym('A'+0.5), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('D'+1), Sym('B'+0))], 56: [(Sym('A'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0))], 52: [(Sym('A'+1), Sym('A'+0)), (Sym('A'+1), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0))], 45: [(Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0))], 40: [(Sym('B'+1), Sym('A'+0))], 48: [(Sym('B'+1), Sym('A'+0))], 53: [(Sym('A'+0.5), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('D'+1), Sym('A'+0))], 60: [(Sym('B'+0.5), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))], 61: [(Sym('B'+0.5), Sym('D'+0)), (Sym('B'+0.5), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))], 68: [(Sym('B'+1), Sym('B'+0)), (Sym('D'+1), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0))], 62: [(Sym('B'+0.5), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))], 69: [(Sym('B'+1), Sym('B'+0)), (Sym('D'+1), Sym('B'+0)), (Sym('D'+1), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0))], 57: [(Sym('D'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0))], 72: [(Sym('B'+1), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))], 73: [(Sym('B'+1), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))]}
>>> for k,value in directions_table.items():
	print(k,value)

	
36 [(Sym('S'+0.0), Sym('S'+0)), (Sym('S'+0.0), Sym('S'+0)), (Sym('A'+1), Sym('S'+0))]
37 [(Sym('S'+0.0), Sym('S'+0)), (Sym('S'+0.0), Sym('S'+0)), (Sym('A'+1), Sym('S'+0))]
44 [(Sym('A'+0.5), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('D'+1), Sym('B'+0))]
56 [(Sym('A'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0))]
52 [(Sym('A'+1), Sym('A'+0)), (Sym('A'+1), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0))]
45 [(Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0))]
40 [(Sym('B'+1), Sym('A'+0))]
48 [(Sym('B'+1), Sym('A'+0))]
53 [(Sym('A'+0.5), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('D'+1), Sym('A'+0))]
60 [(Sym('B'+0.5), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))]
61 [(Sym('B'+0.5), Sym('D'+0)), (Sym('B'+0.5), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))]
68 [(Sym('B'+1), Sym('B'+0)), (Sym('D'+1), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0))]
62 [(Sym('B'+0.5), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))]
69 [(Sym('B'+1), Sym('B'+0)), (Sym('D'+1), Sym('B'+0)), (Sym('D'+1), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0))]
57 [(Sym('D'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0))]
72 [(Sym('B'+1), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))]
73 [(Sym('B'+1), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))]
>>> for k,value in directions_table.items():
	print(k,{pair[0] for pair in value})

	
36 {Sym('A'+1), Sym('S'+0.0)}
37 {Sym('A'+1), Sym('S'+0.0)}
44 {Sym('B'+0.0), Sym('A'+0.5), Sym('D'+1)}
56 {Sym('D'+0.5), Sym('A'+0.5)}
52 {Sym('A'+0.0), Sym('A'+1)}
45 {Sym('B'+0.0)}
40 {Sym('B'+1)}
48 {Sym('B'+1)}
53 {Sym('A'+0.5), Sym('D'+1), Sym('A'+0.0)}
60 {Sym('B'+0.5), Sym('D'+0.0)}
61 {Sym('B'+0.5), Sym('D'+0.0)}
68 {Sym('B'+0.0), Sym('B'+1), Sym('D'+1)}
62 {Sym('B'+0.5), Sym('D'+0.0)}
69 {Sym('B'+0.0), Sym('B'+1), Sym('D'+1)}
57 {Sym('D'+0.5)}
72 {Sym('D'+0.0), Sym('B'+1)}
73 {Sym('D'+0.0), Sym('B'+1)}
>>> for k,value in directions_table.items():
	print(k,{pair[1] for pair in value})

	
36 {Sym('S'+0)}
37 {Sym('S'+0)}
44 {Sym('B'+0)}
56 {Sym('B'+0)}
52 {Sym('A'+0)}
45 {Sym('B'+0)}
40 {Sym('A'+0)}
48 {Sym('A'+0)}
53 {Sym('A'+0)}
60 {Sym('D'+0)}
61 {Sym('D'+0)}
68 {Sym('B'+0)}
62 {Sym('D'+0)}
69 {Sym('B'+0)}
57 {Sym('B'+0)}
72 {Sym('D'+0)}
73 {Sym('D'+0)}
>>> for k,value in directions_table.items():
	print({pair[1] for pair in value},{pair[0] for pair in value})

	
{Sym('S'+0)} {Sym('A'+1), Sym('S'+0.0)}
{Sym('S'+0)} {Sym('A'+1), Sym('S'+0.0)}
{Sym('B'+0)} {Sym('B'+0.0), Sym('A'+0.5), Sym('D'+1)}
{Sym('B'+0)} {Sym('D'+0.5), Sym('A'+0.5)}
{Sym('A'+0)} {Sym('A'+0.0), Sym('A'+1)}
{Sym('B'+0)} {Sym('B'+0.0)}
{Sym('A'+0)} {Sym('B'+1)}
{Sym('A'+0)} {Sym('B'+1)}
{Sym('A'+0)} {Sym('A'+0.5), Sym('D'+1), Sym('A'+0.0)}
{Sym('D'+0)} {Sym('B'+0.5), Sym('D'+0.0)}
{Sym('D'+0)} {Sym('B'+0.5), Sym('D'+0.0)}
{Sym('B'+0)} {Sym('B'+0.0), Sym('B'+1), Sym('D'+1)}
{Sym('D'+0)} {Sym('B'+0.5), Sym('D'+0.0)}
{Sym('B'+0)} {Sym('B'+0.0), Sym('B'+1), Sym('D'+1)}
{Sym('B'+0)} {Sym('D'+0.5)}
{Sym('D'+0)} {Sym('D'+0.0), Sym('B'+1)}
{Sym('D'+0)} {Sym('D'+0.0), Sym('B'+1)}
>>> counts = {}
>>> for k,value in directions_table.items():
	something = {pair[1] for pair in value},{pair[0] for pair in value}
	if not something in counts:
		counts[something]=0
	counts[something] += 1

	
Traceback (most recent call last):
  File "<pyshell#1016>", line 3, in <module>
    if not something in counts:
TypeError: unhashable type: 'set'
>>> for k,value in directions_table.items():
	something = str(({pair[1] for pair in value},{pair[0] for pair in value}))
	if not something in counts:
		counts[something]=0
	counts[something] += 1

	
>>> counts = {}
>>> for k,value in directions_table.items():
	something = str(({pair[1] for pair in value},{pair[0] for pair in value}))
	if not something in counts:
		counts[something]=0
	counts[something] += 1

	
>>> counts
{"({Sym('S'+0)}, {Sym('A'+1), Sym('S'+0.0)})": 2, "({Sym('B'+0)}, {Sym('B'+0.0), Sym('A'+0.5), Sym('D'+1)})": 1, "({Sym('B'+0)}, {Sym('D'+0.5), Sym('A'+0.5)})": 1, "({Sym('A'+0)}, {Sym('A'+0.0), Sym('A'+1)})": 1, "({Sym('B'+0)}, {Sym('B'+0.0)})": 1, "({Sym('A'+0)}, {Sym('B'+1)})": 2, "({Sym('A'+0)}, {Sym('A'+0.5), Sym('D'+1), Sym('A'+0.0)})": 1, "({Sym('D'+0)}, {Sym('B'+0.5), Sym('D'+0.0)})": 3, "({Sym('B'+0)}, {Sym('B'+0.0), Sym('B'+1), Sym('D'+1)})": 2, "({Sym('B'+0)}, {Sym('D'+0.5)})": 1, "({Sym('D'+0)}, {Sym('D'+0.0), Sym('B'+1)})": 2}
>>> for k in counts:
	print(k,counts[k])

	
({Sym('S'+0)}, {Sym('A'+1), Sym('S'+0.0)}) 2
({Sym('B'+0)}, {Sym('B'+0.0), Sym('A'+0.5), Sym('D'+1)}) 1
({Sym('B'+0)}, {Sym('D'+0.5), Sym('A'+0.5)}) 1
({Sym('A'+0)}, {Sym('A'+0.0), Sym('A'+1)}) 1
({Sym('B'+0)}, {Sym('B'+0.0)}) 1
({Sym('A'+0)}, {Sym('B'+1)}) 2
({Sym('A'+0)}, {Sym('A'+0.5), Sym('D'+1), Sym('A'+0.0)}) 1
({Sym('D'+0)}, {Sym('B'+0.5), Sym('D'+0.0)}) 3
({Sym('B'+0)}, {Sym('B'+0.0), Sym('B'+1), Sym('D'+1)}) 2
({Sym('B'+0)}, {Sym('D'+0.5)}) 1
({Sym('D'+0)}, {Sym('D'+0.0), Sym('B'+1)}) 2
>>> for k in counts:
	print(counts[k],k)

	
2 ({Sym('S'+0)}, {Sym('A'+1), Sym('S'+0.0)})
1 ({Sym('B'+0)}, {Sym('B'+0.0), Sym('A'+0.5), Sym('D'+1)})
1 ({Sym('B'+0)}, {Sym('D'+0.5), Sym('A'+0.5)})
1 ({Sym('A'+0)}, {Sym('A'+0.0), Sym('A'+1)})
1 ({Sym('B'+0)}, {Sym('B'+0.0)})
2 ({Sym('A'+0)}, {Sym('B'+1)})
1 ({Sym('A'+0)}, {Sym('A'+0.5), Sym('D'+1), Sym('A'+0.0)})
3 ({Sym('D'+0)}, {Sym('B'+0.5), Sym('D'+0.0)})
2 ({Sym('B'+0)}, {Sym('B'+0.0), Sym('B'+1), Sym('D'+1)})
1 ({Sym('B'+0)}, {Sym('D'+0.5)})
2 ({Sym('D'+0)}, {Sym('D'+0.0), Sym('B'+1)})
>>> counts
{"({Sym('S'+0)}, {Sym('A'+1), Sym('S'+0.0)})": 2, "({Sym('B'+0)}, {Sym('B'+0.0), Sym('A'+0.5), Sym('D'+1)})": 1, "({Sym('B'+0)}, {Sym('D'+0.5), Sym('A'+0.5)})": 1, "({Sym('A'+0)}, {Sym('A'+0.0), Sym('A'+1)})": 1, "({Sym('B'+0)}, {Sym('B'+0.0)})": 1, "({Sym('A'+0)}, {Sym('B'+1)})": 2, "({Sym('A'+0)}, {Sym('A'+0.5), Sym('D'+1), Sym('A'+0.0)})": 1, "({Sym('D'+0)}, {Sym('B'+0.5), Sym('D'+0.0)})": 3, "({Sym('B'+0)}, {Sym('B'+0.0), Sym('B'+1), Sym('D'+1)})": 2, "({Sym('B'+0)}, {Sym('D'+0.5)})": 1, "({Sym('D'+0)}, {Sym('D'+0.0), Sym('B'+1)})": 2}
>>> counts[0]
Traceback (most recent call last):
  File "<pyshell#1029>", line 1, in <module>
    counts[0]
KeyError: 0
>>> def score(item,order):
	points = item[0]
	sym_to = next(item[1][0])
	syms_from = item[1][1]
	left = False
	right = False
	for sym_from in syms_from:
		if order.index(sym_from)
		
SyntaxError: invalid syntax
def score(item,order):
	points = item[0]
	sym_to = next(item[1][0])
	syms_from = item[1][1]
	left = False
	right = False
	for sym_from in syms_from:
		if order.index(sym_from)
>>> next({1})
Traceback (most recent call last):
  File "<pyshell#1038>", line 1, in <module>
    next({1})
TypeError: 'set' object is not an iterator
>>> list({1})[0]
1
>>> def score(counts,order):
	total = 0
	for points,symbols in counts.items()
		sym_to = list(symbols[0])[0]
		syms_from = symbols[1]
		left = False
		right = False
		for sym_from in syms_from:
			offset = (order.index(sym_to.symbol)+sym_to.offset) - (order.index(sym_from.symbol)+sym_from.offset)
			if offset<0:
				left = True
			if offset>0:
				right = True
				
SyntaxError: invalid syntax
>>> def score(counts,order):
	total = 0
	for points,symbols in counts.items():
		sym_to = list(symbols[0])[0]
		syms_from = symbols[1]
		left = False
		right = False
		for sym_from in syms_from:
			offset = (order.index(sym_to.symbol)+sym_to.offset) - (order.index(sym_from.symbol)+sym_from.offset)
			if offset<0:
				left = True
			if offset>0:
				right = True
		total += points*(left+right)
	return total

>>> score(counts,['B','D','A','S'])
Traceback (most recent call last):
  File "<pyshell#1049>", line 1, in <module>
    score(counts,['B','D','A','S'])
  File "<pyshell#1048>", line 4, in score
    sym_to = list(symbols[0])[0]
TypeError: 'int' object is not subscriptable
>>> item = list(counts.items())[0]
>>> points,symbols = list(counts.items())[0]
>>> points
"({Sym('S'+0)}, {Sym('A'+1), Sym('S'+0.0)})"
>>> symbols
2
>>> def score(counts,order):
	total = 0
	for symbols,points in counts.items():
		sym_to = list(symbols[0])[0]
		syms_from = symbols[1]
		left = False
		right = False
		for sym_from in syms_from:
			offset = (order.index(sym_to.symbol)+sym_to.offset) - (order.index(sym_from.symbol)+sym_from.offset)
			if offset<0:
				left = True
			if offset>0:
				right = True
		total += points*(left+right)
	return total

>>> score(counts,['B','D','A','S'])
Traceback (most recent call last):
  File "<pyshell#1056>", line 1, in <module>
    score(counts,['B','D','A','S'])
  File "<pyshell#1055>", line 9, in score
    offset = (order.index(sym_to.symbol)+sym_to.offset) - (order.index(sym_from.symbol)+sym_from.offset)
AttributeError: 'str' object has no attribute 'symbol'
>>> def score(counts,order):
	total = 0
	for symbols,points in counts.items():
		sym_to = list(symbols[0])[0]
		syms_from = symbols[1]
		left = False
		right = False
		for sym_from in syms_from:
			print(sym_to,sym_from)
			offset = (order.index(sym_to.symbol)+sym_to.offset) - (order.index(sym_from.symbol)+sym_from.offset)
			if offset<0:
				left = True
			if offset>0:
				right = True
		total += points*(left+right)
	return total

>>> score(counts,['B','D','A','S'])
(
 {
Traceback (most recent call last):
  File "<pyshell#1059>", line 1, in <module>
    score(counts,['B','D','A','S'])
  File "<pyshell#1058>", line 10, in score
    offset = (order.index(sym_to.symbol)+sym_to.offset) - (order.index(sym_from.symbol)+sym_from.offset)
AttributeError: 'str' object has no attribute 'symbol'
>>> a = dict()
>>> a = {[1]:1}
Traceback (most recent call last):
  File "<pyshell#1061>", line 1, in <module>
    a = {[1]:1}
TypeError: unhashable type: 'list'
>>> a = {(1):1}
>>> a = {(1,2):1}
>>> counts = {}
>>> for k,value in directions_table.items():
	something = tuple({pair[1] for pair in value}),tuple(sorted({pair[0] for pair in value}))
	if not something in counts:
		counts[something]=0
	counts[something] += 1

Traceback (most recent call last):
  File "<pyshell#1066>", line 2, in <module>
    something = tuple({pair[1] for pair in value}),tuple(sorted({pair[0] for pair in value}))
TypeError: '<' not supported between instances of 'Symbol' and 'Symbol'
>>> for k,value in directions_table.items():
	something = tuple({pair[1] for pair in value}),tuple({pair[0] for pair in value})
	if not something in counts:
		counts[something]=0
	counts[something] += 1

>>> counts
{((Sym('S'+0),), (Sym('A'+1), Sym('S'+0.0))): 2, ((Sym('B'+0),), (Sym('B'+0.0), Sym('A'+0.5), Sym('D'+1))): 1, ((Sym('B'+0),), (Sym('D'+0.5), Sym('A'+0.5))): 1, ((Sym('A'+0),), (Sym('A'+0.0), Sym('A'+1))): 1, ((Sym('B'+0),), (Sym('B'+0.0),)): 1, ((Sym('A'+0),), (Sym('B'+1),)): 2, ((Sym('A'+0),), (Sym('A'+0.5), Sym('D'+1), Sym('A'+0.0))): 1, ((Sym('D'+0),), (Sym('B'+0.5), Sym('D'+0.0))): 3, ((Sym('B'+0),), (Sym('B'+0.0), Sym('B'+1), Sym('D'+1))): 2, ((Sym('B'+0),), (Sym('D'+0.5),)): 1, ((Sym('D'+0),), (Sym('D'+0.0), Sym('B'+1))): 2}
>>> for k in counts:
	print(counts[k],k)

2 ((Sym('S'+0),), (Sym('A'+1), Sym('S'+0.0)))
1 ((Sym('B'+0),), (Sym('B'+0.0), Sym('A'+0.5), Sym('D'+1)))
1 ((Sym('B'+0),), (Sym('D'+0.5), Sym('A'+0.5)))
1 ((Sym('A'+0),), (Sym('A'+0.0), Sym('A'+1)))
1 ((Sym('B'+0),), (Sym('B'+0.0),))
2 ((Sym('A'+0),), (Sym('B'+1),))
1 ((Sym('A'+0),), (Sym('A'+0.5), Sym('D'+1), Sym('A'+0.0)))
3 ((Sym('D'+0),), (Sym('B'+0.5), Sym('D'+0.0)))
2 ((Sym('B'+0),), (Sym('B'+0.0), Sym('B'+1), Sym('D'+1)))
1 ((Sym('B'+0),), (Sym('D'+0.5),))
2 ((Sym('D'+0),), (Sym('D'+0.0), Sym('B'+1)))
>>> score(counts,['B','D','A','S'])
Sym('S'+0) Sym('A'+1)
Sym('S'+0) Sym('S'+0.0)
Sym('B'+0) Sym('B'+0.0)
Sym('B'+0) Sym('A'+0.5)
Sym('B'+0) Sym('D'+1)
Sym('B'+0) Sym('D'+0.5)
Sym('B'+0) Sym('A'+0.5)
Sym('A'+0) Sym('A'+0.0)
Sym('A'+0) Sym('A'+1)
Sym('B'+0) Sym('B'+0.0)
Sym('A'+0) Sym('B'+1)
Sym('A'+0) Sym('A'+0.5)
Sym('A'+0) Sym('D'+1)
Sym('A'+0) Sym('A'+0.0)
Sym('D'+0) Sym('B'+0.5)
Sym('D'+0) Sym('D'+0.0)
Sym('B'+0) Sym('B'+0.0)
Sym('B'+0) Sym('B'+1)
Sym('B'+0) Sym('D'+1)
Sym('B'+0) Sym('D'+0.5)
Sym('D'+0) Sym('D'+0.0)
Sym('D'+0) Sym('B'+1)
12
>>> def score(counts,order):
	total = 0
	for symbols,points in counts.items():
		sym_to = list(symbols[0])[0]
		syms_from = symbols[1]
		left = False
		right = False
		for sym_from in syms_from:
			offset = (order.index(sym_to.symbol)+sym_to.offset) - (order.index(sym_from.symbol)+sym_from.offset)
			if offset<0:
				left = True
			if offset>0:
				right = True
		total += points*(left+right)
	return total

>>> score(counts,['B','D','A','S'])
12
>>> import itertools
>>> ('A','B','C').index('B')
1
>>> ('A','B','C').index('C')
2
>>> best_order = ['A','B','S','D']
>>> itertools.perm
Traceback (most recent call last):
  File "<pyshell#1080>", line 1, in <module>
    itertools.perm
AttributeError: module 'itertools' has no attribute 'perm'
>>> itertools.permutate
Traceback (most recent call last):
  File "<pyshell#1081>", line 1, in <module>
    itertools.permutate
AttributeError: module 'itertools' has no attribute 'permutate'
>>> itertools.permutatitions
Traceback (most recent call last):
  File "<pyshell#1082>", line 1, in <module>
    itertools.permutatitions
AttributeError: module 'itertools' has no attribute 'permutatitions'
>>> itertools.permutations
<class 'itertools.permutations'>
>>> for order in itertools.permutations(['A','B','S','D']):
	print(order,score(counts,order))

('A', 'B', 'S', 'D') 18
('A', 'B', 'D', 'S') 16
('A', 'S', 'B', 'D') 14
('A', 'S', 'D', 'B') 14
('A', 'D', 'B', 'S') 16
('A', 'D', 'S', 'B') 18
('B', 'A', 'S', 'D') 12
('B', 'A', 'D', 'S') 14
('B', 'S', 'A', 'D') 16
('B', 'S', 'D', 'A') 16
('B', 'D', 'A', 'S') 12
('B', 'D', 'S', 'A') 15
('S', 'A', 'B', 'D') 16
('S', 'A', 'D', 'B') 16
('S', 'B', 'A', 'D') 14
('S', 'B', 'D', 'A') 14
('S', 'D', 'A', 'B') 18
('S', 'D', 'B', 'A') 16
('D', 'A', 'B', 'S') 18
('D', 'A', 'S', 'B') 16
('D', 'B', 'A', 'S') 14
('D', 'B', 'S', 'A') 18
('D', 'S', 'A', 'B') 19
('D', 'S', 'B', 'A') 19
>>> ('B', 'A', 'S', 'D')
('B', 'A', 'S', 'D')
>>> ('B', 'D', 'A', 'S')
('B', 'D', 'A', 'S')
>>> directions_table
{36: [(Sym('S'+0.0), Sym('S'+0)), (Sym('S'+0.0), Sym('S'+0)), (Sym('A'+1), Sym('S'+0))], 37: [(Sym('S'+0.0), Sym('S'+0)), (Sym('S'+0.0), Sym('S'+0)), (Sym('A'+1), Sym('S'+0))], 44: [(Sym('A'+0.5), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('D'+1), Sym('B'+0))], 56: [(Sym('A'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0))], 52: [(Sym('A'+1), Sym('A'+0)), (Sym('A'+1), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0))], 45: [(Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0))], 40: [(Sym('B'+1), Sym('A'+0))], 48: [(Sym('B'+1), Sym('A'+0))], 53: [(Sym('A'+0.5), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('A'+0.0), Sym('A'+0)), (Sym('D'+1), Sym('A'+0))], 60: [(Sym('B'+0.5), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))], 61: [(Sym('B'+0.5), Sym('D'+0)), (Sym('B'+0.5), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))], 68: [(Sym('B'+1), Sym('B'+0)), (Sym('D'+1), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0))], 62: [(Sym('B'+0.5), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))], 69: [(Sym('B'+1), Sym('B'+0)), (Sym('D'+1), Sym('B'+0)), (Sym('D'+1), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0)), (Sym('B'+0.0), Sym('B'+0))], 57: [(Sym('D'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0)), (Sym('D'+0.5), Sym('B'+0))], 72: [(Sym('B'+1), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))], 73: [(Sym('B'+1), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0)), (Sym('D'+0.0), Sym('D'+0))]}
>>> def states2rules():
    global to_symbols, from_symbols
    to_symbols = {}
    from_symbols = {}
    for k,state in get_quasis([State]):
        if k in used_states:
            instruction = quasis[state.instruction]
            to_symbols[k] = Symbol(instruction.vard,int(state.direction<0)) 
            for symbol,transition,next_state in get_quasis_from(state,[State]):
                next_instruction = quasis[next_state.instruction]
                if not (adjacent_bits(instruction,next_instruction)):
                    if type(symbol)==Symbol:
                        current_loc = symbol
                    else:
                        current_loc = Symbol(instruction.vard,( 
                            instruction.command in ['LOAD','STORE'] and symbol in ['0','1'] or
                            instruction.command=='SEZ' and symbol=='1')/2)
                    if not transition[2] in from_symbols:
                        from_symbols[transition[2]] = set()
                    from_symbols[transition[2]].add(current_loc)

>>> states2rules()
>>> to_symbols
{36: Sym('S'+0), 37: Sym('S'+0), 40: Sym('A'+0), 44: Sym('B'+0), 45: Sym('B'+0), 48: Sym('A'+0), 52: Sym('A'+0), 53: Sym('A'+0), 56: Sym('B'+0), 57: Sym('B'+0), 60: Sym('D'+0), 61: Sym('D'+0), 62: Sym('D'+0), 68: Sym('B'+0), 69: Sym('B'+0), 72: Sym('D'+0), 73: Sym('D'+0)}
>>> from_symbols
{44: {Sym('B'+0.0), Sym('A'+0.5), Sym('D'+1)}, 56: {Sym('D'+0.5), Sym('A'+0.5)}, 52: {Sym('A'+0.0), Sym('A'+1)}, 45: {Sym('B'+0.0)}, 40: {Sym('B'+1)}, 48: {Sym('B'+1)}, 53: {Sym('A'+0.5), Sym('D'+1), Sym('A'+0.0)}, 36: {Sym('A'+1)}, 37: {Sym('A'+1)}, 60: {Sym('B'+0.5)}, 61: {Sym('B'+0.5)}, 68: {Sym('B'+0.0), Sym('B'+1), Sym('D'+1)}, 62: {Sym('B'+0.5)}, 69: {Sym('B'+0.0), Sym('B'+1), Sym('D'+1)}, 57: {Sym('D'+0.5)}, 72: {Sym('D'+0.0), Sym('B'+1)}, 73: {Sym('D'+0.0), Sym('B'+1)}}
>>> to_symbols.keys()==from_symbols.keys()
True
>>> quasis
[End(is_start=True, next_quasis=[40]), FunctionCall(command='MULTo', args=['D', 'A', 'B'], next_quasis=[6]), Instruction(STORE, vard=S, next_quasis=[3, 3]), End(is_start=False, next_quasis=[None]), End(is_start=True, next_quasis=[6]), None, Instruction(LOADNEXT, vard=A, next_quasis=[7, 19]), Instruction(BRANCH, next_quasis=[12, 22, 22, 22]), None, FunctionCall(command='ADDs', args=['D', 'B'], next_quasis=[22]), Instruction(BRANCH, next_quasis=[12, 19, 12, 12]), None, Instruction(SLLs, vard=B, next_quasis=[13]), Instruction(BRANCH, next_quasis=[6, 15, 15, 15]), None, Instruction(LOADI, next_quasis=[16]), Instruction(LOADNEXT, vard=A, next_quasis=[17, 19]), Instruction(BRANCH, next_quasis=[15, 19, 19, 19]), None, Instruction(UNREAD, vard=A, next_quasis=[2]), End(is_start=False, next_quasis=[2]), End(is_start=True, next_quasis=[22]), Instruction(LOADI, next_quasis=[24]), None, Instruction(LOADNEXT, vard=B, next_quasis=[25, 32]), Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[26]), Instruction(LOAD, vard=D, next_quasis=[27, 32]), Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[29]), Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[0]), Instruction(STORENEXT, vard=D, next_quasis=[30, 32]), Instruction(JUMP, next_quasis=[24]), None, Instruction(MAP, map={(0,): (0,), (1,): (1,), (2,): (1,), (3,): (1,)}, next_quasis=[33]), Instruction(UNREAD, vard=B, next_quasis=[34]), Instruction(UNREAD, vard=D, next_quasis=[10]), End(is_start=False, next_quasis=[10]), State(instruction=2, acc=0, transitions={'0': ['0', 0, 3], '1': ['0', 0, 3], "0'": ["0'", 0, 36], "1'": ["1'", 0, 36], Sym('S'+1): [None, 0, 3]}, direction=1), State(instruction=2, acc=1, transitions={'0': ['1', 1, 3], '1': ['1', 1, 3], "0'": ["0'", 1, 37], "1'": ["1'", 1, 37], Sym('S'+1): [None, 1, 3]}, direction=1), State(instruction=2, acc=2, transitions={'0': ['2', 2, 3], '1': ['2', 2, 3], "0'": ["0'", 2, 38], "1'": ["1'", 2, 38], Sym('S'+1): [None, 2, 3]}, direction=1), State(instruction=2, acc=3, transitions={'0': ['3', 3, 3], '1': ['3', 3, 3], "0'": ["0'", 3, 39], "1'": ["1'", 3, 39], Sym('S'+1): [None, 3, 3]}, direction=1), State(instruction=6, acc=0, transitions={'0': ["0'", 0, 44], '1': ["1'", 0, 56], "0'": ["0'", 0, 40], "1'": ["1'", 0, 40], Sym('A'+1): [None, 0, 52]}, direction=1), State(instruction=6, acc=1, transitions={'0': ["0'", 0, 44], '1': ["1'", 0, 56], "0'": ["0'", 1, 41], "1'": ["1'", 1, 41], Sym('A'+1): [None, 1, 53]}, direction=1), State(instruction=6, acc=2, transitions={'0': ["0'", 0, 44], '1': ["1'", 0, 56], "0'": ["0'", 2, 42], "1'": ["1'", 2, 42], Sym('A'+1): [None, 2, 54]}, direction=1), State(instruction=6, acc=3, transitions={'0': ["0'", 0, 44], '1': ["1'", 0, 56], "0'": ["0'", 3, 43], "1'": ["1'", 3, 43], Sym('A'+1): [None, 3, 55]}, direction=1), State(instruction=12, acc=0, transitions={'0': ['0', 0, 44], '1': ['0', 1, 45], "0'": ['0', 0, 44], "1'": ['0', 1, 45], Sym('B'+1): [None, 0, 40]}, direction=1), State(instruction=12, acc=1, transitions={'0': ['1', 0, 44], '1': ['1', 1, 45], "0'": ['1', 0, 44], "1'": ['1', 1, 45], Sym('B'+1): [None, 0, 48]}, direction=1), State(instruction=12, acc=2, transitions={}, direction=None), None, State(instruction=16, acc=0, transitions={'0': ["0'", 0, 48], '1': ["1'", 1, 53], "0'": ["0'", 0, 48], "1'": ["1'", 0, 48], Sym('A'+1): [None, 0, 52]}, direction=1), State(instruction=16, acc=1, transitions={'0': ["0'", 0, 48], '1': ["1'", 1, 53], "0'": ["0'", 1, 49], "1'": ["1'", 1, 49], Sym('A'+1): [None, 1, 53]}, direction=1), State(instruction=16, acc=2, transitions={'0': ["0'", 0, 48], '1': ["1'", 1, 53], "0'": ["0'", 2, 50], "1'": ["1'", 2, 50], Sym('A'+1): [None, 2, 54]}, direction=1), State(instruction=16, acc=3, transitions={'0': ["0'", 0, 48], '1': ["1'", 1, 53], "0'": ["0'", 3, 51], "1'": ["1'", 3, 51], Sym('A'+1): [None, 3, 55]}, direction=1), State(instruction=19, acc=0, transitions={'0': ['0', 0, 52], '1': ['1', 0, 52], "0'": ['0', 0, 52], "1'": ['1', 0, 52], Sym('A'+1): [None, 0, 36]}, direction=1), State(instruction=19, acc=1, transitions={'0': ['0', 1, 53], '1': ['1', 1, 53], "0'": ['0', 1, 53], "1'": ['1', 1, 53], Sym('A'+1): [None, 1, 37]}, direction=1), State(instruction=19, acc=2, transitions={'0': ['0', 2, 54], '1': ['1', 2, 54], "0'": ['0', 2, 54], "1'": ['1', 2, 54], Sym('A'+1): [None, 2, 38]}, direction=1), State(instruction=19, acc=3, transitions={'0': ['0', 3, 55], '1': ['1', 3, 55], "0'": ['0', 3, 55], "1'": ['1', 3, 55], Sym('A'+1): [None, 3, 39]}, direction=1), State(instruction=24, acc=0, transitions={'0': ["0'", 0, 60], '1': ["1'", 1, 61], "0'": ["0'", 0, 56], "1'": ["1'", 0, 56], Sym('B'+1): [None, 0, 68]}, direction=1), State(instruction=24, acc=1, transitions={'0': ["0'", 1, 61], '1': ["1'", 2, 62], "0'": ["0'", 1, 57], "1'": ["1'", 1, 57], Sym('B'+1): [None, 1, 69]}, direction=1), State(instruction=24, acc=2, transitions={'0': ["0'", 2, 62], '1': ["1'", 2, 62], "0'": ["0'", 2, 58], "1'": ["1'", 2, 58], Sym('B'+1): [None, 1, 69]}, direction=1), State(instruction=24, acc=3, transitions={'0': ["0'", 3, 63], '1': ["1'", 3, 63], "0'": ["0'", 3, 59], "1'": ["1'", 3, 59], Sym('B'+1): [None, 1, 69]}, direction=1), State(instruction=26, acc=0, transitions={'0': ["0'", 0, 56], '1': ["1'", 0, 56], "0'": ["0'", 0, 60], "1'": ["1'", 0, 60], Sym('D'+1): [None, 0, 68]}, direction=1), State(instruction=26, acc=1, transitions={'0': ["1'", 0, 56], '1': ["0'", 1, 57], "0'": ["0'", 1, 61], "1'": ["1'", 1, 61], Sym('D'+1): [None, 1, 69]}, direction=1), State(instruction=26, acc=2, transitions={'0': ["0'", 1, 57], '1': ["1'", 1, 57], "0'": ["0'", 2, 62], "1'": ["1'", 2, 62], Sym('D'+1): [None, 1, 69]}, direction=1), State(instruction=26, acc=3, transitions={'0': ["1'", 1, 57], '1': ["1'", 1, 57], "0'": ["0'", 3, 63], "1'": ["1'", 3, 63], Sym('D'+1): [None, 1, 69]}, direction=1), State(instruction=29, acc=0, transitions={'0': ["0'", 0, 56], '1': ["0'", 0, 56], "0'": ["0'", 0, 64], "1'": ["1'", 0, 64], Sym('D'+1): [None, 0, 68]}, direction=1), State(instruction=29, acc=1, transitions={'0': ["1'", 0, 56], '1': ["1'", 0, 56], "0'": ["0'", 1, 65], "1'": ["1'", 1, 65], Sym('D'+1): [None, 1, 69]}, direction=1), State(instruction=29, acc=2, transitions={'0': ["0'", 1, 57], '1': ["0'", 1, 57], "0'": ["0'", 2, 66], "1'": ["1'", 2, 66], Sym('D'+1): [None, 1, 69]}, direction=1), None, State(instruction=33, acc=0, transitions={'0': ['0', 0, 68], '1': ['1', 0, 68], "0'": ['0', 0, 68], "1'": ['1', 0, 68], Sym('B'+1): [None, 0, 72]}, direction=1), State(instruction=33, acc=1, transitions={'0': ['0', 1, 69], '1': ['1', 1, 69], "0'": ['0', 1, 69], "1'": ['1', 1, 69], Sym('B'+1): [None, 1, 73]}, direction=1), State(instruction=33, acc=2, transitions={'0': ['0', 2, 70], '1': ['1', 2, 70], "0'": ['0', 2, 70], "1'": ['1', 2, 70], Sym('B'+1): [None, 2, 74]}, direction=1), None, State(instruction=34, acc=0, transitions={'0': ['0', 0, 72], '1': ['1', 0, 72], "0'": ['0', 0, 72], "1'": ['1', 0, 72], Sym('D'+1): [None, 0, 44]}, direction=1), State(instruction=34, acc=1, transitions={'0': ['0', 1, 73], '1': ['1', 1, 73], "0'": ['0', 1, 73], "1'": ['1', 1, 73], Sym('D'+1): [None, 1, 53]}, direction=1), State(instruction=34, acc=2, transitions={'0': ['0', 2, 74], '1': ['1', 2, 74], "0'": ['0', 2, 74], "1'": ['1', 2, 74], Sym('D'+1): [None, 2, 46]}, direction=1), None]
>>> quasis[0]
End(is_start=True, next_quasis=[40])
>>> to_symbols[40]
Sym('A'+0)
>>> from_symbols[40]
{Sym('B'+1)}
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST')
>>> states2searches()
Traceback (most recent call last):
  File "<pyshell#1101>", line 1, in <module>
    states2searches()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 556, in states2searches
    from_symbols[quasis[0]] = {0}
TypeError: unhashable type: 'End'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST')
>>> states2searches()
>>> to_symbols.keys()==from_symbols.keys()
True
>>> )))
SyntaxError: invalid syntax
>>> for k in to_symbols:
	print(k,to_symbols[k],from_symbols[k])

	
36 Sym('S'+0) {Sym('A'+1)}
37 Sym('S'+0) {Sym('A'+1)}
40 Sym('A'+0) {0, Sym('B'+1)}
44 Sym('B'+0) {Sym('D'+1), Sym('A'+0.5), Sym('B'+0.0)}
45 Sym('B'+0) {Sym('B'+0.0)}
48 Sym('A'+0) {Sym('B'+1)}
52 Sym('A'+0) {Sym('A'+0.0), Sym('A'+1)}
53 Sym('A'+0) {Sym('D'+1), Sym('A'+0.5), Sym('A'+0.0)}
56 Sym('B'+0) {Sym('D'+0.5), Sym('A'+0.5)}
57 Sym('B'+0) {Sym('D'+0.5)}
60 Sym('D'+0) {Sym('B'+0.5)}
61 Sym('D'+0) {Sym('B'+0.5)}
62 Sym('D'+0) {Sym('B'+0.5)}
68 Sym('B'+0) {Sym('D'+1), Sym('B'+0.0), Sym('B'+1)}
69 Sym('B'+0) {Sym('D'+1), Sym('B'+0.0), Sym('B'+1)}
72 Sym('D'+0) {Sym('D'+0.0), Sym('B'+1)}
73 Sym('D'+0) {Sym('D'+0.0), Sym('B'+1)}
>>> def score(to_symbols,from_symbols,order):
	total = 0
	for k in to_symbols():
		to_symbol = to_symbols[k]
		left = False
		right = False
		for from_symbol in from_symbols[k]:
			offset = symbol2int(to_symbol) - symbol2int(from_symbol)
			if offset<0:
				left = True
			if offset>0:
				right = True
		total += (left+right)
	return total

>>> score(to_symbols,from_symbols,['A','B','S','D'])
Traceback (most recent call last):
  File "<pyshell#1113>", line 1, in <module>
    score(to_symbols,from_symbols,['A','B','S','D'])
  File "<pyshell#1112>", line 3, in score
    for k in to_symbols():
TypeError: 'dict' object is not callable
>>> def score(to_symbols,from_symbols,order):
	total = 0
	for k in to_symbols:
		to_symbol = to_symbols[k]
		left = False
		right = False
		for from_symbol in from_symbols[k]:
			offset = symbol2int(to_symbol) - symbol2int(from_symbol)
			if offset<0:
				left = True
			if offset>0:
				right = True
		total += (left+right)
	return total

>>> score(to_symbols,from_symbols,['A','B','S','D'])
Traceback (most recent call last):
  File "<pyshell#1116>", line 1, in <module>
    score(to_symbols,from_symbols,['A','B','S','D'])
  File "<pyshell#1115>", line 8, in score
    offset = symbol2int(to_symbol) - symbol2int(from_symbol)
NameError: name 'symbol2int' is not defined
>>> def symbol2int(symbol,order):
    if type(symbol)==Symbol:
        return order.index(symbol.symbol)+symbol.offset
    else:
        return int(symbol)

>>> score(to_symbols,from_symbols,['A','B','S','D'])
Traceback (most recent call last):
  File "<pyshell#1119>", line 1, in <module>
    score(to_symbols,from_symbols,['A','B','S','D'])
  File "<pyshell#1115>", line 8, in score
    offset = symbol2int(to_symbol) - symbol2int(from_symbol)
TypeError: symbol2int() missing 1 required positional argument: 'order'
>>> def score(to_symbols,from_symbols,order):
	total = 0
	for k in to_symbols:
		to_symbol = to_symbols[k]
		left = False
		right = False
		for from_symbol in from_symbols[k]:
			offset = symbol2int(to_symbol,order) - symbol2int(from_symbol,order)
			if offset<0:
				left = True
			if offset>0:
				right = True
		total += (left+right)
	return total

>>> score(to_symbols,from_symbols,['A','B','S','D'])
18
>>> score(to_symbols,from_symbols,['S','A','B','D'])
17
>>> score(to_symbols,from_symbols,['B','A','S','D'])
13
>>> import itertools
>>> from order itertools.permutations(['B','A','S','D']):
	
SyntaxError: invalid syntax
>>> from order in itertools.permutations(['B','A','S','D']):
	
SyntaxError: invalid syntax
>>> for order in itertools.permutations(['A','B','S','D']):
	print(order,score(to_symbols,from_symbols,order))

	
('A', 'B', 'S', 'D') 18
('A', 'B', 'D', 'S') 16
('A', 'S', 'B', 'D') 14
('A', 'S', 'D', 'B') 14
('A', 'D', 'B', 'S') 16
('A', 'D', 'S', 'B') 18
('B', 'A', 'S', 'D') 13
('B', 'A', 'D', 'S') 15
('B', 'S', 'A', 'D') 16
('B', 'S', 'D', 'A') 16
('B', 'D', 'A', 'S') 12
('B', 'D', 'S', 'A') 15
('S', 'A', 'B', 'D') 17
('S', 'A', 'D', 'B') 17
('S', 'B', 'A', 'D') 15
('S', 'B', 'D', 'A') 14
('S', 'D', 'A', 'B') 19
('S', 'D', 'B', 'A') 17
('D', 'A', 'B', 'S') 19
('D', 'A', 'S', 'B') 17
('D', 'B', 'A', 'S') 15
('D', 'B', 'S', 'A') 18
('D', 'S', 'A', 'B') 20
('D', 'S', 'B', 'A') 20
>>> a = [k for k in range(10)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> A=a
>>> a = 2
>>> b=7
>>> A[:a]+A[a+1:b]+A[a:a+1]+A[b:]
[0, 1, 3, 4, 5, 6, 2, 7, 8, 9]
>>> a=7
>>> b=2
SyntaxError: invalid syntax
>>> =2
SyntaxError: invalid syntax
>>> b=2
>>> A[:a]+A[a+1:b]+A[a:a+1]+A[b:]
[0, 1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a=4
>>> b=4
>>> A[:a]+A[a+1:b]+A[a:a+1]+A[b:]
[0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
>>> a,b=4,5
>>> A[:a]+A[a+1:b]+A[a:a+1]+A[b:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a,b=4,10
>>> A[:a]+A[a+1:b]+A[a:a+1]+A[b:]
[0, 1, 2, 3, 5, 6, 7, 8, 9, 4]
>>> a,b=4,0
>>> A[:a]+A[a+1:b]+A[a:a+1]+A[b:]
[0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> def move_element(A,a,b):
	if b>a+1:
		return A[:a]+A[a+1:b]+A[a:a+1]+A[b:]
	elif
	
SyntaxError: invalid syntax
>>> def move_element(A,a,b):
	if b>a+1:
		return A[:a]+A[a+1:b]+A[a:a+1]+A[b:]
	elif:
		
SyntaxError: invalid syntax
>>> def move_element(A,a,b):
	if b>a+1:
		return A[:a]+A[a+1:b]+A[a:a+1]+A[b:]
	elif ??:
		
SyntaxError: invalid syntax
>>> def move_element(A,a,b):
	if b>a+1:
		return A[:a]+A[a+1:b]+A[a:a+1]+A[b:]
	elif b<a:
		return A[:b]+A[a:a+1]+A[b:a]+A[a:]

	
>>> A
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> move_element(A,3,5)
[0, 1, 2, 4, 3, 5, 6, 7, 8, 9]
>>> move_element(A,5,4)
[0, 1, 2, 3, 5, 4, 5, 6, 7, 8, 9]
>>> def move_element(A,a,b):
	if b>a+1:
		return A[:a]+A[a+1:b]+A[a:a+1]+A[b:]
	elif b<a:
		return A[:b]+A[a:a+1]+A[b:a]+A[a+1:]

	
>>> move_element(A,5,4)
[0, 1, 2, 3, 5, 4, 6, 7, 8, 9]
>>> move_element(A,5,5)
>>> move_element(A,5,6)
>>> move_element(A,5,10)
[0, 1, 2, 3, 4, 6, 7, 8, 9, 5]
>>> move_element(A,5,0)
[5, 0, 1, 2, 3, 4, 6, 7, 8, 9]
>>> move_element(A,0,5)
[1, 2, 3, 4, 0, 5, 6, 7, 8, 9]
>>> move_element(A,10,5)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> move_element(A,9,5)
[0, 1, 2, 3, 4, 9, 5, 6, 7, 8]
>>> move_element(A,randint(0,len(A)),randint(0,len(A)+1))
Traceback (most recent call last):
  File "<pyshell#1173>", line 1, in <module>
    move_element(A,randint(0,len(A)),randint(0,len(A)+1))
NameError: name 'randint' is not defined
>>> from random import randint
>>> move_element(A,randint(0,len(A)),randint(0,len(A)+1))
[0, 1, 2, 3, 4, 5, 6, 8, 7, 9]
>>> def find_optimal_order(order):
    best_order = order
    original_score = score()
    best_score = original_score
    for a in range(len(order)):
	for b in range(len(order)+1):
		new_order = move_element(order,a,b)
		if new_order:
                    new_score = score(new_order)
                    if new_score>best_score:
                        best_score = new_score
                        best_order = new_order
    if best_score>original_score:
        return find_optimal_order(best_order)
    else:
        return order
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def find_optimal_order(order):
    best_order = order
    original_score = score()
    best_score = original_score
    for a in range(len(order)):
	for b in range(len(order)+1):
            new_order = move_element(order,a,b)
            if new_order:
                new_score = score(new_order)
                if new_score>best_score:
                    best_score = new_score
                    best_order = new_order
    if best_score>original_score:
        return find_optimal_order(best_order)
    else:
        return order
SyntaxError: inconsistent use of tabs and spaces in indentation
def find_optimal_order(order):
    best_order = order
    original_score = score()
    best_score = original_score
    for a in range(len(order)):
	for b in range(len(order)+1):
            new_order = move_element(order,a,b)
            if new_order:
                new_score = score(new_order)
                if new_score>best_score:
                    best_score = new_score
                    best_order = new_order
    if best_score>original_score:
        return find_optimal_order(best_order)
    else:
        return order
>>> def find_optimal_order(order):
    best_order = order
    original_score = score()
    best_score = original_score
    for a in range(len(order)):
        for b in range(len(order)+1):
            new_order = move_element(order,a,b)
            if new_order:
                new_score = score(new_order)
                if new_score>best_score:
                    best_score = new_score
                    best_order = new_order
    if best_score>original_score:
        return find_optimal_order(best_order)
    else:
        return order

>>> def score(order):
    global to_symbols, from_symbols
    total = 0
    for k in to_symbols:
        to_symbol = to_symbols[k]
        left = False
        right = False
        for from_symbol in from_symbols[k]:
            offset = symbol2int(to_symbol,order) - symbol2int(from_symbol,order)
            if offset<0:
                left = True
            if offset>0:
                right = True
        total += (left+right)
    return total

>>> to_symbols
{36: Sym('S'+0), 37: Sym('S'+0), 40: Sym('A'+0), 44: Sym('B'+0), 45: Sym('B'+0), 48: Sym('A'+0), 52: Sym('A'+0), 53: Sym('A'+0), 56: Sym('B'+0), 57: Sym('B'+0), 60: Sym('D'+0), 61: Sym('D'+0), 62: Sym('D'+0), 68: Sym('B'+0), 69: Sym('B'+0), 72: Sym('D'+0), 73: Sym('D'+0)}
>>> find_optimal_order(['A','B','S','D'])
Traceback (most recent call last):
  File "<pyshell#1187>", line 1, in <module>
    find_optimal_order(['A','B','S','D'])
  File "<pyshell#1183>", line 3, in find_optimal_order
    original_score = score()
TypeError: score() missing 1 required positional argument: 'order'
>>> def find_optimal_order(order):
    best_order = order
    original_score = score(order)
    best_score = original_score
    for a in range(len(order)):
        for b in range(len(order)+1):
            new_order = move_element(order,a,b)
            if new_order:
                new_score = score(new_order)
                if new_score>best_score:
                    best_score = new_score
                    best_order = new_order
    if best_score>original_score:
        return find_optimal_order(best_order)
    else:
        return order

>>> find_optimal_order(['A','B','S','D'])
['D', 'S', 'A', 'B']
>>> score(['D', 'S', 'A', 'B'])
20
>>> def find_optimal_order(order):
    best_order = order
    original_score = score(order)
    best_score = original_score
    for a in range(len(order)):
        for b in range(len(order)+1):
            new_order = move_element(order,a,b)
            if new_order:
                new_score = score(new_order)
                if new_score<best_score:
                    best_score = new_score
                    best_order = new_order
    if best_score>original_score:
        return find_optimal_order(best_order)
    else:
        return order

>>> for order in itertools.permutations(['D', 'S', 'A', 'B']):
	print(order,find_optimal_order(order))

	
('D', 'S', 'A', 'B') ('D', 'S', 'A', 'B')
('D', 'S', 'B', 'A') ('D', 'S', 'B', 'A')
('D', 'A', 'S', 'B') ('D', 'A', 'S', 'B')
('D', 'A', 'B', 'S') ('D', 'A', 'B', 'S')
('D', 'B', 'S', 'A') ('D', 'B', 'S', 'A')
('D', 'B', 'A', 'S') ('D', 'B', 'A', 'S')
('S', 'D', 'A', 'B') ('S', 'D', 'A', 'B')
('S', 'D', 'B', 'A') ('S', 'D', 'B', 'A')
('S', 'A', 'D', 'B') ('S', 'A', 'D', 'B')
('S', 'A', 'B', 'D') ('S', 'A', 'B', 'D')
('S', 'B', 'D', 'A') ('S', 'B', 'D', 'A')
('S', 'B', 'A', 'D') ('S', 'B', 'A', 'D')
('A', 'D', 'S', 'B') ('A', 'D', 'S', 'B')
('A', 'D', 'B', 'S') ('A', 'D', 'B', 'S')
('A', 'S', 'D', 'B') ('A', 'S', 'D', 'B')
('A', 'S', 'B', 'D') ('A', 'S', 'B', 'D')
('A', 'B', 'D', 'S') ('A', 'B', 'D', 'S')
('A', 'B', 'S', 'D') ('A', 'B', 'S', 'D')
('B', 'D', 'S', 'A') ('B', 'D', 'S', 'A')
('B', 'D', 'A', 'S') ('B', 'D', 'A', 'S')
('B', 'S', 'D', 'A') ('B', 'S', 'D', 'A')
('B', 'S', 'A', 'D') ('B', 'S', 'A', 'D')
('B', 'A', 'D', 'S') ('B', 'A', 'D', 'S')
('B', 'A', 'S', 'D') ('B', 'A', 'S', 'D')
>>> def find_optimal_order(order):
    best_order = order
    original_score = score(order)
    best_score = original_score
    for a in range(len(order)):
        for b in range(len(order)+1):
            new_order = move_element(order,a,b)
            if new_order:
                new_score = score(new_order)
                if new_score<best_score:
                    best_score = new_score
                    best_order = new_order
    if best_score<original_score:
        return find_optimal_order(best_order)
    else:
        return order

>>> for order in itertools.permutations(['D', 'S', 'A', 'B']):
	print(order,find_optimal_order(order))

	
('D', 'S', 'A', 'B') ('B', 'D', 'A', 'S')
('D', 'S', 'B', 'A') ('B', 'D', 'A', 'S')
('D', 'A', 'S', 'B') ('B', 'D', 'A', 'S')
('D', 'A', 'B', 'S') ('B', 'D', 'A', 'S')
('D', 'B', 'S', 'A') ('B', 'D', 'A', 'S')
('D', 'B', 'A', 'S') ('B', 'D', 'A', 'S')
('S', 'D', 'A', 'B') ('B', 'D', 'A', 'S')
('S', 'D', 'B', 'A') ('B', 'D', 'A', 'S')
('S', 'A', 'D', 'B') ('B', 'D', 'A', 'S')
('S', 'A', 'B', 'D') ('B', 'D', 'A', 'S')
('S', 'B', 'D', 'A') ('B', 'D', 'A', 'S')
('S', 'B', 'A', 'D') ('B', 'D', 'A', 'S')
('A', 'D', 'S', 'B') ('B', 'D', 'A', 'S')
('A', 'D', 'B', 'S') ('B', 'D', 'A', 'S')
('A', 'S', 'D', 'B') ('B', 'D', 'A', 'S')
('A', 'S', 'B', 'D') ('B', 'D', 'A', 'S')
('A', 'B', 'D', 'S') ('B', 'D', 'A', 'S')
('A', 'B', 'S', 'D') ('B', 'D', 'A', 'S')
('B', 'D', 'S', 'A') ('B', 'D', 'A', 'S')
('B', 'D', 'A', 'S') ('B', 'D', 'A', 'S')
('B', 'S', 'D', 'A') ('B', 'D', 'A', 'S')
('B', 'S', 'A', 'D') ('B', 'D', 'A', 'S')
('B', 'A', 'D', 'S') ('B', 'D', 'A', 'S')
('B', 'A', 'S', 'D') ('B', 'D', 'A', 'S')
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
Traceback (most recent call last):
  File "<pyshell#1201>", line 1, in <module>
    compile_function('PI')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 527, in compile_function
    states2searches()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 582, in states2searches
    to_symbols[k] = Symbol(instruction.vard,int(state.direction<0))
TypeError: '<' not supported between instances of 'NoneType' and 'int'
>>> for k,quasi in enumerate(sorted(used_states)):
	print(k,quasi)

	
0 0
1 13
2 68
3 69
4 70
5 72
6 73
7 74
8 76
9 77
10 80
11 84
12 88
13 89
14 92
15Traceback (most recent call last):
  File "<pyshell#1204>", line 2, in <module>
    print(k,quasi)
KeyboardInterrupt
>>> for k in sorted(used_states):
	print(k,quasis[k])

	
0 End(is_start=True, next_quasis=[84])
13 End(is_start=False, next_quasis=[None])
68 State(instruction=3, acc=0, transitions={'0': ['0', 0, 136], '1': ['1', 1, 73], "0'": ["0'", 0, 68], "1'": ["1'", 0, 68], Sym('S'+1): [None, 0, 136]}, direction=1)
69 State(instruction=3, acc=1, transitions={'0': ['0', 0, 136], '1': ['1', 1, 73], "0'": ["0'", 1, 69], "1'": ["1'", 1, 69], Sym('S'+1): [None, 1, 73]}, direction=1)
70 State(instruction=3, acc=2, transitions={'0': ['0', 0, 136], '1': ['1', 1, 73], "0'": ["0'", 2, 70], "1'": ["1'", 2, 70], Sym('S'+1): [None, 2, 74]}, direction=1)
72 State(instruction=5, acc=0, transitions={'0': ['1', 0, 72], '1': ['0', 0, 72], "0'": ['1', 0, 72], "1'": ['0', 0, 72], Sym('V'+1): [None, 0, 136]}, direction=1)
73 State(instruction=5, acc=1, transitions={'0': ['0', 1, 73], '1': ['1', 0, 72], "0'": ['0', 1, 73], "1'": ['1', 0, 72], Sym('V'+1): [None, 0, 136]}, direction=1)
74 State(instruction=5, acc=2, transitions={}, direction=None)
76 State(instruction=8, acc=0, transitions={'0': ['0', 0, 76], '1': ['1', 0, 76], "0'": ['0', 0, 76], "1'": ['1', 0, 76], Sym('N'+1): [None, 0, 80]}, direction=1)
77 State(instruction=8, acc=1, transitions={'0': ['1', 0, 76], '1': ['0', 1, 77], "0'": ['1', 0, 76], "1'": ['0', 1, 77], Sym('N'+1): [None, 1, 13]}, direction=1)
80 State(instruction=10, acc=0, transitions={'0': ['1', 0, 80], '1': ['0', 0, 80], "0'": ['1', 0, 80], "1'": ['0', 0, 80], Sym('S'+1): [None, 0, 84]}, direction=1)
84 State(instruction=15, acc=0, transitions={'0': ['0', 0, 84], '1': ['0', 0, 84], "0'": ['0', 0, 84], "1'": ['0', 0, 84], Sym('varr'+1): [None, 0, 88]}, direction=1)
88 State(instruction=17, acc=0, transitions={'0': ['0', 0, 88], '1': ['0', 1, 89], "0'": ['0', 0, 88], "1'": ['0', 1, 89], Sym('varr'+1): [None, 0, 100]}, direction=1)
89 State(instruction=17, acc=1, transitions={'0': ['1', 0, 88], '1': ['1', 1, 89], "0'": ['1', 0, 88], "1'": ['1', 1, 89], Sym('varr'+1): [None, 1, 101]}, direction=1)
92 State(instruction=20, acc=0, transitions={'0': ["1'", 0, 116], '1': ["1'", 0, 116], "0'": ["0'", 0, 92], "1'": ["1'", 0, 92], Sym('V'+0): [None, 0, 96]}, direction=-1)
93 State(instruction=20, acc=1, transitions={'0': ["0'", 1, 89], '1': ["0'", 1, 89], "0'": ["0'", 1, 93], "1'": ["1'", 1, 93], Sym('V'+0): [None, 1, 97]}, direction=-1)
95 State(instruction=20, acc=3, transitions={'0': ["1'", 0, 116], '1': ["1'", 0, 116], "0'": ["0'", 3, 95], "1'": ["1'", 3, 95], Sym('V'+0): [None, 3, 98]}, direction=-1)
96 State(instruction=26, acc=0, transitions={'0': ['0', 0, 96], '1': ['1', 0, 96], "0'": ['0', 0, 96], "1'": ['1', 0, 96], Sym('V'+1): [None, 0, 68]}, direction=1)
97 State(instruction=26, acc=1, transitions={'0': ['0', 1, 97], '1': ['1', 1, 97], "0'": ['0', 1, 97], "1'": ['1', 1, 97], Sym('V'+1): [None, 1, 69]}, direction=1)
98 State(instruction=26, acc=2, transitions={'0': ['0', 2, 98], '1': ['1', 2, 98], "0'": ['0', 2, 98], "1'": ['1', 2, 98], Sym('V'+1): [None, 2, 70]}, direction=1)
100 State(instruction=30, acc=0, transitions={'0': ["0'", 0, 104], '1': ["1'", 1, 105], "0'": ["0'", 0, 100], "1'": ["1'", 0, 100], Sym('varr'+0): [None, 0, 108]}, direction=-1)
101 State(instruction=30, acc=1, transitions={'0': ["0'", 0, 104], '1': ["1'", 1, 105], "0'": ["0'", 1, 101], "1'": ["1'", 1, 101], Sym('varr'+0): [None, 1, 109]}, direction=-1)
104 State(instruction=31, acc=0, transitions={'0': ["0'", 0, 100], '1': ["1'", 1, 109], "0'": ["0'", 0, 104], "1'": ["1'", 0, 104], Sym('N'+0): [None, 0, 108]}, direction=-1)
105 State(instruction=31, acc=1, transitions={'0': ["0'", 3, 111], '1': ["1'", 0, 100], "0'": ["0'", 1, 105], "1'": ["1'", 1, 105], Sym('N'+0): [None, 1, 109]}, direction=-1)
108 State(instruction=35, acc=0, transitions={'0': ['0', 0, 108], '1': ['1', 0, 108], "0'": ['0', 0, 108], "1'": ['1', 0, 108], Sym('varr'+1): [None, 0, 112]}, direction=1)
109 State(instruction=35, acc=1, transitions={'0': ['0', 1, 109], '1': ['1', 1, 109], "0'": ['0', 1, 109], "1'": ['1', 1, 109], Sym('varr'+1): [None, 1, 113]}, direction=1)
111 State(instruction=35, acc=3, transitions={'0': ['0', 3, 111], '1': ['1', 3, 111], "0'": ['0', 3, 111], "1'": ['1', 3, 111], Sym('varr'+1): [None, 3, 115]}, direction=1)
112 State(instruction=36, acc=0, transitions={'0': ['0', 0, 112], '1': ['1', 0, 112], "0'": ['0', 0, 112], "1'": ['1', 0, 112], Sym('N'+1): [None, 0, 92]}, direction=1)
113 State(instruction=36, acc=1, transitions={'0': ['0', 1, 113], '1': ['1', 1, 113], "0'": ['0', 1, 113], "1'": ['1', 1, 113], Sym('N'+1): [None, 1, 93]}, direction=1)
115 State(instruction=36, acc=3, transitions={'0': ['0', 3, 115], '1': ['1', 3, 115], "0'": ['0', 3, 115], "1'": ['1', 3, 115], Sym('N'+1): [None, 3, 95]}, direction=1)
116 State(instruction=41, acc=0, transitions={'0': ["0'", 0, 120], '1': ["1'", 1, 121], "0'": ["0'", 0, 116], "1'": ["1'", 0, 116], Sym('N'+1): [None, 0, 128]}, direction=1)
117 State(instruction=41, acc=1, transitions={'0': ["0'", 1, 121], '1': ["1'", 1, 121], "0'": ["0'", 1, 117], "1'": ["1'", 1, 117], Sym('N'+1): [None, 1, 129]}, direction=1)
120 State(instruction=43, acc=0, transitions={'0': ["0'", 0, 116], '1': ["1'", 1, 117], "0'": ["0'", 0, 120], "1'": ["1'", 0, 120], Sym('varr'+1): [None, 0, 128]}, direction=1)
121 State(instruction=43, acc=1, transitions={'0': ["1'", 0, 116], '1': ["0'", 0, 116], "0'": ["0'", 1, 121], "1'": ["1'", 1, 121], Sym('varr'+1): [None, 1, 129]}, direction=1)
128 State(instruction=50, acc=0, transitions={'0': ['0', 0, 128], '1': ['1', 0, 128], "0'": ['0', 0, 128], "1'": ['1', 0, 128], Sym('N'+1): [None, 0, 132]}, direction=1)
129 State(instruction=50, acc=1, transitions={'0': ['0', 1, 129], '1': ['1', 1, 129], "0'": ['0', 1, 129], "1'": ['1', 1, 129], Sym('N'+1): [None, 1, 133]}, direction=1)
132 State(instruction=51, acc=0, transitions={'0': ['0', 0, 132], '1': ['1', 0, 132], "0'": ['0', 0, 132], "1'": ['1', 0, 132], Sym('varr'+1): [None, 0, 88]}, direction=1)
133 State(instruction=51, acc=1, transitions={'0': ['0', 1, 133], '1': ['1', 1, 133], "0'": ['0', 1, 133], "1'": ['1', 1, 133], Sym('varr'+1): [None, 1, 89]}, direction=1)
136 State(instruction=56, acc=0, transitions={'0': ["0'", 0, 140], '1': ["1'", 1, 141], "0'": ["0'", 0, 136], "1'": ["1'", 0, 136], Sym('V'+1): [None, 0, 148]}, direction=1)
137 State(instruction=56, acc=1, transitions={'0': ["0'", 1, 141], '1': ["1'", 2, 142], "0'": ["0'", 1, 137], "1'": ["1'", 1, 137], Sym('V'+1): [None, 1, 149]}, direction=1)
140 State(instruction=58, acc=0, transitions={'0': ["0'", 0, 136], '1': ["1'", 0, 136], "0'": ["0'", 0, 140], "1'": ["1'", 0, 140], Sym('P'+1): [None, 0, 148]}, direction=1)
141 State(instruction=58, acc=1, transitions={'0': ["1'", 0, 136], '1': ["0'", 1, 137], "0'": ["0'", 1, 141], "1'": ["1'", 1, 141], Sym('P'+1): [None, 1, 149]}, direction=1)
142 State(instruction=58, acc=2, transitions={'0': ["0'", 1, 137], '1': ["1'", 1, 137], "0'": ["0'", 2, 142], "1'": ["1'", 2, 142], Sym('P'+1): [None, 1, 149]}, direction=1)
148 State(instruction=65, acc=0, transitions={'0': ['0', 0, 148], '1': ['1', 0, 148], "0'": ['0', 0, 148], "1'": ['1', 0, 148], Sym('V'+1): [None, 0, 152]}, direction=1)
149 State(instruction=65, acc=1, transitions={'0': ['0', 1, 149], '1': ['1', 1, 149], "0'": ['0', 1, 149], "1'": ['1', 1, 149], Sym('V'+1): [None, 1, 153]}, direction=1)
152 State(instruction=66, acc=0, transitions={'0': ['0', 0, 152], '1': ['1', 0, 152], "0'": ['0', 0, 152], "1'": ['1', 0, 152], Sym('P'+1): [None, 0, 76]}, direction=1)
153 State(instruction=66, acc=1, transitions={'0': ['0', 1, 153], '1': ['1', 1, 153], "0'": ['0', 1, 153], "1'": ['1', 1, 153], Sym('P'+1): [None, 1, 77]}, direction=1)
>>> quasis[5]
Instruction(COMPs, vard=V, next_quasis=[54])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
>>> for order in itertools.permutations(['varr', 'V', 'N', 'P', 'S']):
	print(order,find_optimal_order(order))

	
Traceback (most recent call last):
  File "<pyshell#1210>", line 1, in <module>
    for order in itertools.permutations(['varr', 'V', 'N', 'P', 'S']):
NameError: name 'itertools' is not defined
>>> import itertools
>>> for order in itertools.permutations(['varr', 'V', 'N', 'P', 'S']):
	print(order,find_optimal_order(order))

	
Traceback (most recent call last):
  File "<pyshell#1213>", line 2, in <module>
    print(order,find_optimal_order(order))
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 602, in find_optimal_order
    new_order = move_element(order,a,b)
NameError: name 'move_element' is not defined
>>> def move_element(A,a,b):
    if b>a+1:
        return A[:a]+A[a+1:b]+A[a:a+1]+A[b:]
    elif b<a:
        return A[:b]+A[a:a+1]+A[b:a]+A[a+1:]

>>> for order in itertools.permutations(['varr', 'V', 'N', 'P', 'S']):
	print(order,find_optimal_order(order))

	
('varr', 'V', 'N', 'P', 'S') ('varr', 'N', 'V', 'P', 'S')
('varr', 'V', 'N', 'S', 'P') ('varr', 'N', 'S', 'V', 'P')
('varr', 'V', 'P', 'N', 'S') ('varr', 'V', 'P', 'N', 'S')
('varr', 'V', 'P', 'S', 'N') ('V', 'P', 'S', 'varr', 'N')
('varr', 'V', 'S', 'N', 'P') ('V', 'P', 'S', 'varr', 'N')
('varr', 'V', 'S', 'P', 'N') ('V', 'S', 'P', 'N', 'varr')
('varr', 'N', 'V', 'P', 'S') ('varr', 'N', 'V', 'P', 'S')
('varr', 'N', 'V', 'S', 'P') ('varr', 'N', 'S', 'V', 'P')
('varr', 'N', 'P', 'V', 'S') ('varr', 'N', 'V', 'P', 'S')
('varr', 'N', 'P', 'S', 'V') ('varr', 'N', 'S', 'V', 'P')
('varr', 'N', 'S', 'V', 'P') ('varr', 'N', 'S', 'V', 'P')
('varr', 'N', 'S', 'P', 'V') ('varr', 'N', 'S', 'V', 'P')
('varr', 'P', 'V', 'N', 'S') ('varr', 'V', 'P', 'N', 'S')
('varr', 'P', 'V', 'S', 'N') ('V', 'P', 'S', 'varr', 'N')
('varr', 'P', 'N', 'V', 'S') ('varr', 'N', 'V', 'P', 'S')
('varr', 'P', 'N', 'S', 'V') ('varr', 'N', 'S', 'V', 'P')
('varr', 'P', 'S', 'V', 'N') ('S', 'V', 'P', 'N', 'varr')
('varr', 'P', 'S', 'N', 'V') ('V', 'P', 'S', 'varr', 'N')
('varr', 'S', 'V', 'N', 'P') ('varr', 'N', 'S', 'V', 'P')
('varr', 'S', 'V', 'P', 'N') ('S', 'V', 'P', 'N', 'varr')
('varr', 'S', 'N', 'V', 'P') ('S', 'N', 'varr', 'V', 'P')
('varr', 'S', 'N', 'P', 'V') ('S', 'N', 'varr', 'V', 'P')
('varr', 'S', 'P', 'V', 'N') ('S', 'V', 'P', 'N', 'varr')
('varr', 'S', 'P', 'N', 'V') ('S', 'N', 'varr', 'V', 'P')
('V', 'varr', 'N', 'P', 'S') ('varr', 'N', 'V', 'P', 'S')
('V', 'varr', 'N', 'S', 'P') ('varr', 'N', 'S', 'V', 'P')
('V', 'varr', 'P', 'N', 'S') ('varr', 'V', 'P', 'N', 'S')
('V', 'varr', 'P', 'S', 'N') ('V', 'P', 'S', 'varr', 'N')
('V', 'varr', 'S', 'N', 'P') ('V', 'P', 'S', 'varr', 'N')
('V', 'varr', 'S', 'P', 'N') ('V', 'S', 'P', 'N', 'varr')
('V', 'N', 'varr', 'P', 'S') ('N', 'varr', 'V', 'P', 'S')
('V', 'N', 'varr', 'S', 'P') ('V', 'P', 'N', 'varr', 'S')
('V', 'N', 'P', 'varr', 'S') ('V', 'P', 'N', 'varr', 'S')
('V', 'N', 'P', 'S', 'varr') ('V', 'P', 'N', 'S', 'varr')
('V', 'N', 'S', 'varr', 'P') ('V', 'P', 'N', 'S', 'varr')
('V', 'N', 'S', 'P', 'varr') ('V', 'S', 'P', 'N', 'varr')
('V', 'P', 'varr', 'N', 'S') ('V', 'P', 'varr', 'N', 'S')
('V', 'P', 'varr', 'S', 'N') ('V', 'P', 'S', 'varr', 'N')
('V', 'P', 'N', 'varr', 'S') ('V', 'P', 'N', 'varr', 'S')
('V', 'P', 'N', 'S', 'varr') ('V', 'P', 'N', 'S', 'varr')
('V', 'P', 'S', 'varr', 'N') ('V', 'P', 'S', 'varr', 'N')
('V', 'P', 'S', 'N', 'varr') ('V', 'S', 'P', 'N', 'varr')
('V', 'S', 'varr', 'N', 'P') ('V', 'P', 'S', 'varr', 'N')
('V', 'S', 'varr', 'P', 'N') ('V', 'S', 'P', 'N', 'varr')
('V', 'S', 'N', 'varr', 'P') ('S', 'N', 'varr', 'V', 'P')
('V', 'S', 'N', 'P', 'varr') ('V', 'S', 'P', 'N', 'varr')
('V', 'S', 'P', 'varr', 'N') ('V', 'P', 'S', 'varr', 'N')
('V', 'S', 'P', 'N', 'varr') ('V', 'S', 'P', 'N', 'varr')
('N', 'varr', 'V', 'P', 'S') ('N', 'varr', 'V', 'P', 'S')
('N', 'varr', 'V', 'S', 'P') ('S', 'N', 'varr', 'V', 'P')
('N', 'varr', 'P', 'V', 'S') ('N', 'varr', 'V', 'P', 'S')
('N', 'varr', 'P', 'S', 'V') ('N', 'varr', 'V', 'P', 'S')
('N', 'varr', 'S', 'V', 'P') ('varr', 'N', 'S', 'V', 'P')
('N', 'varr', 'S', 'P', 'V') ('varr', 'N', 'S', 'V', 'P')
('N', 'V', 'varr', 'P', 'S') ('N', 'varr', 'V', 'P', 'S')
('N', 'V', 'varr', 'S', 'P') ('S', 'N', 'varr', 'V', 'P')
('N', 'V', 'P', 'varr', 'S') ('V', 'P', 'N', 'varr', 'S')
('N', 'V', 'P', 'S', 'varr') ('V', 'P', 'N', 'S', 'varr')
('N', 'V', 'S', 'varr', 'P') ('V', 'P', 'S', 'varr', 'N')
('N', 'V', 'S', 'P', 'varr') ('V', 'S', 'P', 'N', 'varr')
('N', 'P', 'varr', 'V', 'S') ('N', 'varr', 'V', 'P', 'S')
('N', 'P', 'varr', 'S', 'V') ('varr', 'N', 'S', 'V', 'P')
('N', 'P', 'V', 'varr', 'S') ('varr', 'N', 'V', 'P', 'S')
('N', 'P', 'V', 'S', 'varr') ('V', 'P', 'S', 'varr', 'N')
('N', 'P', 'S', 'varr', 'V') ('S', 'N', 'varr', 'V', 'P')
('N', 'P', 'S', 'V', 'varr') ('S', 'V', 'P', 'N', 'varr')
('N', 'S', 'varr', 'V', 'P') ('S', 'N', 'varr', 'V', 'P')
('N', 'S', 'varr', 'P', 'V') ('S', 'N', 'varr', 'V', 'P')
('N', 'S', 'V', 'varr', 'P') ('varr', 'N', 'S', 'V', 'P')
('N', 'S', 'V', 'P', 'varr') ('S', 'V', 'P', 'N', 'varr')
('N', 'S', 'P', 'varr', 'V') ('S', 'N', 'varr', 'V', 'P')
('N', 'S', 'P', 'V', 'varr') ('S', 'V', 'P', 'N', 'varr')
('P', 'varr', 'V', 'N', 'S') ('varr', 'V', 'P', 'N', 'S')
('P', 'varr', 'V', 'S', 'N') ('V', 'S', 'P', 'N', 'varr')
('P', 'varr', 'N', 'V', 'S') ('varr', 'N', 'V', 'P', 'S')
('P', 'varr', 'N', 'S', 'V') ('varr', 'N', 'S', 'V', 'P')
('P', 'varr', 'S', 'V', 'N') ('S', 'V', 'P', 'N', 'varr')
('P', 'varr', 'S', 'N', 'V') ('V', 'P', 'N', 'varr', 'S')
('P', 'V', 'varr', 'N', 'S') ('V', 'P', 'varr', 'N', 'S')
('P', 'V', 'varr', 'S', 'N') ('V', 'P', 'S', 'varr', 'N')
('P', 'V', 'N', 'varr', 'S') ('V', 'P', 'N', 'varr', 'S')
('P', 'V', 'N', 'S', 'varr') ('V', 'P', 'N', 'S', 'varr')
('P', 'V', 'S', 'varr', 'N') ('V', 'P', 'S', 'varr', 'N')
('P', 'V', 'S', 'N', 'varr') ('V', 'S', 'P', 'N', 'varr')
('P', 'N', 'varr', 'V', 'S') ('N', 'varr', 'V', 'P', 'S')
('P', 'N', 'varr', 'S', 'V') ('V', 'P', 'N', 'varr', 'S')
('P', 'N', 'V', 'varr', 'S') ('V', 'P', 'N', 'varr', 'S')
('P', 'N', 'V', 'S', 'varr') ('V', 'P', 'N', 'S', 'varr')
('P', 'N', 'S', 'varr', 'V') ('V', 'P', 'N', 'S', 'varr')
('P', 'N', 'S', 'V', 'varr') ('V', 'P', 'N', 'S', 'varr')
('P', 'S', 'varr', 'V', 'N') ('V', 'P', 'S', 'varr', 'N')
('P', 'S', 'varr', 'N', 'V') ('V', 'P', 'S', 'varr', 'N')
('P', 'S', 'V', 'varr', 'N') ('V', 'P', 'S', 'varr', 'N')
('P', 'S', 'V', 'N', 'varr') ('S', 'V', 'P', 'N', 'varr')
('P', 'S', 'N', 'varr', 'V') ('S', 'N', 'varr', 'V', 'P')
('P', 'S', 'N', 'V', 'varr') ('V', 'S', 'P', 'N', 'varr')
('S', 'varr', 'V', 'N', 'P') ('S', 'N', 'varr', 'V', 'P')
('S', 'varr', 'V', 'P', 'N') ('varr', 'V', 'P', 'N', 'S')
('S', 'varr', 'N', 'V', 'P') ('varr', 'N', 'S', 'V', 'P')
('S', 'varr', 'N', 'P', 'V') ('varr', 'N', 'S', 'V', 'P')
('S', 'varr', 'P', 'V', 'N') ('varr', 'V', 'P', 'N', 'S')
('S', 'varr', 'P', 'N', 'V') ('varr', 'N', 'S', 'V', 'P')
('S', 'V', 'varr', 'N', 'P') ('V', 'P', 'S', 'varr', 'N')
('S', 'V', 'varr', 'P', 'N') ('S', 'V', 'P', 'N', 'varr')
('S', 'V', 'N', 'varr', 'P') ('S', 'N', 'varr', 'V', 'P')
('S', 'V', 'N', 'P', 'varr') ('S', 'V', 'P', 'N', 'varr')
('S', 'V', 'P', 'varr', 'N') ('V', 'P', 'S', 'varr', 'N')
('S', 'V', 'P', 'N', 'varr') ('S', 'V', 'P', 'N', 'varr')
('S', 'N', 'varr', 'V', 'P') ('S', 'N', 'varr', 'V', 'P')
('S', 'N', 'varr', 'P', 'V') ('S', 'N', 'varr', 'V', 'P')
('S', 'N', 'V', 'varr', 'P') ('S', 'N', 'varr', 'V', 'P')
('S', 'N', 'V', 'P', 'varr') ('S', 'V', 'P', 'N', 'varr')
('S', 'N', 'P', 'varr', 'V') ('S', 'N', 'varr', 'V', 'P')
('S', 'N', 'P', 'V', 'varr') ('S', 'N', 'varr', 'V', 'P')
('S', 'P', 'varr', 'V', 'N') ('V', 'P', 'S', 'varr', 'N')
('S', 'P', 'varr', 'N', 'V') ('varr', 'N', 'S', 'V', 'P')
('S', 'P', 'V', 'varr', 'N') ('V', 'P', 'S', 'varr', 'N')
('S', 'P', 'V', 'N', 'varr') ('S', 'V', 'P', 'N', 'varr')
('S', 'P', 'N', 'varr', 'V') ('S', 'N', 'varr', 'V', 'P')
('S', 'P', 'N', 'V', 'varr') ('V', 'S', 'P', 'N', 'varr')
>>> score(('varr', 'N', 'V', 'P', 'S'))
31
>>> score(('V', 'P', 'S', 'varr', 'N'))
31
>>> for order in itertools.permutations(['varr', 'V', 'N', 'P', 'S']):
	best= find_optimal_order(order)
	print(order,best,score(best))

	
('varr', 'V', 'N', 'P', 'S') ('varr', 'N', 'V', 'P', 'S') 31
('varr', 'V', 'N', 'S', 'P') ('varr', 'N', 'S', 'V', 'P') 31
('varr', 'V', 'P', 'N', 'S') ('varr', 'V', 'P', 'N', 'S') 31
('varr', 'V', 'P', 'S', 'N') ('V', 'P', 'S', 'varr', 'N') 31
('varr', 'V', 'S', 'N', 'P') ('V', 'P', 'S', 'varr', 'N') 31
('varr', 'V', 'S', 'P', 'N') ('V', 'S', 'P', 'N', 'varr') 31
('varr', 'N', 'V', 'P', 'S') ('varr', 'N', 'V', 'P', 'S') 31
('varr', 'N', 'V', 'S', 'P') ('varr', 'N', 'S', 'V', 'P') 31
('varr', 'N', 'P', 'V', 'S') ('varr', 'N', 'V', 'P', 'S') 31
('varr', 'N', 'P', 'S', 'V') ('varr', 'N', 'S', 'V', 'P') 31
('varr', 'N', 'S', 'V', 'P') ('varr', 'N', 'S', 'V', 'P') 31
('varr', 'N', 'S', 'P', 'V') ('varr', 'N', 'S', 'V', 'P') 31
('varr', 'P', 'V', 'N', 'S') ('varr', 'V', 'P', 'N', 'S') 31
('varr', 'P', 'V', 'S', 'N') ('V', 'P', 'S', 'varr', 'N') 31
('varr', 'P', 'N', 'V', 'S') ('varr', 'N', 'V', 'P', 'S') 31
('varr', 'P', 'N', 'S', 'V') ('varr', 'N', 'S', 'V', 'P') 31
('varr', 'P', 'S', 'V', 'N') ('S', 'V', 'P', 'N', 'varr') 31
('varr', 'P', 'S', 'N', 'V') ('V', 'P', 'S', 'varr', 'N') 31
('varr', 'S', 'V', 'N', 'P') ('varr', 'N', 'S', 'V', 'P') 31
('varr', 'S', 'V', 'P', 'N') ('S', 'V', 'P', 'N', 'varr') 31
('varr', 'S', 'N', 'V', 'P') ('S', 'N', 'varr', 'V', 'P') 31
('varr', 'S', 'N', 'P', 'V') ('S', 'N', 'varr', 'V', 'P') 31
('varr', 'S', 'P', 'V', 'N') ('S', 'V', 'P', 'N', 'varr') 31
('varr', 'S', 'P', 'N', 'V') ('S', 'N', 'varr', 'V', 'P') 31
('V', 'varr', 'N', 'P', 'S') ('varr', 'N', 'V', 'P', 'S') 31
('V', 'varr', 'N', 'S', 'P') ('varr', 'N', 'S', 'V', 'P') 31
('V', 'varr', 'P', 'N', 'S') ('varr', 'V', 'P', 'N', 'S') 31
('V', 'varr', 'P', 'S', 'N') ('V', 'P', 'S', 'varr', 'N') 31
('V', 'varr', 'S', 'N', 'P') ('V', 'P', 'S', 'varr', 'N') 31
('V', 'varr', 'S', 'P', 'N') ('V', 'S', 'P', 'N', 'varr') 31
('V', 'N', 'varr', 'P', 'S') ('N', 'varr', 'V', 'P', 'S') 31
('V', 'N', 'varr', 'S', 'P') ('V', 'P', 'N', 'varr', 'S') 31
('V', 'N', 'P', 'varr', 'S') ('V', 'P', 'N', 'varr', 'S') 31
('V', 'N', 'P', 'S', 'varr') ('V', 'P', 'N', 'S', 'varr') 31
('V', 'N', 'S', 'varr', 'P') ('V', 'P', 'N', 'S', 'varr') 31
('V', 'N', 'S', 'P', 'varr') ('V', 'S', 'P', 'N', 'varr') 31
('V', 'P', 'varr', 'N', 'S') ('V', 'P', 'varr', 'N', 'S') 31
('V', 'P', 'varr', 'S', 'N') ('V', 'P', 'S', 'varr', 'N') 31
('V', 'P', 'N', 'varr', 'S') ('V', 'P', 'N', 'varr', 'S') 31
('V', 'P', 'N', 'S', 'varr') ('V', 'P', 'N', 'S', 'varr') 31
('V', 'P', 'S', 'varr', 'N') ('V', 'P', 'S', 'varr', 'N') 31
('V', 'P', 'S', 'N', 'varr') ('V', 'S', 'P', 'N', 'varr') 31
('V', 'S', 'varr', 'N', 'P') ('V', 'P', 'S', 'varr', 'N') 31
('V', 'S', 'varr', 'P', 'N') ('V', 'S', 'P', 'N', 'varr') 31
('V', 'S', 'N', 'varr', 'P') ('S', 'N', 'varr', 'V', 'P') 31
('V', 'S', 'N', 'P', 'varr') ('V', 'S', 'P', 'N', 'varr') 31
('V', 'S', 'P', 'varr', 'N') ('V', 'P', 'S', 'varr', 'N') 31
('V', 'S', 'P', 'N', 'varr') ('V', 'S', 'P', 'N', 'varr') 31
('N', 'varr', 'V', 'P', 'S') ('N', 'varr', 'V', 'P', 'S') 31
('N', 'varr', 'V', 'S', 'P') ('S', 'N', 'varr', 'V', 'P') 31
('N', 'varr', 'P', 'V', 'S') ('N', 'varr', 'V', 'P', 'S') 31
('N', 'varr', 'P', 'S', 'V') ('N', 'varr', 'V', 'P', 'S') 31
('N', 'varr', 'S', 'V', 'P') ('varr', 'N', 'S', 'V', 'P') 31
('N', 'varr', 'S', 'P', 'V') ('varr', 'N', 'S', 'V', 'P') 31
('N', 'V', 'varr', 'P', 'S') ('N', 'varr', 'V', 'P', 'S') 31
('N', 'V', 'varr', 'S', 'P') ('S', 'N', 'varr', 'V', 'P') 31
('N', 'V', 'P', 'varr', 'S') ('V', 'P', 'N', 'varr', 'S') 31
('N', 'V', 'P', 'S', 'varr') ('V', 'P', 'N', 'S', 'varr') 31
('N', 'V', 'S', 'varr', 'P') ('V', 'P', 'S', 'varr', 'N') 31
('N', 'V', 'S', 'P', 'varr') ('V', 'S', 'P', 'N', 'varr') 31
('N', 'P', 'varr', 'V', 'S') ('N', 'varr', 'V', 'P', 'S') 31
('N', 'P', 'varr', 'S', 'V') ('varr', 'N', 'S', 'V', 'P') 31
('N', 'P', 'V', 'varr', 'S') ('varr', 'N', 'V', 'P', 'S') 31
('N', 'P', 'V', 'S', 'varr') ('V', 'P', 'S', 'varr', 'N') 31
('N', 'P', 'S', 'varr', 'V') ('S', 'N', 'varr', 'V', 'P') 31
('N', 'P', 'S', 'V', 'varr') ('S', 'V', 'P', 'N', 'varr') 31
('N', 'S', 'varr', 'V', 'P') ('S', 'N', 'varr', 'V', 'P') 31
('N', 'S', 'varr', 'P', 'V') ('S', 'N', 'varr', 'V', 'P') 31
('N', 'S', 'V', 'varr', 'P') ('varr', 'N', 'S', 'V', 'P') 31
('N', 'S', 'V', 'P', 'varr') ('S', 'V', 'P', 'N', 'varr') 31
('N', 'S', 'P', 'varr', 'V') ('S', 'N', 'varr', 'V', 'P') 31
('N', 'S', 'P', 'V', 'varr') ('S', 'V', 'P', 'N', 'varr') 31
('P', 'varr', 'V', 'N', 'S') ('varr', 'V', 'P', 'N', 'S') 31
('P', 'varr', 'V', 'S', 'N') ('V', 'S', 'P', 'N', 'varr') 31
('P', 'varr', 'N', 'V', 'S') ('varr', 'N', 'V', 'P', 'S') 31
('P', 'varr', 'N', 'S', 'V') ('varr', 'N', 'S', 'V', 'P') 31
('P', 'varr', 'S', 'V', 'N') ('S', 'V', 'P', 'N', 'varr') 31
('P', 'varr', 'S', 'N', 'V') ('V', 'P', 'N', 'varr', 'S') 31
('P', 'V', 'varr', 'N', 'S') ('V', 'P', 'varr', 'N', 'S') 31
('P', 'V', 'varr', 'S', 'N') ('V', 'P', 'S', 'varr', 'N') 31
('P', 'V', 'N', 'varr', 'S') ('V', 'P', 'N', 'varr', 'S') 31
('P', 'V', 'N', 'S', 'varr') ('V', 'P', 'N', 'S', 'varr') 31
('P', 'V', 'S', 'varr', 'N') ('V', 'P', 'S', 'varr', 'N') 31
('P', 'V', 'S', 'N', 'varr') ('V', 'S', 'P', 'N', 'varr') 31
('P', 'N', 'varr', 'V', 'S') ('N', 'varr', 'V', 'P', 'S') 31
('P', 'N', 'varr', 'S', 'V') ('V', 'P', 'N', 'varr', 'S') 31
('P', 'N', 'V', 'varr', 'S') ('V', 'P', 'N', 'varr', 'S') 31
('P', 'N', 'V', 'S', 'varr') ('V', 'P', 'N', 'S', 'varr') 31
('P', 'N', 'S', 'varr', 'V') ('V', 'P', 'N', 'S', 'varr') 31
('P', 'N', 'S', 'V', 'varr') ('V', 'P', 'N', 'S', 'varr') 31
('P', 'S', 'varr', 'V', 'N') ('V', 'P', 'S', 'varr', 'N') 31
('P', 'S', 'varr', 'N', 'V') ('V', 'P', 'S', 'varr', 'N') 31
('P', 'S', 'V', 'varr', 'N') ('V', 'P', 'S', 'varr', 'N') 31
('P', 'S', 'V', 'N', 'varr') ('S', 'V', 'P', 'N', 'varr') 31
('P', 'S', 'N', 'varr', 'V') ('S', 'N', 'varr', 'V', 'P') 31
('P', 'S', 'N', 'V', 'varr') ('V', 'S', 'P', 'N', 'varr') 31
('S', 'varr', 'V', 'N', 'P') ('S', 'N', 'varr', 'V', 'P') 31
('S', 'varr', 'V', 'P', 'N') ('varr', 'V', 'P', 'N', 'S') 31
('S', 'varr', 'N', 'V', 'P') ('varr', 'N', 'S', 'V', 'P') 31
('S', 'varr', 'N', 'P', 'V') ('varr', 'N', 'S', 'V', 'P') 31
('S', 'varr', 'P', 'V', 'N') ('varr', 'V', 'P', 'N', 'S') 31
('S', 'varr', 'P', 'N', 'V') ('varr', 'N', 'S', 'V', 'P') 31
('S', 'V', 'varr', 'N', 'P') ('V', 'P', 'S', 'varr', 'N') 31
('S', 'V', 'varr', 'P', 'N') ('S', 'V', 'P', 'N', 'varr') 31
('S', 'V', 'N', 'varr', 'P') ('S', 'N', 'varr', 'V', 'P') 31
('S', 'V', 'N', 'P', 'varr') ('S', 'V', 'P', 'N', 'varr') 31
('S', 'V', 'P', 'varr', 'N') ('V', 'P', 'S', 'varr', 'N') 31
('S', 'V', 'P', 'N', 'varr') ('S', 'V', 'P', 'N', 'varr') 31
('S', 'N', 'varr', 'V', 'P') ('S', 'N', 'varr', 'V', 'P') 31
('S', 'N', 'varr', 'P', 'V') ('S', 'N', 'varr', 'V', 'P') 31
('S', 'N', 'V', 'varr', 'P') ('S', 'N', 'varr', 'V', 'P') 31
('S', 'N', 'V', 'P', 'varr') ('S', 'V', 'P', 'N', 'varr') 31
('S', 'N', 'P', 'varr', 'V') ('S', 'N', 'varr', 'V', 'P') 31
('S', 'N', 'P', 'V', 'varr') ('S', 'N', 'varr', 'V', 'P') 31
('S', 'P', 'varr', 'V', 'N') ('V', 'P', 'S', 'varr', 'N') 31
('S', 'P', 'varr', 'N', 'V') ('varr', 'N', 'S', 'V', 'P') 31
('S', 'P', 'V', 'varr', 'N') ('V', 'P', 'S', 'varr', 'N') 31
('S', 'P', 'V', 'N', 'varr') ('S', 'V', 'P', 'N', 'varr') 31
('S', 'P', 'N', 'varr', 'V') ('S', 'N', 'varr', 'V', 'P') 31
('S', 'P', 'N', 'V', 'varr') ('V', 'S', 'P', 'N', 'varr') 31
>>> compile_function('EULER')
>>> counts = {}
>>> for order in itertools.permutations(['F','f','N','n','Q','E','varr']):
	best_score = score(find_optimal_order(order))
	if not best_score in counts:
		counts[best_score]=0
	counts[best_score]+=1

	
>>> counts
{63: 1372, 62: 1775, 61: 934, 66: 137, 64: 737, 65: 85}
>>> sum(counts.values())
5040
>>> 934/5040
0.18531746031746033
>>> (934+1775)/5040
0.5375
>>> find_optimal_order(order)
('Q', 'E', 'N', 'n', 'f', 'F', 'varr')
>>> find_optimal_order(order)
('Q', 'E', 'N', 'n', 'f', 'F', 'varr')
>>> score(('Q', 'E', 'N', 'n', 'f', 'F', 'varr'))
63
>>> for _ in range(10):
	find_optimal_order(order)

	
('Q', 'E', 'N', 'n', 'f', 'F', 'varr')
('Q', 'E', 'N', 'n', 'f', 'F', 'varr')
('Q', 'E', 'N', 'n', 'f', 'F', 'varr')
('Q', 'E', 'N', 'n', 'f', 'F', 'varr')
('Q', 'E', 'N', 'n', 'f', 'F', 'varr')
('Q', 'E', 'N', 'n', 'f', 'F', 'varr')
('Q', 'E', 'N', 'n', 'f', 'F', 'varr')
('Q', 'E', 'N', 'n', 'f', 'F', 'varr')
('Q', 'E', 'N', 'n', 'f', 'F', 'varr')
('Q', 'E', 'N', 'n', 'f', 'F', 'varr')
>>> def find_optimal_order(order):
    best_order = None
    original_score = score(order)
    best_score = original_score
    for a in range(len(order)):
        for b in range(len(order)+1):
            new_order = move_element(order,a,b)
            if new_order and not new_order in explored_orders:
		explored_orders.add(new_order)
		new_score = score(new_order)
                if new_score<=best_score:
		    new_order,new_score = find_optimal_order(new_order)
                    if new_score<best_score:
			best_score = new_score
			best_order = new_order		    
    if best_score<original_score:
        return best_order,best_score
    else:
        return order,original_score
SyntaxError: inconsistent use of tabs and spaces in indentation
def find_optimal_order(order):
    best_order = None
    original_score = score(order)
    best_score = original_score
    for a in range(len(order)):
        for b in range(len(order)+1):
            new_order = move_element(order,a,b)
            if new_order and not new_order in explored_orders:
		explored_orders.add(new_order)
		new_score = score(new_order)
                if new_score<=best_score:
		    new_order,new_score = find_optimal_order(new_order)
                    if new_score<best_score:
			best_score = new_score
			best_order = new_order
    if best_score<original_score:
        return best_order,best_score
    else:
        return order,original_score
>>> def find_optimal_order(order):
    best_order = None
    original_score = score(order)
    best_score = original_score
    for a in range(len(order)):
        for b in range(len(order)+1):
            new_order = move_element(order,a,b)
            if new_order and not new_order in explored_orders:
                explored_orders.add(new_order)
                new_score = score(new_order)
                if new_score<=best_score:
                    new_order,new_score = find_optimal_order(new_order)
                    if new_score<best_score:
                        best_score = new_score
                        best_order = new_order		    
    if best_score<original_score:
        return best_order,best_score
    else:
        return order,original_score

>>> counts = []
>>> counts= {}
>>> k = 0
>>> for order in itertools.permutations(['F','f','N','n','Q','E','varr']):
	if k%100==0:
		print(k)
	best_order,best_score = find_optimal_order(order)
	if not best_score in counts:
		counts[best_score]=0
	counts[best_score]+=1
	k+=1

	
0
Traceback (most recent call last):
  File "<pyshell#1248>", line 4, in <module>
    best_order,best_score = find_optimal_order(order)
  File "<pyshell#1242>", line 8, in find_optimal_order
    if new_order and not new_order in explored_orders:
NameError: name 'explored_orders' is not defined
>>> explored_orders = {}
>>> explored_orders = set()
>>> for order in itertools.permutations(['F','f','N','n','Q','E','varr']):
	if k%100==0:
		print(k)
	best_order,best_score = find_optimal_order(order)
	if not best_score in counts:
		counts[best_score]=0
	counts[best_score]+=1
	k+=1

	
0
100
200
300
Traceback (most recent call last):
  File "<pyshell#1252>", line 4, in <module>
    best_order,best_score = find_optimal_order(order)
  File "<pyshell#1242>", line 10, in find_optimal_order
    new_score = score(new_order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 622, in score
    new_score = score(new_order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 550, in symbol2int
    return order.index(symbol.symbol)+symbol.offset
KeyboardInterrupt
>>> for order in itertools.permutations(['F','f','N','n','Q','E','varr']):
	if k%100==0:
		print(k)
	explored_orders = set()
	best_order,best_score = find_optimal_order(order)
	if not best_score in counts:
		counts[best_score]=0
	counts[best_score]+=1
	k+=1

	
Traceback (most recent call last):
  File "<pyshell#1254>", line 5, in <module>
    best_order,best_score = find_optimal_order(order)
  File "<pyshell#1242>", line 12, in find_optimal_order
    new_order,new_score = find_optimal_order(new_order)
  File "<pyshell#1242>", line 12, in find_optimal_order
    new_order,new_score = find_optimal_order(new_order)
  File "<pyshell#1242>", line 12, in find_optimal_order
    new_order,new_score = find_optimal_order(new_order)
  [Previous line repeated 5 more times]
  File "<pyshell#1242>", line 10, in find_optimal_order
    new_score = score(new_order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 622, in score
    new_score = score(new_order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 550, in symbol2int
    return order.index(symbol.symbol)+symbol.offset
KeyboardInterrupt
>>> counts={}
>>> for order in itertools.permutations(['F','f','N','n','Q','E','varr']):
	if k%100==0:
		print(k)
	explored_orders = set()
	best_order,best_score = find_optimal_order(order)
	if not best_score in counts:
		counts[best_score]=0
	counts[best_score]+=1
	k+=1

	
400
500
600
700
800
900
1000
1100
1200
1300
1400
1500
1600
1700
1800
1900
2000
2100
2200
2300
2400
2500
2600
2700
2800
2900
3000
3100
3200
3300
3400
3500
3600
3700
3800
3900
4000
4100
4200
4300
4400
4500
4600
4700
4800
4900
5000
5100
5200
5300
5400
>>> sum(counts.values())
5040
>>> counts
{62: 2601, 61: 1783, 63: 112, 64: 544}
>>> 1783/5040
0.3537698412698413
>>> (1783+2601)/5040
0.8698412698412699
>>> for _ in range(10):
	find_optimal_order(order)

	
(('varr', 'E', 'Q', 'n', 'N', 'f', 'F'), 72)
(('varr', 'E', 'Q', 'n', 'N', 'f', 'F'), 72)
(('varr', 'E', 'Q', 'n', 'N', 'f', 'F'), 72)
(('varr', 'E', 'Q', 'n', 'N', 'f', 'F'), 72)
(('varr', 'E', 'Q', 'n', 'N', 'f', 'F'), 72)
(('varr', 'E', 'Q', 'n', 'N', 'f', 'F'), 72)
(('varr', 'E', 'Q', 'n', 'N', 'f', 'F'), 72)
(('varr', 'E', 'Q', 'n', 'N', 'f', 'F'), 72)
(('varr', 'E', 'Q', 'n', 'N', 'f', 'F'), 72)
(('varr', 'E', 'Q', 'n', 'N', 'f', 'F'), 72)
>>> for _ in range(10):
	explored_orders = set()
	find_optimal_order(order)

	
(('Q', 'E', 'N', 'n', 'f', 'F', 'varr'), 63)
(('Q', 'E', 'N', 'n', 'f', 'F', 'varr'), 63)
(('Q', 'E', 'N', 'n', 'f', 'F', 'varr'), 63)
(('Q', 'E', 'N', 'n', 'f', 'F', 'varr'), 63)
(('Q', 'E', 'N', 'n', 'f', 'F', 'varr'), 63)
(('Q', 'E', 'N', 'n', 'f', 'F', 'varr'), 63)
(('Q', 'E', 'N', 'n', 'f', 'F', 'varr'), 63)
(('Q', 'E', 'N', 'n', 'f', 'F', 'varr'), 63)
(('Q', 'E', 'N', 'n', 'f', 'F', 'varr'), 63)
(('Q', 'E', 'N', 'n', 'f', 'F', 'varr'), 63)
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2020, 7, 5, 13, 59, 59, 381359)
>>> def test():
	start = datetime.now()
	for _ in range(10):
		random.shuffle(order)
		explored_orders = set()
		find_optimal_order(order)
	print(datetime.now()-start)

	
>>> test()
Traceback (most recent call last):
  File "<pyshell#1273>", line 1, in <module>
    test()
  File "<pyshell#1272>", line 4, in test
    random.shuffle(order)
NameError: name 'random' is not defined
>>> from random import shuffle
>>> def test():
	start = datetime.now()
	for _ in range(10):
		shuffle(order)
		explored_orders = set()
		find_optimal_order(order)
	print(datetime.now()-start)

	
>>> test()
Traceback (most recent call last):
  File "<pyshell#1277>", line 1, in <module>
    test()
  File "<pyshell#1276>", line 4, in test
    shuffle(order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\random.py", line 278, in shuffle
    x[i], x[j] = x[j], x[i]
TypeError: 'tuple' object does not support item assignment
>>> order
('varr', 'E', 'Q', 'n', 'N', 'f', 'F')
>>> order = list(order)
>>> test()
Traceback (most recent call last):
  File "<pyshell#1280>", line 1, in <module>
    test()
  File "<pyshell#1276>", line 6, in test
    find_optimal_order(order)
  File "<pyshell#1242>", line 8, in find_optimal_order
    if new_order and not new_order in explored_orders:
TypeError: unhashable type: 'list'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
KeyboardInterrupt
>>> 
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER')
>>> order=['varr', 'E', 'Q', 'n', 'N', 'f', 'F']
>>> from random import shuffle
>>> from datetime import datetime
>>> 
>>> def test():
	start = datetime.now()
	for _ in range(10):
		shuffle(order)
		explored_orders = set()
		find_optimal_order(order)
	print(datetime.now()-start)

	
>>> test()
Traceback (most recent call last):
  File "<pyshell#1288>", line 1, in <module>
    test()
  File "<pyshell#1287>", line 6, in test
    find_optimal_order(order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 620, in find_optimal_order
    if new_order and not tuple(new_order) in explored_orders:
NameError: name 'explored_orders' is not defined
>>> global explored_orders
>>> def find_optimal_order(order):
    global explored_orders
    best_order = None
    original_score = score(order)
    best_score = original_score
    for a in range(len(order)):
        for b in range(len(order)+1):
            new_order = move_element(order,a,b)
            if new_order and not tuple(new_order) in explored_orders:
                explored_orders.add(tuple(new_order))
                new_score = score(new_order)
                if new_score<=best_score:
                    new_order,new_score = find_optimal_order(new_order)
                    if new_score<best_score:
                        best_score = new_score
                        best_order = new_order		    
    if best_score<original_score:
        return best_order,best_score
    else:
        return order,original_score

>>> def test():
	global explored_orders
	start = datetime.now()
	for _ in range(10):
		shuffle(order)
		explored_orders = set()
		find_optimal_order(order)
	print(datetime.now()-start)

	
>>> test()
0:00:04.640567
>>> def find_optimal_order(order):
    best_order = order
    original_score = score(order)
    best_score = original_score
    for a in range(len(order)):
        for b in range(len(order)+1):
            new_order = move_element(order,a,b)
            if new_order:
                new_score = score(new_order)
                if new_score<best_score:
                    best_score = new_score
                    best_order = new_order
    if best_score<original_score:
        return find_optimal_order(best_order)
    else:
        return order

>>> test()
0:00:01.814150
>>> def find_optimal_order(order):
    global explored_orders
    best_order = None
    original_score = score(order)
    best_score = original_score
    for a in range(len(order)):
        for b in range(len(order)+1):
            new_order = move_element(order,a,b)
            if new_order and not tuple(new_order) in explored_orders:
                explored_orders.add(tuple(new_order))
                new_score = score(new_order)
                if new_score<best_score:
                    new_order,new_score = find_optimal_order(new_order)
                    if new_score<best_score:
                        best_score = new_score
                        best_order = new_order		    
    if best_score<original_score:
        return best_order,best_score
    else:
        return order,original_score

>>> test()
0:00:02.919194
>>> counts={}
>>> k=0
>>> for order in itertools.permutations(['F','f','N','n','Q','E','varr']):
	if k%100==0:
		print(k)
	explored_orders = set()
	best_order,best_score = find_optimal_order(order)
	if not best_score in counts:
		counts[best_score]=0
	counts[best_score]+=1
	k+=1

	
Traceback (most recent call last):
  File "<pyshell#1304>", line 1, in <module>
    for order in itertools.permutations(['F','f','N','n','Q','E','varr']):
NameError: name 'itertools' is not defined
>>> import itertools
>>> for order in itertools.permutations(['F','f','N','n','Q','E','varr']):
	if k%100==0:
		print(k)
	explored_orders = set()
	best_order,best_score = find_optimal_order(order)
	if not best_score in counts:
		counts[best_score]=0
	counts[best_score]+=1
	k+=1

	
0
100
200
300
400
500
600
700
800
900
1000
1100
1200
1300
1400
1500
1600
1700
1800
1900
2000
2100
2200
2300
2400
2500
2600
2700
2800
2900
3000
3100
3200
3300
3400
3500
3600
3700
3800
3900
4000
4100
4200
4300
4400
4500
4600
4700
4800
4900
5000
>>> counts
{62: 2019, 61: 933, 63: 1296, 64: 699, 65: 61, 66: 32}
>>> 1-.185
0.815
>>> 0.815**7
0.23883790946995825
>>> 0.815**14
0.057043546999979974
>>> to_symbols
{129: Sym('F'+0), 130: Sym('F'+0), 133: Sym('F'+0), 134: Sym('F'+0), 137: Sym('F'+0), 138: Sym('F'+0), 141: Sym('n'+0), 145: Sym('n'+0), 149: Sym('N'+0), 150: Sym('N'+0), 153: Sym('N'+0), 154: Sym('N'+0), 157: Sym('n'+0), 158: Sym('n'+0), 165: Sym('N'+0), 166: Sym('N'+0), 169: Sym('n'+0), 170: Sym('n'+0), 173: Sym('F'+0), 174: Sym('F'+0), 177: Sym('f'+0), 178: Sym('f'+0), 185: Sym('F'+0), 186: Sym('F'+0), 189: Sym('f'+0), 190: Sym('f'+0), 193: Sym('n'+0), 194: Sym('n'+0), 197: Sym('f'+0), 198: Sym('f'+0), 201: Sym('n'+0), 205: Sym('n'+0), 206: Sym('n'+0), 209: Sym('f'+0), 210: Sym('f'+0), 213: Sym('F'+0), 214: Sym('F'+0), 215: Sym('F'+0), 221: Sym('f'+0), 222: Sym('f'+0), 225: Sym('F'+0), 226: Sym('F'+0), 230: Sym('varr'+0), 233: Sym('varr'+0), 234: Sym('varr'+0), 237: Sym('Q'+1), 238: Sym('Q'+1), 241: Sym('Q'+0), 245: Sym('varr'+1), 246: Sym('varr'+1), 249: Sym('F'+1), 250: Sym('F'+1), 253: Sym('varr'+0), 254: Sym('varr'+0), 257: Sym('F'+0), 258: Sym('F'+0), 261: Sym('F'+0), 262: Sym('F'+0), 265: Sym('varr'+0), 266: Sym('varr'+0), 273: Sym('F'+0), 274: Sym('F'+0), 277: Sym('varr'+0), 278: Sym('varr'+0), 281: Sym('Q'+0), 282: Sym('Q'+0), 285: Sym('E'+0), 286: Sym('E'+0), 287: Sym('E'+0), 293: Sym('Q'+0), 294: Sym('Q'+0), 297: Sym('E'+0), 298: Sym('E'+0)}
>>> from_symbols
{153: {0, Sym('n'+0.5), Sym('N'+1)}, 129: {Sym('n'+1), Sym('F'+0.0)}, 133: {Sym('F'+1)}, 130: {Sym('n'+1), Sym('F'+0.0)}, 134: {Sym('F'+1)}, 178: {Sym('F'+0.5)}, 185: {Sym('F'+0.0), Sym('F'+1), Sym('f'+1)}, 186: {Sym('F'+0.0), Sym('F'+1), Sym('f'+1)}, 137: {Sym('F'+0.0), Sym('f'+1)}, 193: {Sym('F'+1), Sym('f'+1)}, 138: {Sym('F'+0.0), Sym('f'+1)}, 194: {Sym('F'+1)}, 141: {Sym('n'+1), Sym('n'+0.0)}, 145: {Sym('n'+1), Sym('n'+0.0)}, 173: {Sym('n'+0.5), Sym('f'+0.5)}, 230: {Sym('n'+1), Sym('varr'+0.0)}, 149: {Sym('E'+1), Sym('N'+0.0)}, 150: {Sym('E'+1), Sym('N'+0.0)}, 157: {Sym('N'+0.5)}, 158: {Sym('N'+0.5)}, 165: {Sym('n'+1), Sym('N'+1), Sym('N'+0.0)}, 166: {Sym('n'+1), Sym('N'+1), Sym('N'+0.0)}, 154: {Sym('n'+0.5)}, 169: {Sym('n'+0.0), Sym('N'+1)}, 170: {Sym('n'+0.0), Sym('N'+1)}, 177: {Sym('F'+0.5)}, 174: {Sym('f'+0.5)}, 189: {Sym('f'+0.0), Sym('F'+1)}, 190: {Sym('f'+0.0), Sym('F'+1)}, 197: {Sym('n'+0.5), Sym('f'+0.0), Sym('F'+1)}, 209: {Sym('F'+0.5), Sym('n'+0.5)}, 205: {Sym('n'+1), Sym('n'+0.0)}, 206: {Sym('n'+1), Sym('n'+0.5), Sym('n'+0.0), Sym('F'+1)}, 198: {Sym('f'+0.0)}, 201: {Sym('f'+1)}, 213: {Sym('f'+0.5)}, 214: {Sym('f'+0.5)}, 221: {Sym('f'+0.0), Sym('F'+1), Sym('f'+1)}, 215: {Sym('f'+0.5)}, 222: {Sym('f'+0.0), Sym('F'+1), Sym('f'+1)}, 210: {Sym('F'+0.5)}, 225: {Sym('F'+0.0), Sym('f'+1)}, 226: {Sym('F'+0.0), Sym('f'+1)}, 234: {Sym('Q'+0.5), Sym('varr'+1), Sym('varr'+0.0)}, 233: {Sym('varr'+1), Sym('varr'+0.0)}, 245: {Sym('varr'+1), Sym('F'+0.5)}, 246: {Sym('varr'+1)}, 261: {Sym('Q'+0.5), Sym('varr'+0.5)}, 241: {Sym('Q'+0)}, 281: {Sym('E'+0.5), Sym('Q'+1)}, 249: {Sym('varr'+0.5)}, 250: {Sym('varr'+0.5)}, 253: {Sym('F'+0), Sym('F'+0.5), Sym('varr'+0)}, 254: {Sym('F'+0.5), Sym('F'+0), Sym('varr'+0)}, 257: {Sym('varr'+1), Sym('F'+0.0)}, 258: {Sym('varr'+1), Sym('F'+0.0)}, 237: {Sym('F'+1)}, 238: {Sym('F'+1)}, 265: {Sym('F'+0.5)}, 266: {Sym('F'+0.5)}, 273: {Sym('varr'+1), Sym('F'+0.0), Sym('F'+1)}, 274: {Sym('varr'+1), Sym('F'+0.0), Sym('F'+1)}, 262: {Sym('varr'+0.5)}, 277: {Sym('F'+1), Sym('varr'+0.0)}, 278: {Sym('F'+1), Sym('varr'+0.0)}, 285: {Sym('Q'+0.5)}, 286: {Sym('Q'+0.5)}, 293: {Sym('Q'+0.0), Sym('E'+1), Sym('Q'+1)}, 287: {Sym('Q'+0.5)}, 294: {Sym('Q'+0.0), Sym('E'+1), Sym('Q'+1)}, 282: {Sym('E'+0.5)}, 297: {Sym('E'+0.0), Sym('Q'+1)}, 298: {Sym('E'+0.0), Sym('Q'+1)}}
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER')
Traceback (most recent call last):
  File "<pyshell#1314>", line 1, in <module>
    compile_function('EULER')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 527, in compile_function
    states2searches()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 592, in states2searches
    if not k in transition_symbols:
NameError: name 'transition_symbols' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> transition_symbols[153]
Traceback (most recent call last):
  File "<pyshell#1315>", line 1, in <module>
    transition_symbols[153]
NameError: name 'transition_symbols' is not defined
>>> transition_symbols
Traceback (most recent call last):
  File "<pyshell#1316>", line 1, in <module>
    transition_symbols
NameError: name 'transition_symbols' is not defined
>>> compile_function('EULER')
Traceback (most recent call last):
  File "<pyshell#1317>", line 1, in <module>
    compile_function('EULER')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 527, in compile_function
    states2searches()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 594, in states2searches
    transitions_symbols[k] = {}
NameError: name 'transitions_symbols' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER')
Traceback (most recent call last):
  File "<pyshell#1318>", line 1, in <module>
    compile_function('EULER')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 527, in compile_function
    states2searches()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 594, in states2searches
    transitions_symbols[transition[2]] = {}
NameError: name 'transitions_symbols' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER')
>>> transition_symbols[153]
{149: Sym('N'+1), 157: Sym('n'+0.5)}
>>> from_symbols.keys()==transition_symbols.keys()
True
>>> for k in from_symbols:
	if from_symbols[k]!=set(transition_symbols[k].values()):
		print(k)

		
153
>>> from_symbols[153]
{0, Sym('N'+1), Sym('n'+0.5)}
>>> quasis[0]
End(is_start=True, next_quasis=[153])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER')
Traceback (most recent call last):
  File "<pyshell#1328>", line 1, in <module>
    compile_function('EULER')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 527, in compile_function
    states2searches()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 578, in states2searches
    transition_symbols[quasis[0]] = {0:0}
NameError: name 'transition_symbols' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER')
Traceback (most recent call last):
  File "<pyshell#1329>", line 1, in <module>
    compile_function('EULER')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 527, in compile_function
    states2searches()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 578, in states2searches
    transition_symbols = {quasis[0]:{0:0}}
TypeError: unhashable type: 'End'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER')
>>> {key:set(value.values()) for key,value in transition_symbols.items()}==from_symbols
True
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER')
Traceback (most recent call last):
  File "<pyshell#1332>", line 1, in <module>
    compile_function('EULER')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 529, in compile_function
    best_score = score(order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 636, in score
    offset = symbol2int(to_symbol,order) - symbol2int(from_symbol,order)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 559, in symbol2int
    return order.index(symbol.symbol)+symbol.offset
AttributeError: 'NoneType' object has no attribute 'index'
>>> compile_function('EULER',order=['N','n','F','f','Q','varr','E'])
Traceback (most recent call last):
  File "<pyshell#1333>", line 1, in <module>
    compile_function('EULER',order=['N','n','F','f','Q','varr','E'])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 531, in compile_function
    shuffle(order)
NameError: name 'shuffle' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER',order=['N','n','F','f','Q','varr','E'])
>>> best_order
Traceback (most recent call last):
  File "<pyshell#1335>", line 1, in <module>
    best_order
NameError: name 'best_order' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER',order=['N','n','F','f','Q','varr','E'])
['f', 'F', 'varr', 'Q', 'E', 'N', 'n']
>>> score(['f', 'F', 'varr', 'Q', 'E', 'N', 'n'])
61
>>> len(rules)
363
>>> for key,value in rules.items():
	print(rules)

	






Traceback (most recent call last):
  File "<pyshell#1341>", line 2, in <module>
    print(rules)
KeyboardInterrupt
>>> for key,value in rules.items():
	print(key,value)

	
('129', '0') ('129', '0', 'R')
('129', '1') ('129', '0', 'R')
('129', "0'") ('129', '0', 'R')
('129', "1'") ('129', '0', 'R')
('129', 'varr') ('133L', None, 'L')
('130', '0') ('130', '0', 'R')
('130', '1') ('130', '0', 'R')
('130', "0'") ('130', '0', 'R')
('130', "1'") ('130', '0', 'R')
('130', 'varr') ('134L', None, 'L')
('133', '0') ('178L', "1'", 'L')
('133', '1') ('178L', "1'", 'L')
('133', "0'") ('133', "0'", 'R')
('133', "1'") ('133', "1'", 'R')
('133', 'varr') ('185L', None, 'L')
('134', '0') ('178L', "1'", 'L')
('134', '1') ('178L', "1'", 'L')
('134', "0'") ('134', "0'", 'R')
('134', "1'") ('134', "1'", 'R')
('134', 'varr') ('186L', None, 'L')
('137', '0') ('137', '0', 'R')
('137', '1') ('137', '0', 'R')
('137', "0'") ('137', '0', 'R')
('137', "1'") ('137', '0', 'R')
('137', 'varr') ('193R', None, 'R')
('138', '0') ('138', '0', 'R')
('138', '1') ('138', '0', 'R')
('138', "0'") ('138', '0', 'R')
('138', "1'") ('138', '0', 'R')
('138', 'varr') ('194R', None, 'R')
('141', '0') ('141', '0', 'R')
('141', '1') ('141', '1', 'R')
('141', "0'") ('141', '0', 'R')
('141', "1'") ('141', '1', 'R')
('141', 'f') ('145L', None, 'L')
('145', '0') ('145', '0', 'R')
('145', '1') ('173L', '1', 'L')
('145', 'f') ('230L', None, 'L')
('149', '0') ('149', '0', 'R')
('149', '1') ('149', '1', 'R')
('149', "0'") ('149', '0', 'R')
('149', "1'") ('149', '1', 'R')
('149', 'n') ('153L', None, 'L')
('150', '0') ('149', '1', 'R')
('150', '1') ('150', '0', 'R')
('150', "0'") ('149', '1', 'R')
('150', "1'") ('150', '0', 'R')
('150', 'n') ('halt', None, '')
('153', '0') ('157R', "0'", 'R')
('153', '1') ('158R', "1'", 'R')
('153', "0'") ('153', "0'", 'R')
('153', "1'") ('153', "1'", 'R')
('153', 'n') ('165L', None, 'L')
('154', '0') ('157R', "0'", 'R')
('154', '1') ('158R', "1'", 'R')
('154', "0'") ('154', "0'", 'R')
('154', "1'") ('154', "1'", 'R')
('154', 'n') ('166L', None, 'L')
('157', '0') ('153L', "0'", 'L')
('157', '1') ('153L', "0'", 'L')
('157', "0'") ('157', "0'", 'R')
('157', "1'") ('157', "1'", 'R')
('157', 'f') ('165L', None, 'L')
('158', '0') ('154L', "1'", 'L')
('158', '1') ('154L', "1'", 'L')
('158', "0'") ('158', "0'", 'R')
('158', "1'") ('158', "1'", 'R')
('158', 'f') ('166L', None, 'L')
('165', '0') ('165', '0', 'R')
('165', '1') ('165', '1', 'R')
('165', "0'") ('165', '0', 'R')
('165', "1'") ('165', '1', 'R')
('165', 'n') ('169', None, 'R')
('166', '0') ('166', '0', 'R')
('166', '1') ('166', '1', 'R')
('166', "0'") ('166', '0', 'R')
('166', "1'") ('166', '1', 'R')
('166', 'n') ('170', None, 'R')
('169', '0') ('169', '0', 'R')
('169', '1') ('169', '1', 'R')
('169', "0'") ('169', '0', 'R')
('169', "1'") ('169', '1', 'R')
('169', 'f') ('129L', None, 'L')
('170', '0') ('170', '0', 'R')
('170', '1') ('170', '1', 'R')
('170', "0'") ('170', '0', 'R')
('170', "1'") ('170', '1', 'R')
('170', 'f') ('130L', None, 'L')
('173', '0') ('177L', "0'", 'L')
('173', '1') ('178L', "1'", 'L')
('173', "0'") ('173', "0'", 'R')
('173', "1'") ('173', "1'", 'R')
('173', 'varr') ('185L', None, 'L')
('174', '0') ('177L', "0'", 'L')
('174', '1') ('178L', "1'", 'L')
('174', "0'") ('174', "0'", 'R')
('174', "1'") ('174', "1'", 'R')
('174', 'varr') ('186L', None, 'L')
('177', '0') ('173R', "0'", 'R')
('177', '1') ('173R', "0'", 'R')
('177', "0'") ('177', "0'", 'R')
('177', "1'") ('177', "1'", 'R')
('177', 'F') ('185', None, 'R')
('178', '0') ('174R', "1'", 'R')
('178', '1') ('174R', "1'", 'R')
('178', "0'") ('178', "0'", 'R')
('178', "1'") ('178', "1'", 'R')
('178', 'F') ('186', None, 'R')
('185', '0') ('185', '0', 'R')
('185', '1') ('185', '1', 'R')
('185', "0'") ('185', '0', 'R')
('185', "1'") ('185', '1', 'R')
('185', 'varr') ('189L', None, 'L')
('186', '0') ('186', '0', 'R')
('186', '1') ('186', '1', 'R')
('186', "0'") ('186', '0', 'R')
('186', "1'") ('186', '1', 'R')
('186', 'varr') ('190L', None, 'L')
('189', '0') ('189', '0', 'R')
('189', '1') ('189', '1', 'R')
('189', "0'") ('189', '0', 'R')
('189', "1'") ('189', '1', 'R')
('189', 'F') ('137', None, 'R')
('190', '0') ('190', '0', 'R')
('190', '1') ('190', '1', 'R')
('190', "0'") ('190', '0', 'R')
('190', "1'") ('190', '1', 'R')
('190', 'F') ('138', None, 'R')
('193', '0') ('197L', "0'", 'L')
('193', '1') ('209L', "1'", 'L')
('193', "0'") ('193', "0'", 'R')
('193', "1'") ('193', "1'", 'R')
('193', 'f') ('205L', None, 'L')
('194', '0') ('197L', "0'", 'L')
('194', '1') ('209L', "1'", 'L')
('194', "0'") ('194', "0'", 'R')
('194', "1'") ('194', "1'", 'R')
('194', 'f') ('206L', None, 'L')
('197', '0') ('197', '0', 'R')
('197', '1') ('198', '0', 'R')
('197', "0'") ('197', '0', 'R')
('197', "1'") ('198', '0', 'R')
('197', 'F') ('193R', None, 'R')
('198', '0') ('197', '1', 'R')
('198', '1') ('198', '1', 'R')
('198', "0'") ('197', '1', 'R')
('198', "1'") ('198', '1', 'R')
('198', 'F') ('201R', None, 'R')
('201', '0') ('201', "0'", 'R')
('201', '1') ('206L', "1'", 'L')
('201', "0'") ('201', "0'", 'R')
('201', "1'") ('201', "1'", 'R')
('201', 'f') ('205L', None, 'L')
('205', '0') ('205', '0', 'R')
('205', '1') ('205', '1', 'R')
('205', "0'") ('205', '0', 'R')
('205', "1'") ('205', '1', 'R')
('205', 'f') ('141L', None, 'L')
('206', '0') ('206', '0', 'R')
('206', '1') ('206', '1', 'R')
('206', "0'") ('206', '0', 'R')
('206', "1'") ('206', '1', 'R')
('206', 'f') ('halt', None, '')
('209', '0') ('213R', "0'", 'R')
('209', '1') ('214R', "1'", 'R')
('209', "0'") ('209', "0'", 'R')
('209', "1'") ('209', "1'", 'R')
('209', 'F') ('221L', None, 'L')
('210', '0') ('214R', "0'", 'R')
('210', '1') ('215R', "1'", 'R')
('210', "0'") ('210', "0'", 'R')
('210', "1'") ('210', "1'", 'R')
('210', 'F') ('222L', None, 'L')
('213', '0') ('209L', "0'", 'L')
('213', '1') ('209L', "1'", 'L')
('213', "0'") ('213', "0'", 'R')
('213', "1'") ('213', "1'", 'R')
('213', 'varr') ('221L', None, 'L')
('214', '0') ('209L', "1'", 'L')
('214', '1') ('210L', "0'", 'L')
('214', "0'") ('214', "0'", 'R')
('214', "1'") ('214', "1'", 'R')
('214', 'varr') ('222L', None, 'L')
('215', '0') ('210L', "0'", 'L')
('215', '1') ('210L', "1'", 'L')
('215', "0'") ('215', "0'", 'R')
('215', "1'") ('215', "1'", 'R')
('215', 'varr') ('222L', None, 'L')
('221', '0') ('221', '0', 'R')
('221', '1') ('221', '1', 'R')
('221', "0'") ('221', '0', 'R')
('221', "1'") ('221', '1', 'R')
('221', 'F') ('225', None, 'R')
('222', '0') ('222', '0', 'R')
('222', '1') ('222', '1', 'R')
('222', "0'") ('222', '0', 'R')
('222', "1'") ('222', '1', 'R')
('222', 'F') ('226', None, 'R')
('225', '0') ('225', '0', 'R')
('225', '1') ('225', '1', 'R')
('225', "0'") ('225', '0', 'R')
('225', "1'") ('225', '1', 'R')
('225', 'varr') ('197L', None, 'L')
('226', '0') ('226', '0', 'R')
('226', '1') ('226', '1', 'R')
('226', "0'") ('226', '0', 'R')
('226', "1'") ('226', '1', 'R')
('226', 'varr') ('206R', None, 'R')
('230', '0') ('230', '0', 'R')
('230', '1') ('230', '0', 'R')
('230', "0'") ('230', '0', 'R')
('230', "1'") ('230', '0', 'R')
('230', 'Q') ('234L', None, 'L')
('233', '0') ('233', '0', 'R')
('233', '1') ('234', '0', 'R')
('233', "0'") ('233', '0', 'R')
('233', "1'") ('234', '0', 'R')
('233', 'Q') ('245', None, 'L')
('234', '0') ('233', '1', 'R')
('234', '1') ('234', '1', 'R')
('234', "0'") ('233', '1', 'R')
('234', "1'") ('234', '1', 'R')
('234', 'Q') ('246', None, 'L')
('237', '0') ('261L', "1'", 'L')
('237', '1') ('261L', "1'", 'L')
('237', "0'") ('237', "0'", 'L')
('237', "1'") ('237', "1'", 'L')
('237', 'Q') ('241', None, 'R')
('238', '0') ('234L', "0'", 'L')
('238', '1') ('234L', "0'", 'L')
('238', "0'") ('238', "0'", 'L')
('238', "1'") ('238', "1'", 'L')
('238', 'Q') ('241', None, 'R')
('241', '0') ('241', '0', 'R')
('241', '1') ('241', '1', 'R')
('241', "0'") ('241', '0', 'R')
('241', "1'") ('241', '1', 'R')
('241', 'E') ('281L', None, 'L')
('245', '0') ('249L', "0'", 'L')
('245', '1') ('250L', "1'", 'L')
('245', "0'") ('245', "0'", 'L')
('245', "1'") ('245', "1'", 'L')
('245', 'varr') ('253', None, 'R')
('246', '0') ('249L', "0'", 'L')
('246', '1') ('250L', "1'", 'L')
('246', "0'") ('246', "0'", 'L')
('246', "1'") ('246', "1'", 'L')
('246', 'varr') ('254', None, 'R')
('249', '0') ('245R', "0'", 'R')
('249', '1') ('254R', "1'", 'R')
('249', "0'") ('249', "0'", 'L')
('249', "1'") ('249', "1'", 'L')
('249', 'F') ('253R', None, 'R')
('250', '0') ('253R', "0'", 'R')
('250', '1') ('245R', "1'", 'R')
('250', "0'") ('250', "0'", 'L')
('250', "1'") ('250', "1'", 'L')
('250', 'F') ('254R', None, 'R')
('253', '0') ('253', '0', 'R')
('253', '1') ('253', '1', 'R')
('253', "0'") ('253', '0', 'R')
('253', "1'") ('253', '1', 'R')
('253', 'Q') ('257L', None, 'L')
('254', '0') ('254', '0', 'R')
('254', '1') ('254', '1', 'R')
('254', "0'") ('254', '0', 'R')
('254', "1'") ('254', '1', 'R')
('254', 'Q') ('258L', None, 'L')
('257', '0') ('257', '0', 'R')
('257', '1') ('257', '1', 'R')
('257', "0'") ('257', '0', 'R')
('257', "1'") ('257', '1', 'R')
('257', 'varr') ('237R', None, 'R')
('258', '0') ('258', '0', 'R')
('258', '1') ('258', '1', 'R')
('258', "0'") ('258', '0', 'R')
('258', "1'") ('258', '1', 'R')
('258', 'varr') ('238R', None, 'R')
('261', '0') ('265R', "0'", 'R')
('261', '1') ('266R', "1'", 'R')
('261', "0'") ('261', "0'", 'R')
('261', "1'") ('261', "1'", 'R')
('261', 'varr') ('273L', None, 'L')
('262', '0') ('266R', "0'", 'R')
('262', '1') ('266R', "1'", 'R')
('262', "0'") ('262', "0'", 'R')
('262', "1'") ('262', "1'", 'R')
('262', 'varr') ('274L', None, 'L')
('265', '0') ('261L', "0'", 'L')
('265', '1') ('262L', "1'", 'L')
('265', "0'") ('265', "0'", 'R')
('265', "1'") ('265', "1'", 'R')
('265', 'Q') ('273L', None, 'L')
('266', '0') ('261L', "1'", 'L')
('266', '1') ('261L', "0'", 'L')
('266', "0'") ('266', "0'", 'R')
('266', "1'") ('266', "1'", 'R')
('266', 'Q') ('274L', None, 'L')
('273', '0') ('273', '0', 'R')
('273', '1') ('273', '1', 'R')
('273', "0'") ('273', '0', 'R')
('273', "1'") ('273', '1', 'R')
('273', 'varr') ('277', None, 'R')
('274', '0') ('274', '0', 'R')
('274', '1') ('274', '1', 'R')
('274', "0'") ('274', '0', 'R')
('274', "1'") ('274', '1', 'R')
('274', 'varr') ('278', None, 'R')
('277', '0') ('277', '0', 'R')
('277', '1') ('277', '1', 'R')
('277', "0'") ('277', '0', 'R')
('277', "1'") ('277', '1', 'R')
('277', 'Q') ('233L', None, 'L')
('278', '0') ('278', '0', 'R')
('278', '1') ('278', '1', 'R')
('278', "0'") ('278', '0', 'R')
('278', "1'") ('278', '1', 'R')
('278', 'Q') ('234L', None, 'L')
('281', '0') ('285R', "0'", 'R')
('281', '1') ('286R', "1'", 'R')
('281', "0'") ('281', "0'", 'R')
('281', "1'") ('281', "1'", 'R')
('281', 'E') ('293L', None, 'L')
('282', '0') ('286R', "0'", 'R')
('282', '1') ('287R', "1'", 'R')
('282', "0'") ('282', "0'", 'R')
('282', "1'") ('282', "1'", 'R')
('282', 'E') ('294L', None, 'L')
('285', '0') ('281L', "0'", 'L')
('285', '1') ('281L', "1'", 'L')
('285', "0'") ('285', "0'", 'R')
('285', "1'") ('285', "1'", 'R')
('285', 'N') ('293L', None, 'L')
('286', '0') ('281L', "1'", 'L')
('286', '1') ('282L', "0'", 'L')
('286', "0'") ('286', "0'", 'R')
('286', "1'") ('286', "1'", 'R')
('286', 'N') ('294L', None, 'L')
('287', '0') ('282L', "0'", 'L')
('287', '1') ('282L', "1'", 'L')
('287', "0'") ('287', "0'", 'R')
('287', "1'") ('287', "1'", 'R')
('287', 'N') ('294L', None, 'L')
('293', '0') ('293', '0', 'R')
('293', '1') ('293', '1', 'R')
('293', "0'") ('293', '0', 'R')
('293', "1'") ('293', '1', 'R')
('293', 'E') ('297', None, 'R')
('294', '0') ('294', '0', 'R')
('294', '1') ('294', '1', 'R')
('294', "0'") ('294', '0', 'R')
('294', "1'") ('294', '1', 'R')
('294', 'E') ('298', None, 'R')
('297', '0') ('297', '0', 'R')
('297', '1') ('297', '1', 'R')
('297', "0'") ('297', '0', 'R')
('297', "1'") ('297', '1', 'R')
('297', 'N') ('149', None, 'R')
('298', '0') ('298', '0', 'R')
('298', '1') ('298', '1', 'R')
('298', "0'") ('298', '0', 'R')
('298', "1'") ('298', '1', 'R')
('298', 'N') ('150', None, 'R')
>>> {value[0] for value in rules.values() if value[0][-1] in ['L','R']}
{'286R', '201R', '266R', '214R', '294L', '173L', '141L', '250L', '237R', '166L', '233L', '210L', '257L', '178L', '193R', '206L', '249L', '261L', '186L', '281L', '273L', '185L', '174R', '234L', '189L', '282L', '253R', '190L', '287R', '206R', '258L', '134L', '197L', '238R', '194R', '265R', '245R', '213R', '262L', '129L', '221L', '222L', '215R', '158R', '254R', '285R', '153L', '157R', '230L', '130L', '209L', '173R', '274L', '293L', '145L', '205L', '133L', '154L', '165L', '177L'}
>>> to_symbols[286]
Sym('E'+0)
>>> symbol2string(to_symbols[286],['f', 'F', 'varr', 'Q', 'E', 'N', 'n'])
'E'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('EULER',order=['N','n','F','f','Q','varr','E'])
['f', 'F', 'varr', 'Q', 'E', 'N', 'n']
>>> len(rules)
483
>>> {instruction.vard for instruction in get_quasis([Instruction])}
Traceback (most recent call last):
  File "<pyshell#1349>", line 1, in <module>
    {instruction.vard for instruction in get_quasis([Instruction])}
  File "<pyshell#1349>", line 1, in <setcomp>
    {instruction.vard for instruction in get_quasis([Instruction])}
AttributeError: 'tuple' object has no attribute 'vard'
>>> {instruction.vard for _,instruction in get_quasis([Instruction])}
{'N', 'f', 'n', 'F', 'Q', None, 'E', 'varr'}
>>> for k,instruction in get_quasis([Instruction]:
				    
SyntaxError: invalid syntax
>>> for k,instruction in get_quasis([Instruction]):
	if not instruction.vard:
		print(k)

				    
4
10
13
18
25
27
36
38
46
49
52
54
56
61
64
66
67
69
71
80
82
85
Traceback (most recent call last):
  File "<pyshell#1355>", line 3, in <module>
    print(k)
KeyboardInterrupt
>>> quasis[4]
				    
Instruction(LOADI, imm=1, next_quasis=[0])
>>> {instruction.vard for _,instruction in get_quasis([Instruction]) if instruction.vard}
				    
{'N', 'f', 'n', 'F', 'Q', 'E', 'varr'}
>>> list({instruction.vard for _,instruction in get_quasis([Instruction]) if instruction.vard})
				    
['N', 'f', 'n', 'F', 'Q', 'E', 'varr']
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PRIME')
				    
>>> best_order
				    
['D', 'R', 'N', 'C']
>>> )))
SyntaxError: invalid syntax
>>> ('0'*8).join(best_order+best_order[:1])
'D00000000R00000000N00000000C00000000D'
>>> for key,value in rules.items():
	print(
		key[0],
		key[1] if key[1] else '*',
		value[1] if value[1] else '*',
		value[2].lower(),
		value[0]
	     )

	
68 0 0 r 68
68 1 0 r 68
68 0' 0 r 68
68 1' 0 r 68
68 R * l 72L
69 0 0 r 69
69 1 0 r 69
69 0' 0 r 69
69 1' 0 r 69
69 R * l 73L
72 0 0 r 72
72 1 1 r 72
72 0' 0 r 72
72 1' 1 r 72
72 R * r 96
73 0 1 r 72
73 1 0 r 73
73 0' 1 r 72
73 1' 0 r 73
73 R * r 97
76 0 0 r 76
76 1 1 l 80L
76 N * r 93
80 0 0 r 80
80 1 1 r 80
80 0' 0 r 80
80 1' 1 r 80
80 R * l 152
84 0 0 r 84
84 1 1 r 84
84 0' 0 r 84
84 1' 1 r 84
84 D * l 88L
85 0 1 r 85
85 1 0 r 84
85 0' 1 r 85
85 1' 0 r 84
85 D * l 88L
86 0 0 r 85
86 1 1 r 85
86 0' 0 r 85
86 1' 1 r 85
86 D * l 88L
87 0 1 r 86
87 1 0 r 85
87 0' 1 r 86
87 1' 0 r 85
87 D * l 88L
88 0 0 r 88
88 1 1 l 92L
88 D *  halt
92 0 0 r 92
92 1 1 r 92
92 0' 0 r 92
92 1' 1 r 92
92 C * l 68L
93 0 1 r 92
93 1 0 r 93
93 0' 1 r 92
93 1' 0 r 93
93 C * l 69L
96 0 0 r 96
96 1 0 r 96
96 0' 0 r 96
96 1' 0 r 96
96 N * l 100L
97 0 0 r 97
97 1 0 r 97
97 0' 0 r 97
97 1' 0 r 97
97 N * l 101L
100 0 0 r 100
100 1 0 r 101
100 0' 0 r 100
100 1' 0 r 101
100 N * r 104R
101 0 1 r 100
101 1 1 r 101
101 0' 1 r 100
101 1' 1 r 101
101 N * r 104R
104 0 0' l 108L
104 1 1' l 109L
104 0' 0' l 104
104 1' 1' l 104
104 N * r 112
108 0 0 r 116R
108 1 0 r 116R
108 0' 0' r 108
108 1' 1' r 108
108 N * r 112
109 0 1 r 117R
109 1 1 r 117R
109 0' 0' r 109
109 1' 1' r 109
109 N * r 112
112 0 0 r 112
112 1 1 r 112
112 0' 0 r 112
112 1' 1 r 112
112 C * l 76L
116 0 0' l 120L
116 1 1' l 121L
116 0' 0' l 116
116 1' 1' l 116
116 R * r 124
117 0 0' l 120L
117 1 1' l 121L
117 0' 0' l 117
117 1' 1' l 117
117 R * r 125
120 0 0' r 116R
120 1 1' r 125R
120 0' 0' l 120
120 1' 1' l 120
120 D * r 124R
121 0 0' r 124R
121 1 1' r 116R
121 0' 0' l 121
121 1' 1' l 121
121 D * r 125R
124 0 0 r 124
124 1 1 r 124
124 0' 0 r 124
124 1' 1 r 124
124 N * l 128L
125 0 0 r 125
125 1 1 r 125
125 0' 0 r 125
125 1' 1 r 125
125 N * l 129L
128 0 0 r 128
128 1 1 r 128
128 0' 0 r 128
128 1' 1 r 128
128 R * l 132L
129 0 0 r 129
129 1 1 r 129
129 0' 0 r 129
129 1' 1 r 129
129 R * r 101
132 0 0' r 136R
132 1 1' r 137R
132 0' 0' r 132
132 1' 1' r 132
132 R * l 144L
133 0 0' r 137R
133 1 1' r 137R
133 0' 0' r 133
133 1' 1' r 133
133 R * l 145L
136 0 0' l 132L
136 1 1' l 133L
136 0' 0' r 136
136 1' 1' r 136
136 N * l 144L
137 0 1' l 132L
137 1 0' l 132L
137 0' 0' r 137
137 1' 1' r 137
137 N * l 145L
144 0 0 r 144
144 1 1 r 144
144 0' 0 r 144
144 1' 1 r 144
144 R * r 148
145 0 0 r 145
145 1 1 r 145
145 0' 0 r 145
145 1' 1 r 145
145 R * r 149
148 0 0 r 148
148 1 1 r 148
148 0' 0 r 148
148 1' 1 r 148
148 N * l 100L
149 0 0 r 149
149 1 1 r 149
149 0' 0 r 149
149 1' 1 r 149
149 N * l 101L
152 0 0' r 156R
152 1 1' r 157R
152 0' 0' l 152
152 1' 1' l 152
152 D * r 160
156 0 0' l 152L
156 1 1' l 161L
156 0' 0' l 156
156 1' 1' l 156
156 N * l 160L
157 0 0' l 163L
157 1 1' l 152L
157 0' 0' l 157
157 1' 1' l 157
157 N * l 161L
160 0 0 r 160
160 1 1 r 160
160 0' 0 r 160
160 1' 1 r 160
160 R * r 164R
161 0 0 r 161
161 1 1 r 161
161 0' 0 r 161
161 1' 1 r 161
161 R * r 165R
163 0 0 r 163
163 1 1 r 163
163 0' 0 r 163
163 1' 1 r 163
163 R * r 167R
164 0 0 r 164
164 1 1 r 164
164 0' 0 r 164
164 1' 1 r 164
164 C * r 84
165 0 0 r 165
165 1 1 r 165
165 0' 0 r 165
165 1' 1 r 165
165 C * l 97L
167 0 0 r 167
167 1 1 r 167
167 0' 0 r 167
167 1' 1 r 167
167 C * r 87
137R * * r 137R
Traceback (most recent call last):
  File "<pyshell#1372>", line 6, in <module>
    value[2].lower(),
AttributeError: 'int' object has no attribute 'lower'
>>> {value[2] for value in rules.values()}
{'', 1, 'L', 'R', -1}
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PRIME')
>>> best_order
['D', 'R', 'N', 'C']
>>> result = ''
>>> for key,value in rules.items():
	result += ' '.join([
		key[0],
		key[1] if key[1] else '*',
		value[1] if value[1] else '*',
		value[2].lower(),
		value[0]
	     ]) + '\n'

	
>>> result
"68 0 0 r 68\n68 1 0 r 68\n68 0' 0 r 68\n68 1' 0 r 68\n68 R * l 72L\n69 0 0 r 69\n69 1 0 r 69\n69 0' 0 r 69\n69 1' 0 r 69\n69 R * l 73L\n72 0 0 r 72\n72 1 1 r 72\n72 0' 0 r 72\n72 1' 1 r 72\n72 R * r 96\n73 0 1 r 72\n73 1 0 r 73\n73 0' 1 r 72\n73 1' 0 r 73\n73 R * r 97\n76 0 0 r 76\n76 1 1 l 80L\n76 N * r 93\n80 0 0 r 80\n80 1 1 r 80\n80 0' 0 r 80\n80 1' 1 r 80\n80 R * l 152\n84 0 0 r 84\n84 1 1 r 84\n84 0' 0 r 84\n84 1' 1 r 84\n84 D * l 88L\n85 0 1 r 85\n85 1 0 r 84\n85 0' 1 r 85\n85 1' 0 r 84\n85 D * l 88L\n86 0 0 r 85\n86 1 1 r 85\n86 0' 0 r 85\n86 1' 1 r 85\n86 D * l 88L\n87 0 1 r 86\n87 1 0 r 85\n87 0' 1 r 86\n87 1' 0 r 85\n87 D * l 88L\n88 0 0 r 88\n88 1 1 l 92L\n88 D *  halt\n92 0 0 r 92\n92 1 1 r 92\n92 0' 0 r 92\n92 1' 1 r 92\n92 C * l 68L\n93 0 1 r 92\n93 1 0 r 93\n93 0' 1 r 92\n93 1' 0 r 93\n93 C * l 69L\n96 0 0 r 96\n96 1 0 r 96\n96 0' 0 r 96\n96 1' 0 r 96\n96 N * l 100L\n97 0 0 r 97\n97 1 0 r 97\n97 0' 0 r 97\n97 1' 0 r 97\n97 N * l 101L\n100 0 0 r 100\n100 1 0 r 101\n100 0' 0 r 100\n100 1' 0 r 101\n100 N * r 104R\n101 0 1 r 100\n101 1 1 r 101\n101 0' 1 r 100\n101 1' 1 r 101\n101 N * r 104R\n104 0 0' l 108L\n104 1 1' l 109L\n104 0' 0' l 104\n104 1' 1' l 104\n104 N * r 112\n108 0 0 r 116R\n108 1 0 r 116R\n108 0' 0' r 108\n108 1' 1' r 108\n108 N * r 112\n109 0 1 r 117R\n109 1 1 r 117R\n109 0' 0' r 109\n109 1' 1' r 109\n109 N * r 112\n112 0 0 r 112\n112 1 1 r 112\n112 0' 0 r 112\n112 1' 1 r 112\n112 C * l 76L\n116 0 0' l 120L\n116 1 1' l 121L\n116 0' 0' l 116\n116 1' 1' l 116\n116 R * r 124\n117 0 0' l 120L\n117 1 1' l 121L\n117 0' 0' l 117\n117 1' 1' l 117\n117 R * r 125\n120 0 0' r 116R\n120 1 1' r 125R\n120 0' 0' l 120\n120 1' 1' l 120\n120 D * r 124R\n121 0 0' r 124R\n121 1 1' r 116R\n121 0' 0' l 121\n121 1' 1' l 121\n121 D * r 125R\n124 0 0 r 124\n124 1 1 r 124\n124 0' 0 r 124\n124 1' 1 r 124\n124 N * l 128L\n125 0 0 r 125\n125 1 1 r 125\n125 0' 0 r 125\n125 1' 1 r 125\n125 N * l 129L\n128 0 0 r 128\n128 1 1 r 128\n128 0' 0 r 128\n128 1' 1 r 128\n128 R * l 132L\n129 0 0 r 129\n129 1 1 r 129\n129 0' 0 r 129\n129 1' 1 r 129\n129 R * r 101\n132 0 0' r 136R\n132 1 1' r 137R\n132 0' 0' r 132\n132 1' 1' r 132\n132 R * l 144L\n133 0 0' r 137R\n133 1 1' r 137R\n133 0' 0' r 133\n133 1' 1' r 133\n133 R * l 145L\n136 0 0' l 132L\n136 1 1' l 133L\n136 0' 0' r 136\n136 1' 1' r 136\n136 N * l 144L\n137 0 1' l 132L\n137 1 0' l 132L\n137 0' 0' r 137\n137 1' 1' r 137\n137 N * l 145L\n144 0 0 r 144\n144 1 1 r 144\n144 0' 0 r 144\n144 1' 1 r 144\n144 R * r 148\n145 0 0 r 145\n145 1 1 r 145\n145 0' 0 r 145\n145 1' 1 r 145\n145 R * r 149\n148 0 0 r 148\n148 1 1 r 148\n148 0' 0 r 148\n148 1' 1 r 148\n148 N * l 100L\n149 0 0 r 149\n149 1 1 r 149\n149 0' 0 r 149\n149 1' 1 r 149\n149 N * l 101L\n152 0 0' r 156R\n152 1 1' r 157R\n152 0' 0' l 152\n152 1' 1' l 152\n152 D * r 160\n156 0 0' l 152L\n156 1 1' l 161L\n156 0' 0' l 156\n156 1' 1' l 156\n156 N * l 160L\n157 0 0' l 163L\n157 1 1' l 152L\n157 0' 0' l 157\n157 1' 1' l 157\n157 N * l 161L\n160 0 0 r 160\n160 1 1 r 160\n160 0' 0 r 160\n160 1' 1 r 160\n160 R * r 164R\n161 0 0 r 161\n161 1 1 r 161\n161 0' 0 r 161\n161 1' 1 r 161\n161 R * r 165R\n163 0 0 r 163\n163 1 1 r 163\n163 0' 0 r 163\n163 1' 1 r 163\n163 R * r 167R\n164 0 0 r 164\n164 1 1 r 164\n164 0' 0 r 164\n164 1' 1 r 164\n164 C * r 84\n165 0 0 r 165\n165 1 1 r 165\n165 0' 0 r 165\n165 1' 1 r 165\n165 C * l 97L\n167 0 0 r 167\n167 1 1 r 167\n167 0' 0 r 167\n167 1' 1 r 167\n167 C * r 87\n144L * * l 144L\n144L D * r 144\n128L * * l 128L\n128L D * r 128\n104R * * r 104R\n104R C * l 104\n109L * * l 109L\n109L R * r 109\n152L * * l 152L\n152L R * l 152\n160L * * l 160L\n160L D * r 160\n69L * * l 69L\n69L D * r 69\n157R * * r 157R\n157R C * l 157\n129L * * l 129L\n129L D * r 129\n73L * * l 73L\n73L D * r 73\n72L * * l 72L\n72L D * r 72\n163L * * l 163L\n163L D * r 163\n133L * * l 133L\n133L D * r 133\n124R * * r 124R\n124R R * r 124\n117R * * r 117R\n117R N * l 117\n125R * * r 125R\n125R R * r 125\n101L * * l 101L\n101L R * r 101\n92L * * l 92L\n92L N * r 92\n76L * * l 76L\n76L R * r 76\n132L * * l 132L\n132L D * r 132\n97L * * l 97L\n97L R * r 97\n120L * * l 120L\n120L R * l 120\n136R * * r 136R\n136R R * r 136\n108L * * l 108L\n108L R * r 108\n137R * * r 137R\n137R R * r 137\n167R * * r 167R\n167R N * r 167\n145L * * l 145L\n145L D * r 145\n161L * * l 161L\n161L D * r 161\n80L * * l 80L\n80L D * r 80\n88L * * l 88L\n88L C * r 88\n156R * * r 156R\n156R C * l 156\n165R * * r 165R\n165R N * r 165\n100L * * l 100L\n100L R * r 100\n164R * * r 164R\n164R N * r 164\n116R * * r 116R\n116R N * l 116\n121L * * l 121L\n121L R * l 121\n68L * * l 68L\n68L D * r 68\n"
>>> print(result)

>>> quasis[0]
End(is_start=True, next_quasis=[68])
>>> quasis[68]
State(instruction=2, acc=0, transitions={'0': ['0', 0, 68], '1': ['0', 0, 68], "0'": ['0', 0, 68], "1'": ['0', 0, 68], Sym('D'+1): [None, 0, 72]}, direction=1)
>>> chr(A)
Traceback (most recent call last):
  File "<pyshell#1383>", line 1, in <module>
    chr(A)
NameError: name 'A' is not defined
>>> order('a')
Traceback (most recent call last):
  File "<pyshell#1384>", line 1, in <module>
    order('a')
NameError: name 'order' is not defined
>>> ord('a')
97
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PRIME')
>>> compile_function('TEST')
>>> print(morphett_output())
Traceback (most recent call last):
  File "<pyshell#1388>", line 1, in <module>
    print(morphett_output())
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 683, in morphett_output
    result += ' '.join([
UnboundLocalError: local variable 'result' referenced before assignment
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST')
>>> print(morphett_output())
Traceback (most recent call last):
  File "<pyshell#1390>", line 1, in <module>
    print(morphett_output())
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 686, in morphett_output
    replacements[key[1]] if key[1] else '*',
KeyError: '0'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST')
>>> print(morphett_output())
4 0 0 r 4
4 1 0 r 4
4 2 0 r 4
4 3 0 r 4
4 D * l 8L
8 0 0 r 8
8 1 1 r 8
8 2 0 r 8
8 3 1 r 8
8 D *  halt
8L * * l 8L
8L D * r 8

>>> quasis[0]
End(is_start=True, next_quasis=[4])
>>> used_states
{0, 8, 3, 4}
>>> quasis[3]
End(is_start=False, next_quasis=[None])
>>> quasis[4]
State(instruction=1, acc=0, transitions={'0': ['0', 0, 4], '1': ['0', 0, 4], "0'": ['0', 0, 4], "1'": ['0', 0, 4], Sym('D'+1): [None, 0, 8]}, direction=1)
>>> quasis[5]
State(instruction=1, acc=1, transitions={'0': ['0', 1, 5], '1': ['0', 1, 5], "0'": ['0', 1, 5], "1'": ['0', 1, 5], Sym('D'+1): [None, 1, 9]}, direction=1)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST')
>>> print(morphett_output())
3 0 0 r 3
3 1 1 r 3
3 2 0 r 3
3 3 1 r 3
3 D *  halt

>>> quasis[0]
End(is_start=True, next_quasis=[3])
>>> quasis[3]
State(instruction=1, acc=0, transitions={'0': ['0', 0, 3], '1': ['1', 0, 3], "0'": ['0', 0, 3], "1'": ['1', 0, 3], Sym('D'+1): [None, 0, 2]}, direction=1)
>>> quasis[2]
End(is_start=False, next_quasis=[None])
>>> quasis[4]
State(instruction=1, acc=1, transitions={'0': ['1', 0, 3], '1': ['0', 1, 4], "0'": ['1', 0, 3], "1'": ['0', 1, 4], Sym('D'+1): [None, 1, 2]}, direction=1)
>>> 
