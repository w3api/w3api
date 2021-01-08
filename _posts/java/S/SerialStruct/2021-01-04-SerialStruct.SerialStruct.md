---
title: SerialStruct.SerialStruct()
permalink: Java/SerialStruct/SerialStruct
date: 2021-01-04
key: JavaJava.S.SerialStruct
category: java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialStruct.constructores valor="SerialStruct" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SerialStruct(SQLData in, Map<String,Class<?>> map) throws SerialException
public SerialStruct(Struct in, Map<String,Class<?>> map) throws SerialException
~~~

## Parámetros
* **Class&lt;?&gt;&gt; map**,  {% include w3api/param_description.html metodo=_data parametro="Class<?>> map" %}
* **SQLData in**,  {% include w3api/param_description.html metodo=_data parametro="SQLData in" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **Struct in**,  {% include w3api/param_description.html metodo=_data parametro="Struct in" %}

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
{%- for _ldc in site.data.Java.S.SerialStruct.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
