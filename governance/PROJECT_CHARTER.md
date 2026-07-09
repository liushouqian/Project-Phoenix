# Project Phoenix Charter

---

# 1. Mission（使命）

Project Phoenix is a 26-week engineering transformation program.

It transforms a Frontend Engineer into an AI Application Engineer
capable of building production-grade AI systems and working in international engineering environments.

This is not a learning project.
This is a system-building project.

---

# 2. Product Definition（产品定义）

Project Phoenix will evolve into a production-like system:

> **AI Workspace System**

An AI-powered engineering workspace that includes:

- AI Chat System
- Tool Calling System
- RAG Knowledge System
- Workflow / Agent System
- MCP Tool Integration (future)
- Multi-Agent collaboration (future)

最终它是一个：

> **AI Agent Operating System (AIOS-like system)**

---

# 3. System Vision（系统愿景）

We are building a layered AI system:

### Layer 1: Interface Layer
- Web UI (React / Vue)
- Chat interface

### Layer 2: AI Orchestration Layer
- LLM API integration
- Tool Calling
- Prompt orchestration

### Layer 3: Intelligence Layer
- RAG system
- Memory system
- Agent reasoning

### Layer 4: Workflow Layer
- LangGraph-based workflows
- Multi-step execution
- Planning + Execution separation

### Layer 5: Integration Layer
- MCP tools
- External systems (GitHub, Notion, etc.)

---

# 4. Goals（26周目标）

## Technical Goals
- Build AI Workspace (production-level project)
- Implement Chat + Tools + RAG + Workflow
- Understand AI system architecture
- Deploy real AI services
- Build MCP integration (basic)

## Engineering Goals
- Ability to design AI systems independently
- Ability to debug LLM-based systems
- Ability to structure full-stack AI projects

## Career Goals
- AI Engineer / AI Application Engineer job readiness
- International-level GitHub portfolio
- Ability to explain system design in English

---

# 5. Scope（范围）

## We WILL DO
- AI application engineering
- LLM API systems
- Agent architecture design
- RAG systems
- Workflow orchestration
- Full-stack AI products

## We WILL NOT DO
- Training foundation models
- Deep learning research
- Academic ML theory
- Competitive programming

---

# 6. Principles（核心原则）

- Build > Learn
- System > Tool
- Repo is the single source of truth
- Everything must produce output
- No isolated learning without integration
- Weekly sprint delivery is mandatory
- English is a gradual working language
- AI is a collaborator (Tech Lead Model)

---

# 7. Working Model（工作方式）

We operate like a real engineering team:

## Sprint Cycle
- 1 Sprint = 1 week
- Every Sprint has deliverables
- Every Sprint ends with Review

## Daily Workflow
Learn → Build → Commit → Journal → Review

## Weekly Cycle
- Sunday: Planning (Sprint Design)
- Monday–Saturday: Execution
- Sunday: Review + Next Sprint

---

# 8. AI Collaboration Model（关键新增）

This project is co-developed with an AI Tech Lead.

## AI Role (ChatGPT)
- Sprint planning
- Architecture review
- Code review
- System design guidance
- Career guidance

## Human Role (Engineer)
- Implementation
- Decision execution
- System building
- Daily commits
- Documentation

## Core Rule

> AI does not replace thinking.
> AI accelerates engineering.

---

# 9. Evolution Path（演进路径）

## Phase 1 (Sprint 0–2)
Project foundation + AI Chat system

## Phase 2 (Sprint 3–6)
Tool calling + RAG system

## Phase 3 (Sprint 7–12)
Workflow / LangGraph system

## Phase 4 (Sprint 13–18)
MCP integration + advanced agents

## Phase 5 (Sprint 19–24)
Production system + optimization

## Phase 6 (Sprint 25–26)
Portfolio + interview preparation

---

# 10. Constraints（约束）

- Primary language: Python (backend AI systems)
- Frontend: React / Vue / TypeScript
- No over-engineering in early phases
- All features must be production-oriented
- No “toy demos”

---

# 11. Definition of Success（成功标准）

This project is successful if:

- A working AI Workspace system exists
- GitHub shows real engineering capability
- Candidate can design AI systems independently
- Candidate can pass AI Engineer interviews
- Candidate can communicate in technical English

Failure is defined as:

- Only learning without building
- No production system after 26 weeks
- No portfolio output

## Timekeeping Rule

Project Phoenix uses two separate tracking systems:

1. Global Day Number
- Used for journal entries
- Starts from Day 1 and increases continuously across the whole project

2. Sprint Task Number
- Used for sprint planning and execution
- Format: Sprint X · Task Y
- Must not be mixed with the global day number

Example:
- Journal title: Day 5
- Sprint label: Sprint 1 - AI Workspace Foundation
- Task label: Task 3 - Real LLM Integration

## 技术原则: 聊天系统最小分层
- schemas/: 定义请求和响应的数据结构
- routes/: 处理HTTP层
- services/: 处理业务逻辑、模型调用、上下文拼接
- conversation_store/: 负责会话状态存取
- core/config: 负责环境变量和模型配置