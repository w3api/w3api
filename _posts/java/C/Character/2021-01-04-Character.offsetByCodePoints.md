---
title: Character.offsetByCodePoints()
permalink: Java/Character/offsetByCodePoints
date: 2021-01-04
key: JavaJava.C.Character
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Character.metodos valor="offsetByCodePoints" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static int offsetByCodePoints(char[] a, int start, int count, int index, int codePointOffset)
public static int offsetByCodePoints(CharSequence seq, int index, int codePointOffset)
~~~

## Parámetros
* **char[] a**,  {% include w3api/param_description.html metodo=_data parametro="char[] a" %}
* **int codePointOffset**,  {% include w3api/param_description.html metodo=_data parametro="int codePointOffset" %}
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **int count**,  {% include w3api/param_description.html metodo=_data parametro="int count" %}
* **CharSequence seq**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence seq" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Character](/Java/Character/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Character.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
