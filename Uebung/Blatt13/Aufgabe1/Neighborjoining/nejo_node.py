class NJnode:
  _idnum = 0
  def __init__(self,taxon_name = None):
    self.taxon_name = taxon_name # defined for leaves, None for others
    self._idnum = NJnode._idnum # 0 .. num_of_taxa-1 for leaves,
                                # >= num_of_taxa for others
    NJnode._idnum += 1  # class var storing the next used id number
    self._rvalue = None # value in Rtab for this node
  def idnum(self):
    return self._idnum
  def rvalue_set(self,r):
    self._rvalue = r
  def rvalue(self):
    return self._rvalue
  def __eq__(self,other):
    return self.idnum() == other.idnum()
  def __str__(self):
    if self.taxon_name:
      return '{}'.format(self.taxon_name)
    return '{}'.format(self.idnum())
