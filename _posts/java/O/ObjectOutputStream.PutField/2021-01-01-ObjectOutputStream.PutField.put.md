---
title: ObjectOutputStream.PutField.put()
permalink: Java/ObjectOutputStream/PutField/put
date: 2021-01-11
key: JavaJava.O.ObjectOutputStream.PutField
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectOutputStream.PutField.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void put(String name, boolean val)
public abstract void put(String name, byte val)
public abstract void put(String name, char val)
public abstract void put(String name, double val)
public abstract void put(String name, float val)
public abstract void put(String name, int val)
public abstract void put(String name, long val)
public abstract void put(String name, short val)
public abstract void put(String name, Object val)
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
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ObjectOutputStream.PutField](/Java/ObjectOutputStream/PutField/)

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
