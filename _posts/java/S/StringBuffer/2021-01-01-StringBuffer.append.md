---
title: StringBuffer.append()
permalink: /Java/StringBuffer/append/
date: 2021-01-11
key: Java.S.StringBuffer
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringBuffer.metodos valor="append" %}

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
public java.lang.AbstractStringBuilder append(Object obj)
public java.lang.AbstractStringBuilder append(String str)
public StringBuffer append(char[] str, int offset, int len)
public StringBuffer append(CharSequence s)
public StringBuffer append(CharSequence s, int start, int end)
public StringBuffer append(StringBuffer sb)
~~~

## Parámetros
* **float f**,  {% include w3api/param_description.html metodo=_dato parametro="float f" %}
* **long l**,  {% include w3api/param_description.html metodo=_dato parametro="long l" %}
* **double d**,  {% include w3api/param_description.html metodo=_dato parametro="double d" %}
* **boolean b**,  {% include w3api/param_description.html metodo=_dato parametro="boolean b" %}
* **String str**,  {% include w3api/param_description.html metodo=_dato parametro="String str" %}
* **int end**,  {% include w3api/param_description.html metodo=_dato parametro="int end" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **char c**,  {% include w3api/param_description.html metodo=_dato parametro="char c" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **CharSequence s**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence s" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **StringBuffer sb**,  {% include w3api/param_description.html metodo=_dato parametro="StringBuffer sb" %}
* **int i**,  {% include w3api/param_description.html metodo=_dato parametro="int i" %}
* **char[] str**,  {% include w3api/param_description.html metodo=_dato parametro="char[] str" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[StringBuffer](/Java/StringBuffer/)

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
