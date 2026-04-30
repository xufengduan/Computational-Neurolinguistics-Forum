---
layout: event
title: 语言加工中的“排兵布阵”：语言层级结构引导的高效预测机制
speaker: 邹家杰
institution: 浙江大学
date: 2026-05-29 15:00
permalink: /events/2026-05-Zou-Jiajie/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
abstract: |
  （讲座摘要待更新）
  
bio: |
  邹家杰，浙江大学博士后、马普所生物控制论研究所访问学者。研究方向为融合神经影像与计算建模探究大脑如何加工语言、语音。研究成果发表于 Nature Neuroscience、Nature Communications、eLife 等期刊以及 ACL 等计算机会议。获批国自然青年基金，并多次担任Nature Communications、eLife、the Journal of Neuroscience 等期刊审稿人。
  
outline: |
  1. 讲座内容
  2. 问答环节
  
zoom_id: 958 9105 3788
zoom_password: 213165
status: active
photo: jiajie.jpg
---

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
