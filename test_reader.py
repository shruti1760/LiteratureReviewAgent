import os
from dotenv import load_dotenv

load_dotenv(".env")

import asyncio
from agents.reader import reader_agent
load_dotenv(".env")

import asyncio

from agents.reader import reader_agent


sample_text = """
Title: An Efficient Approach to Image Classification

Authors: Alice Smith, Bob Jones

Publication Year: 2025

Abstract:
This paper presents a lightweight convolutional neural network
for image classification on small datasets.

Research Problem:
Traditional deep learning models often require large datasets
and significant computational resources.

Methodology:
The authors propose a compact CNN architecture and compare it
with two existing baseline models.

Dataset:
The experiments were conducted on the CIFAR-10 dataset.

Key Findings:
The proposed model achieved competitive accuracy while using
fewer parameters than the baseline models.

Limitations:
The experiments were performed on a relatively small set of datasets
and the method may require further evaluation on larger datasets.
"""


async def main():
    result = await reader_agent.run(sample_text)

    print(result.output)


if __name__ == "__main__":
    asyncio.run(main())