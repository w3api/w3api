---
title: StringJoiner.StringJoiner()
permalink: Java/StringJoiner/StringJoiner
date: 2021-01-04
key: JavaJava.S.StringJoiner
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringJoiner.constructores valor="StringJoiner" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringJoiner(CharSequence delimiter)
public StringJoiner(CharSequence delimiter, CharSequence prefix, CharSequence suffix)
~~~

## Parámetros
* **CharSequence suffix**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence suffix" %}
* **CharSequence delimiter**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence delimiter" %}
* **CharSequence prefix**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence prefix" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[StringJoiner](/Java/StringJoiner/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StringJoiner.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
