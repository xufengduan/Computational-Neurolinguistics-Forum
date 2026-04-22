---
layout: event
title: 文本计算揭示跨语言语义共享表征空间与气候的关联
speaker: 付泽
institution: 巴黎高等师范学院
date: 2026-05-11 15:00
permalink: /events/2026-05-Fu-Ze/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
abstract: |
  语言是交流思想、承载意义的重要工具。当今世界现存7000多种语言，各自拥有独特的语音形式、书写系统和句法规则，不同地区的人使用这些迥异的语言交换信息，构建文化内共同知识体系。然而，不同语言使用者理解同一个词多大程度上一致？什么信息在翻译中得以保存，什么又被丢失？跨语言的共性与差异如何产生，仍是领域内广泛讨论的问题。本次报告将分别从共性和差异两个方面展开讨论：一，通过认知视角阐释语言学的问题，探讨认知神经科学中关于概念表征的语义维度模型作为跨语言共同结构的可能性。基于多种语言词嵌入和个体评定空间，报告将探讨大脑中感知与核心认知维度如何构成跨语言语义表征的普遍骨架结构；二，在共同结构基础下，结合"生态-文化演化"的视角——即通过跨文化和历史数据——展示气候、传染病等生态因素如何与跨语言语义差异相关联，揭示语言中概念表征对所处生态环境的适应性发展。
  
bio: |
  付泽现为巴黎高等师范学院博士后，研究兴趣聚焦于从历史心理学视角理解人类如何运用心智模型，以及文化如何促进这一过程。他于2025年获得北京师范大学心理学博士学位，博士期间在北京大学毕彦超实验室Concept Lab开展概念的跨语言与文化演化研究，研究成果发表于Nature Communications、Cerebral Cortex、Communications Psychology。
  
outline: |
  1. 讲座内容
  2. 问答环节
  
zoom_id: 958 9105 3788
zoom_password: 213165
status: active
photo: fuze.png
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
