
def display(digits,val):
  infinity = float('inf')
  if val == infinity:
    if digits == 3:
      return 'inf'
    if digits == 2:
      return 'in'
    if digits == 1:
      return 'i'
  else:
    fmt = '{{:>{}}}'.format(digits)
    return fmt.format(val)

class AffineDPentry:
  def __init__(self):
    self.Rcost = None
    self.Dcost = None
    self.Icost = None


class AffineAlignment:
  def __init__(self,useq,vseq,mismatch_cost,gapopen_cost,gapextend_cost,\
               maximize=False):
    self.useq = useq
    self.vseq = vseq
    self._ulen = len(useq)
    self._vlen = len(vseq)
    self._dptable = list()
    self._choose_best = max if maximize else min
    for _ in range(self._ulen+1):
      new_row = list()
      for _ in range(self._vlen+1):
        new_row.append(AffineDPentry())
      self._dptable.append(new_row)
    self.infinity = float('inf')
    # add your code filling self._dptable here
  def matrix2string(self):
    max_value = 0
    for i in range(self._ulen+1):
      for j in range(self._vlen+1):
        entry = self._dptable[i][j]
        for value in [entry.Rcost,entry.Dcost,entry.Icost]:
          if value != self.infinity and max_value < value:
            max_value = value
    digits = 1 + int(log10(max_value))
    lines = list()
    for i in range(self._ulen+1):
      line = list()
      for j in range(self._vlen+1):
        entry = self._dptable[i][j]
        line.append('{},{},{}'.format(display(digits,entry.Rcost),
                                      display(digits,entry.Dcost),
                                      display(digits,entry.Icost)))
      lines.append('  '.join(line))
    return '\n'.join(lines)

  def affine_edit_distance(self): # min=>distance, max=>score
    last_entry = self._dptable[self._ulen][self._vlen]
    return self._choose_best(last_entry.Rcost,last_entry.Dcost,last_entry.Icost)

