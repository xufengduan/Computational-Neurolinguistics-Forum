---
layout: event
title: 神经表征驱动的脑机对齐与模型增强
speaker: 陈佳炫
institution: 浙江大学
date: 2026-06-18 10:00
permalink: /events/2026-06-Chen-Jiaxuan/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
abstract: |
  （讲座摘要待更新）
  
bio: |
  陈佳炫，浙江大学计算机科学与技术学院在读博士生，主要研究方向为神经解码、脑机智能等。研究成果发表于Nature Communications、IEEE T-IP、ICLR、ICML、CVPR、ICCV、AAAI等国际期刊和CCF-A类会议。主持国自然青年学生基础研究项目（博士研究生），入选中国科协青年人才托举工程博士生专项计划、浙江大学博士研究生求是新星培养计划。
  
outline: |
  1. 讲座内容
  2. 问答环节
  
zoom_id: 958 9105 3788
zoom_password: 213165
status: active
photo: jiaxuan.jpg
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
