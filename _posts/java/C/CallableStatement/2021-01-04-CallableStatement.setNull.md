---
title: CallableStatement.setNull()
permalink: Java/CallableStatement/setNull
date: 2021-01-04
key: JavaJava.C.CallableStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CallableStatement.metodos valor="setNull" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setNull(String parameterName, int sqlType) throws SQLException
void setNull(String parameterName, int sqlType, String typeName) throws SQLException
~~~

## Parámetros
* **String typeName**,  {% include w3api/param_description.html metodo=_data parametro="String typeName" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_data parametro="String parameterName" %}
* **int sqlType**,  {% include w3api/param_description.html metodo=_data parametro="int sqlType" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[CallableStatement](/Java/CallableStatement/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CallableStatement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
