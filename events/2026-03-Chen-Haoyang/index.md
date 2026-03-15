---
layout: event
title: 概念诞生与感知重塑：我们如何用语言"看见"世界
speaker: 陈昊扬
institution: 北京大学
date: 2026-03-13 11:00
permalink: /events/2026-03-Chen-Haoyang/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
video_link: |
  https://cuhk.zoom.us/clips/share/ExxGSQv2QmuTtU2ELrtRKA
abstract: |
  人类智能的核心能力之一是从复杂的感官经验中抽象出概念（符号化），并在此基础上发展出语言。然而，概念如何从底层感知中"脱离"出来，以及语言系统如何反向塑造我们的感知过程，在计算层面仍缺乏统一的解释。本次报告将围绕以下两项研究展开：
  首先，我将探讨概念是如何自下而上形成的。我们将介绍一个统一的概念认知计算框架——CATS Net。该模型通过双模块架构，模拟了人类如何从高维感官体验中提取低维概念，并随后在脱离直接感官输入的情况下进行知觉任务与交流。模型-大脑拟合分析表明，这种自发形成的概念空间与人类腹侧枕颞皮层（VOTC）的表征结构高度对齐。
  随后，我将进一步探讨语言经验如何反向调节视觉感知。通过对比具有不同语言经验的视觉模型，我们发现引入语言经验能显著提升模型对人类VOTC神经表征的解释力。此外，结合脑损伤患者的数据，我们表明：语言网络（左侧角回）与视觉皮层之间的白质连接完整性，会直接影响这一语言经验优势。
  
bio: |
  陈昊扬现于北京大学毕彦超实验室就读心理学博士。他目前结合使用特殊被试人群与深度学习模型，来研究人脑语言系统与视觉系统的交互过程。其研究成果已发表于Nature Human Behavior, Nature Computational Science。
  
outline: |
  1. 讲座内容
  2. 问答环节
  
zoom_id: 958 9105 3788
zoom_password: 213165
status: active
photo: haoyang.jpg
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
