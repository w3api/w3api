---
title: SimpleDateFormat.SimpleDateFormat()
permalink: /Java/SimpleDateFormat/SimpleDateFormat/
date: 2021-01-11
key: Java.S.SimpleDateFormat
category: Java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleDateFormat.constructores valor="SimpleDateFormat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SimpleDateFormat()
public SimpleDateFormat(String pattern)
public SimpleDateFormat(String pattern, DateFormatSymbols formatSymbols)
public SimpleDateFormat(String pattern, Locale locale)
~~~

## Parámetros
* **DateFormatSymbols formatSymbols**,  {% include w3api/param_description.html metodo=_dato parametro="DateFormatSymbols formatSymbols" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}
* **String pattern**,  {% include w3api/param_description.html metodo=_dato parametro="String pattern" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SimpleDateFormat](/Java/SimpleDateFormat/)

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
