#https://www.zhihu.com/api/v4/questions/56706299/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_in
# fo%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Cc
# omment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreat
# ed_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoti
# ng%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%
# 28type%3Dbest_answerer%29%5D.topics&limit=5&offset=5&sort_by=default


import urllib3
import requests
import json
import urllib.parse
import pyquery
import time

urllib3.disable_warnings()
url = 'https://www.zhihu.com/api/v4/questions/56706299/answers?'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/67.0.3396.99 Safari/537.36',

}
def zhihuspider_url(page):
    offset = (page-1)*5
    params = {
        'include':'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].mark_infos[*].url;data[*].author.follower_count,badge[?(type=best_answerer)].topics',
        'limit': '5',
        'offset': offset,
        'sort_by': 'default',
    }
    base = urllib.parse.urlencode(params)
    base_url = url+base
    print(base_url)
    res = requests.get(base_url,headers=headers,verify=False)
    if res.status_code == 200:
        return res.json()
    return None

def parse_page(json1):
    if json1:
        datas = json1['data']
        #print(datas)
        question = '提问:'+datas[0]['question']['title']
        biaodian = ['<p>','</p>','<figure>','</figure>','<noscript>','</noscript>','<b>','</b>','<img src=','>']
        items = {}
        list1 = [question]

        for item in datas:
            if item['type']!='answer':
                continue
            items['回答者'] = item['author']['name']

            created_time = item['created_time']   #获取发表时间的时间戳
            timeA = time.localtime(created_time)
            created_time = time.strftime('%Y-%m-%d %H:%M:%S',timeA)
            items['发表时间'] = created_time

            content = item['content']
            for b in biaodian:
                content=content.replace(b,' ')
                items['回答内容'] = content.replace('<br','\n')

            list1.append(items)
            items={}
    return list1
json1 = zhihuspider_url(1)
list1 = parse_page(json1)
print(list1)