class Ser_vivo {
    public String genero;
    public String altura;
    // método constutor
    public Ser_vivo(String genero, float altura) {
        this.genero = genero;
        this.altura = altura;
    }
}

public class Humano extends Ser_vivo {
    String nome;
    String cpf;
    int idade;

    public Humano(String nome, String cpf, int idade, float altura) {
        super(genero, altura)
        this.nome = nome;
        this.cpf = cpf;
        this.idade = idade;
    }
}
