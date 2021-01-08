---
title: SQLClientInfoException.SQLClientInfoException()
permalink: Java/SQLClientInfoException/SQLClientInfoException
date: 2021-01-04
key: JavaJava.S.SQLClientInfoException
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLClientInfoException.constructores valor="SQLClientInfoException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLClientInfoException()
public SQLClientInfoException(String reason, String SQLState, int vendorCode, Map<String,ClientInfoStatus> failedProperties)
public SQLClientInfoException(String reason, String SQLState, int vendorCode, Map<String,ClientInfoStatus> failedProperties, Throwable cause)
public SQLClientInfoException(String reason, String SQLState, Map<String,ClientInfoStatus> failedProperties)
public SQLClientInfoException(String reason, String SQLState, Map<String,ClientInfoStatus> failedProperties, Throwable cause)
public SQLClientInfoException(String reason, Map<String,ClientInfoStatus> failedProperties)
public SQLClientInfoException(String reason, Map<String,ClientInfoStatus> failedProperties, Throwable cause)
public SQLClientInfoException(Map<String,ClientInfoStatus> failedProperties)
public SQLClientInfoException(Map<String,ClientInfoStatus> failedProperties, Throwable cause)
~~~

## Parámetros
* **String SQLState**,  {% include w3api/param_description.html metodo=_data parametro="String SQLState" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}
* **int vendorCode**,  {% include w3api/param_description.html metodo=_data parametro="int vendorCode" %}
* **ClientInfoStatus&gt; failedProperties**,  {% include w3api/param_description.html metodo=_data parametro="ClientInfoStatus> failedProperties" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}

## Clase Padre
[SQLClientInfoException](/Java/SQLClientInfoException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SQLClientInfoException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
