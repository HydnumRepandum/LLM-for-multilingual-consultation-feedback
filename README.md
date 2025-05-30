# LLM for Multilingual Consultation Feedback

This repository accompanies an article presented at the **ECPR Biennial Conference of the Standing Group on Regulatory Governance**.

---

### Title

**Evaluating the Effectiveness of Open-source LLMs for Automated Analysis of Multilingual Consultation Feedback: A Swiss Case Study**

---

### Abstract

Consultation procedures are a common practice in public policy-making, bringing many benefits to democratic systems. However, they generate a large quantity of opinions, more or less structured, whose processing and synthesis require a significant investment in time and resources on the part of administrations. To meet this challenge, this study proposes the use of open source Large Language Model (LLM) to analyze and synthesize stakeholder opinions in a multilingual context, using the case of Switzerland. The architecture presented was designed with respect for the fundamental principles underlying citizens' trust in democratic institutions. The results show that the proposed approach achieves a satisfactory level of performance in most of the cases studied, with only one obvious error identified. However, the model regularly lacked nuance or omitted certain elements during analysis, which limits its ability to fully replace human expertise. Thus, far from aiming to replace the work of civil servants, this architecture should be seen as a complementary tool, designed to support human analysis and reinforce the effectiveness of consultation procedures, with a view to the continuous improvement of democratic processes.

---

## Repository Structure

The repository is organized into four primary directories:

1. **Colab-Code**

   * Contains all Python scripts used for conducting analyses in Google Colab.
   * Organized by individual analysis cases. The import tax modification case includes comments in English, while the other two cases contain comments in French.

2. **Database-Consultation**

   * Comprises source documents used for the research.
   * Includes PDF files with original stakeholder opinions, covering letters, and the synthesis of consultation results provided by relevant authorities.

3. **Evaluation-Confusion-Matrix**

   * Provides a concise R script utilized to evaluate the accuracy of the analysis through confusion matrices.

4. **Output-Excel**

   * Contains Excel spreadsheets produced by our analytical model for each study case.
   * Primarily presented in French, with selected content in German and Italian.

---

For further questions, please reach out via the GitHub repository.
