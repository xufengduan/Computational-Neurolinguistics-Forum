---
layout: default
title: 加入社群
permalink: /community/
---

# 加入计算神经语言学社群

<div class="card" style="text-align: center; margin: 2rem 0;">
    <p style="font-size: 1.2rem; color: var(--text-light);">
        欢迎加入我们的学术社群！我们致力于促进计算神经语言学领域的跨学科交流与合作。
    </p>
</div>

## 加入方式

<div class="card" style="margin: 2rem 0;">
    <h3 style="color: var(--text-color); margin-bottom: 1rem;">关注微信公众号</h3>
    <p style="font-size: 1.1rem; color: var(--text-light);">
        关注我们的微信公众号：<strong>计算神经语言学</strong>
    </p>
    <p style="color: var(--text-light); margin-top: 1rem;">
        请通过公众号后台获取入群方式
    </p>
    <div style="text-align: center; margin-top: 1.5rem;">
        <button onclick="showQRCode()" class="button" style="background-color: var(--accent-color);">扫码关注</button>
    </div>
</div>

## 社群活动

<div class="card" style="margin: 2rem 0;">
    <h3 style="color: var(--text-color); margin-bottom: 1rem;">📅 不定期活动</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin-top: 1rem;">
        <div class="activity-card">
            <h4>📚 文献讨论会</h4>
            <p>定期组织最新研究文献的深入讨论</p>
        </div>
        <div class="activity-card">
            <h4>💻 技术工作坊</h4>
            <p>分享前沿技术方法和工具使用</p>
        </div>
        <div class="activity-card">
            <h4>🎓 学术沙龙</h4>
            <p>促进跨学科交流与合作</p>
        </div>
    </div>
</div>

<div class="card" style="margin: 2rem 0;">
    <h3 style="color: var(--text-color); margin-bottom: 1rem;">🤝 合作机会</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin-top: 1rem;">
        <div class="activity-card">
            <h4>📋 联合举办学术会议</h4>
            <p>共同组织学术交流活动</p>
        </div>
        <div class="activity-card">
            <h4>📊 共同申请研究项目</h4>
            <p>开展跨机构合作研究</p>
        </div>
        <div class="activity-card">
            <h4>🔬 数据共享与合作</h4>
            <p>促进研究资源的有效利用</p>
        </div>
    </div>
</div>

## 社群守则

<div class="card" style="margin: 2rem 0;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
        <div class="rule-card">
            <h4>1. 尊重学术诚信</h4>
            <p>遵守学术道德规范</p>
        </div>
        <div class="rule-card">
            <h4>2. 保持专业讨论氛围</h4>
            <p>维护良好的学术交流环境</p>
        </div>
        <div class="rule-card">
            <h4>3. 遵守数据使用规范</h4>
            <p>确保数据安全和隐私保护</p>
        </div>
        <div class="rule-card">
            <h4>4. 保护知识产权</h4>
            <p>尊重原创研究成果</p>
        </div>
    </div>
</div>

## 联系我们

<div class="card" style="margin: 2rem 0;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
        <div class="contact-card">
            <h4>📧 邮箱</h4>
            <p><a href="mailto:xufeng.duan@link.cuhk.edu.hk">xufeng.duan@link.cuhk.edu.hk</a></p>
        </div>
        <div class="contact-card">
            <h4>📱 微信公众号</h4>
            <p>计算神经语言学</p>
        </div>
        <div class="contact-card">
            <h4>🌐 网站</h4>
            <p><a href="https://xufengduan.github.io/Computational-Neurolinguistics-Forum/">访问我们的网站</a></p>
        </div>
    </div>
</div>

<style>
.activity-card, .rule-card, .contact-card {
    background: var(--background-light);
    padding: 1.5rem;
    border-radius: var(--border-radius);
    transition: all 0.3s ease;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.activity-card:hover, .rule-card:hover, .contact-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.activity-card h4, .rule-card h4, .contact-card h4 {
    color: var(--text-color);
    margin-bottom: 0.5rem;
}

.activity-card p, .rule-card p, .contact-card p {
    color: var(--text-light);
    margin: 0;
}

.contact-card a {
    color: var(--text-color);
    text-decoration: none;
    transition: color 0.3s ease;
}

.contact-card a:hover {
    color: var(--primary-color);
}
</style>

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

---
