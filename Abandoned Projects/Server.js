const express = require('express')
const app = express()
let { PythonShell } = require('python-shell')

const PORT = process.env.PORT || 3000

app.listen(PORT, () => {
  console.log('server running on port 3000')
})

app.get('/', pythonProcess)

function pythonProcess(req, res) {
  let options = {
    mode: 'text',
    pythonOptions: ['-u'],
  }

  PythonShell.run('Main.py', options, (err, results) => {
    if (err) res.send(err)
    res.send(results)
  })
}