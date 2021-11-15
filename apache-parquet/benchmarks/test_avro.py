import fastavro
import pytest
from six import BytesIO

# pylint: disable-all


class TestBenchmark(object):
    @pytest.fixture
    def avro_schema_json(self):
        return {
            "type": "record",
            "name": "test_record",
            "fields": [
                {"type": ["null", "int"], "name": "union_field"},
                {"type": ["null", "int"], "name": "union_field_null", "default": None},
                {"type": ["null", "int"], "name": "union_field_101", "default": 101},
                {"type": "boolean", "name": "bool_field"},
                {"type": "boolean", "name": "bool_field_F", "default": False},
                {"type": "string", "name": "string_field"},
                {"type": "string", "name": "string_field_foo", "default": "foo❤"},
                {"type": "bytes", "name": "bytes_field"},
                {"type": "bytes", "name": "bytes_field_bar", "default": "bar"},
                {"type": "int", "name": "int_field"},
                {"type": "int", "name": "int_field_1", "default": 1},
                {"type": "long", "name": "long_field"},
                {"type": "long", "name": "long_field_42", "default": 42},
                {"type": "float", "name": "float_field"},
                {"type": "float", "name": "float_field_p75", "default": 0.75},
                {"type": "double", "name": "double_field"},
                {"type": "double", "name": "double_field_pi", "default": 3.14},
            ],
        }

    @pytest.fixture
    def sample_data(self, avro_schema_json):
        return {
            "long_field": 2,
            "long_field_42": 42,
            "bytes_field": b"_",
            "float_field_p75": 0.75,
            "bytes_field_bar": b"bar",
            "bool_field_F": False,
            "string_field_foo": "foo\u2764",
            "float_field": 0.5,
            "union_field_null": None,
            "double_field_pi": 3.14,
            "int_field": 1,
            "union_field_101": 101,
            "union_field": None,
            "int_field_1": 1,
            "double_field": 2.2,
            "string_field": "\u2764",
            "bool_field": True,
        }

    @pytest.fixture
    def fastavro_string_writer_encoder(self, avro_schema_json):
        def encoder(message):
            stringio = BytesIO()
            fastavro.schemaless_writer(stringio, avro_schema_json, message)
            return stringio.getvalue()

        return encoder

    @pytest.fixture
    def fastavro_string_reader_decoder(self, avro_schema_json):
        def decoder(encoded_message):
            if not isinstance(encoded_message, bytes):
                raise TypeError
            stringio = BytesIO(encoded_message)
            return fastavro.schemaless_reader(stringio, avro_schema_json)

        return decoder

    @pytest.fixture(
        params=["avro_string_writer_encoder", "fastavro_string_writer_encoder"]
    )
    def encoder(self, request):
        """This test uses request.getfuncargvalue to parametrize dynamic fixtures.
        The code might appear confusing but there is a proposal from pytest to make it
        better https://docs.pytest.org/en/latest/proposals/parametrize_with_fixtures.html.
        """
        return request.getfuncargvalue(request.param)

    @pytest.fixture(
        params=["avro_string_reader_decoder", "fastavro_string_reader_decoder"]
    )
    def decoder(self, request):
        """This test uses request.getfuncargvalue to parametrize dynamic fixtures.
        The code might appear confusing but there is a proposal from pytest to make it
        better https://docs.pytest.org/en/latest/proposals/parametrize_with_fixtures.html.
        """
        return request.getfuncargvalue(request.param)

    @pytest.mark.benchmark(
        group="encoders",
    )
    def test_encoder(self, benchmark, encoder, sample_data):
        benchmark.pedantic(
            target=encoder,
            args=[sample_data],
            iterations=10,
            rounds=10000,
            warmup_rounds=100,
        )

    @pytest.mark.benchmark(
        group="decoders",
    )
    def test_decoder(self, benchmark, avro_string_writer_encoder, decoder, sample_data):
        encoded_data = avro_string_writer_encoder(sample_data)
        benchmark.pedantic(
            target=decoder,
            args=[encoded_data],
            iterations=10,
            rounds=10000,
            warmup_rounds=100,
        )
