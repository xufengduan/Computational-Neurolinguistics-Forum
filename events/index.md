---
layout: default
title: 讲座列表
permalink: /events/
---

# 🎤 讲座列表

## 即将举行的讲座

<div class="card" style="margin-top: 2rem;">
    <table>
        <thead>
            <tr>
                <th>日期</th>
                <th>演讲者</th>
                <th>主题</th>
                <th>单位</th>
                <th>链接</th>
            </tr>
        </thead>
        <tbody>
            {% for event in site.data.events.events %}
                {% if event.status == 'active' or event.status == 'upcoming' %}
                <tr>
                    <td>{{ event.date | date: "%Y年%m月%d日" }} {% assign hour = event.date | date: "%H" | plus: 0 %}{% if hour < 12 %}上午{% else %}下午{% endif %} {{ event.date | date: "%H:%M" }}</td>
                    <td>{{ event.speaker }}</td>
                    <td><em>{{ event.title }}</em></td>
                    <td>{{ event.institution }}</td>
                    <td>
                        {% if event.status == 'active' %}
                        <a href="{{ site.baseurl }}/events/{{ event.permalink }}/" class="button">详情</a>
                        {% else %}
                        <span class="button" style="background-color: var(--text-light);">即将发布</span>
                        {% endif %}
                    </td>
                </tr>
                {% endif %}
            {% endfor %}
        </tbody>
    </table>
</div>

## 历史讲座

<div class="card">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; overflow: hidden;">
        {% for event in site.data.events.events %}
            {% if event.status == 'past' %}
            <div style="background: var(--background-light); padding: 1rem; border-radius: var(--border-radius); overflow: hidden;">
                <h4>{{ event.date | date: "%Y年%m月" }}</h4>
                <p><strong>{{ event.title }}</strong></p>
                <p>{{ event.speaker }}（{{ event.institution }}）</p>
                {% if event.slides %}
                <a href="{{ event.slides }}" class="button">查看幻灯片</a>
                {% endif %}
                {% if event.video_link %}
                <a href="{{ event.video_link }}" class="button" target="_blank">观看视频</a>
                {% if event.video_password %}
                <p style="color: var(--text-light); font-size: 0.9rem; margin: 0.3rem 0; background: white; padding: 0.3rem; border-radius: 4px; display: inline-block;"><strong>密码：</strong>{{ event.video_password }}</p>
                {% endif %}
                {% endif %}
            </div>
            {% endif %}
        {% endfor %}
    </div>
</div>

## 如何参与

所有讲座都是免费的，面向研究人员、学生和爱好者开放。您可以通过 Zoom 参与讲座并进行问答互动。

## 讲座回放

讲座结束后，视频将上传至我们的 [YouTube 频道](#)。 