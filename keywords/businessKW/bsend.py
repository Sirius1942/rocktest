import json
from bear.log import logger
from bear.SkiCommonData import SkiGlobalData
from driver import d_requests

jwt_access={}
BASE_URL=SkiGlobalData().get_global_data()['BASE_URL']

# 提供通过用户名获取jwt的接口信息方法，获取后的认证字符串放在 jwt_access global 全局变量中
def login(body_data):
    url = '/user/login'
    headers = {'Content-Type': 'application/json'}
    logger.info('in login！')
    login_user=body_data
    r = d_requests.post(url=BASE_URL+url,headers=headers,json=login_user)    # 最基本的GET请求
    logger.info("response is : {0}".format(r))
    logger.info("response is : {0}".format(r.text))
    result=json.loads(r.text)
    global jwt_access
    jwt_access[login_user['username']]=result['data']['access']
    return r
    
def getUserList(user_name):
  global jwt_access
  url = '/users/'
  headers = {'Content-Type': 'application/json','Authorization': 'Bearer '+jwt_access[user_name['name']]}
  logger.info('in getUserinfo heasers is :{0}'.format(headers))
  r = d_requests.get(url=BASE_URL+url,headers=headers)    # 最基本的GET请求
  logger.info("response is : {0}".format(r))
  return r


def adduser(body_data):
    url = '/users/'
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer '+jwt_access[user_jwt['name']]}
    logger.info('in login！')
    login_user=body_data
    r = d_requests.post(url=BASE_URL+url,headers=headers,json=login_user)    # 最基本的GET请求
    logger.info("response is : {0}".format(r))
    return r

def web_login(user_data):
  pass




  