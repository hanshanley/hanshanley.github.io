---
title: "Twits, Toxic Tweets, and Tribal Tendencies: Trends in Politically Polarized Posts on Twitter"
permalink: /publication/twits
date: 2023-10-02
collection: publications
authors: <b>Hans W. A. Hanley</b> and Zakir Durumeric
paperurl: 'https://www.hanshanley.com/files/CSCW_Twits.pdf'
excerpt: 'Within this work, we explore the role that political ideology plays in contributing to toxicity both on an individual user level and a topic level on Twitter.'
citation: 'Hans W. A. Hanley and Zakir Durumeric. "Twits, Toxic Tweets, and Tribal Tendencies: Trends in Politically Polarized Posts on Twitter." (2023).'
---
Social media platforms are often blamed for exacerbating political polarization and worsening public dialogue. Many claim hyperpartisan users post pernicious content, slanted to their political views encouraging raucous and otherwise toxic conversations. However, what factors, actually contribute to increased online toxicity and negative interactions? 

Within this work, we explore the role that political ideology plays in contributing to toxicity both on an individual user level and a topic level on Twitter. First, to do this, we train and open-source a DeBERTa-based toxicity detector with a contrastive objective that outperforms the Google Jigsaw Persective Toxicity detector on the Civil Comments test dataset. Then, after collecting 187 million tweets from 55,415 Twitter users, we determine how several account-level characteristics, including political ideology and account age, predict how often each user posts toxic content. Running a linear regression, we find that the diversity of views and the toxicity of the other accounts with which that user engages has a more marked effect on their own toxicity. Namely, toxic comments are correlated with users who engage with a wider array of political views. Performing topic analysis on the toxic content posted by these accounts using the large language model MPNet and a version of the DP-Means clustering algorithm, we find similar behavior across 6,592~individual topics, with conversations on each topic becoming more toxic as a wider diversity of users become involved. 
