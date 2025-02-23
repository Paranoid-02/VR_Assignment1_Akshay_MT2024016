import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_coins(image_path):
    """
    Detect coins in the image using edge detection and contour finding.
    
    Args:
        image_path: Path to the input image
        
    Returns:
        original_img: Original image
        contours: Detected contours of coins
        coin_count: Number of coins detected
    """
    # Read the image
    original_img = cv2.imread(image_path)
    img = original_img.copy()
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    
    # Edge detection using Canny
    edges = cv2.Canny(blurred, 30, 150)
    
    # Dilate edges to close gaps
    dilated = cv2.dilate(edges, None, iterations=2)
    
    # Find contours
    contours, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours based on area to remove small noise
    min_area = 1000
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]
    
    # Count coins
    coin_count = len(filtered_contours)
    
    return original_img, filtered_contours, coin_count

def visualize_detection(img, contours):
    """
    Visualize detected coins by drawing contours.
    
    Args:
        img: Original image
        contours: Detected contours
        
    Returns:
        outlined_img: Image with outlined coins
    """
    outlined_img = img.copy()
    cv2.drawContours(outlined_img, contours, -1, (0, 255, 0), 3)
    return outlined_img

def segment_coins(img, contours):
    """
    Segment individual coins from the image.
    
    Args:
        img: Original image
        contours: Detected contours
        
    Returns:
        segmented_coins: List of segmented coin images
        mask_img: Image showing the mask of all coins
    """
    # Create a mask for all coins
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, contours, -1, 255, -1)
    
    # Apply the mask to the original image
    mask_img = cv2.bitwise_and(img, img, mask=mask)
    
    # Segment individual coins
    segmented_coins = []
    for i, contour in enumerate(contours):
        # Create a mask for this specific contour
        individual_mask = np.zeros(img.shape[:2], dtype=np.uint8)
        cv2.drawContours(individual_mask, [contour], -1, 255, -1)
        
        # Get bounding rectangle
        x, y, w, h = cv2.boundingRect(contour)
        
        # Apply mask and extract the segment
        coin_segment = cv2.bitwise_and(img, img, mask=individual_mask)
        
        # Crop to bounding box
        cropped_coin = coin_segment[y:y+h, x:x+w]
        
        segmented_coins.append(cropped_coin)
    
    return segmented_coins, mask_img

def main(image_path):
    # Detect coins
    original_img, contours, coin_count = detect_coins(image_path)
    
    # Visualize detection
    outlined_img = visualize_detection(original_img, contours)
    
    # Segment coins
    segmented_coins, mask_img = segment_coins(original_img, contours)
    
    # Display results
    plt.figure(figsize=(15, 10))
    
    # Original image
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')
    
    # Outlined coins
    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(outlined_img, cv2.COLOR_BGR2RGB))
    plt.title(f'Detected Coins: {coin_count}')
    plt.axis('off')
    
    # Mask showing all coins
    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(mask_img, cv2.COLOR_BGR2RGB))
    plt.title('Segmented Coins (Mask)')
    plt.axis('off')
    
    # Display individual coins
    if segmented_coins:
        # Create a subplot grid for individual coins
        rows = int(np.ceil(len(segmented_coins) / 4))
        plt.figure(figsize=(15, rows * 3))
        for i, coin in enumerate(segmented_coins):
            plt.subplot(rows, 4, i + 1)
            plt.imshow(cv2.cvtColor(coin, cv2.COLOR_BGR2RGB))
            plt.title(f'Coin {i+1}')
            plt.axis('off')
        plt.tight_layout()
    
    plt.tight_layout()
    plt.show()
    
    print(f"Total coins detected: {coin_count}")
    return coin_count

if __name__ == "__main__":
    image_path = "coins/coins.jpg"
    main(image_path)