/**
 * WEBSITE: https://themefisher.com
 * TWITTER: https://twitter.com/themefisher
 * FACEBOOK: https://www.facebook.com/themefisher
 * GITHUB: https://github.com/themefisher/
 */

(function ($) {
  'use strict';

  /* ========================================================================= */
  /*	Page Preloader
  /* ========================================================================= */
  $(window).on('load', function () {
    $('#preloader').fadeOut('slow', function () {
      $(this).remove();
    });
  });


  // navbarDropdown
	if ($(window).width() < 992) {
		$('#navigation .dropdown-toggle').on('click', function () {
			$(this).siblings('.dropdown-menu').animate({
				height: 'toggle'
			}, 300);
		});
  }
  
  //Hero Slider
  $('.hero-slider').slick({
    autoplay: true,
    infinite: true,
    arrows: true,
    prevArrow: '<button type=\'button\' class=\'prevArrow\'></button>',
    nextArrow: '<button type=\'button\' class=\'nextArrow\'></button>',
    dots: false,
    autoplaySpeed: 7000,
    pauseOnFocus: false,
    pauseOnHover: false
  });
  $('.hero-slider').slickAnimation();

  /* ========================================================================= */
  /*	Portfolio Filtering Hook
  /* =========================================================================  */
  // filter
  setTimeout(function(){
    var containerEl = document.querySelector('.filtr-container');
    var filterizd;
    if (containerEl) {
      filterizd = $('.filtr-container').filterizr({});
    }
  }, 500);

  /* ========================================================================= */
  /*	Testimonial Carousel
  /* =========================================================================  */
  //Init the slider
  $('.testimonial-slider').slick({
    infinite: true,
    arrows: false,
    autoplay: true,
    autoplaySpeed: 2000
  });


  /* ========================================================================= */
  /*	Clients Slider Carousel
  /* =========================================================================  */
  //Init the slider
  $('.clients-logo-slider').slick({
    infinite: true,
    arrows: false,
    autoplay: true,
    autoplaySpeed: 2000,
    slidesToShow: 5,
    slidesToScroll: 1,
    responsive: [{
      breakpoint: 1024,
      settings: {
        slidesToShow: 4,
        slidesToScroll: 1,
        infinite: true,
        dots: false
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        arrows: false
      }
    }
    ]
  });

  /* ========================================================================= */
  /*	Company Slider Carousel
  /* =========================================================================  */
  $('.company-gallery').slick({
    infinite: true,
    arrows: false,
    autoplay: true,
    autoplaySpeed: 2000,
    slidesToShow: 5,
    slidesToScroll: 1,
    responsive: [{
      breakpoint: 1024,
      settings: {
        slidesToShow: 4,
        slidesToScroll: 1,
        infinite: true,
        dots: false
      }
    },
    {
      breakpoint: 667,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        arrows: false
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        arrows: false
      }
    }
    ]
  });

  /* ========================================================================= */
  /*	On scroll fade/bounce effect
  /* ========================================================================= */
  var scroll = new SmoothScroll('a[href*="#"]');

  // -----------------------------
  //  Count Up
  // -----------------------------
  function counter() {
    var oTop;
    if ($('.counter').length !== 0) {
      oTop = $('.counter').offset().top - window.innerHeight;
    }
    if ($(window).scrollTop() > oTop) {
      $('.counter').each(function () {
        var $this = $(this),
          countTo = $this.attr('data-count');
        $({
          countNum: $this.text()
        }).animate({
          countNum: countTo
        }, {
          duration: 1000,
          easing: 'swing',
          step: function () {
            $this.text(Math.floor(this.countNum));
          },
          complete: function () {
            $this.text(this.countNum);
          }
        });
      });
    }
  }
  // -----------------------------
  //  On Scroll
  // -----------------------------
  $(window).scroll(function () {
    counter();

    var scroll = $(window).scrollTop();
    if (scroll > 50) {
      $('.navigation').addClass('sticky-header');
    } else {
      $('.navigation').removeClass('sticky-header');
    }
  });

  // 表单提交处理
  document.addEventListener('DOMContentLoaded', function() {
    // 首先创建提示框
    const alertDiv = document.createElement('div');
    alertDiv.className = 'floating-alert';
    alertDiv.innerHTML = `
      <div class="alert-content">
        <i class="fas fa-check-circle"></i>
        <p>提交成功！我们会尽快与您联系。</p>
        <button class="alert-confirm">确认</button>
      </div>
    `;
    document.body.appendChild(alertDiv);

    const form = document.getElementById('downloadForm');
    if (form) {
      form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData.entries());
        
        try {
          // 构造模拟的 Shopify 订单数据
          const mockShopifyOrder = {
            id: Date.now(),
            email: data.email,
            financial_status: "paid",
            confirmed: true,
            test: true,
            processed_at: new Date().toISOString(),
            created_at: new Date().toISOString(),
            updated_at: new Date().toISOString(),
            currency: "USD",
            total_price: "0.00",
            customer: {
              email: data.email,
              first_name: data.name || "Test",
              last_name: "User",
              state: "enabled",
              verified_email: true
            },
            line_items: [
              {
                id: Date.now(),
                quantity: 1,
                name: "Rope-Live Stellar: Enhanced AI Live Streaming Tool with Multi-Platform Support - 3-Day Trial",
                price: "0.00",
                sku: "PRO-1D",
                product_id: 8801307623638,
                variant_id: 46356797063382,
                title: "Rope-Live Stellar: Enhanced AI Live Streaming Tool with Multi-Platform Support",
                variant_title: "1-Day Trial",
                vendor: "Rope-Live",
                requires_shipping: false,
                taxable: false,
                gift_card: false
              }
            ]
          };

          console.log('Sending webhook request:', mockShopifyOrder);

          // 发送到webhook服务器
          console.log('Form submitted');
          console.log('Form data:', data);
          console.log('Request options:', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(mockShopifyOrder)
          });

          const webhookResponse = await fetch('https://licensemanager.ai-yy.com/shopify/webhook/order/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(mockShopifyOrder)
          });

          console.log('Response status:', webhookResponse.status);
          const responseText = await webhookResponse.text();
          console.log('Response text:', responseText);

          if (webhookResponse.ok) {
            // 显示悬浮提示
            alertDiv.classList.add('show');
            
            // 清空表单
            e.target.reset();
            // 关闭模态框
            $('#downloadModal').modal('hide');

            // 点击确认按钮后跳转
            const confirmBtn = alertDiv.querySelector('.alert-confirm');
            confirmBtn.addEventListener('click', function() {
              alertDiv.classList.remove('show');
              window.location.href = 'https://pan.baidu.com/s/15TcjRMjhUjkyrhK4ROMpsg?pwd=39bv';
            });
          } else {
            throw new Error('订单处理失败');
          }
        } catch (error) {
          console.error('Error:', error);
          alert('提交失败，请稍后重试。');
        }
      });
    }
  });

})(jQuery);

// 监听滚动事件
window.addEventListener('scroll', function() {
  const nav = document.querySelector('.navigation');
  const logoDefault = document.querySelector('.logo-default');
  const logoWhite = document.querySelector('.logo-white');
  
  if (window.scrollY > 50) {
    nav.classList.remove('top');
    nav.classList.add('scrolled');
    logoDefault.style.display = 'block';
    logoWhite.style.display = 'none';
  } else {
    nav.classList.add('top');
    nav.classList.remove('scrolled');
    logoDefault.style.display = 'none';
    logoWhite.style.display = 'block';
  }
});

// 页面加载时初始化导航栏状态
document.addEventListener('DOMContentLoaded', function() {
  const nav = document.querySelector('.navigation');
  const logoDefault = document.querySelector('.logo-default');
  const logoWhite = document.querySelector('.logo-white');
  
  nav.classList.add('top');
  
  // 触发一次滚动检查
  if (window.scrollY > 50) {
    nav.classList.remove('top');
    nav.classList.add('scrolled');
    logoDefault.style.display = 'block';
    logoWhite.style.display = 'none';
  } else {
    logoDefault.style.display = 'none';
    logoWhite.style.display = 'block';
  }
});

// 添加版本切换的初始化和事件处理
$(document).ready(function() {
  // 初始化标签页
  $('#basic').addClass('show active');
  
  // 为版本切换按钮添加点击事件
  $('.btn-version').on('click', function(e) {
    e.preventDefault();
    
    // 移除所有按钮的 active 类
    $('.btn-version').removeClass('active');
    // 为当前点击的按钮添加 active 类
    $(this).addClass('active');
    
    // 获取目标面板
    const target = $(this).data('target');
    
    // 隐藏所有面板
    $('.tab-pane').removeClass('show active');
    // 显示目标面板
    $(target).addClass('show active');
  });
});