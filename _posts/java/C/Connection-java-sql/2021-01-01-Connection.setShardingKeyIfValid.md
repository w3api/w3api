---
title: Connection.setShardingKeyIfValid()
permalink: /Java/Connection-java-sql/setShardingKeyIfValid/
date: 2021-01-11
key: Java.C.Connection-java-sql
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Connection-java-sql.metodos valor="setShardingKeyIfValid" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default boolean setShardingKeyIfValid(ShardingKey shardingKey, int timeout) throws SQLException
default boolean setShardingKeyIfValid(ShardingKey shardingKey, ShardingKey superShardingKey, int timeout) throws SQLException
~~~

## Parámetros
* **ShardingKey shardingKey**,  {% include w3api/param_description.html metodo=_dato parametro="ShardingKey shardingKey" %}
* **int timeout**,  {% include w3api/param_description.html metodo=_dato parametro="int timeout" %}
* **ShardingKey superShardingKey**,  {% include w3api/param_description.html metodo=_dato parametro="ShardingKey superShardingKey" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[Connection](/Java/Connection-java-sql/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
