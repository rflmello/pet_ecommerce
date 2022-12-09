<template>
    <div class="page-produto">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="imagem mb-6">
                    <img v-bind:src="produto.get_imagem">
                </figure>
            </div>
            
            <div class="column is-3">
                <h1 class="title" style="color:#FF5C05">{{ produto.nome }}</h1>

                <h1 class="subtitle">Informações</h1>
                <p><strong>Descrição:</strong> {{ produto.descricao }}</p>

                <p><strong>Preço: </strong>R${{ produto.preco }}</p>

                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantidade">
                    </div>

                    <div class="control">
                        <a class="button is-success" @click="addCarrinho()">+ Adicionar ao carrinho</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    nome: 'Produto',
    data() {
        return {
            produto: {},
            quantidade: 1
        }
    },
    mounted() {
        this.getProduto() 
    },
    methods: {
        async getProduto() {
            this.$store.commit('setCarregando', true)

            const categoria_filtro = this.$route.params.categoria_filtro
            const produto_filtro = this.$route.params.produto_filtro

            await axios
                .get(`/api/v1/produtos/${categoria_filtro}/${produto_filtro}`)
                .then(response => {
                    this.produto = response.data

                    document.title = this.produto.nome + ' |' + 'PetStore'
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setCarregando', false)
        },
        addCarrinho() {
            if (isNaN(this.quantidade) || this.quantidade < 1) {
                this.quantidade = 1
            }

            const item = {
                produto: this.produto,
                quantidade: this.quantidade
            }

            this.$store.commit('addCarrinho', item)

            toast({
                message: 'O produto foi adicionado ao carrinho',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
    }
}
</script>