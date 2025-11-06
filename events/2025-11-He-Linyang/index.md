---
layout: event
title: 解纠缠的大模型揭示人脑的推理表征
speaker: 何林洋
institution: 哥伦比亚大学
date: 2025-11-17 10:00
permalink: /events/2025-11-He-Linyang/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
abstract: |
  理解人脑如何从处理简单的语言输入发展到执行高级推理，是认知神经科学的一项核心挑战。尽管大型语言模型（LLM）已被广泛用于建模和对齐脑活动，其内部表征仍高度纠缠，混合了词汇、句法、语义与推理等多层信息。直接使用LLM的原始表征难以区分具体由哪些特征驱动脑对齐，从而掩盖了深层认知过程的神经机制。这使得我们对大脑如何实现推理仍知之甚少。本讲座介绍一种新的残差解纠缠方法（Residual Disentanglement），在语言模型中分离出“推理表征”（Reasoning Embedding），并与词汇、句法和语义表征相互正交。结果显示，推理表征呈现出独特的时空响应模式：在时间上表现为约350–400毫秒的延迟高阶峰值，在空间上延伸至视觉皮层，超越传统语言区域。该研究为揭示模型与人脑在深层推理过程中的对应关系提供了新的计算框架，也为理解语言与思维的神经机制开辟了新的方向。
  
bio: |
  何林洋现为哥伦比亚大学祖克曼心智、大脑与行为研究所博士生。他的研究聚焦于AI模型的可解释性，利用可解释AI探索大脑的语言与言语机理以及言语脑机接口。他拥有复旦大学学士学位和密歇根大学硕士学位。他的研究成果已发表在 NeurIPS、EMNLP、ACL、COLING 等会议。
  
outline: |
  1. 讲座内容
  2. 问答环节
  
resources: |
  - [预读论文](https://arxiv.org/abs/2510.22860v1)
  
zoom_id: 958 9105 3788
zoom_password: 213165
status: active
photo: linyang.png
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
