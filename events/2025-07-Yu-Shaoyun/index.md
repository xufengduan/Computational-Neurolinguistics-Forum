---
layout: event
title: 大语言模型遇上阅读中的大脑
speaker: 于劭赟
institution: 香港中文大学
date: 2025-07-28 10:00
permalink: /events/2025-07-Yu-Shaoyun/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
video_link: |
  https://cuhk.zoom.us/rec/share/YTNiKs-gssSIdDnuoI4fUtRwcP8KlGGOAmB2USgc7nIvL3yOW7xQtaAQpMYBbLRP.Rk9C0_3vf7FSmpq4?startTime=1753668128000
abstract: |
  词语预测一直是大语言模型的核心预训练任务，并推动了当前模型的成功。然而，这一任务是否足以支撑大语言模型迈向通用人工智能，仍是学术界广泛讨论的问题。事实上，在人类的语言使用过程中，词语预测远非唯一的认知机制。这在以阅读为代表的语篇加工中尤为显见：我们不仅会预测词语，还需要在句子之上的层面理解语义的连贯性及逻辑关系。本次报告中，我将首先介绍在模型训练中引入句子层级预测任务的尝试，并探讨其对模型与人脑对齐的影响。此外，我还将讨论，虽然大脑中的语义表征同样依赖上下文信息，但其与模型所使用的上下文窗口机制可能有本质不同。最后，模型与大脑的对齐程度也会因被试个体而异，这提示我们本领域研究中仍有很多未知有待探索。
  
bio: |
  于劭赟现为香港中文大学语言学及现代语言系研究助理教授。他于2021年获得名古屋大学人文学博士学位，于2025年在香港理工大学脑、语言及计算实验室完成博士后研究。他的研究兴趣涵盖人类语言的多个基本组成部分，从基础的句法结构、具身认知，到更高层次的语篇理解。他结合计算建模、神经影像和行为实验的方法，以跨学科的视角研究这些课题。其研究成果已发表于Science Advances、 Brain and Language、Frontiers in Psychology、Language Sciences等期刊。
  
outline: |
  1. 讲座内容
  2. 问答环节
  
resources: |
  - [预读论文](https://www.science.org/doi/10.1126/sciadv.adn7744)
  
zoom_id: 958 9105 3788
zoom_password: 213165
video_password: MVZ7eW#u
status: past
photo: shaoyun.jpg
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
