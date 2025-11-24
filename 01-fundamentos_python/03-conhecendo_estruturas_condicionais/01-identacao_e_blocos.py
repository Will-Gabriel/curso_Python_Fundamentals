"""
Identar código é uma forma de manter o código fonte mais legível e manutenível.
Mas em Python ela exerce um segundo papel, através da indentação o interpretador
consegue determinar onde um bloco de comando inicia e onde termina.

As linguagens de programação constumam utilizar caracteres ou palavras reservadas
para determinar o início e fim do bloco. Em Java e C por exemplo, utilizamos chaves.
"""

# =========================================================================
print("====== Exemplo de Bloco em Java (funciona)  ======")
print("""
void sacar(double valor) {  // início do bloco do método
      
    if (this.saldo >= valor) { // início do bloco do if
        this.saldo -= valor;
      
    } // fim do bloco do if
} // fim do bloco do método
""")

# =========================================================================
print("\n====== Exemplo de Bloco em Java sem formatar (funciona)  ======")
print("""
void sacar(double valor) {  // início do bloco do método
if (this.saldo >= valor) { // início do bloco do if
this.saldo -= valor;
} // fim do bloco do if      
} // fim do bloco do método
""")

# =========================================================================
print("\n====== Exemplo de Bloco em Python (funciona)  ======")
print("""
def sacar(self, valor: float) -> None:  # início do bloco do método
            
    if self.saldo >= valor: # início do bloco do if
        self.saldo -= valor
    
    # fim do bloco do if
# fim do bloco do método
""")


# =========================================================================
print("\n====== Exemplo de Bloco em Python sem formatar (não funciona) ======")
print("""
def sacar(self, valor: float) -> None:  # início do bloco do método
if self.saldo >= valor: # início do bloco do if
self.saldo -= valor
# fim do bloco do if
# fim do bloco do método
""")