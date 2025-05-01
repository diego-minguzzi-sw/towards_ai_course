import argparse
import docx
"""
python poc_read_word_docx.py --word-file ${TAI_DATASET_ROOT}/cobot_kb/PARobot-plugin-3.0C1.docx
python poc_read_word_docx.py --word-file ${TAI_DATASET_ROOT}/cobot_kb/Guidance_Programming_Language.docx
"""

class CliArgs:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Process a word file.")
        parser.add_argument("--word-file",type=str,required=True,help="Path to the word file")
        args = parser.parse_args()
        self._wordFile = args.word_file

    @property
    def wordFile(self):
        return self._wordFile

def traverseDocument(filepath):
    # Open the Word document
    doc = docx.Document(filepath)

    # Iterate through all paragraphs
    for paragraph in doc.paragraphs:
        # Check for specific heading styles
        if paragraph.style.name == 'Heading 1':
            print(f"Header 1: {paragraph.text}")
        elif paragraph.style.name == 'Heading 2':
            print(f"Header 2: {paragraph.text}")
        elif paragraph.style.name == 'Heading 3':
            print(f"Header 3: {paragraph.text}")
        elif paragraph.style.name == 'Heading 4':
            print(f"Header 4: {paragraph.text}")
        else:
            # Print normal text if it's not a heading
            if 0==len(str(paragraph.text).strip()):
              continue

            print(f"{paragraph.style.name}: {paragraph.text}")

        # Detect pictures in the paragraph
        for run in paragraph.runs:
            # Check if the run contains an inline shape (potential picture)
            if run._element.xpath('.//w:drawing'):
                print("Picture detected in this paragraph!")



def main():
    pass  # Replace with your code
    cliArgs = CliArgs()
    traverseDocument( cliArgs.wordFile)

if __name__ == "__main__":
    main()
