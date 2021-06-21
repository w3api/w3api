---
title: WebAssembly.compileStreaming()
permalink: /Javascript/WebAssembly/compileStreaming/
date: 2021-01-11
key: Javascript.W.WebAssembly
category: Javascript
tags: ['metodo javascript']
sidebar: 
  nav: javascript
---

{% include w3api/datos.html clase=site.data.Javascript.W.WebAssembly.metodos valor="compileStreaming" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~javascript
Promise<WebAssembly.Module> WebAssembly.compileStreaming(source);
~~~

## Parámetros
* **source**,  {% include w3api/param_description.html metodo=_dato parametro="source" %}

## Objeto Padre
[WebAssembly](/Javascript/WebAssembly/)

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
