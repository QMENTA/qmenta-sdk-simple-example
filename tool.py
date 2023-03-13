# -*- coding: utf-8 -*-
import os


def run(context):
    """
    Function invoked by the SDK that passes a context object. This object can then be used
    to communicate with the platform in the context of that particular analysis to fetch files,
    report progress, and upload results, among others.

    Parameters
    ----------
    context : qmenta.sdk.context.AnalysisContext
        Analysis context object to communicate with the QMENTA Platform.
    """

    """ Basic setup """

    # Define directories for the input and output files inside the container
    input_dir = os.path.join(os.path.expanduser("~"), "INPUT")
    output_dir = os.path.join(os.path.expanduser("~"), "OUTPUT")
    os.makedirs(output_dir, exist_ok=True)
    context.set_progress(value=0, message="Processing")  # Set progress status so it is displayed in the platform

    """ Get the input data """

    # Retrieve input files
    anat_handler = context.get_files("input_anat", file_filter_condition_name="c_anat")[0]  # Only gets one file that passed the filter
    
    anat = anat_handler.download(input_dir)  # DICOM uncompressed folder
    modality = context.get_files("input_anat", file_filter_condition_name="c_anat")[0].get_file_modality()

    # Retrieve settings
    settings = context.get_settings()

    """ Processing code """

    context.set_progress(value=10, message="Choosing output format")
    output_format = settings["output_format"]
    if output_format == "mgz":
        ext = ".mgz"
    elif output_format == "nii":
        ext = ".nii"
    elif output_format == "niigz":
        ext = ".nii.gz"
    else:
        raise Exception("Invalid output format.")

    out_anat = os.path.basename(anat) + ext
    os.system(f"mrconvert {anat} {out_anat}")

    """ Upload results """
    context.upload_file(out_anat, "anatomical_image" + ext, modality=modality)

    """ Setting metadata field """
    context.set_metadata_value(key="output_format", title="Output Format", value=output_format)