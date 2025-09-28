# 统一搜索（Unified Search）
用于 GraphRAG 搜索对比的统一演示程序。

⚠️ 本应用仅用于演示/实验目的，不提供技术支持。在 GraphRAG 代码仓库（repo）中提交的问题可能无法得到处理。

## 环境要求（Requirements）：
- Python 3.11
- UV（Python 包管理工具）
    
本示例应用未发布至 PyPI，因此您需要克隆 GraphRAG 代码仓库，并在对应文件夹中运行。

建议始终使用虚拟环境，操作步骤如下：

- 执行命令 `uv venv --python 3.11`（创建基于 Python 3.11 的虚拟环境）
- 执行命令 `source .venv/bin/activate`（激活虚拟环境，Windows 系统可使用 `.venv\Scripts\activate`）

## 运行索引（Run index）
在运行统一搜索前，需使用 GraphRAG 为数据集建立索引。建议先参考 [快速开始指南](https://microsoft.github.io/graphrag/get_started/)（Getting Started guide）。若要使用统一搜索的全部功能，必须在运行 GraphRAG 索引时启用图嵌入（graph embedding）和 UMAP 功能，配置如下：
``` yaml
embed_graph:
  enabled: true  # 启用图嵌入

umap:
  enabled: true  # 启用UMAP
```

## 数据集（Datasets）
统一搜索支持多个 GraphRAG 索引，需通过目录清单文件（directory listing file）实现。在存储所有数据集（本地或 Blob 存储）的根文件夹中，创建一个 `listing.json` 文件，格式如下（每个数据集对应一条条目）：

```json
[{
    "key": "<用于标识数据集1的关键字>",
    "path": "<数据集1的路径>",
    "name": "<用于标识数据集1的名称>",
    "description": "<数据集1的描述信息>",
    "community_level": "<用于筛选的社区层级整数值>"
},{
    "key": "<用于标识数据集2的关键字>",
    "path": "<数据集2的路径>",
    "name": "<用于标识数据集2的名称>",
    "description": "<数据集2的描述信息>",
    "community_level": "<用于筛选的社区层级整数值>"
}]
```

示例：若您有一个名为 "projects" 的文件夹，其中存储了多个 GraphRAG 索引，且已按照“快速开始指南”完成操作，则该 "projects" 文件夹中的 `listing.json` 可按如下格式编写：
```json
[{
    "key": "ragtest-demo",  // 数据集关键字
    "path": "ragtest",      // 数据集在"projects"文件夹中的相对路径
    "name": "A Christmas Carol",  // 数据集名称（《圣诞颂歌》）
    "description": "Getting Started index of the novel A Christmas Carol",  // 描述（基于小说《圣诞颂歌》创建的快速开始索引）
    "community_level": 2  // 社区层级
}]
```

### 数据源配置（Data Source Configuration）
“projects”文件夹（数据集根目录）的预期结构如下：
- projects_folder（数据集根目录）
    - listing.json（数据集清单文件）
    - dataset_1（数据集1文件夹）
        - settings.yaml（配置文件）
        - .env（环境变量文件，若在其他位置声明环境变量则可选）
        - output（输出文件夹）
        - prompts（提示词文件夹）
    - dataset_2（数据集2文件夹）
        - settings.yaml（配置文件）
        - .env（环境变量文件，若在其他位置声明环境变量则可选）
        - output（输出文件夹）
        - prompts（提示词文件夹）
    - ...（其他数据集文件夹，结构同上）

注意：每个数据集文件夹下的其他未提及文件夹会被忽略，但不会影响应用运行；且仅 `listing.json` 中声明的数据集会用于统一搜索。

## 数据集存储方式（Storing your datasets）
统一搜索的数据集可存储在本地或 Blob 存储中。

### 1. 本地数据文件夹（Local data folder）
1. 按照上述结构，创建包含所有数据和配置文件的本地文件夹
2. 通过以下环境变量，将文件夹的绝对路径告知应用：
- `DATA_ROOT` = `<数据文件夹的绝对路径>`（例如：`DATA_ROOT = "C:\Users\username\projects"`）

### 2. Azure Blob 存储（Azure Blob Storage）
1. 若使用 Azure Blob 存储，需先创建 Blob 存储账户，并新建一个名为“data”的容器，再将所有数据和配置文件按上述结构上传至该容器
2. 执行命令 `az login`，登录拥有该存储账户读取权限的账号
3. 通过以下环境变量，告知应用需使用的 Blob 存储账户：
- `BLOB_ACCOUNT_NAME` = `<Blob存储账户名称>`
4. （可选）若需将数据集存储在自定义名称的容器中（默认使用步骤1中创建的“data”容器），可通过以下环境变量设置：
- `BLOB_CONTAINER_NAME` = `<存储数据集的Blob容器名称>`


# 运行应用（Run the app）

1. 安装所有依赖：执行命令 `uv sync --extra dev`
2. 使用 Streamlit 运行项目：执行命令 `uv run poe start`

# 应用使用说明（How to use it）

![初始页面](images/image-1.png)（Initial page）

## 配置面板（左侧面板）（Configuration panel (left panel)）
启动应用后，初始界面会显示两个主要面板。左侧面板提供应用的多项配置选项，且可关闭，具体功能如下：
1. **数据集（Datasets）**：下拉菜单中会按顺序显示 `listing.json` 文件中定义的所有数据集
2. **建议问题数量（Number of suggested questions）**：用户可通过该选项设置生成的建议问题数量
3. **搜索选项（Search options）**：此部分用于选择应用中启用的搜索类型，使用应用前至少需启用一种搜索类型

## 搜索面板（右侧面板）（Searches panel (right panel)）
右侧面板包含多项功能，具体如下：
1. 面板顶部会显示所选数据集的基本信息（名称和描述）
2. 数据集信息下方有一个“生成建议问题（Suggest some questions）”按钮：点击后，应用会通过全局搜索分析数据集，并生成对应数量的关键问题（问题数量由配置面板中的“建议问题数量”设置决定）；若需选择某一建议问题，点击问题左侧的复选框即可
3. 文本输入框：标签为“输入问题以对比结果（Ask a question to compare the results）”，用户可在此输入需提交的问题
4. 两个标签页：分别为“搜索（Search）”和“图探索器（Graph Explorer）”
    1. 搜索（Search）：此处会显示所有搜索结果及其引用来源（citations）
    2. 图探索器（Graph Explorer）：该标签页分为三个部分——社区报告（Community Reports）、实体图（Entity Graph）和已选报告（Selected Report）

##### 点击“生成建议问题”后（Suggest some question clicked）
![点击“生成建议问题”后](images/image-2.png)

##### 点击选中某一建议问题后（Selected question clicked）
![点击选中某一建议问题后](images/image-3.png)

##### 图探索器标签页（Graph Explorer tab）
![图探索器标签页](images/image-4.png)