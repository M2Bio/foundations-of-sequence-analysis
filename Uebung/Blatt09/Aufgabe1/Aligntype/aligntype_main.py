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
