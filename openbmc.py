import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Login:
    def __init__(self,address,username,password):
        self.address = 'https://{0}'.format(address)
        self.username = username
        self.password = password
        self.session=requests.Session()

    def _login(self):
        url = '{0}/login'.format(self.address)
        login_body = {'data': [self.username, self.password]}
        request = self.session.post(url, json=login_body,verify=False)
        print request
        print request.text

    def _get_DIMM(self,DIMM_number):
        url = '{0}/xyz/openbmc_project/inventory/system/chassis/motherboard/dimm{1}'.format(self.address,DIMM_number)
        print url
        request=self.session.get(url,verify=False)
        print request
        print request.text

    def _enumerate(self):
        url = '{0}/xyz/openbmc_project/sensors/enumerate'.format(self.address)
        print url
        request=self.session.get(url,verify=False)
        print request
        print request.text

    def _gettemp(self,endpoint):
        url='{0}/xyz/openbmc_project/sensors/temperature/{1}'.format(self.address,endpoint)
        response=self.session.get(url,verify=False)
        json_data=json.loads(response.text)
        parsed_data=json_data['data']
        return parsed_data['Value']

    def _getspeed(self,endpoint):
        url='{0}/xyz/openbmc_project/sensors/pwm/speed/{1}'.format(self.address,endpoint)
        response=self.session.get(url,verify=False)
        json_data=json.loads(response.text)
        parsed_data=json_data['data']
        return parsed_data['Value']
