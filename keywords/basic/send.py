import requests
from bear.log import logger
from bear.SkiCommonData import SkiGlobalData

def askbaidu(mod,data):

    logger.info('in ask baidu！')
    r = requests.get(url=data)    # 最基本的GET请求
    return r

