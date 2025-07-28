---
layout: event
title: 多模态语言文本大模型可以全面预测人脑自然语言活动
speaker: 王浩丞
institution: 香港中文大学
date: 2025-09-01 10:00
permalink: /events/2025-09-Wang-Haocheng/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
abstract: |
  本研究提出了一个统一的计算框架，该框架将声学、言语及词级语言结构联系起来，旨在探究人类大脑中日常对话的神经基础。研究中，我们采用皮层脑电图（electrocorticography）记录了参与者进行开放式真实对话时，长达 100 小时的言语生成与理解过程中的神经信号。我们从多模态语音转文本模型（Whisper）中提取了低层级声学嵌入、中间层级言语嵌入和语境化词嵌入，并构建了编码模型，通过线性映射将这些嵌入与言语生成及理解过程中的大脑活动关联起来。值得注意的是，对于未参与模型训练的数小时新对话，该模型仍能准确预测语言处理层级中每个层级的神经活动。模型的内部处理层级与负责言语和语言处理的皮层层级相匹配：感觉和运动区域与模型的言语嵌入更契合，而高层级语言区域则与模型的语言嵌入更匹配。Whisper 模型能够捕捉到言语生成中词汇发音前 “语言到言语” 的编码时间序列，以及言语理解中发音后 “言语到语言” 的编码时间序列。相比符号模型，该模型习得的嵌入在捕捉支持自然言语和语言的神经活动方面表现更优。这些发现为研究范式的转变提供了支持，即转向采用统一计算模型来捕捉现实对话中言语理解与生成的完整处理层级。
  
bio: |
  王浩丞是普林斯顿大学的在读博士生。他拥有生物学、数学和计算神经科学学士学位。他热衷于构建更精准的大脑计算模型，目前正专注于通过对比皮层脑电图（ECoG）数据与大型语言模型，来研究大脑中语义表征的特性。
  
outline: |
  1. 讲座内容
  2. 问答环节
  
resources: |
  - [预读论文](https://doi.org/10.1038/s41562-025-02105-9)
  
zoom_id: 958 9105 3788
zoom_password: 213165
status: active
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
