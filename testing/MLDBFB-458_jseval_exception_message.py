#
# MLDBFB-458_jseval_exception_message.py.py
# Mich, 2016-04-05
# Copyright (c) 2016 Datacratic Inc. All rights reserved.
#

mldb = mldb_wrapper.wrap(mldb)  # noqa

class JsevalExceptionMessageTest(MldbUnitTest):  # noqa
    def test_it(self):
        ds = mldb.create_dataset({'id' : 'ds', 'type' : 'sparse.mutable'})
        ds.record_row('row1', [])
        ds.commit()

        query = """
            SELECT jseval('
                {}
                return {{"foo" : "bar"}};
                ',
                'cols',
                {{*}}
            ) AS *
            FROM ds
                """

        # the query works
        mldb.log(mldb.query(query.format("")))

        # add an exception, good luck understanding what's going on now...
        mldb.query(query.format('throw "this query is weird";'))

if __name__ == '__main__':
    mldb.run_tests()
