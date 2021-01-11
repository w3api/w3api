---
title: Statement
permalink: Java/Statement-java-sql
date: 2021-01-11
key: JavaJava.S.Statement-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.Statement-java-sql.description }}

## Sintaxis
~~~java
public interface Statement extends Wrapper, AutoCloseable
~~~

## Campos
* [CLOSE_ALL_RESULTS](/Java/Statement-java-sql/CLOSE_ALL_RESULTS)
* [CLOSE_CURRENT_RESULT](/Java/Statement-java-sql/CLOSE_CURRENT_RESULT)
* [EXECUTE_FAILED](/Java/Statement-java-sql/EXECUTE_FAILED)
* [KEEP_CURRENT_RESULT](/Java/Statement-java-sql/KEEP_CURRENT_RESULT)
* [NO_GENERATED_KEYS](/Java/Statement-java-sql/NO_GENERATED_KEYS)
* [RETURN_GENERATED_KEYS](/Java/Statement-java-sql/RETURN_GENERATED_KEYS)
* [SUCCESS_NO_INFO](/Java/Statement-java-sql/SUCCESS_NO_INFO)

## Métodos
* [addBatch()](/Java/Statement-java-sql/addBatch)
* [cancel()](/Java/Statement-java-sql/cancel)
* [clearBatch()](/Java/Statement-java-sql/clearBatch)
* [clearWarnings()](/Java/Statement-java-sql/clearWarnings)
* [close()](/Java/Statement-java-sql/close)
* [closeOnCompletion()](/Java/Statement-java-sql/closeOnCompletion)
* [enquoteIdentifier()](/Java/Statement-java-sql/enquoteIdentifier)
* [enquoteLiteral()](/Java/Statement-java-sql/enquoteLiteral)
* [enquoteNCharLiteral()](/Java/Statement-java-sql/enquoteNCharLiteral)
* [execute()](/Java/Statement-java-sql/execute)
* [executeBatch()](/Java/Statement-java-sql/executeBatch)
* [executeLargeBatch()](/Java/Statement-java-sql/executeLargeBatch)
* [executeLargeUpdate()](/Java/Statement-java-sql/executeLargeUpdate)
* [executeQuery()](/Java/Statement-java-sql/executeQuery)
* [executeUpdate()](/Java/Statement-java-sql/executeUpdate)
* [getConnection()](/Java/Statement-java-sql/getConnection)
* [getFetchDirection()](/Java/Statement-java-sql/getFetchDirection)
* [getFetchSize()](/Java/Statement-java-sql/getFetchSize)
* [getGeneratedKeys()](/Java/Statement-java-sql/getGeneratedKeys)
* [getLargeMaxRows()](/Java/Statement-java-sql/getLargeMaxRows)
* [getLargeUpdateCount()](/Java/Statement-java-sql/getLargeUpdateCount)
* [getMaxFieldSize()](/Java/Statement-java-sql/getMaxFieldSize)
* [getMaxRows()](/Java/Statement-java-sql/getMaxRows)
* [getMoreResults()](/Java/Statement-java-sql/getMoreResults)
* [getQueryTimeout()](/Java/Statement-java-sql/getQueryTimeout)
* [getResultSet()](/Java/Statement-java-sql/getResultSet)
* [getResultSetConcurrency()](/Java/Statement-java-sql/getResultSetConcurrency)
* [getResultSetHoldability()](/Java/Statement-java-sql/getResultSetHoldability)
* [getResultSetType()](/Java/Statement-java-sql/getResultSetType)
* [getUpdateCount()](/Java/Statement-java-sql/getUpdateCount)
* [getWarnings()](/Java/Statement-java-sql/getWarnings)
* [isClosed()](/Java/Statement-java-sql/isClosed)
* [isCloseOnCompletion()](/Java/Statement-java-sql/isCloseOnCompletion)
* [isPoolable()](/Java/Statement-java-sql/isPoolable)
* [isSimpleIdentifier()](/Java/Statement-java-sql/isSimpleIdentifier)
* [setCursorName()](/Java/Statement-java-sql/setCursorName)
* [setEscapeProcessing()](/Java/Statement-java-sql/setEscapeProcessing)
* [setFetchDirection()](/Java/Statement-java-sql/setFetchDirection)
* [setFetchSize()](/Java/Statement-java-sql/setFetchSize)
* [setLargeMaxRows()](/Java/Statement-java-sql/setLargeMaxRows)
* [setMaxFieldSize()](/Java/Statement-java-sql/setMaxFieldSize)
* [setMaxRows()](/Java/Statement-java-sql/setMaxRows)
* [setPoolable()](/Java/Statement-java-sql/setPoolable)
* [setQueryTimeout()](/Java/Statement-java-sql/setQueryTimeout)

## Ejemplo
~~~java
{{ site.data.Java.S.Statement-java-sql.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Statement-java-sql.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
