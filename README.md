# Huawei (not) in the Grid: Keyword and Sentiment Analysis of Media Discourse on the 2020 Huawei 5G Ban in the United Kingdom


## Brief Description
This project delves into the interplay between media narratives, nationalism, and the discourse surrounding the UK's Huawei 5G ban, utilizing a mixed-methods approach to examine how British and Chinese media frame this geopolitical issue.

## Author Information and Contact
- **Name:** Chi Vu
- **Affiliation:** Denison University, Senior Research Seminar, Data Analytics 
- **Contact:** vu_c1@denison.edu

## Prerequisites
- **Software Needed:** Python 3.8+
- **Libraries**: nltk, pandas, re, matplotlib, scikit-learn

## Data
The dataset includes news articles from major British and Chinese media outlets from July 2020 until February 2024. The articles are stored in an Excel file (`huawei articles Local.xlsx`), which is processed to clean and analyze the text.

## Analysis Process
### Text Preprocessing
The articles undergo several preprocessing steps:
- URL removal
- Lowercasing
- Punctuation and numeric removal
- Stopword removal using NLTK's English stopwords list
- Lemmatization using NLTK's WordNet lemmatizer
- Additional stopword removal: Stopwords specific to the context of Huawei and 5G, which do not contribute meaningful information to the analysis, are also removed.
- Source Normalization: Media source names are normalized to ensure consistency across the dataset, facilitating group analysis.

### TF-IDF Analysis
TF-IDF (Term Frequency-Inverse Document Frequency) analysis is conducted to identify the most relevant words and phrases in the articles related to each source. This helps in understanding the focus of each media source regarding the Huawei 5G ban.

### Sentiment Analysis
Using the TextBlob library, the sentiment of each article is analyzed to determine the general tone (positive, negative, neutral) and subjectivity expressed in the discourse.

## Results
Results of the analysis, including charts and plots generated using matplotlib, provide insights into how different media landscapes perceive and communicate issues related to the Huawei 5G ban. These findings can be used to gauge the impact of media framing on public perception and policy-making.

## Contribution and Lincenses
- Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request.
- The project is licensed under the MIT License - see the LICENSE file for details.

*This project is aimed at contributing to academic discussions on media studies, nationalism, and international relations, with a focus on educational purposes.*
