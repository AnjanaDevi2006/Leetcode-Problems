class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closestX = max(x1, min(x2, xCenter))
        closestY = max(y1, min(y2, yCenter))
        dist = ((xCenter - closestX) ** 2 + (yCenter - closestY) ** 2) ** 0.5
        return dist <= radius