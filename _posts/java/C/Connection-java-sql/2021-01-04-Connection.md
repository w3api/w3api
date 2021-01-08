---
title: Connection
permalink: Java/Connection-java-sql
date: 2021-01-04
key: JavaJava.C.Connection-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Connection-java-sql.description }}

## Sintaxis
~~~java
public interface Connection extends Wrapper, AutoCloseable
~~~

## Campos
* [TRANSACTION_NONE](/Java/Connection-java-sql/TRANSACTION_NONE)
* [TRANSACTION_READ_COMMITTED](/Java/Connection-java-sql/TRANSACTION_READ_COMMITTED)
* [TRANSACTION_READ_UNCOMMITTED](/Java/Connection-java-sql/TRANSACTION_READ_UNCOMMITTED)
* [TRANSACTION_REPEATABLE_READ](/Java/Connection-java-sql/TRANSACTION_REPEATABLE_READ)
* [TRANSACTION_SERIALIZABLE](/Java/Connection-java-sql/TRANSACTION_SERIALIZABLE)

## Métodos
* [abort()](/Java/Connection-java-sql/abort)
* [beginRequest()](/Java/Connection-java-sql/beginRequest)
* [clearWarnings()](/Java/Connection-java-sql/clearWarnings)
* [close()](/Java/Connection-java-sql/close)
* [commit()](/Java/Connection-java-sql/commit)
* [createArrayOf()](/Java/Connection-java-sql/createArrayOf)
* [createBlob()](/Java/Connection-java-sql/createBlob)
* [createClob()](/Java/Connection-java-sql/createClob)
* [createNClob()](/Java/Connection-java-sql/createNClob)
* [createSQLXML()](/Java/Connection-java-sql/createSQLXML)
* [createStatement()](/Java/Connection-java-sql/createStatement)
* [createStruct()](/Java/Connection-java-sql/createStruct)
* [endRequest()](/Java/Connection-java-sql/endRequest)
* [getAutoCommit()](/Java/Connection-java-sql/getAutoCommit)
* [getCatalog()](/Java/Connection-java-sql/getCatalog)
* [getClientInfo()](/Java/Connection-java-sql/getClientInfo)
* [getHoldability()](/Java/Connection-java-sql/getHoldability)
* [getMetaData()](/Java/Connection-java-sql/getMetaData)
* [getNetworkTimeout()](/Java/Connection-java-sql/getNetworkTimeout)
* [getSchema()](/Java/Connection-java-sql/getSchema)
* [getTransactionIsolation()](/Java/Connection-java-sql/getTransactionIsolation)
* [getTypeMap()](/Java/Connection-java-sql/getTypeMap)
* [getWarnings()](/Java/Connection-java-sql/getWarnings)
* [isClosed()](/Java/Connection-java-sql/isClosed)
* [isReadOnly()](/Java/Connection-java-sql/isReadOnly)
* [isValid()](/Java/Connection-java-sql/isValid)
* [nativeSQL()](/Java/Connection-java-sql/nativeSQL)
* [prepareCall()](/Java/Connection-java-sql/prepareCall)
* [prepareStatement()](/Java/Connection-java-sql/prepareStatement)
* [releaseSavepoint()](/Java/Connection-java-sql/releaseSavepoint)
* [rollback()](/Java/Connection-java-sql/rollback)
* [setAutoCommit()](/Java/Connection-java-sql/setAutoCommit)
* [setCatalog()](/Java/Connection-java-sql/setCatalog)
* [setClientInfo()](/Java/Connection-java-sql/setClientInfo)
* [setHoldability()](/Java/Connection-java-sql/setHoldability)
* [setNetworkTimeout()](/Java/Connection-java-sql/setNetworkTimeout)
* [setReadOnly()](/Java/Connection-java-sql/setReadOnly)
* [setSavepoint()](/Java/Connection-java-sql/setSavepoint)
* [setSchema()](/Java/Connection-java-sql/setSchema)
* [setShardingKey()](/Java/Connection-java-sql/setShardingKey)
* [setShardingKeyIfValid()](/Java/Connection-java-sql/setShardingKeyIfValid)
* [setTransactionIsolation()](/Java/Connection-java-sql/setTransactionIsolation)
* [setTypeMap()](/Java/Connection-java-sql/setTypeMap)

## Ejemplo
~~~java
{{ site.data.Java.C.Connection-java-sql.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Connection-java-sql.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
