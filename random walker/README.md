Random Walker Paper: http://vision.cse.psu.edu/people/chenpingY/paper/grady2006random.pdf

original image: Alloy_noise

# Steps

1. Read the image
2. Check for histogram based segemntation.
3. For histogram based segmentation, remove the noise. 
4. buch of values are present in between the peaks so perform CLAHE
5. put the markers in the region where we know we are highly confident. Markers are saved in markers.jpg
6. Pefrom random walker and assign labels Image saved in random_walker.jpg
7. Split them into segments. Image saved in random_walker_segments.jpg
