---
title: DecimalFormat.parse()
permalink: /Java/DecimalFormat/parse/
date: 2021-01-11
key: Java.D.DecimalFormat
category: Java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DecimalFormat.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Number parse(String text, ParsePosition pos)
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **ParsePosition pos**,  {% include w3api/param_description.html metodo=_dato parametro="ParsePosition pos" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DecimalFormat](/Java/DecimalFormat/)

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
