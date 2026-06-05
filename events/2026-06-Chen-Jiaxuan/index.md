---
layout: event
title: 神经表征驱动的脑机对齐与模型增强
speaker: 陈佳炫
institution: 浙江大学
date: 2026-06-22 10:00
permalink: /events/2026-06-Chen-Jiaxuan/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
abstract: |
  近年来，人工智能的发展几乎都遵循着同一个逻辑：参数更大、数据更多、模型更强，但模型虽然"知道得更多"，却未必"理解得更深"——它们可以记住海量知识，却依然会在抽象概念理解、跨场景泛化、概念关系推理等方面暴露出局限性。与此同时，以脑机接口为代表的神经技术快速发展，使得脑与机的结合愈加紧密，脑机融合及一体化逐渐成为人工智能发展的重要趋势。在这一背景下，脑机融合与增强研究受到广泛关注，成为弥补脑机行为差异、提升人工模型认知能力的关键途径之一。本报告将聚焦神经表征学习、脑机表征对齐等问题，探讨神经表征驱动的脑机对齐技术及其在脑机增强中的应用，阐述其研究背景、基本概念与实现形式。
  
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
