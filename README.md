
![输入图片说明](./img/logo.png)


#  😈 SaossionPage 介绍 



 **SaossionPage**   简称 【骚神page】   Drissionpage 的变异版 Python库，内涵各种黑魔法👹 慎用🔞！！！！

您的星星⭐是对我最大的支持

<a href='https://gitee.com/haiyang0726/SaossionPage/stargazers'><img src='https://gitee.com/haiyang0726/SaossionPage/badge/star.svg?theme=dark' alt='star'></img></a> <a href='https://gitee.com/g1879/DrissionPage/members'><img src='https://gitee.com/haiyang0726/SaossionPage/badge/fork.svg?theme=dark' alt='fork'></img></a>

---



#  ☠️ 黑魔法介绍



---
-  ### 👻 魔法一 免费观看VIP视频

```
if __name__ == '__main__':
     
    #连接浏览器
    browser=Browser(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    #观看vip视频 
    browser.vip_open('https://v.qq.com/x/cover/mzc00200whsp9r6/j0047aj1c1n.html?ptag=11972')

```
---
-  ### 🦇 魔法二  查看某个元素的子目录树

```
if __name__ == '__main__':
     
    #连接浏览器
    browser=Browser(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    browser.open('https://www.qq.com/')
    body=browser.newest_page('x:/html/body')
    Tool.tree(body)    

```
---
-  ### 🦴 魔法三  调用jQuery 操作网页元素

```
if __name__ == '__main__':
     
    #连接浏览器
    browser=Browser(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    #打开网页
    browser.open('https://www.qq.com/')
    #载入jQuery
    browser.loadjQuery()
    browser.run(r'$("div").css("color", "red");')
       

```
---
-  ### 🔥 魔法四  实时查看库的帮助文档

```
if __name__ == '__main__':
     
    #连接浏览器
    browser=Browser(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    #  实时查看库的帮助文档
    browser.help('定位语法')
       

```
---

