<template>
    <div class="nanum container">
      <h3>상품 상세정보</h3>

      <hr>
      <p>은행이름 : {{ product.kor_co_nm }}</p>
      <p>예금이름 : {{ product.fin_prdt_nm }}</p>
      <p>가입기간 : {{ product.etc_note }}</p>
      <p>가입대상 : {{ product.join_member }}</p>
      <p>가입방법 : {{ product.join_way }}</p>
      <p> {{product.spcl_cnd}} </p>
      <hr>
    <button class="btn btn-primary" :class="{ 'btn-danger': isSubscribed }" @click="forSubscription" v-if="$store.state.username !== null">
      {{ isSubscribed ? '즐겨찾기 취소' : '상품 즐겨찾기' }}
    </button>
    <br><br><br><br><br><br><br><br><br><br><br><br><br>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  const API_URL = 'http://127.0.0.1:8000'
  
  export default {
      name : 'ProductDetailView',
  
      computed: {
      isSubscribed() {
        return this.$store.state.isSub;
          },
      options() {
        return this.$store.state.options
          },
      },
      data() {
          return {
              product : null
          }
      }, // 끝
      created() {
          this.getProductDetail()
          this.checkSubscription()
      }, //끝
      methods: {
          getProductDetail() {
          axios({
              method: 'get',
              url: `${API_URL}/products/deposit-products/${this.$route.params.id}/`,
          })
          .then((res) => {
              console.log(res)
              this.product = res.data
              this.$store.state.productId = this.product.id
          })
          .catch((err) => {
              console.log(err)
          })
          },
          checkSubscription() {
            this.$store.dispatch('checkSub')
            },
          forSubscription() {
            const Config = {
            headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${this.$store.state.token}`,
            },
            };
            axios.post(`${API_URL}/products/${this.$route.params.id}/subscription/`, null, Config)
            .then((res) => {
              alert(res.data.message);
              this.checkSubscription()
              this.isSubscribed = !this.isSubscribed;
            })
          },
      }
  }
        
  </script>
  
  
  <style>
  
  
  </style>