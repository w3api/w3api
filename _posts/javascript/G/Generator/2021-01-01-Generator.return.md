---
title: Generator.return()
permalink: /Javascript/Generator/return/
date: 2021-01-11
key: Javascript.G.Generator
category: Javascript
tags: ['metodo javascript']
sidebar: 
  nav: javascript
---

{% include w3api/datos.html clase=site.data.Javascript.G.Generator.metodos valor="return" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~javascript
gen.return(value)
~~~

## Parámetros
* **value**,  {% include w3api/param_description.html metodo=_dato parametro="value" %}

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
