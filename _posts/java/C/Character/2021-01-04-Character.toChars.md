---
title: Character.toChars()
permalink: Java/Character/toChars
date: 2021-01-04
key: JavaJava.C.Character
category: java
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
* **char[] dst**,  {% include w3api/param_description.html metodo=_data parametro="char[] dst" %}
* **int dstIndex**,  {% include w3api/param_description.html metodo=_data parametro="int dstIndex" %}
* **int codePoint**,  {% include w3api/param_description.html metodo=_data parametro="int codePoint" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
