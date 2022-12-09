<template>
  <div id="wrapper">
    <nav class="navbar is-info">
      <div class="navbar-brand">

        <router-link to="/" class="navbar-logo"><img src="../src/assets/logo.png" alt="Avatar Logo" style="width:100px; margin-left:15%;"> </router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/pesquisa">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="O que você está procurando?" name="query">
                </div>

                <div class="control">
                  <button class="button is-success">
                      <span class="icon">
                      <i class="fas fa-search"></i>
                      </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>

        <div class="navbar-end">
          <router-link to="/" class="navbar-item">
            <span class="icon"><i class="fas fa-home"></i></span>
            <span>  Início</span>
          </router-link>

          <router-link to="/cachorro" class="navbar-item">
            <span class="icon"><i class="fas fa-dog"></i></span>
            <span> Cachorros</span>
          </router-link>

          <router-link to="/gato" class="navbar-item">
            <span class="icon"><i class="fas fa-cat"></i></span>
            <span> Gatos</span>
          </router-link>

          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/minha-conta" class="botao button is-light">
                  <span class="icon"><i class="fas fa-paw"></i></span>
                  <span>Minha conta</span>
                </router-link>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-light">Login</router-link>
              </template>

              <router-link to="/carrinho" class="botao button is-success" style="background-color: #FF5C05">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Carrinho ({{ tamanhoTotalCarrinho }})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <router-view/>
    </section>
    <br><br>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,
      carrinho: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('iniciarReserva')
    
    const token = this.$store.state.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    document.title = 'PetStore'
    this.carrinho = this.$store.state.carrinho
  },
  computed: {
      tamanhoTotalCarrinho() {
          let tamanhoTotal = 0

          for (let i = 0; i < this.carrinho.items.length; i++) {
            tamanhoTotal += this.carrinho.items[i].quantidade
          }

          return tamanhoTotal
      }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
.botao {
  background-color: rgb(255, 102, 0);
}
body {
  background-color: #cdedffa8;
  font-family: Arial, Helvetica, sans-serif;
}
</style>
