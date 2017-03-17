;(function(window) {

  var svgSprite = '<svg>' +
    '' +
    '<symbol id="icon-saomadenglu01" viewBox="0 0 1024 1024">' +
    '' +
    '<path d="M894.428969 894.295939 894.428969 835.365782 835.499835 835.365782Z"  ></path>' +
    '' +
    '<path d="M187.258894 187.125865 334.587358 187.126888 334.587358 334.453305 393.517515 393.383462 393.517515 128.196731 128.32976 128.196731Z"  ></path>' +
    '' +
    '<path d="M894.426923 658.57224 835.496765 658.57224 835.497788 599.642083 629.241214 599.642083 629.241214 629.108185 688.170349 688.037319 688.170349 658.57224 747.100506 658.57224 747.100506 717.502397 717.635427 717.502397 835.496765 835.363735 835.496765 776.433578 894.426923 776.433578Z"  ></path>' +
    '' +
    '<path d="M305.121256 304.987203 305.121256 216.590943 216.727043 216.590943Z"  ></path>' +
    '' +
    '<path d="M452.448696 128.196731l58.929134 0 0 58.930157-58.929134 0 0-58.930157Z"  ></path>' +
    '' +
    '<path d="M629.241214 128.195707 629.241214 393.382439l265.187755 0L894.428969 128.195707 629.241214 128.195707zM835.497788 334.453305l-147.325393 0L688.172395 187.126888l147.325393 0L835.497788 334.453305z"  ></path>' +
    '' +
    '<path d="M717.637474 216.591967l88.396259 0 0 88.396259-88.396259 0 0-88.396259Z"  ></path>' +
    '' +
    '<path d="M658.706293 570.175981 658.706293 511.245823 717.637474 511.245823 717.637474 452.315666 570.30901 452.315666 570.30901 363.921453 511.379876 363.921453 511.379876 452.315666 452.450742 452.315666 511.379876 511.245823 570.30901 511.245823 570.30901 570.175981Z"  ></path>' +
    '' +
    '<path d="M511.379876 304.987203 570.30901 304.987203 570.30901 187.125865 511.379876 187.125865 511.379876 246.057045 452.449719 246.057045 452.449719 363.918383 511.379876 363.918383Z"  ></path>' +
    '' +
    '<path d="M835.497788 452.314643 776.567631 452.314643 776.567631 511.245823 717.638497 511.245823 717.638497 570.175981 894.428969 570.175981 894.428969 511.245823 835.499835 511.245823Z"  ></path>' +
    '' +
    '</symbol>' +
    '' +
    '<symbol id="icon-pclogin" viewBox="0 0 1024 1024">' +
    '' +
    '<path d="M1024 936.228571v87.771429l-87.771429-87.771429h87.771429z m-175.542857-146.285714v58.514286l-146.285714-146.285714h234.057142v-614.4h-848.457142l-87.771429-87.771429h1024v789.942857h-175.542857z m0-175.542857h-234.057143l-438.857143-438.857143h672.914286v438.857143z" fill="#00B4CC" ></path>' +
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