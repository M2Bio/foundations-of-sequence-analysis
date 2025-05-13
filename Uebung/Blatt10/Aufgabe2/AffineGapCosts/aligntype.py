#!/usr/bin/env python3

class Alignment:

  def __init__(self,u, v):
  # wird nach dem Erzeugen einer Alignment()-Instanz aufgerufen
    self._useq = u
    self._vseq = v
    self._eops = list()
    self._eopnumbers = list()

  def add_eop(self,eop, number):
    assert len(self._eops) == len(self._eopnumbers)
    if (not self._eops) or self._eops[-1] != eop:
      self._eops.append(eop)
      self._eopnumbers.append(number)
    else:
      self._eopnumbers[-1] += number

  def add_replacement(self,nof_ops = 1):
    self.add_eop('R', nof_ops)

  def add_insertion(self,nof_ops = 1):
    self.add_eop('I', nof_ops)

  def add_deletion(self,nof_ops = 1):
    self.add_eop('D', nof_ops)

  def reverse(self):
    i, j = 0, len(self._eops)-1
    while i < j:
      tmp = self._eops[i]
      self._eops[i] = self._eops[j]
      self._eops[j] = tmp
      tmp = self._eopnumbers[i]
      self._eopnumbers[i] = self._eopnumbers[j]
      self._eopnumbers[j] = tmp
      i += 1
      j -= 1

  def pretty_u_line(self):
    #first line representing u
    uctr = 0
    al_useq_list = list()
    for eop, number in zip(self._eops,self._eopnumbers):
      if eop == 'R' or eop == 'D':
        for _ in range(number):
          al_useq_list.append('{}'.format(self._useq[uctr]))
          uctr += 1
      else:
        assert eop[0] == 'I'
        al_useq_list.append('{}'.format('-' * number))
    return ''.join(al_useq_list)

  def pretty_m_line(self):
    #middle line showing the
    al_m_list = list()
    uctr = 0
    vctr = 0
    for eop, number in zip(self._eops,self._eopnumbers):
      if eop == 'R':
        for _ in range(number):
          if self._useq[uctr] == self._vseq[vctr]:
            al_m_list.append('{}'.format('|'))
          else:
            al_m_list.append('{}'.format(' '))
          uctr += 1
          vctr += 1
      else:
        al_m_list.append('{}'.format(' ' * number))
        if eop == 'D':
          uctr += number
        else:
          vctr += number
    return ''.join(al_m_list)

  def pretty_v_line(self):
    # last line representing v
    vctr = 0
    al_v_list = list()
    for eop, number in zip(self._eops,self._eopnumbers):
      if eop == 'R' or eop == 'I':
        for _ in range(number):
          al_v_list.append('{}'.format(self._vseq[vctr]))
          vctr += 1
      else:
        assert eop == 'D'
        al_v_list.append('{}'.format('-' * number))
    return ''.join(al_v_list)

  def __eq__(self,other):
    return len(self._eops) == len(other._eops) and \
           all([a == b for a,b in zip(self._eops,other._eops)]) and \
           all([a == b for a,b in zip(self._eopnumbers,other._eopnumbers)])

  def __str__(self):
    return '\n'.join([self.pretty_u_line(),
                      self.pretty_m_line(),
                      self.pretty_v_line()])

  def eoplist(self):
    return [('{}'.format(eop),num) \
            for eop,num in zip(self._eops,self._eopnumbers)]

  def cigarstring(self):
    return ''.join('{}{}'.format(eop[0],str(eop[1])) for eop in self.eoplist())

  def evaluate(self,mismatch_cost = 1, indel_cost = 1):
    totalcost = 0
    uctr = 0
    vctr = 0
    for eop, number in zip(self._eops,self._eopnumbers):
      if eop == 'R':
        for i in range(number):
          if self._useq[uctr] != self._vseq[vctr]:
            totalcost += mismatch_cost
          uctr += 1
          vctr += 1
      else:
        totalcost += number * indel_cost
        if eop == 'D':
          uctr += number
        else:
          assert eop == 'I'
          vctr += number
    return totalcost

if __name__ == '__main__': # Beispielhafte Benutzung der Klasse Alignment
  u = 'acgtagatatatagat'
  v = 'agaaagaggtaagaggga'
  a = Alignment(u, v)
  a.add_replacement(7)
  a.add_insertion(2)
  a.add_replacement(2)
  a.add_deletion()
  a.add_replacement(3)
  a.add_insertion()
  a.add_replacement(3)
  print(a)
  print('Gesamtkosten: {}'.format(a.evaluate()))
