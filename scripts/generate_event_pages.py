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

    # 添加所有可选字段
    optional_fields = ['zoom_link', 'slides', 'video_link',
                       'abstract', 'bio', 'outline', 'resources']
    for field in optional_fields:
        if field in event:
            content += f'{field}: |\n'
            # 确保多行文本正确缩进
            for line in event[field].split('\n'):
                content += f'  {line}\n'

    # 添加数字类型的字段
    if 'zoom_id' in event:
        content += f'zoom_id: {event["zoom_id"]}\n'
    if 'zoom_password' in event:
        content += f'zoom_password: {event["zoom_password"]}\n'
    if 'video_password' in event:
        content += f'video_password: {event["video_password"]}\n'
    # 添加状态字段
    if 'status' in event:
        content += f'status: {event["status"]}\n'
    # 添加照片字段（不需要多行处理）
    if 'photo' in event:
        content += f'photo: {event["photo"]}\n'

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

- 时间：{{ page.date | date: "%Y年%m月%d日" }} {% assign hour = page.date | date: "%H" | plus: 0 %}{% if hour < 12 %}上午{% else %}下午{% endif %} {{ page.date | date: "%H:%M" }}（北京时间）
- 平台：Zoom
- 语言：中文

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
