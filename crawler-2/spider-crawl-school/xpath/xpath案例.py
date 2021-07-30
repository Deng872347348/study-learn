html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
   <div>
       <ul>
           <li class="item-0"><a href="link1.html">first item</a> </li>
           <li class="item-1"><a href="link2.html">second item</a> </li>
           <li class="item-inactive"><a href="link3.html">third item</a> </li>
       </ul>
   </div>
</body>
</html>
"""
from lxml import etree
html_name= etree.HTML(html)
a=html_name.xpath('//ul/li/a[2]/text()')
print(a)