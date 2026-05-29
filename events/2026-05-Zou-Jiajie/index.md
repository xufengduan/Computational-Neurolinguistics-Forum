---
layout: event
title: 语言加工中的“排兵布阵”：语言层级结构引导的高效预测机制
speaker: 邹家杰
institution: 浙江大学
date: 2026-05-29 15:00
permalink: /events/2026-05-Zou-Jiajie/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
video_link: |
  https://cuhk.zoom.us/rec/share/WAahQhblpvaboDrW-EszF4di3XTw_1e7UH49ddiW612ORshW000HoqKPtxoDF3uZ.b38stpHygv470pB-
abstract: |
  语言研究中存在一场持久的争论：语言信息究竟应被表示为以统计关系为核心的序列，还是以句法为核心的层级结构？随着大语言模型的语言能力的快速提升，有相当多的有影响力的研究提出，人类与大模型的语言加工或许共享着相似的机制，即基于统计关系的下一个字预测。本报告将展示我们对这一争论的最新探索。通过系列行为、MEG与ECoG实验数据，我们揭示了人脑与大语言模型在语言加工上的关键差异：大语言模型通过访问前文所有词来实现对下一个词的准确预测；而大脑则以语言层级结构压缩前文信息，在有限资源下实现高效但并不精确的预测。对于新潮的脑与模型的相互启发研究而言，我们说明脑与模型在资源上的差异将使两者演化出不同的计算策略；对于经典的心理语言学研究而言，我们为语言层级结构提供了有力的神经科学证据，也给出了一个可能的计算层面的解释：层级结构的神经编码，可能正是大脑在有限认知资源下权衡预测准确度与预测效率的最优解。
  
bio: |
  邹家杰，浙江大学博士后、马普所生物控制论研究所访问学者。研究方向为融合神经影像与计算建模探究大脑如何加工语言、语音。研究成果发表于 Nature Neuroscience、Nature Communications、eLife 等期刊以及 ACL 等计算机会议。获批国自然青年基金，并多次担任Nature Communications、eLife、the Journal of Neuroscience 等期刊审稿人。
  
outline: |
  1. 讲座内容
  2. 问答环节
  
zoom_id: 958 9105 3788
zoom_password: 213165
video_password: c.w2+Bcf
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
