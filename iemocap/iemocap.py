# coding=utf-8
# Copyright 2022 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import datasets  # type: ignore
import json
import ast

logger = datasets.logging.get_logger(__name__)


"""IEMOCAP TODO"""

_CITATION = """\
TODO
"""

_DESCRIPTION = """\
TODO
"""

_HOMEPAGE = "TODO"
_LICENSE = "TODO"

_ROOT_DIR = "iemocap"
_DATA_URL = f"data/{_ROOT_DIR}.zip"


_EMOTION_MAP = {
    "neu": "neutral",
    "fru": "frustrated",
    "sad": "sad",
    "sur": "surprised",
    "ang": "anger",
    "hap": "happy",
    "exc": "disgust",
    "fea": "fear",
    "dis": "disgust",
    "xxx": "uncertain",
    "oth": "other",
}

# _INTENSITY_MAP = {
#     "LO": "Low",
#     "MD": "Medium",
#     "HI": "High",
#     "XX": "Unspecified",
#     ## one stray file
#     "X": "Unspecified",
# }

_CLASS_NAMES = list(_EMOTION_MAP.keys())


class IemocapDataset(datasets.GeneratorBasedBuilder):
    """The Iemocap dataset"""

    VERSION = datasets.Version("1.0.0")

    def _info(self):
        sampling_rate = 16_000
        features = datasets.Features(
            {
                # "duration": datasets.Value("string"),
                "audio": datasets.Audio(sampling_rate=sampling_rate),
                "text": datasets.Value("string"),
                "rating1": datasets.Value("string"),
                "rating2": datasets.Value("string"),
                "rating3": datasets.Value("string"),
                "gender": datasets.Value("string"),
                "valence": datasets.Value("float32"),
                "activation": datasets.Value("float32"),
                "dominance": datasets.Value("float32"),
                "label": datasets.ClassLabel(names=_CLASS_NAMES),
            }
        )

        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            citation=_CITATION,
            license=_LICENSE,
            # task_templates=[datasets.TaskTemplate("audio-classification")],
        )

    def _split_generators(self, dl_manager):

        archive_path = dl_manager.download_and_extract(_DATA_URL)

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    "archive_path": archive_path,
                    # "local_extracted_archive": local_extracted_archive,
                    # "audio_files": dl_manager.iter_archive(archive),
                },
            )
        ]

    def _generate_examples(self, archive_path):

        filepath = os.path.join(archive_path, _ROOT_DIR, "session1.json")
        with open(filepath, "r") as f:
            data = json.load(f)
            objects = [
                {**obj, "folder_name": "_".join(folder_name.split("_")[:-1])}
                for key in data
                for folder_name, obj in data[key].items()
            ]
            id_ = 0
            for obj in objects:
                fpath = os.path.join(
                    archive_path,
                    _ROOT_DIR,
                    "Session1",
                    "sentences",
                    "wav",
                    obj["folder_name"],
                    f"{obj['audio_file_path']}.wav",
                )
                with open(fpath, "rb") as f:
                    audio_bytes = f.read()
                # duration = 0
                # print(obj)
                gender = obj["audio_file_path"][obj["audio_file_path"].rfind("_") + 1]

                valence, activation, dominance = map(
                    float, obj["intensity"].strip("[]").split(", ")
                )

                base = {
                    "text": obj["text"],
                    "rating1": obj["rating1"],
                    "rating2": obj["rating2"],
                    "rating3": obj["rating3"],
                    "label": obj["emotion"],
                    "valence": valence,
                    "activation": activation,
                    "dominance": dominance,
                    "gender": gender,
                    # duration: duration,
                }
                audio = {"path": fpath, "bytes": audio_bytes}
                yield id_, {**base, "audio": audio}
                id_ += 1
