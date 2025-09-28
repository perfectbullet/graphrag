# GraphRAG（图增强检索增强生成）

👉 [微软研究院博客文章](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/)<br/>
👉 [阅读文档](https://microsoft.github.io/graphrag)<br/>
👉 [GraphRAG 预印本（arXiv）](https://arxiv.org/pdf/2404.16130)

<div align="left">
  <a href="https://pypi.org/project/graphrag/">
    <img alt="PyPI - 版本" src="https://img.shields.io/pypi/v/graphrag">
  </a>
  <a href="https://pypi.org/project/graphrag/">
    <img alt="PyPI - 下载量" src="https://img.shields.io/pypi/dm/graphrag">
  </a>
  <a href="https://github.com/microsoft/graphrag/issues">
    <img alt="GitHub 问题" src="https://img.shields.io/github/issues/microsoft/graphrag">
  </a>
  <a href="https://github.com/microsoft/graphrag/discussions">
    <img alt="GitHub 讨论" src="https://img.shields.io/github/discussions/microsoft/graphrag">
  </a>
</div>

## 概述
GraphRAG 项目是一套数据流水线与转换工具集，旨在借助大语言模型（LLM）的能力，从非结构化文本中提取有意义的结构化数据。

如需深入了解 GraphRAG，以及如何利用它提升大语言模型对私有数据的推理能力，请访问 [微软研究院博客文章](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/)。

## 快速开始
若要启动 GraphRAG 系统，建议尝试 [命令行快速开始指南](https://microsoft.github.io/graphrag/get_started/)。

## 仓库说明
本仓库提供了一种利用知识图谱存储结构提升大语言模型输出效果的方法。请注意，所提供的代码仅作为演示用途，并非微软官方支持的产品。

⚠️ *警告：GraphRAG 索引构建可能是一项高成本操作，请完整阅读所有文档以了解相关流程和成本，建议从小规模场景开始尝试。*

## 深入探索
- 如需了解贡献指南，请参阅 [CONTRIBUTING.md](./CONTRIBUTING.md)
- 如需开始开发 GraphRAG，请参阅 [DEVELOPING.md](./DEVELOPING.md)
- 欢迎加入讨论并提供反馈，可访问 [GitHub 讨论板块](https://github.com/microsoft/graphrag/discussions)

## 提示词调优
直接将 GraphRAG 应用于您的数据，可能无法获得最佳效果。
我们强烈建议您遵循文档中的 [提示词调优指南](https://microsoft.github.io/graphrag/prompt_tuning/overview/)，对提示词进行微调。

## 版本控制
有关本项目版本控制方法的说明，请参阅 [重大变更文档](./breaking-changes.md)。

*在小版本更新之间，务必运行 `graphrag init --root [路径] --force` 命令，以确保使用最新的配置格式。若为大版本更新，若您希望避免重新为先前的数据集构建索引，请运行提供的迁移笔记本。请注意，此操作会覆盖您的配置和提示词，因此如有需要，请提前备份。*

## 负责任的人工智能常见问题（Responsible AI FAQ）
请参阅 [RAI_TRANSPARENCY.md](./RAI_TRANSPARENCY.md)

- [什么是 GraphRAG？](./RAI_TRANSPARENCY.md#what-is-graphrag)
- [GraphRAG 能做什么？](./RAI_TRANSPARENCY.md#what-can-graphrag-do)
- [GraphRAG 的目标用途是什么？](./RAI_TRANSPARENCY.md#what-are-graphrags-intended-uses)
- [GraphRAG 是如何评估的？使用哪些指标衡量其性能？](./RAI_TRANSPARENCY.md#how-was-graphrag-evaluated-what-metrics-are-used-to-measure-performance)
- [GraphRAG 有哪些局限性？用户在使用该系统时，如何最大限度降低局限性带来的影响？](./RAI_TRANSPARENCY.md#what-are-the-limitations-of-graphrag-how-can-users-minimize-the-impact-of-graphrags-limitations-when-using-the-system)
- [哪些运营因素和设置有助于高效、负责任地使用 GraphRAG？](./RAI_TRANSPARENCY.md#what-operational-factors-and-settings-allow-for-effective-and-responsible-use-of-graphrag)

## 商标声明
本项目可能包含相关项目、产品或服务的商标或标识。经授权使用微软商标或标识，需遵守 [微软商标与品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) 的规定。在本项目的修改版本中使用微软商标或标识，不得造成混淆，也不得暗示微软对此提供赞助。
任何第三方商标或标识的使用，均需遵守该第三方的相关规定。

## 隐私政策
[微软隐私声明](https://privacy.microsoft.com/en-us/privacystatement)