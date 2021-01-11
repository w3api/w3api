---
title: DataSource.getConnection()
permalink: Java/DataSource-javax-sql/getConnection
date: 2021-01-11
key: JavaJava.D.DataSource-javax-sql
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataSource-javax-sql.metodos valor="getConnection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Connection getConnection() throws SQLException
Connection getConnection(String username, String password) throws SQLException
~~~

## Parámetros
* **String password**,  {% include w3api/param_description.html metodo=_dato parametro="String password" %}
* **String username**,  {% include w3api/param_description.html metodo=_dato parametro="String username" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLTimeoutException](/Java/SQLTimeoutException/)

## Clase Padre
[DataSource](/Java/DataSource-javax-sql/)

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
