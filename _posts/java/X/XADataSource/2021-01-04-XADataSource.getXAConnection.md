---
title: XADataSource.getXAConnection()
permalink: Java/XADataSource/getXAConnection
date: 2021-01-04
key: JavaJava.X.XADataSource
category: java
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
* **String user**,  {% include w3api/param_description.html metodo=_data parametro="String user" %}
* **String password**,  {% include w3api/param_description.html metodo=_data parametro="String password" %}

## Excepciones
[SQLTimeoutException](/Java/SQLTimeoutException/), [SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[XADataSource](/Java/XADataSource/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XADataSource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
