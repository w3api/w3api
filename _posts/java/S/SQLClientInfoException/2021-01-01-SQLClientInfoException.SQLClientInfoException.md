---
title: SQLClientInfoException.SQLClientInfoException()
permalink: Java/SQLClientInfoException/SQLClientInfoException
date: 2021-01-11
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
* **ClientInfoStatus&gt; failedProperties**,  {% include w3api/param_description.html metodo=_dato parametro="ClientInfoStatus> failedProperties" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_dato parametro="String SQLState" %}
* **int vendorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int vendorCode" %}
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}

## Clase Padre
[SQLClientInfoException](/Java/SQLClientInfoException/)

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
