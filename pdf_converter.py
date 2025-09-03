#!/usr/bin/env python3
"""
PDF to Text Converter for CardioIA Project
Converts all PDF files in the docs directory to text format and organizes them.
"""

import os
import sys
from pathlib import Path
import PyPDF2
import pdfplumber
from typing import List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PDFConverter:
    def __init__(self, base_dir: str = None):
        """Initialize the PDF converter with base directory."""
        if base_dir is None:
            self.base_dir = Path(__file__).parent
        else:
            self.base_dir = Path(base_dir)
        
        self.docs_dir = self.base_dir / "docs"
        self.output_dir = self.docs_dir / ".txt"
        
    def create_output_directory(self) -> None:
        """Create the output directory for text files."""
        self.output_dir.mkdir(exist_ok=True)
        logger.info(f"Output directory created/verified: {self.output_dir}")
    
    def find_pdf_files(self) -> List[Path]:
        """Find all PDF files in the docs directory."""
        pdf_files = []
        if self.docs_dir.exists():
            pdf_files = list(self.docs_dir.glob("*.pdf"))
            logger.info(f"Found {len(pdf_files)} PDF files")
            for pdf_file in pdf_files:
                logger.info(f"  - {pdf_file.name}")
        else:
            logger.warning(f"Docs directory not found: {self.docs_dir}")
        return pdf_files
    
    def extract_text_pypdf2(self, pdf_path: Path) -> Optional[str]:
        """Extract text using PyPDF2 (fallback method)."""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text() + "\n"
                return text.strip()
        except Exception as e:
            logger.error(f"PyPDF2 extraction failed for {pdf_path.name}: {e}")
            return None
    
    def extract_text_pdfplumber(self, pdf_path: Path) -> Optional[str]:
        """Extract text using pdfplumber (primary method)."""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = ""
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                return text.strip()
        except Exception as e:
            logger.error(f"pdfplumber extraction failed for {pdf_path.name}: {e}")
            return None
    
    def extract_text_from_pdf(self, pdf_path: Path) -> Optional[str]:
        """Extract text from PDF using multiple methods."""
        logger.info(f"Extracting text from: {pdf_path.name}")
        
        # Try pdfplumber first (better for complex layouts)
        text = self.extract_text_pdfplumber(pdf_path)
        
        # Fallback to PyPDF2 if pdfplumber fails
        if not text or len(text.strip()) < 100:
            logger.info(f"Trying PyPDF2 for {pdf_path.name}")
            text = self.extract_text_pypdf2(pdf_path)
        
        if text and len(text.strip()) > 0:
            logger.info(f"Successfully extracted {len(text)} characters from {pdf_path.name}")
            return text
        else:
            logger.error(f"Failed to extract text from {pdf_path.name}")
            return None
    
    def save_text_file(self, text: str, original_pdf_path: Path) -> Path:
        """Save extracted text to a .txt file."""
        # Create output filename by replacing .pdf with .txt
        txt_filename = original_pdf_path.stem + ".txt"
        txt_path = self.output_dir / txt_filename
        
        try:
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(text)
            logger.info(f"Saved text file: {txt_path}")
            return txt_path
        except Exception as e:
            logger.error(f"Failed to save text file {txt_path}: {e}")
            raise
    
    def convert_all_pdfs(self) -> List[Path]:
        """Convert all PDF files to text format."""
        self.create_output_directory()
        pdf_files = self.find_pdf_files()
        
        if not pdf_files:
            logger.warning("No PDF files found to convert")
            return []
        
        converted_files = []
        failed_files = []
        
        for pdf_path in pdf_files:
            try:
                text = self.extract_text_from_pdf(pdf_path)
                if text:
                    txt_path = self.save_text_file(text, pdf_path)
                    converted_files.append(txt_path)
                else:
                    failed_files.append(pdf_path)
            except Exception as e:
                logger.error(f"Error processing {pdf_path.name}: {e}")
                failed_files.append(pdf_path)
        
        # Summary
        logger.info(f"\nConversion Summary:")
        logger.info(f"Successfully converted: {len(converted_files)} files")
        logger.info(f"Failed conversions: {len(failed_files)} files")
        
        if converted_files:
            logger.info("\nConverted files:")
            for txt_file in converted_files:
                logger.info(f"  ✓ {txt_file.name}")
        
        if failed_files:
            logger.warning("\nFailed files:")
            for pdf_file in failed_files:
                logger.warning(f"  ✗ {pdf_file.name}")
        
        return converted_files
    
    def get_conversion_stats(self) -> dict:
        """Get statistics about the conversion process."""
        pdf_files = self.find_pdf_files()
        txt_files = list(self.output_dir.glob("*.txt")) if self.output_dir.exists() else []
        
        return {
            "total_pdfs": len(pdf_files),
            "converted_txts": len(txt_files),
            "output_directory": str(self.output_dir),
            "pdf_files": [f.name for f in pdf_files],
            "txt_files": [f.name for f in txt_files]
        }

def main():
    """Main function to run the PDF converter."""
    print("CardioIA PDF to Text Converter")
    print("=" * 40)
    
    try:
        converter = PDFConverter()
        converted_files = converter.convert_all_pdfs()
        
        if converted_files:
            print(f"\n✅ Successfully converted {len(converted_files)} PDF files to text format!")
            print(f"📁 Text files saved in: {converter.output_dir}")
        else:
            print("\n❌ No files were converted. Check the logs for details.")
            
    except Exception as e:
        logger.error(f"Application error: {e}")
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
