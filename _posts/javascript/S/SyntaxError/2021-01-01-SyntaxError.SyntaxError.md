---
title: SyntaxError.SyntaxError()
permalink: /Javascript/SyntaxError/SyntaxError/
date: 2021-01-11
key: Javascript.S.SyntaxError
category: javascript
tags: ['constructor javascript']
sidebar: 
  nav: javascript
---

{% include w3api/datos.html clase=site.data.Javascript.S.SyntaxError.constructores valor="SyntaxError" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~javascript
new SyntaxError([message[, fileName[, lineNumber]]])
~~~

## Parámetros
* **message**,  {% include w3api/param_description.html metodo=_dato parametro="message" %}
* **fileName**,  {% include w3api/param_description.html metodo=_dato parametro="fileName" %}
* **lineNumber**,  {% include w3api/param_description.html metodo=_dato parametro="lineNumber" %}

## Objeto Padre
[SyntaxError](/Javascript/SyntaxError/)

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
