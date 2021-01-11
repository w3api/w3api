---
title: WebAssembly.instantiate()
permalink: Javascript/WebAssembly/instantiate
date: 2021-01-11
key: JavascriptJavascript.W.WebAssembly
category: javascript
tags: ['metodo javascript']
sidebar: 
  nav: javascript
---

{% include w3api/datos.html clase=site.data.Javascript.W.WebAssembly.metodos valor="instantiate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~javascript
Promise<ResultObject> WebAssembly.instantiate(bufferSource, importObject);
~~~

## Parámetros
* **bufferSource**,  {% include w3api/param_description.html metodo=_dato parametro="bufferSource" %}
* **importObject**,  {% include w3api/param_description.html metodo=_dato parametro="importObject" %}

## Objeto Padre
[WebAssembly](/javascript/WebAssembly/)

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
