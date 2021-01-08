---
title: BatchUpdateException.BatchUpdateException()
permalink: Java/BatchUpdateException/BatchUpdateException
date: 2021-01-04
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
* **String SQLState**,  {% include w3api/param_description.html metodo=_data parametro="String SQLState" %}
* **long[] updateCounts**,  {% include w3api/param_description.html metodo=_data parametro="long[] updateCounts" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}
* **int vendorCode**,  {% include w3api/param_description.html metodo=_data parametro="int vendorCode" %}
* **int[] updateCounts**,  {% include w3api/param_description.html metodo=_data parametro="int[] updateCounts" %}

## Clase Padre
[BatchUpdateException](/Java/BatchUpdateException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BatchUpdateException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
