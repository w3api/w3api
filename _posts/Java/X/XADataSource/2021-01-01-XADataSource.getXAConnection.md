---
title: XADataSource.getXAConnection()
permalink: /Java/XADataSource/getXAConnection/
date: 2021-01-11
key: Java.X.XADataSource
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XADataSource.metodos valor="getXAConnection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
XAConnection getXAConnection() throws SQLException
XAConnection getXAConnection(String user, String password) throws SQLException
~~~

## Parámetros
* **String user**,  {% include w3api/param_description.html metodo=_dato parametro="String user" %}
* **String password**,  {% include w3api/param_description.html metodo=_dato parametro="String password" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/), [SQLTimeoutException](/Java/SQLTimeoutException/)

## Clase Padre
[XADataSource](/Java/XADataSource/)

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
