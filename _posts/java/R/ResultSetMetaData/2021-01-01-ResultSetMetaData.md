---
title: ResultSetMetaData
permalink: /Java/ResultSetMetaData/
date: 2021-01-11
key: Java.R.ResultSetMetaData
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ResultSetMetaData.description }}

## Sintaxis
~~~java
public interface ResultSetMetaData extends Wrapper
~~~

## Campos
* [columnNoNulls](/Java/ResultSetMetaData/columnNoNulls)
* [columnNullable](/Java/ResultSetMetaData/columnNullable)
* [columnNullableUnknown](/Java/ResultSetMetaData/columnNullableUnknown)

## Métodos
* [getCatalogName()](/Java/ResultSetMetaData/getCatalogName)
* [getColumnClassName()](/Java/ResultSetMetaData/getColumnClassName)
* [getColumnCount()](/Java/ResultSetMetaData/getColumnCount)
* [getColumnDisplaySize()](/Java/ResultSetMetaData/getColumnDisplaySize)
* [getColumnLabel()](/Java/ResultSetMetaData/getColumnLabel)
* [getColumnName()](/Java/ResultSetMetaData/getColumnName)
* [getColumnType()](/Java/ResultSetMetaData/getColumnType)
* [getColumnTypeName()](/Java/ResultSetMetaData/getColumnTypeName)
* [getPrecision()](/Java/ResultSetMetaData/getPrecision)
* [getScale()](/Java/ResultSetMetaData/getScale)
* [getSchemaName()](/Java/ResultSetMetaData/getSchemaName)
* [getTableName()](/Java/ResultSetMetaData/getTableName)
* [isAutoIncrement()](/Java/ResultSetMetaData/isAutoIncrement)
* [isCaseSensitive()](/Java/ResultSetMetaData/isCaseSensitive)
* [isCurrency()](/Java/ResultSetMetaData/isCurrency)
* [isDefinitelyWritable()](/Java/ResultSetMetaData/isDefinitelyWritable)
* [isNullable()](/Java/ResultSetMetaData/isNullable)
* [isReadOnly()](/Java/ResultSetMetaData/isReadOnly)
* [isSearchable()](/Java/ResultSetMetaData/isSearchable)
* [isSigned()](/Java/ResultSetMetaData/isSigned)
* [isWritable()](/Java/ResultSetMetaData/isWritable)

## Ejemplo
~~~java
{{ site.data.Java.R.ResultSetMetaData.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ResultSetMetaData.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
