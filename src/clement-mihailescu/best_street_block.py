# Google Coding Interview With A Normal Software Engineer
# https://youtu.be/rw4s4M3hFfs
# %%
from typing import Dict, List, Tuple


INF = 999


class Block(Dict[str, bool]):
    """Description of block places."""


class BlockInterests(Dict[str, int]):
    """Description of block interesting places distances."""

    @classmethod
    def build_from_block_interests(cls, block: Block, interests: List[str]) -> "BlockInterests":
        return cls((interest, 0 if block.get(interest, False) else INF) for interest in interests)

    def calculate_grade(self) -> int:
        return max(self.values())


class Street:
    """Description of block structures."""

    def __init__(self, street_description: List[Dict[str, bool]]) -> None:
        self._blocks: List[Block] = [Block(block_description) for block_description in street_description]

    def __getitem__(self, index: int) -> Block:
        return self._blocks[index]

    def find_best_block(self, interests: List[str]) -> Tuple[int, int]:
        champion_index, champion_grade = 0, INF
        for index in range(len(self._blocks)):
            block_interests = BlockInterests.build_from_block_interests(self[index], interests)
            for depth in range(len(self._blocks)):
                left_index, right_index = index - depth, index + depth
                if left_index < 0 and right_index >= len(self._blocks):
                    break
                for interest in interests:
                    if block_interests[interest] != INF:
                        continue
                    if left_index >= 0 and self[left_index].get(interest, False):
                        block_interests[interest] = depth
                        continue
                    if right_index < len(self._blocks) and self[right_index].get(interest, False):
                        block_interests[interest] = depth
                        continue
            current_block_grade = block_interests.calculate_grade()
            if current_block_grade < champion_grade:
                champion_index, champion_grade = index, current_block_grade

        return champion_index, champion_grade


street = Street(
    [
        {"gym": False, "school": True, "store": False},
        {"gym": True, "school": False, "store": False},
        {"gym": True, "school": True, "store": False},
        {"gym": False, "school": True, "store": False},
        {"gym": False, "school": True, "store": True},
    ]
)
index, grade = street.find_best_block(["gym", "school", "store"])
print(index, grade)

# %%
