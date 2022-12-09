<template>
  <div class="home">
    <section class="hero is-medium is-success mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Bem vindo a PetStore! 🐾
            </p>
            <p class="subtitle">
                A loja online de itens para o bem-estar do seu Pet
            </p>
        </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Últimas novidades :)</h2>
      </div>

      <ProdutoBox 
        v-for="produto in ultimosProdutos"
        v-bind:key="produto.id"
        v-bind:produto="produto" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import ProdutoBox from '@/components/ProdutoBox'

export default {
  nome: 'PetStore',
  data() {
    return {
      ultimosProdutos: []
    }
  },
  components: {
    ProdutoBox
  },
  mounted() {
    this.getUltimosProdutos()

    document.title = 'PetStore'
  },
  methods: {
    async getUltimosProdutos() {
      this.$store.commit('setCarregando', true)

      await axios
        .get('/api/v1/latest-produtos/')
        .then(response => {
          this.ultimosProdutos = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setCarregando', false)
    }
  }
}
</script>
<style>

</style>