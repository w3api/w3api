---
title: Character.codePointAt()
permalink: /Java/Character/codePointAt/
date: 2021-01-11
key: Java.C.Character
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Character.metodos valor="codePointAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static int codePointAt(char[] a, int index)
public static int codePointAt(char[] a, int index, int limit)
public static int codePointAt(CharSequence seq, int index)
~~~

## Parámetros
* **CharSequence seq**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence seq" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **char[] a**,  {% include w3api/param_description.html metodo=_dato parametro="char[] a" %}
* **int limit**,  {% include w3api/param_description.html metodo=_dato parametro="int limit" %}

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
