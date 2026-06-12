# 我收藏/创作的 Skill

Claude Code 自定义 Skill 合集，跨设备同步使用。

## 快速安装

```bash
git clone https://github.com/yinmc7-mc/my-claude-skills.git
cd my-claude-skills
bash install.sh
```

## 更新

```bash
cd my-claude-skills && git pull
```

## 卸载单个 Skill

```bash
rm ~/.claude/skills/<skill名>
```

## Skill 清单

### 思维框架 / 人物视角类（20个）

| Skill | 说明 |
|---|---|
| dario-amodei-perspective | Anthropic CEO Dario Amodei 思维框架 |
| darwin-skill | 达尔文式自主优化器 |
| elon-musk-skill | 马斯克思维操作系统 |
| feynman-skill | 费曼思维框架 |
| ilya-sutskever-skill | Ilya Sutskever 思维框架 |
| karpathy-skill | Karpathy 思维框架 |
| liu-qiangdong-perspective | 刘强东思维框架 |
| manus-team-perspective | Manus团队思维框架 |
| mrbeast-skill | MrBeast 内容创造操作系统 |
| munger-skill | 芒格思维框架 |
| naval-skill | Naval 思维操作系统 |
| paul-graham-skill | Paul Graham 思维框架 |
| steve-jobs-perspective | 乔布斯思维框架 |
| sun-yuchen-perspective | 孙宇晨思维框架 |
| taleb-skill | 塔勒布思维框架 |
| trump-skill | 特朗普思维框架 |
| x-mentor-skill | X/Twitter 运营导师 |
| zhang-xiaolong-perspective | 张小龙思维框架 |
| zhang-yiming-skill | 张一鸣思维框架 |
| zhangxuefeng-skill | 张雪峰思维框架 |

### PPT / 演示类（3个）

| Skill | 说明 |
|---|---|
| guizang-ppt-skill | 归藏PPT：WebGL背景横向翻页网页PPT |
| ppt-to-editable | PPT截图转可编辑PPT |
| rw-consulting-ppt | 咨询风PPT生成 |

### 内容创作类（6个）:star: :gift: 全部原创

| Skill | 说明 | 状态 |
|---|---|---|
| codebase-to-course | 代码库转课程 | 原创 |
| follow-builders | 关注Builder动态 | 原创 |
| frontend-slides | 前端幻灯片生成 | 原创 |
| newspaper-style | 报纸风格排版 | 原创 |
| youtube-to-ebook | YouTube视频转电子书 | 原创 |
| write-academic-report | 学术报告写作 | 原创 |

### 工具 / 数据类（7个）

| Skill | 说明 |
|---|---|
| baidu-search | 百度AI搜索 |
| data-todo-auto-new | 自动创建月度待办 |
| github-trending | GitHub趋势 |
| hackernews | Hacker News API |
| huashu-nuwa | 女娲造人：深度调研人物 |
| producthunt | Product Hunt 搜索 |
| zach-product-research | Sorftime选品分析 |

### 其他（2个）

| Skill | 说明 |
|---|---|
| skill-creator | 创建/修改skill的工具 |
| zach-feature-demand-validator | 亚马逊Feature需求验证 |

## 目录结构

```
my-claude-skills/
├── install.sh          # 一键安装脚本
├── README.md           # 本文件
├── skills/             # 目录型 skill（安装时符号链接）
└── standalone/         # 单文件 skill（安装时复制）
```

## 安装原理

- 目录型 skill → 符号链接到 `~/.claude/skills/`，方便 git pull 更新
- 单文件 skill → 复制到 `~/.claude/skills/`
- 已存在的 skill 自动跳过，不覆盖
