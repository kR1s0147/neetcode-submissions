class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        # Frequency map
        freq = {}
        for card in hand:
            freq[card] = freq.get(card, 0) + 1
        
        hand.sort()  # Always try smallest card first
        
        for card in hand:
            if freq[card] == 0:
                continue  # Already used this card
            
            # Try to form a group starting from `card`
            for i in range(groupSize):
                if freq.get(card + i, 0) == 0:
                    return False  # Can't form group
                freq[card + i] -= 1  # Use one card
        
        return True
        

