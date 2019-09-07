# Message In A Bubble

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

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Code Dependencies
```
- matplotlib
- numpy
- openCV
- scikit-image
- scipy
```

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Deployment

## Built With


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/NekroDarkmoon/MessageInABubble) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

## Authors

* **Kishi** - *Author* - [Kishi](https://github.com/Kishi115)

* **Nekro Darkmoon** - *Author* - [NekroDarkmoon](https://github.com/NekroDarkmoon)

* **Schaw?** - *Author* - [Insert Link](#)

See also the list of [contributors](https://github.com/NekroDarkmoon/MessageInABubble/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
