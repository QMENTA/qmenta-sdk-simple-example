# QMENTA SDK Tool Tutorial

<img src="assets/qmenta_logo.png" alt="QMENTA" style="width: 50%">

---

This repository contains the data, code, scripts and configuration files associated with the 
[Getting Started tutorial](https://docs.qmenta.com/sdk/getting_started.html) in the 
[QMENTA SDK documentation](https://docs.qmenta.com/sdk/) portal.

## Description

The tutorial helps you learn the foundations of using the QMENTA SDK and the technological ecosystem around it,
including Docker and the [QMENTA platform](https://client.qmenta.com/#/login).

As a case study, the tutorial goes over the implementation of a tool that takes as input a T1 anatomical image in DICOM
format and converts it to NIfTI or MGZ format. This simple tool illustrates the following SDK capabilities:

- Download files from platform
- Define parameters
- Upload files into the platform
- Set metadata values

# Local testing

The tool is ready to test locally by running a simple command. First, make the script executable:
```shell
chmod +x test_local_sdk.sh
```

And execute it
```shell
./test_local_sdk.sh
```

Once the local testing has been successfully run, you can create the docker image
using the following. Update the image name and version:

```shell
docker build -t image_name:version .
```

The next step is to test the tool locally using the docker image you just created. To perform
this operation, use the script provided running the following. Update again the image name and version:

```shell
python test_container_sdk.py --settings settings.json --values settings_values.json image_name:version data/input data/output/
```

The tool will run inside the container and provide the output files in the `/data/output` folder

---

Now that you have seen the SDK tool development pipeline, we encourage you to try implement your own.
Follow the steps described here and check [Getting Started tutorial](https://docs.qmenta.com/sdk/getting_started.html) in the 
[QMENTA SDK documentation](https://docs.qmenta.com/sdk/) portal to get more information.
