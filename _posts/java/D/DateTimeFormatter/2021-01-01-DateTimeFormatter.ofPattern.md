---
title: DateTimeFormatter.ofPattern()
permalink: /Java/DateTimeFormatter/ofPattern/
date: 2021-01-11
key: Java.D.DateTimeFormatter
category: Java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatter.metodos valor="ofPattern" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DateTimeFormatter ofPattern(String pattern)
public static DateTimeFormatter ofPattern(String pattern, Locale locale)
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}
* **String pattern**,  {% include w3api/param_description.html metodo=_dato parametro="String pattern" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DateTimeFormatter](/Java/DateTimeFormatter/)

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
