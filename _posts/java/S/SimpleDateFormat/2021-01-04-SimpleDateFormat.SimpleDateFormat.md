---
title: SimpleDateFormat.SimpleDateFormat()
permalink: Java/SimpleDateFormat/SimpleDateFormat
date: 2021-01-04
key: JavaJava.S.SimpleDateFormat
category: java
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
* **String pattern**,  {% include w3api/param_description.html metodo=_data parametro="String pattern" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}
* **DateFormatSymbols formatSymbols**,  {% include w3api/param_description.html metodo=_data parametro="DateFormatSymbols formatSymbols" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SimpleDateFormat](/Java/SimpleDateFormat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleDateFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
