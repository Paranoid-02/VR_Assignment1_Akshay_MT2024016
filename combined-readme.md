# Computer Vision Projects: Coin Detection and Panorama Stitching

This repository contains two computer vision projects implemented in Python:
1. Coin Detection and Segmentation
2. Panorama Image Stitching

## Project Structure

```
VR_Assignment1_[YourName]_[YourRollNo]/
├── src/
│   ├── coin_detection.py
│   ├── panorama.py
│   └── stitch.py
├── images/
│   ├── coins/
│   │   └── coins.jpg
│   └── panorama/
│       ├── image1.jpg
│       ├── image2.jpg
│       └── ...
├── output/
│   ├── coin_detection/
│   │   ├── detected_coins.jpg
│   │   ├── segmented_coins.jpg
│   │   └── individual_coins/
│   └── panorama/
│       ├── matched_points.jpg
│       └── panorama_image.jpg
└── README.md
```

## Dependencies

```bash
pip install opencv-python numpy matplotlib imutils
```

Required packages:
- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib
- imutils

## 1. Coin Detection and Segmentation

### Features
- Automatic coin detection using edge detection
- Contour-based coin segmentation
- Individual coin extraction
- Visualization of detection results
- Coin counting functionality

### Implementation Details

#### Detection Process
1. Image Preprocessing:
   - Grayscale conversion
   - Gaussian blur (11x11 kernel)
   - Canny edge detection (thresholds: 30, 150)
   - Edge dilation

#### Segmentation Process
1. Contour Detection:
   - External contour finding
   - Area-based filtering (min_area: 1000 pixels)
2. Individual Coin Extraction:
   - Mask creation
   - Bounding box cropping

### Usage

```bash
python src/coin_detection.py
```

### Results
As shown in the output images:
- Successfully detected 4 Indian coins
- Clear segmentation with green contour highlighting
- Individual coin isolation in separate images
- Clean mask generation showing coin boundaries

## 2. Panorama Image Stitching

### Features
- SIFT-based feature detection and matching
- Homography computation using RANSAC
- Perspective warping for seamless stitching
- Support for multiple image stitching
- Keypoint match visualization

### Implementation Details

#### Stitching Process
1. Feature Detection:
   - SIFT keypoint detection
   - Feature descriptor computation
2. Feature Matching:
   - Brute force matcher with Lowe's ratio test
   - Homography computation using RANSAC
3. Image Warping:
   - Perspective transformation
   - Image blending

### Usage

```bash
python src/stitch.py
```
When prompted, enter the pattern for your image files (e.g., 'images/panorama/*.jpg')

### Results
As demonstrated in the output images:
- Successful feature matching between adjacent images
- Seamless panorama creation
- Green lines showing matched keypoints
- Clean stitching without visible seams

## Parameters and Configuration

### Coin Detection
- Gaussian blur kernel size: (11, 11)
- Canny edge thresholds: (30, 150)
- Minimum contour area: 1000 pixels
- Dilation iterations: 2

### Panorama Stitching
- Lowe's ratio: 0.75
- RANSAC threshold: 4.0
- Feature matching: Brute Force
- Warping method: Perspective

## Observations

### Coin Detection
- Successfully handles non-overlapping coins
- Accurate detection on uniform backgrounds
- Robust to moderate lighting variations
- Clear segmentation boundaries

### Panorama Stitching
- Best results with significant overlap between images
- Handles exposure differences well
- Maintains image quality in the final panorama
- Accurate feature matching as shown by green lines

## Limitations

### Coin Detection
- Requires good lighting conditions
- Coins should not overlap
- Best results with high contrast between coins and background

### Panorama Stitching
- Requires overlapping regions between adjacent images
- Best results with images taken from similar viewpoints
- Processing time increases with image size

## Future Improvements

### Coin Detection
- Implement coin denomination classification
- Add support for overlapping coins
- Enhance robustness to varying lighting conditions

### Panorama Stitching
- Implement multi-band blending
- Add exposure compensation
- Optimize processing time
- Include error handling for failed matches

## Author

[Your Name]
Roll No: [Your Roll No]

## License

This project is licensed under the MIT License - see the LICENSE file for details
