---
title: SQLSyntaxErrorException.SQLSyntaxErrorException()
permalink: Java/SQLSyntaxErrorException/SQLSyntaxErrorException
date: 2021-01-04
key: JavaJava.S.SQLSyntaxErrorException
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLSyntaxErrorException.constructores valor="SQLSyntaxErrorException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLSyntaxErrorException()
public SQLSyntaxErrorException(String reason)
public SQLSyntaxErrorException(String reason, String SQLState)
public SQLSyntaxErrorException(String reason, String SQLState, int vendorCode)
public SQLSyntaxErrorException(String reason, String SQLState, int vendorCode, Throwable cause)
public SQLSyntaxErrorException(String reason, String SQLState, Throwable cause)
public SQLSyntaxErrorException(String reason, Throwable cause)
public SQLSyntaxErrorException(Throwable cause)
~~~

## Parámetros
* **int vendorCode**,  {% include w3api/param_description.html metodo=_data parametro="int vendorCode" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_data parametro="String SQLState" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[SQLSyntaxErrorException](/Java/SQLSyntaxErrorException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SQLSyntaxErrorException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
