---
layout: event
title: 大语言模型与人脑语言加工的对齐机制
speaker: 李吉星博士
institution: 香港城市大学
date: 2025-07-08 10:00
permalink: /events/2025-07-Li-Jixing/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
abstract: |
  近年来，大语言模型与人脑对齐的研究不断深入，不仅加深了我们对人类大脑语言处理机制的理解，也为未来构建更类脑的人工智能系统提供了重要启示。在本次报告中，我将首先介绍一项基于fMRI数据的相关性研究。研究表明，与指令微调相比，模型规模的扩展更显著地增强了其对人脑语言信息的表征能力。随后，我将分享一项因果性研究，通过对大语言模型的特定模块或参数进行系统性屏蔽与扰动，来观察其在语言任务中的功能变化。结果显示，经过“损伤”处理的模型更容易表现出类似韦尼克失语症的语义障碍，而模拟布洛卡失语症中以句法受损为特征的语言障碍则相对困难。这一发现揭示了当前语言模型在模块化语言加工方面与人脑之间的异同。
  
bio: |
  李吉星现为香港城市大学语言学系助理教授。她于2019年获得康奈尔大学语言学博士学位，于2022年在纽约大学阿布扎比分校的语言神经科学实验室完成博士后研究。她的研究结合自然语言处理模型，探索人脑的语言加工机制，综合语言学、心理学、认知神经科学及自然语言处理等多个学科领域。其研究成果已发表于Nature Computational Science、 eLife、Journal of Neuroscience、Scientific Data、Imaging Neuroscience等期刊，以及 ACL 等自然语言处理顶级会议。担任Communications Psychology编委会成员。
  
outline: |
  1. 讲座内容
  2. 问答环节
  
resources: |
  - [预读论文](https://www.biorxiv.org/content/10.1101/2024.08.15.608196v4)
zoom_id: 958 9105 3788
zoom_password: 213165
photo: jixing.png
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
