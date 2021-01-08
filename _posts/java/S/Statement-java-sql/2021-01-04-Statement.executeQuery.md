---
title: Statement.executeQuery()
permalink: Java/Statement-java-sql/executeQuery
date: 2021-01-04
key: JavaJava.S.Statement-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Statement-java-sql.metodos valor="executeQuery" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ResultSet executeQuery(String sql) throws SQLException
~~~

## Parámetros
* **String sql**,  {% include w3api/param_description.html metodo=_data parametro="String sql" %}

## Excepciones
[SQLTimeoutException](/Java/SQLTimeoutException/), [SQLException](/Java/SQLException/)

## Clase Padre
[Statement](/Java/Statement-java-sql/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Statement-java-sql.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
