---
title: Character.toChars()
permalink: /Java/Character/toChars/
date: 2021-01-11
key: Java.C.Character
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Character.metodos valor="toChars" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static char[] toChars(int codePoint)
public static int toChars(int codePoint, char[] dst, int dstIndex)
~~~

## Parámetros
* **char[] dst**,  {% include w3api/param_description.html metodo=_dato parametro="char[] dst" %}
* **int codePoint**,  {% include w3api/param_description.html metodo=_dato parametro="int codePoint" %}
* **int dstIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int dstIndex" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
