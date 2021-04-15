#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""MicroPhone & Play Sound"""

from __future__ import print_function

import pyaudio
import wave
from six.moves import queue

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 512

# MicrophoneStream - original code in https://goo.gl/7Xy3TT
class MicrophoneStream(object):
	"""Opens a recording stream as a generator yielding the audio chunks."""
	def __init__(self, rate, chunk):  # rate와 chunk를 갖는 객체 생성
		self._rate = rate
		self._chunk = chunk

		# Create a thread-safe buffer of audio data
		self._buff = queue.Queue()
		self.closed = True

	def __enter__(self):
		self._audio_interface = pyaudio.PyAudio()
		self._audio_stream = self._audio_interface.open(
			format=pyaudio.paInt16,
			channels=1, rate=self._rate,
			input=True, frames_per_buffer=self._chunk,
			# Run the audio stream asynchronously to fill the buffer object.
			# This is necessary so that the input device's buffer doesn't
			# overflow while the calling thread makes network requests, etc.
			stream_callback=self._fill_buffer,
		)

		self.closed = False

		return self

	def __exit__(self, type, value, traceback):
		self._audio_stream.stop_stream()
		self._audio_stream.close()
		self.closed = True
		# Signal the generator to terminate so that the client's
		# streaming_recognize method will not block the process termination.
		self._buff.put(None)
		self._audio_interface.terminate()

	def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
		"""Continuously collect data from the audio stream, into the buffer."""
		self._buff.put(in_data)
		return None, pyaudio.paContinue

	def generator(self):  # iterator 생성
		while not self.closed:
			# Use a blocking get() to ensure there's at least one chunk of
			# data, and stop iteration if the chunk is None, indicating the
			# end of the audio stream.
			chunk = self._buff.get()  #버퍼에서 chunk하나를 가져옴
			'''
			queue.get(block=True, timeout=None) : 큐에서 항목을 제거하고 제거한 항목을 반환
			block이 참이고 timeout이 None(기본값)이면, 항목이 사용 가능할 때까지 필요하면 블록합니다
			timeout이 양수면, 최대 timeout 초 동안 블록하고 그 시간 내에 사용 가능한 항목이 없으면 Empty 예외가 발생합니다. 
			block이 거짓이면, 즉시 사용할 수 있는 항목이 있으면 반환하고, 그렇지 않으면 Empty 예외를 발생시킵니다 (이때 timeout은 무시됩니다).
			'''
			if chunk is None:  # 버퍼에서 가져온 chunk가 None이면 리턴
				return
			data = [chunk]  # datat list에 버퍼에서 가져온 chunk 삽입

			# Now consume whatever other data's still buffered.
			while True:
				try:
					chunk = self._buff.get(block=False)  #block이 False이므로 즉시 사용할 수 있는 항목이없으면 예외 발생
					if chunk is None:
						return
					data.append(chunk)
				except queue.Empty:  # 예외처리, 큐가 비어있으면
					break  # 반복문 종료

			yield b''.join(data)  # 함수 안에서 yield를 사용하면 함수는 Generator가 되며 yield에는 값(변수)을 지정합니다.
			'''
			ex)
			generator 함수 number_generator를 실행하면
			for i in number_generator(): print(i) 는
			0
			1 
			2 
			을 출력
			'''
# [END audio_stream]

def play_file(fname):
	# create an audio object
	wf = wave.open(fname, 'rb')
	p = pyaudio.PyAudio()
	chunk = 1024

	# open stream based on the wave object which has been input.
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
					channels=wf.getnchannels(),
					rate=wf.getframerate(),
					output=True)

	# read data (based on the chunk size)
	data = wf.readframes(chunk)

	# play stream (looping from beginning of file to the end)
	while len(data) > 0:
		# writing to the stream is what *actually* plays the sound.
		stream.write(data)
		data = wf.readframes(chunk)

		# cleanup stuff.
	stream.close()
	p.terminate()
