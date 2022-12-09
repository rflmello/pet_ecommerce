import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import Home from '../views/Home.vue'

import Produto from '../views/Produto.vue'
import Categoria from '../views/Categoria.vue'
import Pesquisa from '../views/Pesquisa.vue'
import Carrinho from '../views/Carrinho.vue'
import Increver from '../views/Increver.vue'
import LogIn from '../views/LogIn.vue'
import MinhaConta from '../views/MinhaConta.vue'
import Confira from '../views/Confira.vue'
import Successo from '../views/Successo.vue'

const routes = [
  {
    path: '/',
    nome: 'Home',
    component: Home
  },
  {
    path: '/increver',
    nome: 'Increver',
    component: Increver
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/minha-conta',
    nome: 'MinhaConta',
    component: MinhaConta,
    meta: {
        requireLogin: true
    }
  },
  {
    path: '/pesquisa',
    nome: 'Pesquisa',
    component: Pesquisa
  },
  {
    path: '/carrinho',
    nome: 'Carrinho',
    component: Carrinho
  },
  {
    path: '/carrinho/sucesso',
    nome: 'Successo',
    component: Successo
  },
  {
    path: '/carrinho/confira',
    nome: 'Confira',
    component: Confira,
    meta: {
        requireLogin: true
    }
  },
  {
    path: '/:categoria_filtro/:produto_filtro',
    nome: 'Produto',
    component: Produto
  },
  {
    path: '/:categoria_filtro',
    nome: 'Categoria',
    component: Categoria
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
