#if error, run as admin and set: "set-executionpolicy" to "remotesigned"
cls

1..10 | foreach {echo ($_ * 2)}
