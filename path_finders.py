from tree import Node

class KnightPathFinder:
  def __init__(self, root):
    self._root = root
    self._considered_possitions = {root}

  def get_valid_moves(self, pos):
      valid_moves = set()
      x, y = pos
      if x + 1 < 8:
        if y + 2 < 8:
          valid_moves.add((x + 1, y + 2))
        if y - 2 >= 0:
          valid_moves.add((x + 1, y - 2))
        if x + 2 < 8:
          if y + 1 < 8:
            valid_moves.add((x + 2, y + 1))
          if y - 1 >= 0:
            valid_moves.add((x + 2, y - 1))
      if x - 1 >= 0:
        if y + 2 < 8:
          valid_moves.add((x - 1, y + 2))
        if y - 2 >= 0:
          valid_moves.add((x - 1, y - 2))
        if x - 2 >= 0:
          if y + 1 < 8:
            valid_moves.add((x - 2, y + 1))
          if y - 1 >= 0:
            valid_moves.add((x - 2, y - 1))
      return valid_moves

  def new_move_possitions(self, pos):
    valid_moves = self.get_valid_moves(pos)
    new_moves = valid_moves.difference(self._considered_possitions)
    self._considered_possitions = self._considered_possitions.union(new_moves)
    return new_moves



finder = KnightPathFinder((1,2))
print(finder.new_move_possitions((3,3)))
print(finder._root)
