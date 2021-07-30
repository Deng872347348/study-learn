from bs4 import BeautifulSoup
html="""
<html><head><title>测试bs4</title></head>
<body>
<p class="title" name="dromouse"><b>story</b></p>
<p class="story">there were three little sisters;
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
"""


