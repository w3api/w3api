---
title: SerialRef.getObject()
permalink: /Java/SerialRef/getObject/
date: 2021-01-11
key: Java.S.SerialRef
category: Java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialRef.metodos valor="getObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getObject() throws SerialException
public Object getObject(Map<String,Class<?>> map) throws SerialException
~~~

## Parámetros
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **Class&lt;?&gt;&gt; map**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?>> map" %}

## Excepciones
[SerialException](/Java/SerialException/)

## Clase Padre
[SerialRef](/Java/SerialRef/)

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
