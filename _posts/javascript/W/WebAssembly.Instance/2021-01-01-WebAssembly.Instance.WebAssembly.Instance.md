---
title: WebAssembly.Instance.WebAssembly.Instance()
permalink: /Javascript/WebAssembly/Instance/WebAssembly/Instance/
date: 2021-01-11
key: Javascript.W.WebAssembly.Instance
category: Javascript
tags: ['constructor javascript']
sidebar: 
  nav: javascript
---

{% include w3api/datos.html clase=site.data.Javascript.W.WebAssembly.Instance.constructores valor="WebAssembly.Instance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~javascript
new WebAssembly.Instance(module, importObject);
~~~

## Parámetros
* **module**,  {% include w3api/param_description.html metodo=_dato parametro="module" %}
* **importObject**,  {% include w3api/param_description.html metodo=_dato parametro="importObject" %}

## Objeto Padre
[WebAssembly.Instance](/Javascript/WebAssembly/Instance/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
