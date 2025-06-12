---
layout: default
title: 首页
permalink: /
---

# 🧠 计算神经语言学论坛

<div style="text-align: center; margin: 2rem 0;">
    <p style="font-size: 1.2rem; color: var(--text-light);">
        欢迎来到<strong>计算神经语言学论坛</strong>的官方网站，这是一个由<strong>计算神经语言学</strong>公众号主办的学术交流平台。
    </p>
    <p style="font-size: 1.2rem; color: var(--text-light);">
        我们专注于<strong>心理语言学、神经科学和计算建模</strong>的交叉领域，促进开放、跨学科的对话。
    </p>
</div>

## 🎤 即将举行的讲座

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
                    <td>{{ event.date | date: "%Y年%m月%d日" }}</td>
                    <td>{{ event.speaker }}</td>
                    <td><em>{{ event.title }}</em></td>
                    <td>{{ event.institution }}</td>
                    <td>
                        {% if event.status == 'active' %}
                        <a href="{{ site.baseurl }}/events/{{ event.permalink }}/" class="button">详情</a>
                        {% elsif event.status == 'upcoming' %}
                        <span class="button" style="background-color: var(--text-light); cursor: not-allowed;">即将发布</span>
                        {% endif %}
                    </td>
                </tr>
                {% endif %}
            {% endfor %}
        </tbody>
    </table>
</div>

> 所有讲座都是免费的，面向研究人员、学生和爱好者开放。欢迎通过 Zoom 参与讲座并进行问答互动！

## 🧭 关于论坛

<div class="card">
    <h3>为什么创办这个论坛</h3>
    <p>现代认知神经科学和计算语言学在方法论上有许多惊人的重叠。我们相信，真正的创新来自于研究者之间的<strong>跨界对话</strong>。</p>

    <h3>我们的工作</h3>
    <ul style="list-style: none; padding: 0;">
        <li style="margin-bottom: 1rem;">🎯 举办领域内顶尖学者的在线讲座</li>
        <li style="margin-bottom: 1rem;">📚 分享技术资源、分析流程和阅读清单</li>
        <li style="margin-bottom: 1rem;">🤝 建立专注于跨学科合作的学术社群</li>
    </ul>
</div>

## 📚 历史讲座

<div class="card">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
        {% assign past_events = site.data.events.events | where: "status", "past" | sort: "date" | reverse %}
        {% for event in past_events %}
        <div style="background: var(--background-light); padding: 1rem; border-radius: var(--border-radius);">
            <h4>{{ event.date | date: "%Y年%m月" }}</h4>
            <p><strong>{{ event.title }}</strong></p>
            <p>{{ event.speaker }}（{{ event.institution }}）</p>
            {% if event.slides %}
            <a href="{{ event.slides }}" class="button">查看幻灯片</a>
            {% endif %}
            {% if event.video %}
            <a href="{{ event.video }}" class="button">观看视频</a>
            {% endif %}
        </div>
        {% endfor %}
    </div>
</div>

## 👥 组织者

<div class="card">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
        <div style="text-align: center;">
            <img src="{{ site.baseurl }}/assets/images/organizers/xufeng.jpg" alt="段旭峰" style="width: 150px; height: 150px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
            <h3 style="margin: 0.5rem 0;">段旭峰</h3>
            <p style="color: var(--text-light); margin: 0.5rem 0;">香港中文大学</p>
            <div style="margin-top: 1rem;">
                <a href="https://xufengduan.github.io/" class="button" style="margin: 0.5rem;">个人主页</a>
            </div>
        </div>
        
        <div style="text-align: center;">
            <img src="{{ site.baseurl }}/assets/images/organizers/shuqi.jpg" alt="王书琪" style="width: 150px; height: 150px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
            <h3 style="margin: 0.5rem 0;">王书琪</h3>
            <p style="color: var(--text-light); margin: 0.5rem 0;">香港中文大学</p>
            <div style="margin-top: 1rem;">
                <a href="https://scholar.google.com/citations?user=zfmMDg4AAAAJ&hl=en" class="button" style="margin: 0.5rem;">Google Scholar</a>
            </div>
        </div>
        
        <div style="text-align: center;">
            <img src="{{ site.baseurl }}/assets/images/organizers/hanlin.jpg" alt="吴翰林" style="width: 150px; height: 150px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
            <h3 style="margin: 0.5rem 0;">吴翰林</h3>
            <p style="color: var(--text-light); margin: 0.5rem 0;">香港中文大学</p>
            <div style="margin-top: 1rem;">
                <a href="https://hanlin.phd/" class="button" style="margin: 0.5rem;">个人主页</a>
            </div>
        </div>
    </div>
</div>

## 👥 加入社群

<div class="card" style="text-align: center;">
    <h3>想要加入我们的学术交流圈？</h3>
    <p style="margin: 1rem 0;">我们欢迎所有对计算神经语言学感兴趣的研究者和学生</p>
    <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 1rem;">
        <a href="{{ site.baseurl }}/community/" class="button">立即加入</a>
        <button onclick="showQRCode()" class="button" style="background-color: var(--accent-color);">关注公众号</button>
    </div>
</div>

<!-- 二维码模态框 -->
<div id="qrcodeModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.5); z-index: 1000;">
    <div style="position: relative; background-color: white; margin: 15% auto; padding: 20px; width: 300px; border-radius: 5px; text-align: center;">
        <span onclick="hideQRCode()" style="position: absolute; right: 10px; top: 5px; cursor: pointer; font-size: 20px;">&times;</span>
        <h3 style="margin-bottom: 20px;">扫码关注公众号</h3>
        <img src="{{ site.baseurl }}/assets/images/qrcode.jpg" alt="公众号二维码" style="width: 200px; height: 200px;">
    </div>
</div>

<script>
function showQRCode() {
    document.getElementById('qrcodeModal').style.display = 'block';
}

function hideQRCode() {
    document.getElementById('qrcodeModal').style.display = 'none';
}

// 点击模态框外部关闭
window.onclick = function(event) {
    var modal = document.getElementById('qrcodeModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}
</script>

## 📬 联系我们

<div class="card">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
        <div>
            <h4>合作机会</h4>
            <ul style="list-style: none; padding: 0;">
                <li>📢 演讲者推荐</li>
                <li>🤝 与实验室或院系的联合活动</li>
                <li>🔧 技术工作坊合作</li>
            </ul>
        </div>
        <div>
            <h4>联系方式</h4>
            <p>📧 <a href="mailto:neuro.language.research@gmail.com">neuro.language.research@gmail.com</a></p>
        </div>
    </div>
</div>

## ⭐️ 致谢

<div class="card" style="text-align: center;">
    <p>本论坛由<a href="https://mp.weixin.qq.com/">计算神经语言学</a>公众号背后的研究者组织，得到了来自心理学家、语言学家和计算科学家组成的跨学科社群的支持。</p>
</div>

---

> "语言不仅仅是代码 —— 它是运动中的认知。"