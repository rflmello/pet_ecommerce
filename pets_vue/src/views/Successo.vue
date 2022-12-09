<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12" style="text-align: center">
                <h1 class="title" style="color: rgb(255, 102, 0)">Obrigado por escolher a PetStore!</h1>
                <p style="color: #48c774"> <b>Seu pedido será processado em até 24 horas</b></p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    nome: 'Sucesso',
    mounted() {
        document.title = 'PetStore'
    },
   
}
</script>