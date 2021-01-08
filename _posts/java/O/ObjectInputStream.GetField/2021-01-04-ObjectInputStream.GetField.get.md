---
title: ObjectInputStream.GetField.get()
permalink: Java/ObjectInputStream/GetField/get
date: 2021-01-04
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
* **float val**,  {% include w3api/param_description.html metodo=_data parametro="float val" %}
* **byte val**,  {% include w3api/param_description.html metodo=_data parametro="byte val" %}
* **long val**,  {% include w3api/param_description.html metodo=_data parametro="long val" %}
* **char val**,  {% include w3api/param_description.html metodo=_data parametro="char val" %}
* **short val**,  {% include w3api/param_description.html metodo=_data parametro="short val" %}
* **int val**,  {% include w3api/param_description.html metodo=_data parametro="int val" %}
* **Object val**,  {% include w3api/param_description.html metodo=_data parametro="Object val" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **double val**,  {% include w3api/param_description.html metodo=_data parametro="double val" %}
* **boolean val**,  {% include w3api/param_description.html metodo=_data parametro="boolean val" %}

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
{%- for _ldc in site.data.Java.O.ObjectInputStream.GetField.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
