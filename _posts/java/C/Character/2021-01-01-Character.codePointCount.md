---
title: Character.codePointCount()
permalink: /Java/Character/codePointCount/
date: 2021-01-11
key: Java.C.Character
category: Java
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
* **char[] a**,  {% include w3api/param_description.html metodo=_dato parametro="char[] a" %}
* **int count**,  {% include w3api/param_description.html metodo=_dato parametro="int count" %}
* **int beginIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int beginIndex" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **CharSequence seq**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence seq" %}
* **int endIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int endIndex" %}

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
