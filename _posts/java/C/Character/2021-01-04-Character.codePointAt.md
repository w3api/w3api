---
title: Character.codePointAt()
permalink: Java/Character/codePointAt
date: 2021-01-04
key: JavaJava.C.Character
category: java
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
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **int limit**,  {% include w3api/param_description.html metodo=_data parametro="int limit" %}
* **CharSequence seq**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence seq" %}
* **char[] a**,  {% include w3api/param_description.html metodo=_data parametro="char[] a" %}

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
