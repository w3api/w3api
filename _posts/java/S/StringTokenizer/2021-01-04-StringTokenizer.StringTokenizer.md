---
title: StringTokenizer.StringTokenizer()
permalink: Java/StringTokenizer/StringTokenizer
date: 2021-01-04
key: JavaJava.S.StringTokenizer
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringTokenizer.constructores valor="StringTokenizer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringTokenizer(String str)
public StringTokenizer(String str, String delim)
public StringTokenizer(String str, String delim, boolean returnDelims)
~~~

## Parámetros
* **String delim**,  {% include w3api/param_description.html metodo=_data parametro="String delim" %}
* **String str**,  {% include w3api/param_description.html metodo=_data parametro="String str" %}
* **boolean returnDelims**,  {% include w3api/param_description.html metodo=_data parametro="boolean returnDelims" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[StringTokenizer](/Java/StringTokenizer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StringTokenizer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
