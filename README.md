## Message In A Bubble

### Aim and motivation

The aim of this project is to create an application capable of identifying bubbles (and, more in general, text areas) in manga pages. This goal is to be pursued through the methods of element detection, eventually implementing machine learning.

The primary motivation is to aid the work of scanlators by automatically generating a model file that can then be filled with the scripts; choices regarding accuracy and other relevant parameters of the algorithm will be made with this point in mind.

### Methodology

At least in the first stage, our code will be based on the approach described by Kuboi in his Master's Thesis, which describes in detail specific issues and solutions for the problem at hand.  
(Kuboi, T., _Element detection in Japanese comic book panels_. Master's Thesis, California Polytchnic State University, 2014.) The paper is freely available at ResearchGate, [here](https://www.researchgate.net/publication/270546570_ELEMENT_DETECTION_IN_JAPANESE_COMIC_BOOK_PANELS).

We will employ Python and its libraries for image detection and machine learning.  Specific choices are still a matter of discussion and may vary depending on our needs.

An indicative structure of the project (modules):
1. Image loading and pre-processing
	- Image segmentation
	- Feature extraction
2. Element detection algorithm
	- Identification of features of interest
3. Converting the information into strings and appending it to a suitable text file
4. Repeating to extract the information from an entire chapter at once

Advanced features to be added later on:
- Detection of generic text elements (boxes, background text, sfxs...)
- Graphical interface

### Examples

No examples yet.

 ### Contributions

We'll get there when we get there.

### License 

MIT License
