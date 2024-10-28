import pypdf

library = {'1': r"C:\Users\Igor\PycharmProjects\pythonProject\EnglishWordsReferencer\Collaborative_Enhancement_of_Endothelial_Targeting_of_Nanocarriers.pdf",
           '2': r"C:\Users\Igor\PycharmProjects\pythonProject\EnglishWordsReferencer\Multi-photon excitation microscopy.pdf",
           '3': r"C:\Users\Igor\PycharmProjects\pythonProject\EnglishWordsReferencer\Effect_of_titanium_dioxide_nanoparticles_and_β_cyclodextrin_polymer.pdf",
           '4': r"C:\Users\Igor\PycharmProjects\pythonProject\EnglishWordsReferencer\Dual_surface_modified_virus_capsids_for_targeted_delivery_of_photodynamic.pdf",
           '5': r"C:\Users\Igor\PycharmProjects\pythonProject\EnglishWordsReferencer\Optimal_conditions_for_producing_bactericidal_sodium_hyaluronate.pdf",
           '6': r"C:\Users\Igor\PycharmProjects\pythonProject\EnglishWordsReferencer\Virus-based nanocarriers for drug delivery.pdf",
           '7': r"C:\Users\Igor\PycharmProjects\pythonProject\EnglishWordsReferencer\Synthesis,_characterization_and_antimicrobial_activity_of_Schiff.pdf",
           '8': r"C:\Users\Igor\PycharmProjects\pythonProject\EnglishWordsReferencer\Chitosan_Based_Scaffolds_and_Their_Applications_in_Wound_Healing.pdf",
           '9': r"C:\Users\Igor\PycharmProjects\pythonProject\EnglishWordsReferencer\Nanomedicines for cardiovascular disease.pdf",
           '10': r"C:\Users\Igor\PycharmProjects\pythonProject\EnglishWordsReferencer\Amphiphilic_Polysaccharide_Hydrophobicized_Graft_Polymeric_Micelles.pdf",
           '11': r"C:\Users\Igor\PycharmProjects\pythonProject\EnglishWordsReferencer\Gold_nanoparticles_Optical_properties_and_implementations_in_cancer.pdf"}



for key in library.keys():
    reader = pypdf.PdfReader(library[key])

    print(len(reader.pages))
    print(reader.pages[0].extract_text())
