---
layout: event
title: 大型语言模型如何预测大脑活动
speaker: 李伟博士
institution: MIT BCS
date: 2025-06-28
permalink: /events/2025-06-Li-Wei/
zoom_link: https://mit.zoom.us/j/123456789
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

- 时间：{{ page.date | date: "%Y年%m月%d日" }} 20:00-21:30（北京时间）
- 平台：Zoom
- 语言：中文
- 费用：免费

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
