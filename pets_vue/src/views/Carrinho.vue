<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Carrinho</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth" v-if="tamanhoTotalCarrinho">
                    <thead>
                        <tr>
                            <th>Produto</th>
                            <th>Preço</th>
                            <th>Quantidade</th>
                            <th>Total</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <ItemCarrinho
                            v-for="item in carrinho.items"
                            v-bind:key="item.produto.id"
                            v-bind:initialItem="item"
                            v-on:removeItemCarrinho="removeItemCarrinho" />
                    </tbody>
                </table>

                <p v-else style="color:#FF5C05">Você não tem nenhum produto em seu carrinho ainda...</p>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle" style="color:#48c774"><b>Resumo do Carrinho</b></h2>

                <strong>R${{ precoTotalCarrinho.toFixed(2) }}</strong> - Total de {{ tamanhoTotalCarrinho }} itens

                <hr>

                <router-link to="/carrinho/confira" class="button is-dark" style="background-color: #FF5C05; width: 100%">Finalizar compra</router-link>
            </div>
        </div>
    </div>
</template>

<script>

import ItemCarrinho from '@/components/ItemCarrinho.vue'

export default {
    nome: 'Carrinho',
    components: {
        ItemCarrinho
    },
    data() {
        return {
            carrinho: {
                items: []
            }
        }
    },
    mounted() {
        this.carrinho = this.$store.state.carrinho
        if (this.tamanhoTotalCarrinho > 0) {

        }
    },
    
    methods: {
        removeItemCarrinho(item) {
            this.carrinho.items = this.carrinho.items.filter(i => i.produto.id !== item.produto.id)
        }
    },
    computed: {
        tamanhoTotalCarrinho() {
            return this.carrinho.items.reduce((acc, curVal) => {
                return acc += curVal.quantidade
            }, 0)
        },
        precoTotalCarrinho() {
            return this.carrinho.items.reduce((vf, vp) => {
                return vf += vp.produto.preco * vp.quantidade
            }, 0)
        },
    }
}
</script>