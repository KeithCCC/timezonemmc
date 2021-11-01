need pip install -t lib -r requirements.txt
sandbox.py need white list
GCP documents and resoruces https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env#test_the_application


(TimeCat) G:\Dev\TimeCat\FindTime>gcloud app deploy --project findtime-177314
Services to deploy:

descriptor:      [G:\Dev\TimeCat\FindTime\app.yaml]
source:          [G:\Dev\TimeCat\FindTime]
target project:  [findtime-177314]
target service:  [default]
target version:  [20170827t235719]
target url:      [https://globaltime-178216.appspot.com]

console message

Do you want to continue (Y/n)?  y

Beginning deployment of service [default]...
Some files were skipped. Pass `--verbosity=info` to see which ones.
You may also view the gcloud log file, found at
[C:\Users\Keith\AppData\Roaming\gcloud\logs\2017.08.27\23.57.14.399000.log].
#============================================================#
#= Uploading 6 files to Google Cloud Storage                =#
#============================================================File upload done.
Updating service [default]...done.
Waiting for operation [apps/findtime-177314/operations/07dbcc5f-59a9-46c9-a6da-cb45c3e0d5f4] to complete...done.
Updating service [default]...done.
Deployed service [default] to [https://findtime-177314.appspot.com]

You can stream logs from the command line by running:
  $ gcloud app logs tail -s default

To view your application in the web browser run:
  $ gcloud app browse

(TimeCat) G:\Dev\TimeCat\FindTime>


python G:\Dev\globaltime\Lib\site-packages\google_appengine\dev_appserver.py app.yaml


runtime: python27
env: standard
threadsafe: true
instance_class: F1
handlers:
  - url: "/favicon\\.ico"
    application_readable: false
    static_files: static/img/favicon.ico
    require_matching_file: false
    upload: "static/img/favicon\\.ico"
  - url: '/static/(.*)'
    application_readable: false
    static_files: "static/\\1"
    require_matching_file: false
    upload: 'static/.*'
  - url: '/.*'
    script: main.app
automatic_scaling:
  min_idle_instances: automatic
  max_idle_instances: automatic
  min_pending_latency: automatic
  max_pending_latency: automatic