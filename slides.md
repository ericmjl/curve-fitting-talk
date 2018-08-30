---
title: Curve Fitting!
---

# Fret Not, It's Curve Fitting All The Way Down!

![](./static/images/ericmjl.png) <!-- .element width="250px" align="left" -->

Eric J. Ma, Digility 2018 <!-- .element align="right" -->

Scan QR Code to save my contact info. <!-- .element align="right" -->

---

# Follow Along!

[https://ericmjl.github.io/**curve-fitting-talk**](https://ericmjl.github.io/curve-fitting-talk)

![](./static/images/talk.png) <!-- .element width="250px" -->

Scan QR code to bookmark slides!

---

# About Myself

- Investigator, Scientific Data Analysis, NIBR <!-- .element: class="fragment" -->
- MIT Biological Engineering, ScD, 2017 <!-- .element: class="fragment" -->
- Self-taught machine & deep learner, Bayesian Pythonista <!-- .element: class="fragment" -->

---

# Goals

1. Demystify Bayesian statistical inference. <!-- .element: class="fragment" -->
1. Illustrate the link between Bayesian statistics and deep learning<!-- .element: class="fragment" -->

----

# Agenda

1. Bayes' rule. <!-- .element: class="fragment" -->
1. Bayesian estimation. <!-- .element: class="fragment" -->
1. Bayesian linear regression. <!-- .element: class="fragment" -->
1. Bayesian logistic regression. <!-- .element: class="fragment" -->
1. Arbitrary Bayesian curve fitting. <!-- .element: class="fragment" -->

---

<!-- .slide: data-background="static/images/bayes-rule-neon-sign.jpg" -->

---

## Estimation

![](./static/images/framework/estimation/data.png) <!-- .element width="20%" class="fragment"-->
![](./static/images/framework/estimation/point.png) <!-- .element width="20%"  class="fragment"-->
![](./static/images/framework/estimation/distribution.png) <!-- .element width="20%"  class="fragment"-->
![](./static/images/framework/estimation/hierarchical.png) <!-- .element width="20%"  class="fragment"-->

----

## Linear regression

![](./static/images/framework/linreg/data.png) <!-- .element width="20%" class="fragment"-->
![](./static/images/framework/linreg/point.png) <!-- .element width="20%"  class="fragment"-->
![](./static/images/framework/linreg/distribution.png) <!-- .element width="20%"  class="fragment"-->
![](./static/images/framework/linreg/hierarchical.png) <!-- .element width="20%"  class="fragment"-->

----

## Logistic regression

![](./static/images/framework/logreg/data.png) <!-- .element width="20%" class="fragment"-->
![](./static/images/framework/logreg/point.png) <!-- .element width="20%"  class="fragment"-->
![](./static/images/framework/logreg/distribution.png) <!-- .element width="20%"  class="fragment"-->
![](./static/images/framework/logreg/hierarchical.png) <!-- .element width="20%"  class="fragment"-->

----

## Parametric Curves

![](./static/images/framework/curves/data.png) <!-- .element width="20%" class="fragment"-->
![](./static/images/framework/curves/point.png) <!-- .element width="20%"  class="fragment"-->
![](./static/images/framework/curves/distribution.png) <!-- .element width="20%"  class="fragment"-->
![](./static/images/framework/curves/hierarchical.png) <!-- .element width="20%"  class="fragment"-->

----

## Neural Networks

![](./static/images/framework/nn/data.png) <!-- .element width="20%" class="fragment"-->
![](./static/images/framework/nn/point.png) <!-- .element width="20%"  class="fragment"-->
![](./static/images/framework/nn/distribution.png) <!-- .element width="20%"  class="fragment"-->
![](./static/images/framework/nn/hierarchical.png) <!-- .element width="20%"  class="fragment"-->

----

![](./static/images/bayesian-framework.png) <!-- .element width="63%"-->

---

# Example: Darwin's Finches

<!-- Core idea: we have darwin's finches, use Bayesian hierarchical modelling to write a model that estimates Finch beak dimensions (both wing and beak), and then use QR codes to display this information. -->

---

