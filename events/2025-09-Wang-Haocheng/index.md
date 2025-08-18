---
layout: event
title: 多模态语言文本大模型可以全面预测人脑自然语言活动
speaker: 王浩丞
institution: 普林斯顿大学
date: 2025-09-01 10:00
permalink: /events/2025-09-Wang-Haocheng/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
abstract: |
  人类在日常对话中可以毫不费力地在听和说之间无缝切换。那么，人脑的神经机制是如何支持自然语言理解和生成的呢？在本研究中，我们采集了一个大规模的皮层脑电图（ECoG）数据集。被试者在长达一周的时间里，与病房中的家人、朋友、医生和医护人员等进行了开放式真实对话。我们从中提取出了总计约一百个小时（五十万词）的语言理解和生成的脑电图数据，以及同步的语音和文本信息。近年来快速发展的大语言模型为我们提供了一个分析自然数据的计算框架，因为这些模型能够捕捉到现实世界中语言的多样性和丰富的语境。我们使用了一个多模态语音转文本模型 Whisper，从中提取出声学、语音和语言的嵌入向量（vector embedding），并构建了一系列编码（encoding）模型，利用这些嵌入向量来预测大脑活动。结果显示，我们的编码模型能够准确预测语言理解和生成的时间序列，并且模型内部的处理层级与人类语言系统的层级结构相吻合。此外，基于嵌入向量的编码模型在预测大脑活动方面优于传统的符号模型。这些发现表明，大语言模型可以成为一个统一的计算框架，用于预测人脑语言理解和生成的时间进程、空间分布和层级结构。
  
bio: |
  王浩丞现于普林斯顿大学Hasson Lab就读心理学博士。他拥有生物学，数学，和计算神经科学学士学位。他目前使用大规模自然数据集和深度学习模型来研究人脑如何理解和生成语言。他的研究兴趣包括人脑语言系统与记忆系统的交流，脑对脑交流，和语言习得等。其研究成果已发表于Nature Human Behavior, Nature Communications, Nature Computational Science, eLife等期刊。
  
outline: |
  1. 讲座内容
  2. 问答环节
  
resources: |
  - [预读论文](https://doi.org/10.1038/s41562-025-02105-9)
  
zoom_id: 958 9105 3788
zoom_password: 213165
status: active
photo: haocheng.jpg
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
