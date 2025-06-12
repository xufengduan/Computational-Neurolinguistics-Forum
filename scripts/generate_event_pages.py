#!/usr/bin/env python3
import os
import yaml
from datetime import datetime
import shutil


def load_events():
    with open('_data/events.yml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def generate_event_page(event):
    # 创建讲座目录
    event_dir = f'events/{event["permalink"]}'
    os.makedirs(event_dir, exist_ok=True)

    # 生成讲座页面内容
    content = f'''---
layout: event
title: {event["title"]}
speaker: {event["speaker"]}
institution: {event["institution"]}
date: {event["date"]}
permalink: /events/{event["permalink"]}/
'''

    # 添加可选字段
    if 'zoom_link' in event:
        content += f'zoom_link: {event["zoom_link"]}\n'
    if 'slides' in event:
        content += f'slides: {event["slides"]}\n'
    if 'video' in event:
        content += f'video: {event["video"]}\n'

    content += '''---

## 讲座简介

{% if page.abstract %}
{{ page.abstract }}
{% else %}
本次讲座将探讨{{ page.title }}。具体内容即将更新。
{% endif %}

## 演讲者简介

{% if page.bio %}
{{ page.bio }}
{% else %}
{{ page.speaker }}是{{ page.institution }}的研究人员。
{% endif %}

## 参与方式

- 时间：{{ page.date | date: "%Y年%m月%d日" }} 20:00-21:30（北京时间）
- 平台：Zoom
- 语言：中文
- 费用：免费

## 讲座大纲

{% if page.outline %}
{{ page.outline }}
{% else %}
1. 引言
2. 主要内容
3. 讨论
4. 问答环节
{% endif %}

## 相关资源

{% if page.resources %}
{{ page.resources }}
{% else %}
- 预读材料即将更新
- 讲座回放将在讲座结束后提供
{% endif %}
'''

    # 写入文件
    with open(f'{event_dir}/index.md', 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    # 加载所有讲座数据
    events_data = load_events()

    # 只生成 active 和 upcoming 状态的讲座页面
    for event in events_data['events']:
        if event['status'] in ['active', 'upcoming']:
            print(f"生成讲座页面：{event['title']}")
            generate_event_page(event)


if __name__ == '__main__':
    main()
