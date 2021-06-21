---
title: EvalError.EvalError()
permalink: /Javascript/EvalError/EvalError/
date: 2021-01-11
key: Javascript.E.EvalError
category: Javascript
tags: ['constructor javascript']
sidebar: 
  nav: javascript
---

{% include w3api/datos.html clase=site.data.Javascript.E.EvalError.constructores valor="EvalError" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~javascript
new EvalError([message[, fileName[, lineNumber]]])
~~~

## Parámetros
* **message**,  {% include w3api/param_description.html metodo=_dato parametro="message" %}
* **fileName**,  {% include w3api/param_description.html metodo=_dato parametro="fileName" %}
* **lineNumber**,  {% include w3api/param_description.html metodo=_dato parametro="lineNumber" %}

## Objeto Padre
[EvalError](/Javascript/EvalError/)

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
