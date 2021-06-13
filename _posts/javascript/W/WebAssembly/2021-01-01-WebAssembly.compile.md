---
title: WebAssembly.compile()
permalink: /Javascript/WebAssembly/compile/
date: 2021-01-11
key: Javascript.W.WebAssembly
category: Javascript
tags: ['metodo javascript']
sidebar: 
  nav: javascript
---

{% include w3api/datos.html clase=site.data.Javascript.W.WebAssembly.metodos valor="compile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~javascript
Promise<WebAssembly.Module> WebAssembly.compile(bufferSource);
~~~

## Parámetros
* **bufferSource**,  {% include w3api/param_description.html metodo=_dato parametro="bufferSource" %}

## Objeto Padre
[WebAssembly](/Javascript/WebAssembly/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
