from tree import Node

class KnightPathFinder:
  def __init__(self, root):
    self._root = Node(root)
    self._considered_positions = {root}

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

  def new_move_positions(self, pos):
    valid_moves = self.get_valid_moves(pos)
    new_moves = valid_moves.difference(self._considered_positions)
    self._considered_positions = self._considered_positions.union(new_moves)
    return new_moves

  def build_move_tree(self):
    Q = [self._root]
    while len(Q):
        curr_node = Q.pop(0)
        new_moves = self.new_move_positions(curr_node.value)
        for move in new_moves:
          move_node = Node(move)
          curr_node.add_child(move_node)
          Q.append(move_node)
    return None

  def find_path(self, end_pos):
    end_node = self._root.depth_search(end_pos)
    return self.trace_to_route(end_node)

  def trace_to_route(self, end_node, path=[]):
    end_list = [end_node.value]
    end_list.extend(path)
    if not end_node.parent:
      return end_list
    return self.trace_to_route(end_node.parent, end_list)


finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder.find_path((1,7)))
