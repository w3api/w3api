---
title: SerialArray.SerialArray()
permalink: Java/SerialArray/SerialArray
date: 2021-01-04
key: JavaJava.S.SerialArray
category: java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialArray.constructores valor="SerialArray" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SerialArray(Array array) throws SerialException, SQLException
public SerialArray(Array array, Map<String,Class<?>> map) throws SerialException, SQLException
~~~

## Parámetros
* **Class&lt;?&gt;&gt; map**,  {% include w3api/param_description.html metodo=_data parametro="Class<?>> map" %}
* **Array array**,  {% include w3api/param_description.html metodo=_data parametro="Array array" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}

## Excepciones
[SQLException](/Java/SQLException/), [SerialException](/Java/SerialException/)

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
