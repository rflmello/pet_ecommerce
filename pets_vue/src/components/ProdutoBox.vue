<template>
    <div class="column is-3">
        <div class="box">
            <figure class="imagem mb-4">
                <img v-bind:src="produto.get_imagem_pequena">
            </figure>

            <h3 class="is-size-4">{{ produto.nome }}</h3>
            <p class="is-size-6 has-text-grey">R${{ produto.preco }}</p>

            <router-link v-bind:to="produto.get_url" class="button is-info mt-4" style="background-color: #FF5C05; width: 100%">Ver detalhes</router-link>
        </div>
    </div>
</template>

<script>
export default {
    nome: 'ProdutoBox',
    props: {
        produto: Object
    }
}
</script>

<style scoped>
  .imagem {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>