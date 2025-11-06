---
layout: event
title: 隐式神经反馈驱动的人工智能系统
speaker: 叶子逸教授
institution: 复旦大学可信具身智能研究院
date: 2025-10-31 19:00
permalink: /events/2025-10-Ye-Zianyi/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
video_link: |
  https://cuhk.zoom.us/rec/share/aLnlC_k9U5HbDfR3XFbsXn7iA4gKSI5W-MZ1DCs5dCvBWZ2uDR2KhbT--ZfijbbQ.lN80ayOJswC6axGL?startTime=1761908669000
abstract: |
  传统的人工智能系统严重依赖于人工的显式反馈（如基准测试的数据标注，交互系统中的用户点击等），这种模式不仅效率低下，且难以表现人类真实的认知状态，这不仅限制了系统的自适应能力，也为其留下了越狱的空间。为此，我们探索了隐式神经反馈驱动的人工智能系统，通过解码用户在与AI交互过程中的内在认知状态，构建一个更高效、更具适应性的交互闭环。在这个问题下，我们进行了两项前沿探索：首先，在交互式信息检索中，我们利用脑信号来监测用户的真实意图和对检索内容的满意度。实验证明，系统能够利用这种隐式的反馈，动态调整检索策略。其次，我们将其应用于解决大语言模型的幻觉抑制这一关键挑战。通过捕捉人脑的错误相关电位验证和分析幻觉存在风险等级的现象，并设计风险探针对模型行为进行操控。本研究期待为构建下一代能够深度理解并适应人类内在状态的、更可信和个性化的人工智能系统，提供一条神经科学驱动的技术路径。
  
bio: |
  叶子逸，复旦大学可信具身智能研究院副研究员，分别于2025年和2020年在清华大学获得博士学位和学士学位。主要从事多模态计算、信息检索相关的科研工作，代表性工作包括基于脑机接口的信息检索系统，大语言模型的鲁棒可解释偏好对齐等。研究成果已发表于Nature Communications Biology, ICLR, SIGIR, TOIS, Multimedia等国际一流期刊和会议，并被应用于多个工业场景当中。曾获中国中文信息学会优秀博士毕业论文、ACM上海分会优秀博士毕业论文，北京市优秀毕业生，清华大学启航金奖，CCIR 2024最佳论文提名奖等。个人主页：https://yeziyi1998.github.io/。
  
outline: |
  1. 讲座内容
  2. 问答环节
  
zoom_id: 958 9105 3788
zoom_password: 213165
video_password: k+y6AFsA
status: past
photo: ziyi.png
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
