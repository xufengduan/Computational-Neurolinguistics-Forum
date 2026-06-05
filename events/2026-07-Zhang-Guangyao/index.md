---
layout: event
title: 大脑先验知识指导概念学习的计算神经机制
speaker: 张光耀
institution: 北京师范大学
date: 2026-07-06 14:00
permalink: /events/2026-07-Zhang-Guangyao/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
abstract: |
  （讲座摘要待更新）
  
bio: |
  张光耀，北京师范大学博士后，其研究利用行为实验、fMRI、计算建模等多种技术方法，探索概念加工与学习的认知神经机制。研究成果发表在Nature Communications, Nature Human Behavior等期刊。主持国自然青年基金，博士后特别资助和面上资助项目。
  
outline: |
  1. 讲座内容
  2. 问答环节
  
zoom_id: 958 9105 3788
zoom_password: 213165
status: active
photo: guangyao.png
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
