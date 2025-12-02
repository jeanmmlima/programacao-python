class Livro:
    def __init__(self, titulo: str, autor: str, disponivel: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel
    def emprestar(self):
        self.disponivel = False
        print(f"O livro {self.titulo} foi emprestado!\n")
    def devolver(self):
        self.disponivel = True
        print(f"O livro {self.titulo} foi devolvido!\n")
        
class Biblioteca:
    def __init__(self, lista_livros: list):
        self.lista_livros = lista_livros
    def adicionar_livro(self, novo_livro: Livro):
        self.lista_livros.append(novo_livro)
        print(f"O livro {novo_livro.titulo} foi adicionado a biblioteca!\n")
    def listar_livros(self):
        for livro in self.lista_livros:
            status = ''
            if livro.disponivel:
                status = 'Disponivel'
            else:
                status = 'Emprestado'
            print(f'Livro: {livro.titulo} - Autor: {livro.autor} - Status: {status}')


l1 = Livro("O senhor dos aneis - sociedade do anel", "Tolkien")
l2 = Livro("O senhor dos aneis - as duas torres", "Tolkien")
l3 = Livro("O senhor dos aneis - o retorno do Rei", "Tolkien")
l4 = Livro("Harry Potter", "JK Rowling")

l1.emprestar()
l4.emprestar()

biblioteca = Biblioteca([])

biblioteca.adicionar_livro(l1)
biblioteca.adicionar_livro(l2)
biblioteca.adicionar_livro(l3)
biblioteca.adicionar_livro(l4)

biblioteca.listar_livros()