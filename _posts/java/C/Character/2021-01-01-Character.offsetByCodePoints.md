---
title: Character.offsetByCodePoints()
permalink: /Java/Character/offsetByCodePoints/
date: 2021-01-11
key: Java.C.Character
category: Java
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
* **char[] a**,  {% include w3api/param_description.html metodo=_dato parametro="char[] a" %}
* **int count**,  {% include w3api/param_description.html metodo=_dato parametro="int count" %}
* **int codePointOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int codePointOffset" %}
* **CharSequence seq**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence seq" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Character](/Java/Character/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
