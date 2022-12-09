import { createStore } from 'vuex'

export default createStore({
  state: {
    carrinho: {
        items: [],
    },
    isAuthenticated: false,
    token: '',
    isLoading: false
  },
  mutations: {
    iniciarReserva(state) {
      if (localStorage.getItem('carrinho')) {
        state.carrinho = JSON.parse(localStorage.getItem('carrinho'))
      } else {
        localStorage.setItem('carrinho', JSON.stringify(state.carrinho))
      }

      if (localStorage.getItem('token')) {
          state.token = localStorage.getItem('token')
          state.isAuthenticated = true
      } else {
          state.token = ''
          state.isAuthenticated = false
      } 
    },
    addCarrinho(state, item) {
      const exists = state.carrinho.items.filter(i => i.produto.id === item.produto.id)
      if (exists.length) {
        exists[0].quantidade = parseInt(exists[0].quantidade) + parseInt(item.quantidade)
      } else {
        state.carrinho.items.push(item)
      }

      localStorage.setItem('carrinho', JSON.stringify(state.carrinho))
    },
    setCarregando(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
        state.token = token
        state.isAuthenticated = true
    },  
    removeToken(state) {
        state.token = ''
        state.isAuthenticated = false
    },
    limparCarrinho(state) {
      state.carrinho = { items: [] }

      localStorage.setItem('carrinho', JSON.stringify(state.carrinho))
    },
  },
  actions: {
  },
  modules: {
  }
})
