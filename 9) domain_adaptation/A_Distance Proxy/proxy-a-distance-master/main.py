"""
Main driver code
"""


import argparse # option parsing
from src.dataset import Dataset
from src.model import SVM
import random
import numpy as np
import pprint

def process_command_line():
  """
  Return a 1-tuple: (args list).
  `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
  """

  parser = argparse.ArgumentParser(description='usage') # add description
  # positional arguments
  parser.add_argument('d1s', metavar='domain1-source', type=str, help='domain 1 source')
  parser.add_argument('d1t', metavar='domain1-target', type=str, help='domain 1 target')

  parser.add_argument('d2s', metavar='domain2-source', type=str, help='domain 2 source')
  parser.add_argument('d2t', metavar='domain2-target', type=str, help='domain 2 target')

  parser.add_argument('v', metavar='vocab', type=str, help='shared bpe vocab')

  # optional arguments
  parser.add_argument('-x', '--averaging-over', dest='x', type=int, default=10, help='How many PAD approximations to compute and average over')
  parser.add_argument('-b', '--batch-size', dest='b', type=int, default=320, help='batch_size')

  args = parser.parse_args()
  return args


def main(domain1_source, domain1_target, domain2_source, domain2_target, vocab, batch_size, x):
    data_iterator = Dataset(domain1_source, 
                            domain1_target, 
                            domain2_source, 
                            domain2_target, 
                            vocab, 
                            batch_size=batch_size)
    """
    #COMMENTED OUT BY ME TO ADD THE FOLLOWING SNIPPET
    model = SVM(batch_size, data_iterator.get_vocab_size())
    model.fit(data_iterator)
    print 'INFO: testing...'
    test_mae = model.test(data_iterator, mae=True)
    print 'INFO: test MAE: ', test_mae
    print 'INFO: PAD value: ', 2. * (1. - 2. * test_mae)
    """
    PAD_Results = []
    print "================================="
    print "Source: {} -> Target: {} [Averaging over {:d} batches]\n".format(domain1_source, domain2_source, x)
    for B in range(1, x+1):
        print "\nBatch Number {:d} out of {:d} executing..".format(B,x)
        model = SVM(batch_size, data_iterator.get_vocab_size())
        model.fit(data_iterator)
        print 'INFO: testing...'
        test_mae = model.test(data_iterator, mae=True)
        #print 'INFO: test MAE: ', test_mae
        currentPAD = 2. * (1. - 2. * test_mae)
        print 'INFO: PAD value: ', currentPAD
        PAD_Results.append(currentPAD)
	print "-------------------------------"
    print "All PAD values throughout the {:d} approximations are:".format(x)
    pprint.pprint(PAD_Results)
    print "\nThe Final Average PAD is: {:10.6f}".format(sum(PAD_Results)/float(len(PAD_Results)))
    print "================================="
if __name__ == '__main__':

  #  s1 = '../../../datasets/mantis_to_erp_next/mantis_en_issues_sentences.txt'
   # s2 = '../../../datasets/mantis_to_erp_next/erp_next_issues_sentences.txt'

   # v = '../../../datasets/mantis_to_erp_next/Vocab_erp_next_issues_mantis_en_issues.txt'
  #  v2 = '../../../datasets/mantis_to_erp_next/Vocab_erp_next_issues_mantis_en_issues.txt'

  #  main(s1, s1, s2, s2, v2, 320, 10)

    args = process_command_line()
    main(args.d1s, args.d1t, args.d2s, args.d2t, args.v, args.b, args.x)