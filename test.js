'use strict'

const recorder = require('node-record-lpcm16')
const fs = require('fs')

const file = fs.createWriteStream('test.wav', { encoding: 'binary' })

const recording = recorder.record({
  recorder: 'sox'
})

recording.stream()
  .pipe(file)

// Stop recording after three seconds and write to file
setTimeout(() => {
  recording.stop()
}, 2000)

