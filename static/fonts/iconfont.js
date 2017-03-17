;(function(window) {

  var svgSprite = '<svg>' +
    '' +
    '<symbol id="icon-saoyisao" viewBox="0 0 1024 1024">' +
    '' +
    '<path d="M83.872223 494.160703l856.255555 0 0 35.677571-856.255555 0 0-35.677571Z"  ></path>' +
    '' +
    '<path d="M940.127777 404.968311l0-267.533173c0-29.581736-23.794939-53.562916-53.562916-53.562916L636.870985 83.872223l0 71.355141L842.10323 155.227364c14.879895 0 26.669406 11.939937 26.669406 26.669406l0 223.071541L940.127777 404.968311z"  ></path>' +
    '' +
    '<path d="M940.127777 619.031689l0 267.533173c0 29.767977-23.981181 53.562916-53.562916 53.562916L636.870985 940.127777l0-71.354118L842.10323 868.773659c14.729469 0 26.669406-11.789511 26.669406-26.669406L868.772636 619.031689 940.127777 619.031689z"  ></path>' +
    '' +
    '<path d="M83.872223 404.968311l0-267.533173c0-29.767977 23.981181-53.562916 53.562916-53.562916l249.694899 0 0 71.355141L181.895747 155.227364c-14.729469 0-26.669406 11.789511-26.669406 26.669406l0 223.071541L83.872223 404.968311z"  ></path>' +
    '' +
    '<path d="M83.872223 619.031689l0 267.533173c0 29.581736 23.794939 53.562916 53.562916 53.562916l249.694899 0 0-71.354118L181.895747 868.773659c-14.879895 0-26.669406-11.939937-26.669406-26.669406L155.226341 619.031689 83.872223 619.031689z"  ></path>' +
    '' +
    '</symbol>' +
    '' +
    '</svg>'
  var script = function() {
    var scripts = document.getElementsByTagName('script')
    return scripts[scripts.length - 1]
  }()
  var shouldInjectCss = script.getAttribute("data-injectcss")

  /**
   * document ready
   */
  var ready = function(fn) {
    if (document.addEventListener) {
      if (~["complete", "loaded", "interactive"].indexOf(document.readyState)) {
        setTimeout(fn, 0)
      } else {
        var loadFn = function() {
          document.removeEventListener("DOMContentLoaded", loadFn, false)
          fn()
        }
        document.addEventListener("DOMContentLoaded", loadFn, false)
      }
    } else if (document.attachEvent) {
      IEContentLoaded(window, fn)
    }

    function IEContentLoaded(w, fn) {
      var d = w.document,
        done = false,
        // only fire once
        init = function() {
          if (!done) {
            done = true
            fn()
          }
        }
        // polling for no errors
      var polling = function() {
        try {
          // throws errors until after ondocumentready
          d.documentElement.doScroll('left')
        } catch (e) {
          setTimeout(polling, 50)
          return
        }
        // no errors, fire

        init()
      };

      polling()
        // trying to always fire before onload
      d.onreadystatechange = function() {
        if (d.readyState == 'complete') {
          d.onreadystatechange = null
          init()
        }
      }
    }
  }

  /**
   * Insert el before target
   *
   * @param {Element} el
   * @param {Element} target
   */

  var before = function(el, target) {
    target.parentNode.insertBefore(el, target)
  }

  /**
   * Prepend el to target
   *
   * @param {Element} el
   * @param {Element} target
   */

  var prepend = function(el, target) {
    if (target.firstChild) {
      before(el, target.firstChild)
    } else {
      target.appendChild(el)
    }
  }

  function appendSvg() {
    var div, svg

    div = document.createElement('div')
    div.innerHTML = svgSprite
    svgSprite = null
    svg = div.getElementsByTagName('svg')[0]
    if (svg) {
      svg.setAttribute('aria-hidden', 'true')
      svg.style.position = 'absolute'
      svg.style.width = 0
      svg.style.height = 0
      svg.style.overflow = 'hidden'
      prepend(svg, document.body)
    }
  }

  if (shouldInjectCss && !window.__iconfont__svg__cssinject__) {
    window.__iconfont__svg__cssinject__ = true
    try {
      document.write("<style>.svgfont {display: inline-block;width: 1em;height: 1em;fill: currentColor;vertical-align: -0.1em;font-size:16px;}</style>");
    } catch (e) {
      console && console.log(e)
    }
  }

  ready(appendSvg)


})(window)