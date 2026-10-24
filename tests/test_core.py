import unittest
from join_fanout_ledger import run
class Tests(unittest.TestCase):
 def test_duplicate_dimension_inflates_left_amount(self):
  r=run({'left':[{'id':'a','key':'x','amount_cents':100}],'right':[{'id':'1','key':'x'},{'id':'2','key':'x'}]});self.assertEqual(r['left_total_cents'],100);self.assertEqual(r['left_join_total_cents'],200);self.assertEqual(r['rows'][0]['matched_right_rows'],2)
 def test_null_keys_do_not_match_each_other(self):
  r=run({'left':[{'id':'a','key':None,'amount_cents':77}],'right':[{'id':'b','key':None}]});self.assertEqual(r['rows'][0]['matched_right_rows'],0);self.assertEqual(r['left_join_total_cents'],77)
 def test_negative_credit_and_per_row_identity_conserve_delta(self):
  r=run({'left':[{'id':'a','key':'x','amount_cents':100},{'id':'b','key':'x','amount_cents':-20}],'right':[{'id':str(i),'key':'x'}for i in range(3)]});self.assertEqual(r['fanout_delta_cents'],160);self.assertEqual(sum(x['extra_cents']for x in r['rows']),r['fanout_delta_cents'])
 def test_empty_right_keeps_unmatched_left_rows(self):self.assertEqual(run({'left':[{'id':'a','key':'x','amount_cents':9}],'right':[]})['left_join_total_cents'],9)
