---
title: ObjectInputStream.GetField.get()
permalink: /Java/ObjectInputStream/GetField/get/
date: 2021-01-11
key: JavaJava.O.ObjectInputStream.GetField
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInputStream.GetField.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean get(String name, boolean val) throws IOException
public abstract byte get(String name, byte val) throws IOException
public abstract char get(String name, char val) throws IOException
public abstract double get(String name, double val) throws IOException
public abstract float get(String name, float val) throws IOException
public abstract int get(String name, int val) throws IOException
public abstract long get(String name, long val) throws IOException
public abstract short get(String name, short val) throws IOException
public abstract Object get(String name, Object val) throws IOException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **long val**,  {% include w3api/param_description.html metodo=_dato parametro="long val" %}
* **byte val**,  {% include w3api/param_description.html metodo=_dato parametro="byte val" %}
* **boolean val**,  {% include w3api/param_description.html metodo=_dato parametro="boolean val" %}
* **Object val**,  {% include w3api/param_description.html metodo=_dato parametro="Object val" %}
* **char val**,  {% include w3api/param_description.html metodo=_dato parametro="char val" %}
* **short val**,  {% include w3api/param_description.html metodo=_dato parametro="short val" %}
* **double val**,  {% include w3api/param_description.html metodo=_dato parametro="double val" %}
* **float val**,  {% include w3api/param_description.html metodo=_dato parametro="float val" %}
* **int val**,  {% include w3api/param_description.html metodo=_dato parametro="int val" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[ObjectInputStream.GetField](/Java/ObjectInputStream/GetField/)

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
