---
title: PreparedStatement
permalink: /Java/PreparedStatement/
date: 2021-01-11
key: Java.P.PreparedStatement
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PreparedStatement.description }}

## Sintaxis
~~~java
public interface PreparedStatement extends Statement
~~~

## Métodos
* [addBatch()](/Java/PreparedStatement/addBatch/)
* [clearParameters()](/Java/PreparedStatement/clearParameters/)
* [execute()](/Java/PreparedStatement/execute/)
* [executeLargeUpdate()](/Java/PreparedStatement/executeLargeUpdate/)
* [executeQuery()](/Java/PreparedStatement/executeQuery/)
* [executeUpdate()](/Java/PreparedStatement/executeUpdate/)
* [getMetaData()](/Java/PreparedStatement/getMetaData/)
* [getParameterMetaData()](/Java/PreparedStatement/getParameterMetaData/)
* [setArray()](/Java/PreparedStatement/setArray/)
* [setAsciiStream()](/Java/PreparedStatement/setAsciiStream/)
* [setBigDecimal()](/Java/PreparedStatement/setBigDecimal/)
* [setBinaryStream()](/Java/PreparedStatement/setBinaryStream/)
* [setBlob()](/Java/PreparedStatement/setBlob/)
* [setBoolean()](/Java/PreparedStatement/setBoolean/)
* [setByte()](/Java/PreparedStatement/setByte/)
* [setBytes()](/Java/PreparedStatement/setBytes/)
* [setCharacterStream()](/Java/PreparedStatement/setCharacterStream/)
* [setClob()](/Java/PreparedStatement/setClob/)
* [setDate()](/Java/PreparedStatement/setDate/)
* [setDouble()](/Java/PreparedStatement/setDouble/)
* [setFloat()](/Java/PreparedStatement/setFloat/)
* [setInt()](/Java/PreparedStatement/setInt/)
* [setLong()](/Java/PreparedStatement/setLong/)
* [setNCharacterStream()](/Java/PreparedStatement/setNCharacterStream/)
* [setNClob()](/Java/PreparedStatement/setNClob/)
* [setNString()](/Java/PreparedStatement/setNString/)
* [setNull()](/Java/PreparedStatement/setNull/)
* [setObject()](/Java/PreparedStatement/setObject/)
* [setRef()](/Java/PreparedStatement/setRef/)
* [setRowId()](/Java/PreparedStatement/setRowId/)
* [setShort()](/Java/PreparedStatement/setShort/)
* [setSQLXML()](/Java/PreparedStatement/setSQLXML/)
* [setString()](/Java/PreparedStatement/setString/)
* [setTime()](/Java/PreparedStatement/setTime/)
* [setTimestamp()](/Java/PreparedStatement/setTimestamp/)
* [setUnicodeStream()](/Java/PreparedStatement/setUnicodeStream/)
* [setURL()](/Java/PreparedStatement/setURL/)

## Ejemplo
~~~java
{{ site.data.Java.P.PreparedStatement.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PreparedStatement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
