---
title: Generator.next()
permalink: Javascript/Generator/next
date: 2021-01-11
key: JavascriptJavascript.G.Generator
category: javascript
tags: ['metodo javascript']
sidebar: 
  nav: javascript
---

{% include w3api/datos.html clase=site.data.Javascript.G.Generator.metodos valor="next" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~javascript
gen.next(value)
~~~

## Parámetros
* **value**,  {% include w3api/param_description.html metodo=_dato parametro="value" %}

## Objeto Padre
[Generator](/Javascript/Generator/)

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
