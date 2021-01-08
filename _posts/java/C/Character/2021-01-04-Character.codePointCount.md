---
title: Character.codePointCount()
permalink: Java/Character/codePointCount
date: 2021-01-04
key: JavaJava.C.Character
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Character.metodos valor="codePointCount" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static int codePointCount(char[] a, int offset, int count)
public static int codePointCount(CharSequence seq, int beginIndex, int endIndex)
~~~

## Parámetros
* **int beginIndex**,  {% include w3api/param_description.html metodo=_data parametro="int beginIndex" %}
* **char[] a**,  {% include w3api/param_description.html metodo=_data parametro="char[] a" %}
* **int endIndex**,  {% include w3api/param_description.html metodo=_data parametro="int endIndex" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
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
