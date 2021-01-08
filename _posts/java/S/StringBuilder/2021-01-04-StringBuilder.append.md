---
title: StringBuilder.append()
permalink: Java/StringBuilder/append
date: 2021-01-04
key: JavaJava.S.StringBuilder
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringBuilder.metodos valor="append" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public java.lang.AbstractStringBuilder append(boolean b)
public java.lang.AbstractStringBuilder append(char c)
public java.lang.AbstractStringBuilder append(char[] str)
public java.lang.AbstractStringBuilder append(double d)
public java.lang.AbstractStringBuilder append(float f)
public java.lang.AbstractStringBuilder append(int i)
public java.lang.AbstractStringBuilder append(long l)
public java.lang.AbstractStringBuilder append(CharSequence s)
public java.lang.AbstractStringBuilder append(Object obj)
public java.lang.AbstractStringBuilder append(String str)
public StringBuilder append(char[] str, int offset, int len)
public StringBuilder append(CharSequence s, int start, int end)
public StringBuilder append(StringBuffer sb)
~~~

## Parámetros
* **int i**,  {% include w3api/param_description.html metodo=_data parametro="int i" %}
* **String str**,  {% include w3api/param_description.html metodo=_data parametro="String str" %}
* **int end**,  {% include w3api/param_description.html metodo=_data parametro="int end" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_data parametro="Object obj" %}
* **StringBuffer sb**,  {% include w3api/param_description.html metodo=_data parametro="StringBuffer sb" %}
* **CharSequence s**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence s" %}
* **float f**,  {% include w3api/param_description.html metodo=_data parametro="float f" %}
* **char[] str**,  {% include w3api/param_description.html metodo=_data parametro="char[] str" %}
* **boolean b**,  {% include w3api/param_description.html metodo=_data parametro="boolean b" %}
* **double d**,  {% include w3api/param_description.html metodo=_data parametro="double d" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **char c**,  {% include w3api/param_description.html metodo=_data parametro="char c" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **long l**,  {% include w3api/param_description.html metodo=_data parametro="long l" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

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
