---
title: "DPSelect: A Differential Privacy Based Guard Relay Selection Algorithm for Tor"
collection: publications
permalink: /publication/dpselect-differential-privacy
excerpt: 'This paper concerns counteracting information leakage in Tor relay selection algorithms.'
date: 2019-07-01
authors: <b>Hans W. A. Hanley</b>, Yixin Sun, Sameer Wagh, and Prateek Mittal
venue: '19th Privacy Enhancing Technologies Symposium (2) (PoPETs 2019)'
paperurl: 'https://www.hanshanley.com/files/DPSelect.pdf'
citation: 'Hans Hanley, Yixin Sun, Sameer Wagh, and Prateek Mittal. "DPSelect: A differential privacy based guard relay selection algorithm for Tor." Proceedings on Privacy Enhancing Technologies 2019, no. 2 (2019)'
---

Recent work has shown that Tor is vulnerable to attacks that manipulate inter-domain routing to compromise user privacy. Proposed solutions such
as Counter-RAPTOR attempt to ameliorate this issue by favoring Tor entry relays that have high resilience to these attacks. However, because these defenses bias Tor path selection on the identity of the client, they invariably leak probabilistic information about client identities. In this work, we make the following contributions. First, we identify a novel means to quantify privacy leakage in guard selection algorithms using the metric of Max-Divergence. Max-Divergence ensures that probabilistic privacy loss is within strict bounds while also providing composability over time. Second, we utilize Max-Divergence and multiple notions of entropy to understand privacy loss in the worst-case for Counter-RAPTOR. Our worst-case analysis provides a fresh perspective to the field, as prior work such as Counter-RAPTOR only analyzed average case-privacy loss. Third, we propose modifications to Counter-RAPTOR that incorporate worst-case MaxDivergence in its design. Specifically, we utilize the exponential mechanism (a mechanism for differential privacy) to guarantee a worst-case bound on MaxDivergence/privacy loss. For the quality function used in the exponential mechanism, we show that a MonteCarlo sampling-based method for stochastic optimization can be used to improve multi-dimensional trade-offs between security, privacy, and performance. Finally, we demonstrate that compared to Counter-RAPTOR, our approach achieves an 83% decrease in Max-Divergence after one guard selection and a 245% increase in worst-case Shannon entropy after 5 guard selections. Notably, experimental evaluations using the Shadow emulator shows that our approach provides these privacy benefits with minimal impact on system performance.

