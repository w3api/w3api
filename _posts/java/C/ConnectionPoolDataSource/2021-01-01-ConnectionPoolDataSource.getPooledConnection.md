---
title: ConnectionPoolDataSource.getPooledConnection()
permalink: Java/ConnectionPoolDataSource/getPooledConnection
date: 2021-01-11
key: JavaJava.C.ConnectionPoolDataSource
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConnectionPoolDataSource.metodos valor="getPooledConnection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
PooledConnection getPooledConnection() throws SQLException
PooledConnection getPooledConnection(String user, String password) throws SQLException
~~~

## Parámetros
* **String user**,  {% include w3api/param_description.html metodo=_dato parametro="String user" %}
* **String password**,  {% include w3api/param_description.html metodo=_dato parametro="String password" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[ConnectionPoolDataSource](/Java/ConnectionPoolDataSource/)

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
