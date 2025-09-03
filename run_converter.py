#!/usr/bin/env python3
"""
Simple runner script for the PDF converter
"""

from pdf_converter import PDFConverter
import sys

def main():
    """Run the PDF converter with simple interface."""
    print("🔄 Iniciando conversão de PDFs para texto...")
    
    try:
        converter = PDFConverter()
        
        # Show current status
        stats = converter.get_conversion_stats()
        print(f"📊 Status atual:")
        print(f"   PDFs encontrados: {stats['total_pdfs']}")
        print(f"   Arquivos já convertidos: {stats['converted_txts']}")
        print(f"   Diretório de saída: {stats['output_directory']}")
        
        # Run conversion
        converted_files = converter.convert_all_pdfs()
        
        if converted_files:
            print(f"\n✅ Conversão concluída com sucesso!")
            print(f"📁 {len(converted_files)} arquivos convertidos em: docs/corpus_textual/")
            
            # List converted files
            for txt_file in converted_files:
                print(f"   ✓ {txt_file.name}")
        else:
            print("\n⚠️  Nenhum arquivo foi convertido.")
            
    except Exception as e:
        print(f"\n❌ Erro durante a conversão: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
