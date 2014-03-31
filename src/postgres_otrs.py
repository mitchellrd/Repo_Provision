diff --git a/src/repo_conf.py b/src/repo_conf.py
new file mode 100644
index 0000000..fbd2e67
--- /dev/null
+++ b/src/repo_conf.py
@@ -0,0 +1,24 @@
+'''
+Created on Mar 30, 2014
+
+@author: roger
+'''
+Linux_OS = {
+        'Type': ['RPM', 'DEBIAN'],
+        'Name': ['Common OTRS Services', 'Local Repository'],
+        'BaseURL': ["ftp://xxx.xx.2.224/pub", "http://LocalRepo.xxx"],
+        'gpgcheck': ["0", "1"],
+        'Enabled': ["0", "1"],
+        't': 'package',
+        }
+
+# Example:
+#  [CS_OTRS_YumServer]
+#  name="Common OTRS Services Yum Repository"
+#  baseurl=ftp://xxx.xxx.xxx.xxx/pub
+#  gpgcheck=0
+#  enabled=1
+#
+# Dependencies:
+#   {}If using FTP each client has to have FTP loaded
+#
\ No newline at end of file