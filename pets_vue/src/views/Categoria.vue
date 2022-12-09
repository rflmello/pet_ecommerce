<template>
    <div class="page-categoria">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ categoria.nome }}</h2>
            </div>

            <ProdutoBox 
                v-for="produto in categoria.produtos"
                v-bind:key="produto.id"
                v-bind:produto="produto" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

import ProdutoBox from '@/components/ProdutoBox'

export default {
    nome: 'Categoria',
    components: {
        ProdutoBox
    },
    data() {
        return {
            categoria: {
                produtos: []
            }
        }
    },
    mounted() {
        this.getCategoria()
    },
    watch: {
        $route(to, from) {
            if (to.nome === 'Categoria') {
                this.getCategoria()
            }
        }
    },
    watch: {
        "$route.params.categoria_filtro"(val){
                this.getCategoria()
        }
    },
    methods: {
        async getCategoria() {
            const categoriaFiltro = this.$route.params.categoria_filtro

            this.$store.commit('setCarregando', true)

            axios
                .get(`/api/v1/produtos/${categoriaFiltro}/`)
                .then(response => {
                    this.categoria = response.data

                    document.title = this.categoria.nome + ' |' + ' PetStore'
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: 'Algo deu errado. Por favor, tente novamente.',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })

            this.$store.commit('setCarregando', false)
        }
    }
}
</script>