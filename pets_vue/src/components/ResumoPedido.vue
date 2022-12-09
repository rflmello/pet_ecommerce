<template>
    <div class="box mb-4">
        <h3 class="is-size-4 mb-6">Número do Pedido #<b>{{ pedido.id }}</b></h3>

        <h4 class="is-size-5">Produtos</h4>

        <table class="table is-fullwidth">
            <thead>
                <tr>
                    <th>Produto</th>
                    <th>Preço</th>
                    <th>Quantidade</th>
                    <th>Total</th>
                </tr>
            </thead>

            <tbody>
                <tr
                    v-for="item in pedido.items"
                    v-bind:key="item.produto.id"
                >
                    <td>{{ item.produto.nome }}</td>
                    <td>R${{ item.produto.preco }}</td>
                    <td>{{ item.quantidade }}</td>
                    <td>R${{ getItemTotal(item).toFixed(2) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    nome: 'ResumoPedido',
    props: {
        pedido: Object
    },
    methods: {
        getItemTotal(item) {
            return item.quantidade * item.produto.preco
        },
        TanhoTotalPedido(pedido) {
            return pedido.items.reduce((vf, vp) => {
                return vf += vp.quantidade
            }, 0)
        },
    }
}
</script>