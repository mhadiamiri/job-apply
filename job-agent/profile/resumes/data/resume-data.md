<!-- GENERATED from resume-data.pdf by scripts/sync_resumes.py. Do not edit. -->
# Hadi Amiri
mhadiamiri27@gmail.com Ottawa, Canada 343-988-5434 LinkedIn GitHub

## Summary

Cloud Data Engineer with over 4 years of experience specializing in cloud data platforms and AI
engineering. Proven ability to migrate complex ETL processes to Microsoft Fabric and Azure
Databricks, optimize data pipelines, and implement robust data governance. Successfully
leveraged expertise in data architecture and AI integration to drive innovation and efficiency
implementing applied AI, RAG system and agentic workflows.

## Work Experience

Cloud Data Engineer / Data Platform Engineer / Applied AI Engineer, Revolution Data Platforms
2024 – Present
Transformed Excel-based financial reporting into a Microsoft Fabric lakehouse, processing
over 1M records annually across 30+ tables sourced from a PeopleSoft ERP; implemented
bronze/silver/gold Delta layers, event-driven Data Factory ingestion, parameterized PySpark
transformation notebooks, data masking, and role-based access, thereby automating 7-8
hour manual tasks with scheduled workflows.
Spearheaded an SSIS-to-cloud migration program for a federal government department,
converting legacy ETL packages into Microsoft Fabric pipelines and Spark SQL notebooks
over a landing/staging/mart lakehouse, incorporating ARM-template deployment, a 3-
environment Dev/Staging/Prod workspace model, and Azure DevOps CI/CD.
Engineered a behavior-based routing engine that classified 1,761 SSIS packages into 5
migration lanes by structural behavior, achieving 75.1% automated/template coverage,
alongside a T-SQL to Spark SQL conversion pipeline that successfully processed 420 out of
420 production views with full fidelity.
Delivered 24 clinical data extract packages end-to-end with confirmed live Fabric imports,
featuring a 4-layer validation framework (structure, coverage, flow sanity, live import) and
delivering a sign-off-quality architecture document accompanied by a manager-facing
presentation.
Constructed and deployed an automated data-governance dashboard on Azure Databricks
using Delta Live Tables materialized views, exposing catalog, schema, table privileges, user
activity, and pipeline run history from Unity Catalog system tables, deployed as a Databricks
Asset Bundle operating under a service principal.
Led a feasibility study on Databricks-to-Azure SQL connectivity across five methods
(Lakehouse Federation, Spark JDBC, Unity Catalog JDBC, server-side DML, PyTDS) on
both Serverless and Classical compute, validating read and write paths over private
endpoints and VNet injection, and subsequently defined the production adoption
architecture.
Established on-premises data gateway integrations to transfer SQL Server tables and flat
files into a Microsoft Fabric Lakehouse, and installed the OneStream SIC gateway with
Simba Spark ODBC and OAuth service-principal authentication, enabling direct querying of
Databricks from the finance platform.
Executed ITIL-based on-call monitoring across 6 Databricks workspaces and 2 platform
environments with a 4-hour proactive sweep cadence and a 15-minute P1 SLA, supporting a
multi-hop Delta Share pipeline feeding an on-premises SCADA system, managing incidents
in ServiceNow and PagerDuty, and authoring post-incident Standard Operating Procedures
(SOPs).
Migrated multi-year legacy SPSS survey data to Azure on a medallion architecture using
Synapse Analytics and Data Factory, incorporating event-driven schema-change detection
across 10+ survey types and role-based controls, reducing manual processing by
approximately 70%.

Developed cargo-operations pipelines and a data-governance framework on Azure Logic
Apps with integrated validation rules and pipeline-health monitoring, and rebuilt a payroll
data platform on Data Factory and Synapse with automated validation compliant with data-
privacy requirements.
Accelerated document ingestion time by 2.3x and reduced average RAG agent response
time by approximately 80% (from 36s to 6.6s) on an air-gapped, Kubernetes-hosted agentic
AI platform, while implementing hybrid dense+sparse retrieval on Qdrant with content-hash
deduplication and a synthetic golden-dataset evaluation pipeline.
Built a LangGraph agent toolbox featuring parallel validation and judge nodes, ensuring
deterministic AI usage and human-gated workflows within the client's Azure AI Foundry
tenant for data sovereignty, and developed a provider-agnostic client capable of switching
between Anthropic, Azure OpenAI, and Azure AI Foundry without code modifications.
Deployed a production PII de-identification service (Microsoft Presidio + RoBERTa NER) as
an Azure ML managed endpoint, processing approximately 10 million clinical records with
94.9% redaction accuracy, and integrated it into the client's SSIS ETL via a thread-safe C#
task supporting bulk loading.
Research Assistant & Teaching Assistant, University of Ottawa, Ottawa, Canada
2020 – 2023
Developed approximate Bayesian neural networks for inference-time uncertainty
quantification in probabilistic classification, enhancing reliability for clinical decision support,
with findings published in IEEE.
Constructed a multimodal emotion and bipolar-severity assessment system using datasets
exceeding 2 million frames, integrating VGG-Face and FER2013 visual features, a deep
belief network for audio, early fusion techniques, and an LSTM for video classification.
Instructed tutorials for groups of up to 180 students on topics including uncertainty
evaluation in machine learning, computer architecture, and electrical circuits.
Backend & Database Developer, Tamtaam Development Company
2016 – 2019
Designed and optimized MS SQL Server databases, including normalization, indexing, and
stored procedures, and automated data loading processes using SSIS ETL packages.
Developed C#/ASP.NET backends, configured REST APIs, and integrated third-party
services.

## Education

University of Ottawa, M.Sc., Electrical & Computer Engineering (Software Engineering),
Tehran, Iran
2020 – 2022
Shahid Beheshti University, B.Sc., Electrical & Computer Engineering (Power Systems),
Tehran, Iran
2011 – 2015

## Skills

Microsoft Fabric
Azure
Databricks
ETL/ELT pipeline design
Medallion architecture
Delta Lake
Dimensional modeling
Star schema
Data warehousing
SSIS migration
Unity Catalog
Azure DevOps CI/CD
ARM templates
On-premises data gateway
OneStream SIC
ODBC/JDBC

## Languages

English(C1) Persian(native)
French(A1)

## Certificates And Clearances

Databricks Certified Generative AI Engineer Associate, Databricks
Government of Canada reliability status : security clearance
09/2026
REST APIs
Python
SQL
Spark SQL
T-SQL
C#
ASP.NET
PyTDS
sqlglot
Streamlit
Git
RAG
LangGraph
Microsoft Presidio
RoBERTa
PyTorch
TensorFlow
scikit-learn
HuggingFace Transformers
Client-facing delivery
Architecture documentation
Stakeholder presentation
ITIL incident management
SOP authoring
Root cause analysis
