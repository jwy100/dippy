# Document Images to PDF in Python (Dippy)

Need to scan some documents, but don't have a scanner to hand, and don't want to pay an IPhone app to do it? Then here is a not so user-friendly (but free) way to do it!

Suitable for text documents, where the expected result is black text on a white background. 

## Requirements

- A set of JPEG images of documents that you want to turn into a combined PDF
- Python 3
- Pipenv

## Usage

Run the following command in the same directory as this project, and substitute the arguments ($IMAGE_1, $IMAGE_2, ... ) for the file paths of the images you want to process and turn into a combined PDF. Supply the file names in the order that they should appear in the PDF

```
pipenv run python main.py $IMAGE_1 $IMAGE_2 ...
```

## Notes

Note that this short script was produced for a one-off usecase, so may not be applicable to wider usecases. 

Results of the PDF will depend on the lighting of the document in the image(s). Try to use images with even lighting. This code can't perform miracles.

