---
layout: event
title: 模型规模对模型-大脑对齐的影响
speaker: 李吉星博士
institution: 香港城市大学
date: 2025-07-08 10:00
permalink: /events/2025-07-Li-Jixing/
zoom_link: |
  https://cuhk.zoom.us/j/99902681951?pwd=KFTCQIbwRYLOMjj65Ylhr4EorvdlvY.1
abstract: |
  本研究探讨了大型语言模型（LLMs）与人类大脑语言处理的对齐关系。研究了模型规模（scaling）和指令微调（instruction tuning）对模型-大脑对齐的影响。
  通过比较不同规模的基座模型和微调模型与人类眼动和功能磁共振成像（fMRI）数据的对应关系，我们发现模型规模对模型-大脑对齐的影响大于指令微调。
  这一发现对理解LLMs的认知合理性及其在研究自然语言理解中的作用具有重要意义。
  
bio: |
  李吉星博士是香港城市大学语言学及翻译学系和行为及社会科学系的助理教授。
  她的研究主要应用计算模型来理解人类大脑在语言理解过程中如何表示和计算语义和句法信息。
  
outline: |
  1. 讲座内容
  2. 问答环节
  
resources: |
  - [预读论文](https://www.biorxiv.org/content/10.1101/2024.08.15.608196v4)
zoom_id: 999 0268 1951
zoom_password: 957301
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
{% if page.zoom_id %}
- 会议ID：{{ page.zoom_id }}
{% endif %}
{% if page.zoom_password %}
- 会议密码：{{ page.zoom_password }}
{% endif %}

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
