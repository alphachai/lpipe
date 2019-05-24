import pytest

from lpipe import kinesis

KINESIS_STREAMS = ["test_stream"]


@pytest.mark.postbuild
@pytest.mark.usefixtures("kinesis")
class TestPutRecords:
    def test_batch_put_records_one(self, kinesis_client, kinesis_streams):
        responses = kinesis.batch_put_records(
            stream_name=kinesis_streams[0],
            records=[
                {"foo": "bar", "wiz": "bang"},
                {"lorem": "ipsum", "quid": "est"},
                {"foo": "bar", "wiz": "bang"},
                {"lorem": "ipsum", "quid": "est"},
            ],
            batch_size=2,
        )
        assert len(responses) == 2
        assert all([r["ResponseMetadata"]["HTTPStatusCode"] == 200 for r in responses]) == True
