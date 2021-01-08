---
title: StringJoiner.merge()
permalink: Java/StringJoiner/merge
date: 2021-01-04
key: JavaJava.S.StringJoiner
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringJoiner.metodos valor="merge" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringJoiner merge(StringJoiner other)
~~~

## Parámetros
* **StringJoiner other**,  {% include w3api/param_description.html metodo=_data parametro="StringJoiner other" %}

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
