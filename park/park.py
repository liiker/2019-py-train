class Park(object):
  def __init__(self, name, max_count=100):
    self.name = name
    self.count = 0
    self.max_count = max_count;