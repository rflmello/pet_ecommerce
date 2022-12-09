<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Confira</h1>
            </div>

            <div class="column is-12 box">
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
                            v-for="item in carrinho.items"
                            v-bind:key="item.produto.id"
                        >
                            <td>{{ item.produto.nome }}</td>
                            <td>R${{ item.produto.preco }}</td>
                            <td>{{ item.quantidade }}</td>
                            <td>R${{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>

                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ tamanhoTotalCarrinho }}</td>
                            <td>R${{ carrinhoTotalPreco.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle" style="color:#FF5C05">Detalhes de envio</h2>
                
                <p class="has-text-grey mb-4">Todos os campos são necessários!</p>
                
                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <hr>
                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>CEP*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="cep">
                            </div>
                        </div>
    
                        <div class="field">
                            <label>Rua*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="rua">
                            </div>
                        </div>
    
                        <div class="field">
                            <label>Número*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="numero">
                            </div>
                        </div>
    
                        <div class="field">
                            <label>Complemento*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="complemento">
                            </div>
                        </div>
    
                        <div class="field">
                            <label>Bairro*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="bairro">
                            </div>
                        </div>
    
                        <div class="field">
                            <label>Cidade*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="cidade">
                            </div>
                        </div>
    
                        <div class="field">
                            <label>Estado*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="estado">
                            </div>
                        </div>
                </div>
                    <div class="column is-6">
                        <div class="field">
                            <label>Primeiro nome*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="primeiro_nome">
                            </div>
                        </div>

                        <div class="field">
                            <label>Segundo nome*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="segundo_nome">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label>Telefone*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="telefone">
                            </div>
                        </div>
                    </div>
                </div>
                </div>


                <div id="card-element" class="mb-5"></div>

                <template v-if="(tamanhoTotalCarrinho > 0)">
                    <hr>
                    <button class="button is-dark" @click="submitForm" style="background-color: #FF5C05; width: 120%">Pagar</button>
                </template>
            </div>
        </div>
    
</template>

<script>
import axios from 'axios'
export default {
    nome: 'Confira',
    data() {
        return {
            carrinho: {
                items: []
            },
            primeiro_nome: '',
            segundo_nome: '',
            email: '',
            telefone: '',
            cep: '',
            rua: '',
            numero: '',
            complemento: '',
            bairro: '',
            cidade: '',
            estado: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'PetStore'

        this.carrinho = this.$store.state.carrinho

    },
    methods: {
        getItemTotal(item) {
            return item.quantidade * item.produto.preco
        },
        submitForm() {
            this.errors = []

            if (this.primeiro_nome === '') {
                this.errors.push('Informe o primeiro nome!')
            }

            else if (this.segundo_nome === '') {
                this.errors.push('Informe o segundo nome!')
            }

            else if (this.email === '') {
                this.errors.push('Informe seu e-mail!')
            }

            else if (this.telefone === '') {
                this.errors.push('Informe seu telefone!')
            }
            else if (this.cep === '') {
                this.errors.push('Informe seu CEP!')
            }

            else if (this.rua === '') {
                this.errors.push('Informe sua rua!')
            }

            else if (this.numero === '') {
                this.errors.push('Informe seu numero!')
            }

            else if (this.complemento === '') {
                this.errors.push('Informe o complemento!')
            }

            else if (this.bairro === '') {
                this.errors.push('Informe seu bairro!')
            }

            else if (this.cidade === '') {
                this.errors.push('Informe sua cidade!')
            }

            else if (this.estado === '') {
                this.errors.push('Informe seu estado!')
            }

            else if (!this.errors.length) {
                this.$store.commit('setCarregando', true)
                 this.token()               
            }
            
        },
        async token() {
            const items = []
            
            for (let i = 0; i < this.carrinho.items.length; i++) {
                const item = this.carrinho.items[i]
                const obj = {
                    produto: item.produto.id,
                    preco: item.produto.preco * item.quantidade,
                    quantidade: item.quantidade
                }
                
                items.push(obj)
            }
            
            const data = {
                'primeiro_nome': this.primeiro_nome,
                'segundo_nome': this.segundo_nome,
                'email': this.email,
                'cep': this.cep,
                'rua': this.rua,
                'numero': this.numero,
                'complemento': this.complemento,
                'bairro': this.bairro,
                'cidade': this.cidade,
                'estado': this.estado,
                'telefone': this.telefone,
                'items': items,
                // 'user': this.token.id
            }
            
            await axios
            .post('/api/v1/confira/', data) 
            .then(response => {
                this.$router.push('/carrinho/sucesso')
                this.$store.commit('limparCarrinho')
            })
            .catch(error => {
                this.errors.push('Algo deu errado. Por favor, tente novamente')
                
                console.log(error)
            })
            
            this.$store.commit('setCarregando', false)
            this.$store.commit('limparCarrinho')
        }
    },
    computed: {
        carrinhoTotalPreco() {
            return this.carrinho.items.reduce((vf, vp) => {
                return vf += vp.produto.preco * vp.quantidade
            }, 0)
        },
        tamanhoTotalCarrinho() {
            console.log(this.carrinho.items)
            return this.carrinho.items.reduce((vf, vp) => {
                return vf += vp.quantidade
            }, 0)
        }
    }
}
</script>