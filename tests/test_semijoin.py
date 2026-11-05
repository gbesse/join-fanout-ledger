import unittest
from join_fanout_ledger.core import run
class SemijoinTests(unittest.TestCase):
 def test_actual_semijoin_control(self):
  x=run({'left':[dict(id='a',key='K',amount_cents=100),dict(id='b',key=None,amount_cents=-20)],'right':[dict(id='x',key='K'),dict(id='y',key='K')]})
  self.assertEqual(x['matched_once_total_cents'],100);self.assertEqual(x['unmatched_total_cents'],-20);self.assertEqual(x['left_total_cents'],80);self.assertEqual(x['left_join_total_cents'],180)
 def test_empty(self):
  x=run({'left':[],'right':[]});self.assertEqual(x['matched_once_total_cents'],0)
