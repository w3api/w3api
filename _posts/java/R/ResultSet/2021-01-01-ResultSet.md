---
title: ResultSet
permalink: Java/ResultSet
date: 2021-01-11
key: JavaJava.R.ResultSet
category: java
tags: ['java se', 'java.sql', 'java.sql', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ResultSet.description }}

## Sintaxis
~~~java
public interface ResultSet extends Wrapper, AutoCloseable
~~~

## Campos
* [CLOSE_CURSORS_AT_COMMIT](/Java/ResultSet/CLOSE_CURSORS_AT_COMMIT)
* [CONCUR_READ_ONLY](/Java/ResultSet/CONCUR_READ_ONLY)
* [CONCUR_UPDATABLE](/Java/ResultSet/CONCUR_UPDATABLE)
* [FETCH_FORWARD](/Java/ResultSet/FETCH_FORWARD)
* [FETCH_REVERSE](/Java/ResultSet/FETCH_REVERSE)
* [FETCH_UNKNOWN](/Java/ResultSet/FETCH_UNKNOWN)
* [HOLD_CURSORS_OVER_COMMIT](/Java/ResultSet/HOLD_CURSORS_OVER_COMMIT)
* [TYPE_FORWARD_ONLY](/Java/ResultSet/TYPE_FORWARD_ONLY)
* [TYPE_SCROLL_INSENSITIVE](/Java/ResultSet/TYPE_SCROLL_INSENSITIVE)
* [TYPE_SCROLL_SENSITIVE](/Java/ResultSet/TYPE_SCROLL_SENSITIVE)

## Métodos
* [absolute()](/Java/ResultSet/absolute)
* [afterLast()](/Java/ResultSet/afterLast)
* [beforeFirst()](/Java/ResultSet/beforeFirst)
* [cancelRowUpdates()](/Java/ResultSet/cancelRowUpdates)
* [clearWarnings()](/Java/ResultSet/clearWarnings)
* [close()](/Java/ResultSet/close)
* [deleteRow()](/Java/ResultSet/deleteRow)
* [findColumn()](/Java/ResultSet/findColumn)
* [first()](/Java/ResultSet/first)
* [getArray()](/Java/ResultSet/getArray)
* [getAsciiStream()](/Java/ResultSet/getAsciiStream)
* [getBigDecimal()](/Java/ResultSet/getBigDecimal)
* [getBinaryStream()](/Java/ResultSet/getBinaryStream)
* [getBlob()](/Java/ResultSet/getBlob)
* [getBoolean()](/Java/ResultSet/getBoolean)
* [getByte()](/Java/ResultSet/getByte)
* [getBytes()](/Java/ResultSet/getBytes)
* [getCharacterStream()](/Java/ResultSet/getCharacterStream)
* [getClob()](/Java/ResultSet/getClob)
* [getConcurrency()](/Java/ResultSet/getConcurrency)
* [getCursorName()](/Java/ResultSet/getCursorName)
* [getDate()](/Java/ResultSet/getDate)
* [getDouble()](/Java/ResultSet/getDouble)
* [getFetchDirection()](/Java/ResultSet/getFetchDirection)
* [getFetchSize()](/Java/ResultSet/getFetchSize)
* [getFloat()](/Java/ResultSet/getFloat)
* [getHoldability()](/Java/ResultSet/getHoldability)
* [getInt()](/Java/ResultSet/getInt)
* [getLong()](/Java/ResultSet/getLong)
* [getMetaData()](/Java/ResultSet/getMetaData)
* [getNCharacterStream()](/Java/ResultSet/getNCharacterStream)
* [getNClob()](/Java/ResultSet/getNClob)
* [getNString()](/Java/ResultSet/getNString)
* [getObject()](/Java/ResultSet/getObject)
* [getRef()](/Java/ResultSet/getRef)
* [getRow()](/Java/ResultSet/getRow)
* [getRowId()](/Java/ResultSet/getRowId)
* [getShort()](/Java/ResultSet/getShort)
* [getSQLXML()](/Java/ResultSet/getSQLXML)
* [getStatement()](/Java/ResultSet/getStatement)
* [getString()](/Java/ResultSet/getString)
* [getTime()](/Java/ResultSet/getTime)
* [getTimestamp()](/Java/ResultSet/getTimestamp)
* [getType()](/Java/ResultSet/getType)
* [getUnicodeStream()](/Java/ResultSet/getUnicodeStream)
* [getURL()](/Java/ResultSet/getURL)
* [getWarnings()](/Java/ResultSet/getWarnings)
* [insertRow()](/Java/ResultSet/insertRow)
* [isAfterLast()](/Java/ResultSet/isAfterLast)
* [isBeforeFirst()](/Java/ResultSet/isBeforeFirst)
* [isClosed()](/Java/ResultSet/isClosed)
* [isFirst()](/Java/ResultSet/isFirst)
* [isLast()](/Java/ResultSet/isLast)
* [last()](/Java/ResultSet/last)
* [moveToCurrentRow()](/Java/ResultSet/moveToCurrentRow)
* [moveToInsertRow()](/Java/ResultSet/moveToInsertRow)
* [next()](/Java/ResultSet/next)
* [previous()](/Java/ResultSet/previous)
* [refreshRow()](/Java/ResultSet/refreshRow)
* [relative()](/Java/ResultSet/relative)
* [rowDeleted()](/Java/ResultSet/rowDeleted)
* [rowInserted()](/Java/ResultSet/rowInserted)
* [rowUpdated()](/Java/ResultSet/rowUpdated)
* [setFetchDirection()](/Java/ResultSet/setFetchDirection)
* [setFetchSize()](/Java/ResultSet/setFetchSize)
* [updateArray()](/Java/ResultSet/updateArray)
* [updateAsciiStream()](/Java/ResultSet/updateAsciiStream)
* [updateBigDecimal()](/Java/ResultSet/updateBigDecimal)
* [updateBinaryStream()](/Java/ResultSet/updateBinaryStream)
* [updateBlob()](/Java/ResultSet/updateBlob)
* [updateBoolean()](/Java/ResultSet/updateBoolean)
* [updateByte()](/Java/ResultSet/updateByte)
* [updateBytes()](/Java/ResultSet/updateBytes)
* [updateCharacterStream()](/Java/ResultSet/updateCharacterStream)
* [updateClob()](/Java/ResultSet/updateClob)
* [updateDate()](/Java/ResultSet/updateDate)
* [updateDouble()](/Java/ResultSet/updateDouble)
* [updateFloat()](/Java/ResultSet/updateFloat)
* [updateInt()](/Java/ResultSet/updateInt)
* [updateLong()](/Java/ResultSet/updateLong)
* [updateNCharacterStream()](/Java/ResultSet/updateNCharacterStream)
* [updateNClob()](/Java/ResultSet/updateNClob)
* [updateNString()](/Java/ResultSet/updateNString)
* [updateNull()](/Java/ResultSet/updateNull)
* [updateObject()](/Java/ResultSet/updateObject)
* [updateRef()](/Java/ResultSet/updateRef)
* [updateRow()](/Java/ResultSet/updateRow)
* [updateRowId()](/Java/ResultSet/updateRowId)
* [updateShort()](/Java/ResultSet/updateShort)
* [updateSQLXML()](/Java/ResultSet/updateSQLXML)
* [updateString()](/Java/ResultSet/updateString)
* [updateTime()](/Java/ResultSet/updateTime)
* [updateTimestamp()](/Java/ResultSet/updateTimestamp)
* [wasNull()](/Java/ResultSet/wasNull)

## Ejemplo
~~~java
{{ site.data.Java.R.ResultSet.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ResultSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
