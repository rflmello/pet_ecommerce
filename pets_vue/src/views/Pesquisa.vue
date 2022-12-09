<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Pesquisa</h1>

                <h2 class="is-size-5 has-text-grey">Pesquisa: "{{ query }}"</h2>
            </div>

            <ProdutoBox 
                v-for="produto in produtos"
                v-bind:key="produto.id"
                v-bind:produto="produto" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ProdutoBox from '@/components/ProdutoBox.vue'

export default {
    nome: 'Pesquisa',
    components: {
        ProdutoBox
    },
    data() {
        return {
            produtos: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'PetStore'

        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')

            this.pPesquisa()
        }
    },
    methods: {
        async pPesquisa() {
            this.$store.commit('setCarregando', true)

            await axios
                .post('/api/v1/produtos/pesquisa/', {'query': this.query})
                .then(response => {
                    this.produtos = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setCarregando', false)
        }
    }
}
</script>