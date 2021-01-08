---
title: ObjectOutputStream.PutField.put()
permalink: Java/ObjectOutputStream/PutField/put
date: 2021-01-04
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
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ObjectOutputStream.PutField](/Java/ObjectOutputStream/PutField/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectOutputStream.PutField.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
