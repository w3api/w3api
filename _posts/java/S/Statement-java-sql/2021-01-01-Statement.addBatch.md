---
title: Statement.addBatch()
permalink: Java/Statement-java-sql/addBatch
date: 2021-01-11
key: JavaJava.S.Statement-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Statement-java-sql.metodos valor="addBatch" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addBatch(String sql) throws SQLException
~~~

## Parámetros
* **String sql**,  {% include w3api/param_description.html metodo=_dato parametro="String sql" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[Statement](/Java/Statement-java-sql/)

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
