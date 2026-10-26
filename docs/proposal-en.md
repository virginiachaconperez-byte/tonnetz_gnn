# Project Proposal

**Status:** Draft.

**Date:** 28 October 2026.

## Title

Learning Harmonic Representations with Tonnetz-Based Graph Neural Networks: Chord Prediction and Explainability

## Background and motivation

The Tonnetz organizes harmonic relationships between notes and chords through a structure that can be represented as a graph [1]. This structure makes it possible to incorporate musical knowledge into machine learning.

## Objective

The project will evaluate what the Tonnetz contributes to next-chord prediction from a musical passage and study the quality of the model's explanations.

## Proposed methodology

The study will use data describing the notes and identifying the chord at each moment. The dataset and chord vocabulary remain to be selected; information reliability and data licensing will be reviewed.

A graph neural network (GNN) will process the notes at each moment on a fixed Tonnetz graph, without distinguishing octaves or inversions. A GRU, a sequence model, will use these representations in order to predict the next chord. The piece's key will not be supplied to the model.

The comparison will include a GRU without graph processing and a variant of the proposed model without information exchange between nodes. All models will receive the same musical features and be trained under comparable conditions. Evaluation pieces will be separate from training pieces.

## Evaluation

A prediction will count as correct when its root and chord type match the reference. Measures will include accuracy, top-3 accuracy, and log loss. Agreement between the notes in both chords will provide an additional error diagnostic.

Explanations will be evaluated for faithfulness to model behavior, stability under small changes, and complexity understood as the number of highlighted elements. GraphFramEx and Quantus will guide this evaluation [2, 3].

## Expected outcomes

Deliverables will include reproducible code for data preparation, model training, and evaluation, together with a results report and explanation visualizations.

## References

[1] Catanzaro, M. J. *Generalized Tonnetze*. Journal of Mathematics and Music, 2011. arXiv:1612.03519.

[2] Amara, K. et al. *GraphFramEx: Towards Systematic Evaluation of Explainability Methods for Graph Neural Networks*. Learning on Graphs, 2022. arXiv:2206.09677.

[3] Hedström, A. et al. *Quantus: An Explainable AI Toolkit for Responsible Evaluation of Neural Network Explanations and Beyond*. Journal of Machine Learning Research, 24, 2023. arXiv:2202.06861.
