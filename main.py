import fastavro


with open(
    "/Users/mert/Downloads/core_core_test_test_2022-07-06 21_45_31.184180_export-000000000000.avro",
    "rb",
) as f:
    reader = fastavro.reader(f)
    print("schema:", reader.writer_schema)
    for record in reader:
        print("record:", record)
