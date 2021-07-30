import requests, asyncio, aiohttp, aiofiles
import json
import os
from  fake_useragent import  UserAgent
async def get_cid(url,headers):
    resp = requests.get(url=url, headers=headers, verify=False)
    if not os.path.exists('./西游记'):
        os.mkdir('./西游记')
    tasks = []
    async with aiohttp.ClientSession(headers=headers) as session:
    # 传入公共使用的headers，并只创建一个session提高效率
        for item in resp.json()['data']['novel']['items']:
            title = item['title']
            cid = item['cid']
            tasks.append(asyncio.create_task(get_content(title, cid, book_id,session)))
            # 创建异步任务传入异步程序
        await asyncio.wait(tasks)

async def get_content(title, cid, book_id,session):
    base_url = 'http://dushu.baidu.com/api/pc/getChapterContent?data={}'
    data = {
        "book_id": book_id,
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    # 字典转化成json字符串，方便url拼接
    content_url = base_url.format(data)
    async with session.get(url=content_url) as resp:
        dic = await resp.json()
        # 返回的是字典内容，所以用json(),若想要页面源码,用text()，可以用etree继续解析得到想要内容、
        content = dic['data']['novel']['content']
        async with aiofiles.open(f'./西游记/{title}', mode='w', encoding='utf-8') as file:
            await file.write(content)
            # 写入文本也是IO操作，所以要在前面加入await
    print(title,'over')
if __name__ == '__main__':
    # main()
    # 若添加main函数 把下面内容写在main()函数中，运行会出现loop is closed 的错误，还不知道解决方案!!
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
    book_id = "4306063500"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    }
    asyncio.run(get_cid(url,headers))

