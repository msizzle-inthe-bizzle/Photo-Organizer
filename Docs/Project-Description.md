# Photo Organizer

## Overview
This project organizes photos automatically based on metadata such as:
- Date taken
- Location (GPS)
- Camera information

## Goals
- Automatically sort images into folders
- Extract EXIF metadata
- Support batch processing of large photo collections

## Features
- Read metadata from images
- Create folder structure by date (YYYY/MM/DD)
- Move or copy files into organized directories

## System Architecture
- Input: folder of raw images
- Processing: metadata extraction (Python script)
- Output: organized folder structure

##Future Work
- Be able to delete duplicate photos for clearing space - pixel comparison?
- Be able to prompt for which type of photos to be deleted. Ex: "Delete photos with a notebook in them"

## Technologies
- Python
- EXIF libraries (e.g., Pillow, exifread)
