# Testing the Installation

If you want to test your installation, or maybe hunt for bugs(Thank you!), then here are the instructions to do so.

First, you want to decompress the included zip file in Test_Data. Included inside is some ChIPSeq data you can test.

Navigate to the resulting folder, and run this command:

```bash
danpos dtriple WT_ChIP:KO_ChIP -b WT_ChIP:WT_Input,KO_ChIP:KO_Input -o analysis_results
```

Essentially, this runs the dtriple command, which runs all 3 of the main functions of DANPOS. This gives you a pretty good testing suite. Optionally, you can use nohup to run it in the backround, or use `>` to pipe the output into a file.

The Output will be in a folder named `analysis_results`, and you can analyze the output from there.
