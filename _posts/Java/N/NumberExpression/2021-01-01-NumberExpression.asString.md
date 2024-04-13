---
title: NumberExpression.asString()
permalink: /Java/NumberExpression/asString/
date: 2021-01-11
key: Java.N.NumberExpression
category: Java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumberExpression.metodos valor="asString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
StringBinding asString()
StringBinding asString(String format)
StringBinding asString(Locale locale, String format)
~~~

## Parámetros
* **String format**,  {% include w3api/param_description.html metodo=_dato parametro="String format" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Clase Padre
[NumberExpression](/Java/NumberExpression/)

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
