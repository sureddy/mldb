#
# MLDB-1708-sum-token-csv.py
# Simon Lemieux, 2016-06-07
# Copyright (c) 2016 Datacratic Inc. All rights reserved.
#

mldb = mldb_wrapper.wrap(mldb)  # noqa

class Mldb1708SumTokenCsv(MldbUnitTest):  # noqa
    def test(self):
        ds = mldb.create_dataset({'id' : 'ds', 'type' : 'sparse.mutable'})
        ds.record_row('row0', [['x', 'patate poil', 0]])
        ds.record_row('row1', [['x', 'patate chose', 0]])
        ds.record_row('row2', [['x', ' ', 0]])
        ds.commit()

        mldb.post('/v1/procedures', {
            'type': 'transform',
            'params': {
                'inputData': "select tokenize(x, {splitchars: ' '}) from ds",
                'outputDataset': 'ds2',
                'runOnCreation': True
            }
        })

        mldb.log(mldb.query('select * from ds2'))
        mldb.log(mldb.query('select sum({*}) from ds2'))


if __name__ == '__main__':
    mldb.run_tests()
