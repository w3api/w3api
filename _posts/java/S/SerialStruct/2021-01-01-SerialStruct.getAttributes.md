---
title: SerialStruct.getAttributes()
permalink: Java/SerialStruct/getAttributes
date: 2021-01-11
key: JavaJava.S.SerialStruct
category: java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialStruct.metodos valor="getAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object[] getAttributes() throws SerialException
public Object[] getAttributes(Map<String,Class<?>> map) throws SerialException
~~~

## Parámetros
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **Class&lt;?&gt;&gt; map**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?>> map" %}

## Excepciones
[SerialException](/Java/SerialException/)

## Clase Padre
[SerialStruct](/Java/SerialStruct/)

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
