---
title: StringBuilder.insert()
permalink: Java/StringBuilder/insert
date: 2021-01-04
key: JavaJava.S.StringBuilder
category: java
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
* **int i**,  {% include w3api/param_description.html metodo=_data parametro="int i" %}
* **String str**,  {% include w3api/param_description.html metodo=_data parametro="String str" %}
* **int end**,  {% include w3api/param_description.html metodo=_data parametro="int end" %}
* **int dstOffset**,  {% include w3api/param_description.html metodo=_data parametro="int dstOffset" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_data parametro="Object obj" %}
* **CharSequence s**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence s" %}
* **char[] str**,  {% include w3api/param_description.html metodo=_data parametro="char[] str" %}
* **boolean b**,  {% include w3api/param_description.html metodo=_data parametro="boolean b" %}
* **double d**,  {% include w3api/param_description.html metodo=_data parametro="double d" %}
* **float f**,  {% include w3api/param_description.html metodo=_data parametro="float f" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **char c**,  {% include w3api/param_description.html metodo=_data parametro="char c" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **long l**,  {% include w3api/param_description.html metodo=_data parametro="long l" %}

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
{%- for _ldc in site.data.Java.S.StringBuilder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
