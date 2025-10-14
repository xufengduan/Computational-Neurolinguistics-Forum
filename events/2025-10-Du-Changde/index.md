---
layout: event
title: 认知启发的多模态大语言模型概念表征机理解析
speaker: 杜长德教授
institution: 中科院自动化所
date: 2025-10-10 19:00
permalink: /events/2025-10-Du-Changde/
zoom_link: |
  https://cuhk.zoom.us/j/95891053788?pwd=lWyxDJW0hy9Bkjaubfo9pmUz9qUh7h.1
video_link: |
  https://cuhk.zoom.us/rec/share/6G7xT7ykl9H11FnFEEj2z0SPNUsCCzwp3p8R5OBBsFNWV_19bQzoq0PfIwSqykA.Vywfs5-J9uA0xRhc
abstract: |
  人类如何认知和概念化世界万物是认知科学的核心问题。随着多模态大语言模型（MLLM）的兴起，一个关键问题随之而来：这些先进的AI模型是否发展出与人类相似的物体概念表征？我们借鉴认知心理学的经典“三选一”范式，利用大语言模型（LLM）和MLLM收集了数百万次关于上千种自然物体的相似性判断。通过对这些海量行为数据进行表征学习，我们成功解析出模型内部用于概念判断的66个核心维度。研究发现，这些维度不仅稳定、可泛化，并且具有高度的可解释性，涌现出了与人类极为相似的语义结构。将这些大模型的概念表征与人类大脑功能性磁共振成像（fMRI）数据进行对比，发现在负责物体、场景和人脸识别的关键脑区（如EBA, PPA, FFA）中存在高度一致性。这些发现表明，尽管学习机制不同，多模态大模型仍能够发展出与人类类似的内部概念表征。
  
bio: |
  杜长德，中国科学院自动化研究所副研究员，硕士生导师，聚焦于生物智能与人工智能的交叉前沿，通过神经科学、认知科学与人工智能的深度融合，揭示大脑信息处理的基本原理，并以此推动新一代人工智能的发展。研究成果已发表于 Nature Machine Intelligence、IEEE TPAMI、ICLR、ICML等顶级期刊/会议。担任《The Innovation Informatics》青年编委。个人主页：https://changdedu.github.io/。
  
outline: |
  1. 讲座内容
  2. 问答环节
  
zoom_id: 958 9105 3788
zoom_password: 213165
video_password: 5^nUA7mu
status: past
photo: changde.jpg
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
