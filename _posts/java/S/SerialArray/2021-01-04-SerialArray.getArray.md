---
title: SerialArray.getArray()
permalink: Java/SerialArray/getArray
date: 2021-01-04
key: JavaJava.S.SerialArray
category: java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialArray.metodos valor="getArray" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getArray() throws SerialException
public Object getArray(long index, int count) throws SerialException
public Object getArray(long index, int count, Map<String,Class<?>> map) throws SerialException
public Object getArray(Map<String,Class<?>> map) throws SerialException
~~~

## Parámetros
* **long index**,  {% include w3api/param_description.html metodo=_data parametro="long index" %}
* **int count**,  {% include w3api/param_description.html metodo=_data parametro="int count" %}
* **Class&lt;?&gt;&gt; map**,  {% include w3api/param_description.html metodo=_data parametro="Class<?>> map" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}

## Excepciones
[SerialException](/Java/SerialException/)

## Clase Padre
[SerialArray](/Java/SerialArray/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SerialArray.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
