#!/usr/bin/env python

# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Text-To-Speech API sample application .

Example usage:
    python synthesize_file.py --text resources/hello.txt
    python synthesize_file.py --ssml resources/hello.ssml
"""

import argparse
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/home/pi/Downloads/ai-speaker-e1dab-15354136c034.json"


# [START tts_synthesize_ssml_file]
def synthesize_ssml_file(ssml_file):
    """Synthesizes speech from the input file of ssml.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    f = open("The_Little_Matchgirl", 'r')
    linenum = 0
    while True:
        ssml = f.readline()
        linenum += 1
        if not ssml: break

        input_text = texttospeech.SynthesisInput(ssml=ssml)

        if linenum == 1 or linenum == 48:
            voice = texttospeech.VoiceSelectionParams(
                language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE
        )
        # Note: the voice can also be specified by name.
        # Names of voices can be retrieved with client.list_voices().
        else:
            voice = texttospeech.VoiceSelectionParams(
                language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
            )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = client.synthesize_speech(
            input=input_text, voice=voice, audio_config=audio_config
        )


        # The response's audio_content is binary.
        filename = "The_Little_Matchgirl_Line" + str(linenum) + ".mp3"
        with open(filename, "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "',filename,'"')

# [END tts_synthesize_ssml_file]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="The text file from which to synthesize speech.")
    group.add_argument("--ssml", help="The ssml file from which to synthesize speech.")

    args = parser.parse_args()

    synthesize_ssml_file(args.ssml)
