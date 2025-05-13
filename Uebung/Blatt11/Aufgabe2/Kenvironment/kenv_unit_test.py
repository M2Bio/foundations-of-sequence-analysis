#!/usr/bin/env python3

import unittest
from scorematrix import Scorematrix
from kenv_enum import thresholds_get, enum_environment

class TestKenv(unittest.TestCase):
  acgt_score = Scorematrix('acgt-purine-pyrimidine.txt')
  ac_score = Scorematrix('ac-score.txt')
  blosum62_score = Scorematrix('blosum62-asize20.txt')
  def check_thresholds_get(self,scorematrix,qgrams_with_thresholds):
    for qgram, score_thresholds_expected in qgrams_with_thresholds:
      assert len(score_thresholds_expected) > 0
      score_thresholds = thresholds_get(scorematrix,
                                        score_thresholds_expected[-1],
                                        qgram)
      self.assertEqual(score_thresholds,score_thresholds_expected)
  def test_thresholds_get_aca(self):
    dna_qgrams_with_thresholds = [('aca',[-1, 1, 3])]
    self.check_thresholds_get(TestKenv.ac_score,dna_qgrams_with_thresholds)
  def test_thresholds_get_DNA(self):
    dna_qgrams_with_thresholds = [('acta',[-1, 0, 1, 2]),
                                  ('ctac',[-1, 0, 1, 2]),
                                  ('tact',[-1, 0, 1, 2]),
                                  ('actc',[-1, 0, 1, 2]),
                                  ('ctca',[-1, 0, 1, 2]),
                                  ('tcag',[-1, 0, 1, 2]),
                                  ('cagc',[-1, 0, 1, 2]),
                                  ('agca',[-1, 0, 1, 2]),
                                  ('gcat',[-1, 0, 1, 2]),
                                  ('catc',[-1, 0, 1, 2]),
                                  ('atca',[-1, 0, 1, 2])]
    self.check_thresholds_get(TestKenv.acgt_score,dna_qgrams_with_thresholds)
  def test_thresholds_get_protein(self):
    aa_qgrams_with_thresholds = [('MGHL',[4, 10, 18, 22]),
                                 ('GHLP',[3, 11, 15, 22]),
                                 ('HLPL',[7, 11, 18, 22]),
                                 ('LPLA',[7, 14, 18, 22]),
                                 ('PLAW',[3, 7, 11, 22]),
                                 ('LAWL',[3, 7, 18, 22]),
                                 ('AWLS',[3, 14, 18, 22]),
                                 ('WLSQ',[9, 13, 17, 22])]
    self.check_thresholds_get(TestKenv.blosum62_score,aa_qgrams_with_thresholds)
  def test_thresholds_get_protein_long(self):
    aa_qgrams_with_thresholds = [('SFY',[2, 8, 15]),
				 ('FYT',[3, 10, 15]),
				 ('YTA',[6, 11, 15]),
				 ('TAI',[7, 11, 15]),
				 ('AIA',[7, 11, 15]),
				 ('IAQ',[6, 10, 15]),
				 ('AQA',[6, 11, 15]),
				 ('QAF',[5, 9, 15]),
				 ('AFL',[5, 11, 15]),
				 ('FLS',[7, 11, 15]),
				 ('LSN',[5, 9, 15]),
				 ('SNE',[4, 10, 15]),
				 ('NEK',[5, 10, 15]),
				 ('EKL',[6, 11, 15]),
				 ('KLP',[4, 8, 15]),
				 ('LPN',[2, 9, 15]),
				 ('PNL',[5, 11, 15]),
				 ('NLD',[5, 9, 15]),
				 ('LDC',[0, 6, 15]),
				 ('DCI',[2, 11, 15]),
				 ('CIQ',[6, 10, 15]),
				 ('IQN',[4, 9, 15]),
				 ('QNA',[5, 11, 15]),
				 ('NAN',[5, 9, 15]),
				 ('ANK',[4, 10, 15]),
				 ('NKG',[4, 9, 15]),
				 ('KGT',[4, 10, 15]),
				 ('GTH',[2, 7, 15]),
				 ('THT',[2, 10, 15]),
				 ('HTS',[6, 11, 15]),
				 ('TSL',[7, 11, 15]),
				 ('SLM',[6, 10, 15]),
				 ('LMQ',[5, 10, 15]),
				 ('MQR',[5, 10, 15]),
				 ('QRL',[6, 11, 15]),
				 ('RLR',[6, 10, 15]),
				 ('LRN',[4, 9, 15]),
				 ('RNR',[4, 10, 15]),
				 ('NRG',[4, 9, 15]),
				 ('RGE',[4, 10, 15]),
				 ('GER',[5, 10, 15]),
				 ('ERD',[4, 9, 15]),
				 ('RDR',[4, 10, 15]),
				 ('DRE',[5, 10, 15]),
				 ('RER',[5, 10, 15]),
				 ('ERE',[5, 10, 15]),
				 ('RER',[5, 10, 15]),
				 ('ERE',[5, 10, 15]),
				 ('RER',[5, 10, 15]),
				 ('ERE',[5, 10, 15]),
				 ('REM',[5, 10, 15]),
				 ('EMR',[5, 10, 15]),
				 ('MRR',[5, 10, 15]),
				 ('RRS',[6, 11, 15]),
				 ('RSS',[7, 11, 15]),
				 ('SSG',[5, 9, 15]),
				 ('SGL',[5, 11, 15]),
				 ('GLR',[6, 10, 15]),
				 ('LRA',[6, 11, 15]),
				 ('RAG',[5, 9, 15]),
				 ('AGS',[5, 11, 15]),
                                 ('GSR',[6, 10, 15])]
    self.check_thresholds_get(TestKenv.blosum62_score,aa_qgrams_with_thresholds)
  def check_this_sequence(self,scorematrix,sequence,qvalue,score_threshold,
                          env_elems_reference):
    env_elems = list()
    for pos in range(len(sequence) - qvalue + 1):
      word = sequence[pos:pos+qvalue]
      for env_seq, env_seq_score in enum_environment(scorematrix,
                                                     score_threshold,word):
        escore = scorematrix.eval_score(word,env_seq)
        self.assertEqual(escore,env_seq_score)
        env_elems.append((env_seq,env_seq_score,pos))
    self.assertEqual(sorted(env_elems),sorted(env_elems_reference))
  def test_kenv_environment_aca(self):
    env_elems_reference = [('cca',3,0),
                           ('aca',6,0),
                           ('acc',3,0),
                           ('aaa',3,0)]
    scorematrix = TestKenv.ac_score
    sequence = 'aca'
    qvalue = 3
    score_threshold = 3
    self.check_this_sequence(scorematrix,sequence,qvalue,score_threshold,
                             env_elems_reference)
  def test_kenv_environment_DNA(self):
    env_elems_reference = [('gcta',2,0),
                           ('atta',2,0),
                           ('acta',4,0),
                           ('actg',2,0),
                           ('acca',2,0),
                           ('ttac',2,1),
                           ('ctgc',2,1),
                           ('ctac',4,1),
                           ('ctat',2,1),
                           ('ccac',2,1),
                           ('tgct',2,2),
                           ('tatt',2,2),
                           ('tacc',2,2),
                           ('tact',4,2),
                           ('cact',2,2),
                           ('gctc',2,3),
                           ('attc',2,3),
                           ('actc',4,3),
                           ('actt',2,3),
                           ('accc',2,3),
                           ('ttca',2,4),
                           ('ctta',2,4),
                           ('ctca',4,4),
                           ('ctcg',2,4),
                           ('ccca',2,4),
                           ('ttag',2,5),
                           ('tcgg',2,5),
                           ('tcaa',2,5),
                           ('tcag',4,5),
                           ('ccag',2,5),
                           ('tagc',2,6),
                           ('cggc',2,6),
                           ('cagc',4,6),
                           ('cagt',2,6),
                           ('caac',2,6),
                           ('ggca',2,7),
                           ('agta',2,7),
                           ('agca',4,7),
                           ('agcg',2,7),
                           ('aaca',2,7),
                           ('gtat',2,8),
                           ('gcgt',2,8),
                           ('gcac',2,8),
                           ('gcat',4,8),
                           ('acat',2,8),
                           ('tatc',2,9),
                           ('cgtc',2,9),
                           ('catc',4,9),
                           ('catt',2,9),
                           ('cacc',2,9),
                           ('gtca',2,10),
                           ('atta',2,10),
                           ('atca',4,10),
                           ('atcg',2,10),
                           ('acca',2,10)]
    scorematrix = TestKenv.acgt_score
    sequence = 'actactcagcatca'
    qvalue = 4
    score_threshold = 2
    self.check_this_sequence(scorematrix,sequence,qvalue,score_threshold,
                             env_elems_reference)
  def test_kenv_environment_protein(self):
    env_elems_reference = [('MGHL',23,0),
                           ('GHVP',22,1),
                           ('GHMP',23,1),
                           ('GHLP',25,1),
                           ('GHIP',23,1),
                           ('HLPL',23,2),
                           ('PVAW',23,4),
                           ('PFAW',22,4),
                           ('PMAW',24,4),
                           ('PLVW',22,4),
                           ('PLTW',22,4),
                           ('PLSW',23,4),
                           ('PLGW',22,4),
                           ('PLCW',22,4),
                           ('PLAW',26,4),
                           ('PIAW',24,4),
                           ('LAWL',23,5),
                           ('AWLS',23,6),
                           ('WMSQ',22,7),
                           ('WLSQ',24,7),
                           ('WISQ',22,7)]
    scorematrix = TestKenv.blosum62_score
    sequence = 'MGHLPLAWLSQ'
    qvalue = 4
    score_threshold = 22
    self.check_this_sequence(scorematrix,sequence,qvalue,score_threshold,
                             env_elems_reference)
  def test_kenv_environment_protein_long(self):
    env_elems_reference = [('SFY',17,0),
			   ('YYT',15,1),
			   ('FYT',18,1),
			   ('YTA',16,2),
			   ('QAF',15,7),
			   ('SNE',15,11),
			   ('NEK',16,12),
			   ('KLP',16,14),
			   ('MPN',15,15),
			   ('LPN',17,15),
			   ('IPN',15,15),
			   ('PNI',15,16),
			   ('PNL',17,16),
			   ('PNM',15,16),
			   ('NLD',16,17),
			   ('VDC',16,18),
			   ('FDC',15,18),
			   ('MDC',17,18),
			   ('LEC',15,18),
			   ('LDC',19,18),
			   ('IDC',17,18),
			   ('ECI',15,19),
			   ('DCI',19,19),
			   ('DCL',17,19),
			   ('DCM',16,19),
			   ('DCF',15,19),
			   ('DCV',18,19),
			   ('CVQ',17,20),
			   ('CMQ',15,20),
			   ('CLQ',16,20),
			   ('CIQ',18,20),
			   ('CIE',15,20),
			   ('IQN',15,21),
			   ('QNA',15,22),
			   ('NAN',16,23),
			   ('ANK',15,24),
			   ('NKG',17,25),
			   ('KGT',16,26),
			   ('GTH',19,27),
			   ('GSH',15,27),
			   ('THT',18,28),
			   ('HTS',17,29),
			   ('MQR',15,33),
			   ('LRN',15,36),
			   ('RNR',16,37),
			   ('NRG',17,38),
			   ('RGE',16,39),
			   ('GER',16,40),
			   ('ERD',16,41),
			   ('RDR',16,42),
			   ('DRE',16,43),
			   ('RER',15,44),
			   ('ERE',15,45),
			   ('RER',15,46),
			   ('ERE',15,47),
			   ('RER',15,48),
			   ('ERE',15,49),
			   ('REM',15,50),
			   ('EMR',15,51),
			   ('MRR',15,52),
			   ('GLR',15,57),
                           ('RAG',15,59),
                           ('GSR',15,61)]
    scorematrix = TestKenv.blosum62_score
    sequence = 'SFYTAIAQAFLSNEKLPNLDCIQNANKGTHTSLMQRLRNRGERDREREREREMRRSSGLRAGSR'
    qvalue = 3
    score_threshold = 15
    self.check_this_sequence(scorematrix,sequence,qvalue,score_threshold,
                             env_elems_reference)

unittest.main()
