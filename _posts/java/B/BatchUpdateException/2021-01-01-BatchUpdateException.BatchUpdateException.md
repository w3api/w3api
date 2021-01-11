---
title: BatchUpdateException.BatchUpdateException()
permalink: Java/BatchUpdateException/BatchUpdateException
date: 2021-01-11
key: JavaJava.B.BatchUpdateException
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BatchUpdateException.constructores valor="BatchUpdateException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BatchUpdateException()
public BatchUpdateException(int[] updateCounts)
public BatchUpdateException(int[] updateCounts, Throwable cause)
public BatchUpdateException(String reason, int[] updateCounts)
public BatchUpdateException(String reason, int[] updateCounts, Throwable cause)
public BatchUpdateException(String reason, String SQLState, int[] updateCounts)
public BatchUpdateException(String reason, String SQLState, int[] updateCounts, Throwable cause)
public BatchUpdateException(String reason, String SQLState, int vendorCode, int[] updateCounts)
public BatchUpdateException(String reason, String SQLState, int vendorCode, int[] updateCounts, Throwable cause)
public BatchUpdateException(String reason, String SQLState, int vendorCode, long[] updateCounts, Throwable cause)
public BatchUpdateException(Throwable cause)
~~~

## Parámetros
* **long[] updateCounts**,  {% include w3api/param_description.html metodo=_dato parametro="long[] updateCounts" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_dato parametro="String SQLState" %}
* **int[] updateCounts**,  {% include w3api/param_description.html metodo=_dato parametro="int[] updateCounts" %}
* **int vendorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int vendorCode" %}
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}

## Clase Padre
[BatchUpdateException](/Java/BatchUpdateException/)

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
