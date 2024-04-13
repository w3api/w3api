---
title: DateTimeFormatterBuilder.padNext()
permalink: /Java/DateTimeFormatterBuilder/padNext/
date: 2021-01-11
key: Java.D.DateTimeFormatterBuilder
category: Java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatterBuilder.metodos valor="padNext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DateTimeFormatterBuilder padNext(int padWidth)
public DateTimeFormatterBuilder padNext(int padWidth, char padChar)
~~~

## Parámetros
* **char padChar**,  {% include w3api/param_description.html metodo=_dato parametro="char padChar" %}
* **int padWidth**,  {% include w3api/param_description.html metodo=_dato parametro="int padWidth" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DateTimeFormatterBuilder](/Java/DateTimeFormatterBuilder/)

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
