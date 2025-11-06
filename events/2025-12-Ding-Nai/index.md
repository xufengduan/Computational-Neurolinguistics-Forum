---
layout: event
title: 语句理解的神经动力学机制
speaker: 丁鼐教授
institution: 浙江大学
date: 2025-12-03 10:00
permalink: /events/2025-12-Ding-Nai/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
abstract: |
  TBD
  
bio: |
  丁鼐，浙江大学生物医学工程与仪器科学学院研究员，生物医学工程教育部重点实验室副主任。主要研究领域为听觉、语言、音乐理解的认知神经机制，在Nature Neuroscience，Nature Human Behaviour等期刊发表论文数十篇，连续多年入选爱思唯尔“中国高被引学者”，获国际听觉领域的APAN青年科学家奖，Society for Neurobiology of Language（语言神经生物学学会）理事会成员。
  
zoom_id: 958 9105 3788
zoom_password: 213165
status: active
photo: nai.jpg
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
