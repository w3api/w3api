---
title: TransactionalWriter.rollback()
permalink: /Java/TransactionalWriter/rollback/
date: 2021-01-11
key: Java.T.TransactionalWriter
category: Java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransactionalWriter.metodos valor="rollback" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void rollback() throws SQLException
void rollback(Savepoint s) throws SQLException
~~~

## Parámetros
* **Savepoint s**,  {% include w3api/param_description.html metodo=_dato parametro="Savepoint s" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[TransactionalWriter](/Java/TransactionalWriter/)

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
