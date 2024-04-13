---
title: TransactionalWriter
permalink: /Java/TransactionalWriter/
date: 2021-01-11
key: Java.T.TransactionalWriter
category: Java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TransactionalWriter.description }}

## Sintaxis
~~~java
public interface TransactionalWriter extends RowSetWriter
~~~

## Métodos
* [commit()](/Java/TransactionalWriter/commit)
* [rollback()](/Java/TransactionalWriter/rollback)

## Ejemplo
~~~java
{{ site.data.Java.T.TransactionalWriter.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TransactionalWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
