#!/usr/bin/env python
# -*- coding:utf-8 -*-
# http://g1879.gitee.io/drissionpagedocs/whatsnew/4_0/
# pip install DrissionPage==4.0.0b34
import os
import re
import time

from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
from colorama import Fore, init
from tabulate import tabulate


import cmd


class Config:
    def __init__(self):
        self.browser_path = r"C:\Program Files\Twinkstar Browser\twinkstar.exe"
        self.info = " "
        self.url = "https://www.qq.com"
        self.introduce = f"""
        -------------   SaossionPage浏览器----------------------
        使用的浏览器:{self.browser_path}
        
        """

    def showinfo(self):
        # print(self.logo)
        print(self.introduce)


class Browser:
    def __init__(self, browser_path):
        self.browser_path = browser_path
        self.co = ChromiumOptions()
        self.co.set_browser_path(self.browser_path)
        self.co.set_argument("--hide-crash-restore-bubble")

        self.page = ChromiumPage(addr_or_opts=self.co)

        self.tabs = []
        self.eles = {}
        self.cmd = r"""
                    function loadjQuery() {
                  // 创建一个 script 元素
                  var script = document.createElement('script');
                
                  // 设置 script 元素的 src 属性为 jQuery 的 CDN 地址
                  script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
                  script.id = 'jq';
                
                  // 将 script 元素添加到文档的头部或 body 中
                  document.head.appendChild(script);
                  // 或者使用 document.body.appendChild(script);
                    }
                    loadjQuery();
                    """
        self.jiekou = [
            "https://www.ckplayer.vip/jiexi/?url=",
            "https://jx.yparse.com/index.php?url=",
            "https://www.8090g.cn/?url=",
            "https://www.ckplayer.vip/jiexi/?url=",
            "https://jx.qqwtt.com/?url=",
            "https://www.pouyun.com/?url=",
            "https://jx.m3u8.tv/jiexi/?url=",
            "https://z1.m1907.top/?jx=",
            "https://www.8090.la/8090/?url=",
            "https://www.pangujiexi.com/jiexi/?url=",
            "https://dmjx.m3u8.tv/?url=",
            "https://vip.bljiex.com/?v=",
            "https://www.mtosz.com/m3u8.php?url=",
            "https://www.playm3u8.cn/jiexi.php?url=",
            "https://www.yemu.xyz/?url=",
            "https://jx.m3u8.tv/jiexi/?url=",
            "https://api.qianqi.net/vip/?url=",
            "https://jx.playerjy.com/?url=",
            "https://jx.we-vip.com/?url=",
            "https://www.8090g.cn/jiexi/?url=",
            "https://vip.mpos.ren/v/?url=",
            "https://movie.heheda.top/?v=",
            "http://vip.wandhi.com/?v=",
            "https://jx.jsonplayer.com/player/?url=",
            "https://jx.playerjy.com/?url=",
            "https://jx.xmflv.com/?url=",
            "https://jx.xmflv.cc/?url=",
            "https://jx.yparse.com/index.php?url=",
            "https://im1907.top/?jx=",
            "https://www.8090g.cn/?url=",
            "https://api.qianqi.net/vip/?url=",
            "https://jx.yangtu.top/?url=",
            "https://www.ckplayer.vip/jiexi/?url=",
        ]

    # def start(self, url):
    #     # 创建页面对象，并启动或接管浏览器
    #     self.page = ChromiumPage(addr_or_opts=self.co)
    #     self.page.get(url)

    def open(self, url):
        self.tabs.append(self.page.new_tab(url))
        return self

    @property
    def newest_page(self):
        return self.page.get_tab(self.page.latest_tab)

    def download_path(self, path):
        self.page.set.download_path(path)
        return self

    def download(self, url):
        self.page.download(url)
        return self

    def show_title(self):
        print(self.tab.title)
        return self

    def max(self):
        self.page.set.window.max()
        return self

    def min(self):
        self.page.set.window.mini()
        return self

    def hide(self):
        self.page.set.window.hide()
        return self

    def show(self):
        self.page.set.window.show()
        return self

    def wait(self, num: int):
        self.page.actions.wait(num)
        return self

    def vip_open(self, url):
        self.page.get(self.jiekou[0] + url)

    def help(self, keyword):
        h = Help()
        h.doc(keyword=keyword)
        return self

    @property
    def jquery(self):
        return Jquery(self)

    def elements(self, k: str, v: str):
        ele = self.tab.eles(f"@{k}={v}")
        return ele

    @staticmethod
    def read_file(file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
        return content

    def run(self, script_file: str):
        _page = self.newest_page
        _page.run_js(Browser.read_file(script_file))

    def loadjQuery(self):
        if self.newest_page.ele("#jq", timeout=0.2):
            print("jQuery 已经加载")
        else:
            self.newest_page.run_js(self.cmd)
            print("jQuery 成功加载入页面...")

    @property
    def tab(self):  # 返回最新的标签页
        return self.page.get_tab(self.page.latest_tab)

    def download_all_img(self, tag):
        for i in tag.eles("t:img"):
            for j in ["png", "jpg", "jpeg", "webp", "gif", "tiff"]:
                if j in i.link:
                    self.page.download(i.link)

        return self


class Jquery:
    def __init__(self, browser: Browser):
        self.b = browser
        self.cmd = r"""
                    function loadjQuery() {
                  // 创建一个 script 元素
                  var script = document.createElement('script');
                
                  // 设置 script 元素的 src 属性为 jQuery 的 CDN 地址
                  script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
                  script.id = 'jq';
                
                  // 将 script 元素添加到文档的头部或 body 中
                  document.head.appendChild(script);
                  // 或者使用 document.body.appendChild(script);
                }
                loadjQuery();
                """
        self.load_jquery()

    def load_jquery(self):
        if self.b.newest_page.ele("#jq"):
            print("jQuery 已经加载")
        else:
            self.run(self.cmd)
            print("jQuery 成功加载入页面...")

    def run(self, js_str: str):
        self.b.newest_page.run_js(js_str)
        return self

    def exe(self, js_str: str):  # 有返回值
        return self.b.newest_page.run_js(js_str)


class Help:
    def __init__(self) -> None:
        self.info = [
            ["写法", "精确匹配", "模糊匹配", "匹配开头", "匹配结尾", "说明"],
            ["@属性名 ", "@属性名=", "@属性名:", "@属性名^", "@属性名$", "按某个属性查找"],
            ["@!属性名 ", r"@!属性名=", "@!属性名:", "@!属性名^", "@!属性名$", "查找属性不符合指定条件的元素"],
            ["text", "text=", "text:或不写", "text^", "text$", "按某个文本查找"],
            [
                "@text()",
                "@text()=",
                "@text():",
                "text()^",
                "text()$",
                "text与@或@@配合使用时改为text()，常用于多条件匹配",
            ],
            ["tag", "tag=或tag:", "无", "无", "无", "查找某个类型的元素"],
            ["xpath", "xpath=或xpath:", "无", "无", "无", "用 xpath 方式查找元素"],
            ["css", "css=或css:", "无", "无", "无", "用 css selector 方式查找元素"],
        ]

    def doc(self, keyword: str):
        if "定位语法" in keyword:
            print('----------语法定位帮助-----------')
            print(
                tabulate(self.info[1:], headers=self.info[0], tablefmt="simple_outline")
            )


class Tool:
    @staticmethod
    def sniff_and_download_video(
        page, kw: str = 'x://*[@id="post"]/article/div[3]/div'
    ):
        player = page.ele(kw)
        page.actions.wait(2).click(player)
        player.drag(50, 50, 2)
        player.click.at(40, 70)
        print("视频下载中.......")

    @staticmethod
    def sniff_and_download_videos(ele):
        player = ele
        page.actions.wait(2).click(player)
        player.drag(50, 50, 2)
        player.click.at(40, 70)
        print("视频下载中.......")

    @staticmethod
    def download_img(page):
        for picture in page("@itemprop=articleBody").eles("t:img"):
            picture.save(path=page.title)
            print("saving the picture..." + str(picture.tag))

    @staticmethod
    def click_next(page):
        page.ele("text:下一篇").click()
        time.sleep(3)

    @staticmethod
    def screenshot(ele, name="viewer"):
        ele.get_screenshot(name=name, scroll_to_center=True)

    @staticmethod
    def tree(ele):
        init()
        e = ele
        print(f"{Fore.BLUE}{Fore.CYAN}<{e.tag}>  {Fore.RESET}{e.attrs}")
        Tool.__tree(e)

    @staticmethod
    def __tree(ele: any, layer=7, has_next_brother=True, body=""):
        if ele.tag == "iframe":
            ele = page.get_frame(ele)
            ele = ele("x:/html")
            # print(ele.html)
            # print(ele.children())
        try:
            list_ele = ele.children(timeout=0.1)
        except:
            list_ele = []
            print(ele)
            print("无法获取该元素子元素")

        length = len(list_ele)
        body_unit = "│   " if has_next_brother else "    "
        tail = "├───"
        new_body = body + body_unit

        if length > 0 and layer >= 1:
            has_next_brother2 = True
            for i in range(length):
                if i == length - 1:
                    tail = "└───"
                    has_next_brother2 = False
                e = list_ele[i]
                all_body = f"{Fore.BLUE}{new_body}{tail}{Fore.RESET}"

                print(f"{all_body}{Fore.CYAN}<{e.tag}>{Fore.RESET} ")
                Tool.tree_attr(e, all_body, has_next_brother2, layer)

                Tool.__tree(e, layer - 1, has_next_brother2, new_body)

    @staticmethod
    def tree_attr(ele, body, has_next_brother=True, layer=3):
        e: dict = ele.attrs
        has_child = True if ele.tag == "iframe" or ele.child(timeout=0.2) else False

        if layer == 1:
            has_child = False

        part1 = "│" if has_next_brother else " "
        part2 = "│" if has_child else " "
        replace_part = part1 + "   " + part2
        new_body = body.replace("├───", replace_part).replace("└───", replace_part)

        text = "" if ele.tag == "iframe" else ele.text.split("\n")[0]
        if len(text) >= 1:
            e["inner_txt"] = text if len(text) < 150 else text[0:150] + "......"

        if len(e) > 0:
            e["xpath"] = ele.xpath

            max_k_len = max([len(key) for key in e.keys()])
            head = "┌" + "─" * max_k_len + "┐"
            tail = "└" + "─" * max_k_len + "┘"
            print(new_body, head)

            for k, v in e.items():
                key = Fore.GREEN + str(k).ljust(max_k_len) + Fore.RESET + "│"
                content = f"{key}: {v}"

                print(new_body, "│" + key, v)

            print(new_body, tail)


if __name__ == "__main__":
    # 创建配置对象

    # url2=r'https://tv.wandhi.com/go.html'

    # 连接浏览器
    browser = Browser(
        r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe"
    )

    

    # 黑魔法一 观看vip视频
    browser.vip_open(
        "https://v.qq.com/x/cover/mzc00200whsp9r6/j0047aj1c1n.html?ptag=11972"
    )

    # 黑魔法二  查看某个元素的子元素结构树
    browser.open("https://www.qq.com/")
    body = browser.newest_page("x:/html/body")
    Tool.tree(body)

    # 黑魔法三  调用jQuery操作网页
    browser.loadjQuery()
    browser.run(r'$("div").css("color", "red");')

    browser.wait(550)

    # 黑魔法四 实时查看库的帮助文档
    browser.help('定位语法')
