from unstructured.partition.auto import partition
elements = partition(filename="5_SQL Aggregates.pdf")
# print("\n\n".join([str(el) for el in elements]))

# from unstructured.partition.auto import partition
# elements = partition("data/PerksPlus.pdf")
# print("\n\n".join([str(el) for el in elements]))
# for element in elements[:5]:
#     print(element)
#     print("\n")
# The above code is partitioning
from unstructured.documents.elements import NarrativeText
from unstructured.partition.text_type import sentence_count

# for element in elements[:100]:
#     if isinstance(element, NarrativeText) and sentence_count(element.text) > 2:
#         print(element)
#         print("\n")
# The above code is for staging
from unstructured.staging.base import convert_to_dict
convert_to_dict(elements)
from unstructured.staging.base import elements_to_json, elements_from_json


filename = "outputs.json"
elements_to_json(elements, filename=filename)
elements = elements_from_json(filename=filename)
# # Converting to json
from unstructured.chunking.title import chunk_by_title
chunks = chunk_by_title(elements)

for chunk in chunks:
    print(chunk,"\n \n")
    print("\n\n" + "-"*80)
    input()
# The above code is for chunking


import os

from unstructured.documents.elements import Text
from unstructured.embed.openai import OpenAIEmbeddingEncoder

# Initialize the encoder with OpenAI credentials
embedding_encoder = OpenAIEmbeddingEncoder(api_key="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")

for chunk in chunks:
    if hasattr(chunk, 'text'):
        # Embed the text
        embedding = embedding_encoder.embed_query(query=chunk.text)
        print(chunk,"\n \n")
        print(embedding, "\n \n")

# Embed a list of Elements
elements = embedding_encoder.embed_documents(
    elements=[Text("This is sentence 1"), Text("This is sentence 2")],
)

# Embed a single query string
query = "This is the query"
query_embedding = embedding_encoder.embed_query(query=query)

# Print embeddings
[print(e.embeddings, e,"\n \n") for e in elements]
print(query_embedding," ", query,"\n \n")
print(embedding_encoder.is_unit_vector(), embedding_encoder.num_of_dimensions())
# #The above code is for Embeddings

'''import os

from unstructured.ingest.interfaces import (
    FsspecConfig,
    PartitionConfig,
    ProcessorConfig,
    ReadConfig,
)
from unstructured.ingest.runner import AzureRunner

if _name_ == "_main_":
    runner = AzureRunner(
        processor_config=ProcessorConfig(
            verbose=True,
            output_dir="azure-ingest-output",
            num_processes=2,
        ),
        read_config=ReadConfig(),
        partition_config=PartitionConfig(),
        fsspec_config=FsspecConfig(
            remote_url="abfs://container1/",
        ),
    )
    runner.run(
        account_name="azureunstructured1",
    )'''

# import os

# from unstructured.ingest.interfaces import PartitionConfig, ProcessorConfig, ReadConfig
# from unstructured.ingest.runner import ElasticSearchRunner

# if _name_ == "_main_":
#     runner = ElasticSearchRunner(
#         processor_config=ProcessorConfig(
#             verbose=True,
#             output_dir="elasticsearch-ingest-output",
#             num_processes=2,
#         ),
#         read_config=ReadConfig(),
#         partition_config=PartitionConfig(
#             metadata_exclude=["filename", "file_directory", "metadata.data_source.date_processed"],
#         ),
#     )
#     runner.run(
#         url="http://localhost:9200",
#         index_name="movies",
#         jq_query="{ethnicity, director, plot}",
#     )

# import os
# import subprocess

# command = [
#     "unstructured-ingest",
#     "s3",
#     "--remote-url", "s3://utic-dev-tech-fixtures/small-pdf-set/",
#     "--anonymous",
#     "--output-dir", "s3-small-batch-output-to-azure",
#     "--num-processes", "2",
#     "--verbose",
#     "--strategy", "fast",
#     "azure-cognitive-search",
#     "--key", "VmM0fMtVNqbwZKbomZrZgRKnadwl12Qc3KXxMsXIzIAzSeBAgDyI",
#     "--endpoint", "https://gptkb-cdzj2obpa54em.search.windows.net",
#     "--index", "gptkbindex",
# ]

# # Run the command
# process = subprocess.Popen(command, stdout=subprocess.PIPE)
# output, error = process.communicate()

# # Print output
# if process.returncode == 0:
#     print("Command executed successfully. Output:")
#     print(output.decode())
# else:
#     print("Command failed. Error:")
#     print(error.decode() if error else "No error message available.")

# from unstructured.ingest.runner import AzureRunner
# from unstructured.ingest.interfaces import FsspecConfig, PartitionConfig, ProcessorConfig, ReadConfig

# if _name_ == "_main_":
#     runner = AzureRunner(
#         processor_config=ProcessorConfig(
#             verbose=True,
#             output_dir="s3-small-batch-output-to-azure",
#             num_processes=2,
#         ),
#         read_config=ReadConfig(),
#         partition_config=PartitionConfig(),
#         fsspec_config=FsspecConfig(
#     remote_url="s3://utic-dev-tech-fixtures/small-pdf-set/",
#     access_kwargs={
#         "account_name": "gptkb-cdzj2obpa54em",  # Replace with your actual storage account name
#         "account_key": "VmM0fMtVNqbwZKbomZrZgRKnadwl12Qc3KXxMsXIzIAzSeBAgDyI",  # Replace with your actual storage account key
#     },
# ),
#     )
#     runner.run(
#         account_name="gptkb-cdzj2obpa54em",
#         key="VmM0fMtVNqbwZKbomZrZgRKnadwl12Qc3KXxMsXIzIAzSeBAgDyI",
#         endpoint="https://gptkb-cdzj2obpa54em.search.windows.net",
#         index="gptkbindex",
#     )
