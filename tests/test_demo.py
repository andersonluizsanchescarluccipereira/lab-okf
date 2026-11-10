import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main


class TesteOKF(unittest.TestCase):
    def test_bundle_valido(self):
        erros, avisos = main.validar()
        self.assertEqual(erros, [])
        self.assertEqual(avisos, [])

    def test_navegacao_suv_hibrido(self):
        fontes, trilha = main.navegar("Qual veículo é um SUV híbrido?")
        self.assertTrue(fontes)
        self.assertIn("rules/hybrid-classification.md", [f.caminho for f in fontes])
        self.assertIn("index.md", trilha)
        self.assertIn("rules/index.md", trilha)

    def test_busca_preco_medio(self):
        fontes, _ = main.navegar("Como calcular preço médio dos veículos?", max_documentos=5)
        self.assertIn("metrics/average-price.md", [f.caminho for f in fontes])

    def test_leitura_frontmatter(self):
        meta, texto = main.ler_conceito(main.BUNDLE / "tables" / "vehicles.md")
        self.assertEqual(meta["type"], "Table")
        self.assertIn("Haval H6", texto)

    def test_impede_sair_do_bundle(self):
        self.assertIsNone(main.caminho_seguro(main.BUNDLE / "index.md", "../../README.md"))
        self.assertIsNone(main.caminho_seguro(main.BUNDLE / "index.md", "https://example.org"))

    def test_palavras_sem_acentos(self):
        self.assertEqual(main.tokens("HÍBRIDOS"), main.tokens("hibridos"))


if __name__ == "__main__":
    unittest.main()
