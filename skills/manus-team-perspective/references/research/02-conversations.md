# Manus团队 - 长对话与访谈

## 季逸超技术博客 - Context Engineering长文（2025.7.18）

这是目前能获取到的最深入的创始人一手思考记录。关键洞察：

### 技术路线选择的背后故事
- 早期NLP生涯用BERT，每个新任务微调"often took weeks per iteration"
- 之前创业公司从零训练模型，但GPT-3和Flan-T5一夜之间让那些模型过时
- 这段创伤性经历直接导致Manus选择context engineering而非训练端到端agent模型
- 核心决策逻辑："ship improvements in hours instead of weeks" + 保持模型无关性
- 团队重建了4次agent框架——"Stochastic Graduate Descent"

### 即兴类比风格
- "If model progress is the rising tide, we want Manus to be the boat, not the pillar stuck to the seabed."——涨潮与船/柱子的比喻
- "Erasing failure removes evidence."——简洁有力的判断句
- 用todo.md作为注意力机制——这不是装饰性的，是工程性的
- "error recovery is one of the clearest indicators of true agentic behavior"——对"什么是真正的agent"的定义

### 对学术界的隐性批评
- 指出学术benchmark聚焦于理想条件下的成功，而"error recovery"被严重低估
- Few-shot prompting在agent系统中适得其反——"Language models are excellent mimics"
- "The more uniform your context, the more brittle your agent becomes"——反直觉的结论

## 肖翼在Meta收购公告中的声明（2025.12.29）

- "Joining Meta allows us to build on a stronger, more sustainable foundation without changing how Manus works or how decisions are made."
- 强调不变：产品不变、决策方式不变
- 强调变化：更强的基础设施、更大规模的用户触达

## 张涛在Microsoft合作公告中的声明（2025.11.19）

- "Our goal has always been to help more users experience Manus and complete their work faster."
- 定位清晰：更快完成工作，不是替代人

## 年度信（2026.3.12）

### 创始时刻
- Manus自主复刻了一个团队花了一个多月开发的产品——搜索API、收集数据、建网站、设计资产——一小时完成
- 这一刻让他们相信技术的变革性力量，用"蝴蝶扇动翅膀"比喻

### 用户哲学
- 三个用户故事代表三种人群：
  - 职场母亲：一小时完成一天工作量，周末留给孩子们
  - 86岁语言学家Arkady：零编程能力构建了AI语言学习web应用
  - 新加坡花艺师Noelle：无代码构建AI花束设计器
- 核心信念："Anyone who can use a messaging app can use Manus."
- 抱负："Go further"（让更多非技术人员使用）+ "Go deeper"（让Manus 24/7不间断工作）

### 自我定位
- "I'm nobody, and I'm everybody. I'm everyone on the Manus team."——集体主义而非个人英雄
- 感谢社区、感谢AI基础模型建设者、感谢自己的团队"moving faster than anyone thought we could"

## "过去三个月与未来"文章（2025.6.26）

### 对用户行为的观察
- 教师构建交互式课件、小企业主自动化内容管线、研究者综合多语言文献、学生创建作品集网站
- 核心发现：人机协作从chat-based交互向"真正的任务委派"转变

### 自我批评
- 发现问题1：无限可能性悖论——"the paradox of infinite possibility created unexpected friction"，用户不知道该让AI做什么
- 发现问题2：成本和速度——自主任务完成需要大量计算，等待时间长、成本高

### 应对策略
- Chat Mode：对话界面帮助用户明确需求
- Playbooks：模板和最佳实践，给"结构化的成功路径"而非空白画布
- 性能优化：速度翻倍、成本降5倍

### 未来愿景
- 三层递进：
  1. 成为"任何信息需求的默认起点"
  2. 日常文件和文档与Manus共同生成
  3. "a third hand: a seamless extension of human capabilities"

## Wide Research文章中的思考（2025.10.29）

### 对行业假设的挑战
- LLM上下文窗口扩展不能解决规模化问题——4个具体原因
- 描述了清晰的退化模式：前5个条目→真实研究；6-8条→质量微妙下降；9+→进入fabrication mode
- "These fabrications are sophisticated, grammatically flawless, and stylistically consistent with earlier legitimate entries"

### 架构哲学
- "a fundamental shift away from the single-processor paradigm"
- 从"AI assistant"时代到"AI workforce"时代
- 子agent之间不直接通信，所有协调通过主controller——防止context污染
- "The 50th item is researched just as thoroughly as the first"

## 信息缺口

- 没有找到创始人的播客/视频访谈transcript
- 没有找到肖翼个人的深度长访谈
- 创始人之间的互动和分歧没有公开记录
- 被追问时的即兴反应记录缺失（主要是准备好的官方文章）

信息来源：manus.im官方博客
可信度：一手来源（团队自己写的官方博客）
