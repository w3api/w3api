---
title: StringBuilder.insert()
permalink: /Java/StringBuilder/insert/
date: 2021-01-11
key: Java.S.StringBuilder
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringBuilder.metodos valor="insert" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringBuilder insert(int offset, boolean b)
public StringBuilder insert(int offset, char c)
public StringBuilder insert(int offset, char[] str)
public StringBuilder insert(int index, char[] str, int offset, int len)
public StringBuilder insert(int offset, double d)
public StringBuilder insert(int offset, float f)
public StringBuilder insert(int offset, int i)
public StringBuilder insert(int offset, long l)
public StringBuilder insert(int dstOffset, CharSequence s)
public StringBuilder insert(int dstOffset, CharSequence s, int start, int end)
public StringBuilder insert(int offset, Object obj)
public StringBuilder insert(int offset, String str)
~~~

## Parámetros
* **float f**,  {% include w3api/param_description.html metodo=_dato parametro="float f" %}
* **long l**,  {% include w3api/param_description.html metodo=_dato parametro="long l" %}
* **double d**,  {% include w3api/param_description.html metodo=_dato parametro="double d" %}
* **boolean b**,  {% include w3api/param_description.html metodo=_dato parametro="boolean b" %}
* **int dstOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int dstOffset" %}
* **String str**,  {% include w3api/param_description.html metodo=_dato parametro="String str" %}
* **int end**,  {% include w3api/param_description.html metodo=_dato parametro="int end" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int i**,  {% include w3api/param_description.html metodo=_dato parametro="int i" %}
* **char c**,  {% include w3api/param_description.html metodo=_dato parametro="char c" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **CharSequence s**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence s" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **char[] str**,  {% include w3api/param_description.html metodo=_dato parametro="char[] str" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [StringIndexOutOfBoundsException](/Java/StringIndexOutOfBoundsException/)

## Clase Padre
[StringBuilder](/Java/StringBuilder/)

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
