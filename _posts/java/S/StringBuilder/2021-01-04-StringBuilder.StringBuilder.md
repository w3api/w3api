---
title: StringBuilder.StringBuilder()
permalink: Java/StringBuilder/StringBuilder
date: 2021-01-04
key: JavaJava.S.StringBuilder
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringBuilder.constructores valor="StringBuilder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringBuilder()
public StringBuilder(int capacity)
public StringBuilder(CharSequence seq)
public StringBuilder(String str)
~~~

## Parámetros
* **int capacity**,  {% include w3api/param_description.html metodo=_data parametro="int capacity" %}
* **CharSequence seq**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence seq" %}
* **String str**,  {% include w3api/param_description.html metodo=_data parametro="String str" %}

## Excepciones
[NegativeArraySizeException](/Java/NegativeArraySizeException/)

## Clase Padre
[StringBuilder](/Java/StringBuilder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StringBuilder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
