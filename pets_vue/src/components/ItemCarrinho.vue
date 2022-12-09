<template>
    <tr>
        <td><router-link :to="item.produto.get_url">{{ item.produto.nome }}</router-link></td>
        <td>R${{ item.produto.preco }}</td>
        <td>
            {{ item.quantidade }}
            <a @click="removeQuantidade(item)">-</a>
            <a @click="addQuantidade(item)">+</a>
        </td>
        <td>R${{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete" @click="removeItemCarrinho(item)"></button></td>
    </tr>
</template>

<script>
export default {
    nome: 'ItemCarrinho',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantidade * item.produto.preco
        },
        removeQuantidade(item) {
            item.quantidade -= 1

            if (item.quantidade === 0) {
                this.$emit('removeItemCarrinho', item)
            }

            this.updateCarrinho()
        },
        addQuantidade(item) {
            item.quantidade += 1

            this.updateCarrinho()
        },
        updateCarrinho() {
            localStorage.setItem('carrinho', JSON.stringify(this.$store.state.carrinho))
        },
        removeItemCarrinho(item) {
            this.$emit('removeItemCarrinho', item)

            this.updateCarrinho()
        },
    },
}
</script>