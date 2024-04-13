---
title: Generator.throw()
permalink: /Javascript/Generator/throw/
date: 2021-01-11
key: Javascript.G.Generator
category: Javascript
tags: ['metodo javascript']
sidebar: 
  nav: javascript
---

{% include w3api/datos.html clase=site.data.Javascript.G.Generator.metodos valor="throw" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~javascript
gen.throw(exception)
~~~

## Parámetros
* **exception**,  {% include w3api/param_description.html metodo=_dato parametro="exception" %}

## Objeto Padre
[Generator](/Javascript/Generator/)

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
