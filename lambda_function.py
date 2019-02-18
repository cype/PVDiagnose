import json
import urllib
from botocore.vendored import requests
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import urllib.request
import logging
import http.client as http_client
import math
from html.parser import HTMLParser


print('Loading function')

def median(alist):
    data = sorted(alist)
    if len(data) % 2 == 1:
        return data[(len(data)) // 2]
    else:
        return (data[len(data) // 2] + data[(len(data)-1) // 2]) / 2

def our_abs(data):
    mdev = median(data)
    dataSize = len(data)
    d = [None] * dataSize
    for i in range(dataSize):
        d[i] = data[i] - mdev
    return d

def reject_outliers_2(data, m = 2.):
    d = our_abs(data)
    mdev = median(d)
    s = []
    for i in range(len(data)):
        val = d[i]/(mdev if mdev else 1.)
        if val < m:
            s.append(data[i])
    return s

def detectDeviation(apiArray, userArray):
    arraySize = len(apiArray)
    deviationArray = [None] * arraySize
    i = 0
    while i < arraySize:
        deviationArray[i] = apiArray[i] - userArray[i]
        i += 1
    return deviationArray

def result_detection(apiArray, userArray):
    deviationArray = detectDeviation(apiArray, userArray)
    print(deviationArray)
    data_points = deviationArray
    filtered_d_2 = reject_outliers_2(data_points)
    print(filtered_d_2)
    res = {}
    j = 0
    i = 0
    while i < len(deviationArray):
        if deviationArray[i] == filtered_d_2[j]:
            j += 1
        else:
            res[i] = deviationArray[j]
        if j >= len(filtered_d_2):
            return res
        i+=1
    return res

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }
    

def get_coordinates(address_string):
    url = "https://api3.geo.admin.ch/rest/services/api/SearchServer"
    user_agent = "Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.02"
    querystring = {"lang":"en","searchText":address_string,"type":"locations"}
    payload = ""
    headers = {
        'User-Agent': user_agent
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    attrs = json.loads(response.text)['results'][0]['attrs']
    
    return (attrs['x'], attrs['y'], attrs['lat'], attrs['lon'])
    
#pre: give a list
#post: returns the average of the list
def average(alist):
    aver = 0
    for n in alist:
        aver += n
    return aver / len(alist)


#pre: give the list
#post: returns the variance of the list
def std(alist):
    summe = 0
    aver = average(alist)
    for n in alist:
        summe += (n - aver)**2
    return math.sqrt(summe/(len(alist)-1))


def pv_has_malfunction(area, expected, measured):
    """
    Tests if the deviation from the expected is significantly less than gamma0.
    expected and measured can have arbitrary length but they need to be of the same length.
    :param area: area covered by the pv in m^2
    :param expected: list of expected kWh/m^2 ordered by month
    :param measured: list of measured kWh values ordered by months the same way as expected
    :return: true if there is a malfunction
    """
    gamma0 = 0 # could also be a small negative number
    #alpha = 0.05 # level of test
    #0.95-quantiles of t-distribution of degrees 1 to 11  
    tinv = [-6.341, -2.920, -2.353, -2.132, -2.015, -1.943, -1.895, -1.860, -1.833, -1.812, -1.796] 
    ex = [area*e for e in expected]
    z = []
    for i in range(len(measured)):
       z.append(measured[i]-ex[i]) 
    if std(z) > 0:
        P = math.sqrt(len(measured))*(average(z)-gamma0)/std(z)
        return P < tinv[len(measured)-2]
    else:
        return average(z) < gamma0
        
def pv_has_malfunction_with_correction(area, peak_power, expected, measured):
    
    pv_efficiency = pv_compute_efficiency(area, peak_power)
    
    ex = pv_correct_expected(pv_efficiency, expected)
    me = measured

    return pv_has_malfunction(area, ex, me)

        
def pv_correct_expected(efficiency, expected):
    """
    :param expected: list of expected kWh/m^2 ordered by month
    :param efficiency: has to be provided by the user
    :return: correct expectation with efficiency of the pv installation
    """
    
    #assumed efficiency used in sonnendach.ch computation = 0.17%

    corrected = [value * float(efficiency) / 0.17 for value in expected]

    return corrected
    
def pv_compute_efficiency(area, peak_power):
    """
    :param area: m^2
    :param peak_power: has to be provided by the user in kWp
    :return: computed efficiency of pv installation
    """

    return float(peak_power) / area
    
def get_everything(coord):
    url = "https://api3.geo.admin.ch/rest/services/api/MapServer/identify"
    y = str(coord[0])
    x = str(coord[1])
    querystring = {"geometryType":"esriGeometryPoint","returnGeometry":"false","layers":"all:ch.bfe.solarenergie-eignung-daecher","geometry": str(x + "," + y),"mapExtent": str(x + "," + y + "," + x + "," + y),"imageDisplay":"532,360,96","tolerance":"1","order":"distance","lang":"de"}
    payload = ""
    user_agent = "Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.02"
    headers = {
        'User-Agent': user_agent
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    
    return json.loads(response.text)
    
def get_results_page():
    url = "http://energy-data-hackdays-d.s3-website.eu-central-1.amazonaws.com/results.html"
    user_agent = "Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.02"
    querystring = {}
    payload = ""
    headers = {
        'User-Agent': user_agent
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    
    return response.text

def lambda_handler(event, context):
    '''A simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.
    '''
    year_user_input_data = []
    for i in range(0, 11):
        year_user_input_data.append(float(str(event['queryStringParameters'][str(i)])))
        
    area = event['queryStringParameters']['pvsize']
    coord = get_coordinates(str(event['queryStringParameters']['address']))
    expected_sonnendach_api = get_everything(coord)['results'][0]['attributes']['monats_ertrag']
    kwp = event['queryStringParameters']['pvsize']

    #TODO: detected = result_detection(expected_sonnendach_api,year_user_input_data)
    #TODO: $VALUE_LIST$
    #TODO: [{x: 1, y: 12.0}, {x: 2.0, y: 33.1}, {x: 3.00, y: 6.33}, {x: 4.00, y: -0.0}]

    
    results_str = get_results_page()
    malfun_msg = ""
    
    if pv_has_malfunction_with_correction(float(area), float(kwp), expected_sonnendach_api, year_user_input_data):
        malfun_msg = "Your device might have issues :("
        malfun_msg = "You're fine. Device performs optimally :)"
    
    v1 = results_str.replace("$LAT$", str(coord[2]))
    v2 = v1.replace("$LONG$", str(coord[3]))
    v3 = v2.replace("$MALFUNMSG$", malfun_msg)

    response = {
        "statusCode": 200,
        "body": v3,
        "headers": {
            'Content-Type': 'text/html',
            }
    }

    return (response)
