---
title: "TATA: Stance Detection via Topic-Agnostic and Topic-Aware Embeddings"
permalink: /publication/tata
date: 2023-12-06
collection: publications
venue: The 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)
authors: <b>Hans W. A. Hanley</b> and Zakir Durumeric
excerpt: 'In this work, we utilize contrastive learning with a triplet loss and synthetic data to engineer topic-aware and topic-agnostic embedding layers for performing stance detection.'
recording: https://www.youtube.com/watch?v=bJMcwrgz3yY
code: https://github.com/hanshanley/tata
paperurl: 'https://www.hanshanley.com/files/tata.pdf'
citation: 'Hans W. A. Hanley and Zakir Durumeric. "TATA: Stance Detection via Topic-Agnostic and Topic-Aware Embeddings." The 2023 Conference on Empirical Methods in Natural Language Processing.'
---

Stance detection is important for understanding different attitudes and beliefs on the Internet. However, given that a passage's stance toward a given topic is often highly dependent on that topic, building a stance detection model that generalizes to unseen topics is difficult. In this work, we propose using contrastive learning as well as an unlabeled dataset of news articles that cover a variety of different topics to train topic-agnostic/TAG and topic-aware/TAW embeddings for use in downstream stance detection. Combining these embeddings in our full TATA model, we achieve state-of-the-art performance across several public stance detection datasets (0.771 $F_1$-score on the Zero-shot VAST dataset). We release our code and data at https://github.com/hanshanley/tata.
