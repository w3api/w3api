---
title: StringTokenizer.nextToken()
permalink: Java/StringTokenizer/nextToken
date: 2021-01-04
key: JavaJava.S.StringTokenizer
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringTokenizer.metodos valor="nextToken" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String nextToken()
public String nextToken(String delim)
~~~

## Parámetros
* **String delim**,  {% include w3api/param_description.html metodo=_data parametro="String delim" %}

## Excepciones
[NoSuchElementException](/Java/NoSuchElementException/), [NullPointerException](/Java/NullPointerException/)

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
