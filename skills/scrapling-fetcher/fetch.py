#!/usr/bin/env python3
# Scrapling Fetcher Skill
# 用于 OpenClaw 的网页抓取技能

import sys
import json
from scrapling import Fetcher

def fetch_page(url: str, selector: str = None, stealth: bool = False) -> dict:
    """
    抓取网页内容
    
    Args:
        url: 目标网址
        selector: CSS 选择器（可选）
        stealth: 是否使用隐身模式
        
    Returns:
        dict: 抓取结果
    """
    try:
        # 创建 Fetcher
        if stealth:
            from scrapling import StealthyFetcher
            f = StealthyFetcher()
        else:
            f = Fetcher()
        
        # 抓取页面
        response = f.get(url)
        
        # 构建结果
        result = {
            "url": url,
            "status": response.status,
            "title": response.css('title::text').get() if response.css('title::text').get() else "N/A",
            "content_length": len(response.text),
            "success": True
        }
        
        # 如果有选择器，提取数据
        if selector:
            extracted = response.css(selector).get()
            result["extracted"] = extracted if extracted else "No match found"
        else:
            # 返回前 500 字符
            result["content"] = response.text[:500] + "..." if len(response.text) > 500 else response.text
        
        return result
        
    except Exception as e:
        return {
            "url": url,
            "success": False,
            "error": str(e)
        }

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "Usage: fetch.py <url> [--selector <css_selector>] [--stealth]"
        }, ensure_ascii=False))
        sys.exit(1)
    
    # 解析参数
    url = None
    selector = None
    stealth = False
    
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == '--selector':
            if i + 1 < len(sys.argv):
                selector = sys.argv[i + 1]
                i += 2
            else:
                print(json.dumps({"error": "--selector requires a value"}))
                sys.exit(1)
        elif arg == '--stealth':
            stealth = True
            i += 1
        elif arg.startswith('-'):
            i += 1
        else:
            if url is None:
                url = arg
            i += 1
    
    if not url:
        print(json.dumps({"error": "URL is required"}))
        sys.exit(1)
    
    # 执行抓取
    result = fetch_page(url, selector, stealth)
    
    # 输出结果
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
