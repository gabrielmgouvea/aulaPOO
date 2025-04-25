//Questão 4
package java;

class CadastroPessoa;
    public String nome;
    public String cpf;
    public String profissao;
    public String endereco;


public CadastroPessoa(String nome, String cpf, String profissao, String endereco) {
    this.nome = nome;
    this.cpf = cpf;
    this.profissao = profissao;
    this.endereco = endereco;
}


public void apresentar() {
    System.out.println("Nome: " + nome + "CPF: " + cpf + "Profissão: " + profissao + "Endereço: " + endereco)

}

public static void main(String args) {
    CadastroPessoa pessoa = NovaPessoa
    CadastroPessoa("Gabriel", "1234567890", "Programador/Engenheiro de Software", "Rua Das Flores - 123 - RJ");
    pessoa.apresentar();
}