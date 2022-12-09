<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12" style="text-align:center">
                <h1 class="title" style="color: #48c774"><b>🐾 Minha conta </b></h1>
            </div>

            <div class="column is-12" style="text-align:center">
                <button @click="logout()" class="button is-danger">Sair</button>
            </div>

            <hr>

            <div class="column is-12">
                <h2 class="subtitle" style="color: rgb(255, 102, 0)"><b>Meus pedidos</b></h2>

                <ResumoPedido
                    v-for="pedido in pedidos"
                    v-bind:key="pedido.id"
                    v-bind:pedido="pedido" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import ResumoPedido from '@/components/ResumoPedido.vue'

export default {
    nome: 'MinhaConta',
    components: {
        ResumoPedido
    },
    data() {
        return {
            pedidos: []
        }
    },
    mounted() {
        document.title = 'PetStore'

        this.getMeusPedidos()
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')

            this.$router.push('/')
        },
        async getMeusPedidos() {
            this.$store.commit('setCarregando', true)

            await axios
                .get('/api/v1/pedidos/')
                .then(response => {
                    this.pedidos = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setCarregando', false)
        }
    }
}
</script>