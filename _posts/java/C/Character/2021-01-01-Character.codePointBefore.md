---
title: Character.codePointBefore()
permalink: Java/Character/codePointBefore
date: 2021-01-11
key: JavaJava.C.Character
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Character.metodos valor="codePointBefore" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static int codePointBefore(char[] a, int index)
public static int codePointBefore(char[] a, int index, int start)
public static int codePointBefore(CharSequence seq, int index)
~~~

## Parámetros
* **CharSequence seq**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence seq" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **char[] a**,  {% include w3api/param_description.html metodo=_dato parametro="char[] a" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
