---
title: CachedRowSet
permalink: Java/CachedRowSet
date: 2021-01-04
key: JavaJava.C.CachedRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CachedRowSet.description }}

## Sintaxis
~~~java
public interface CachedRowSet extends RowSet, Joinable
~~~

## Campos
* [COMMIT_ON_ACCEPT_CHANGES](/Java/CachedRowSet/COMMIT_ON_ACCEPT_CHANGES)

## Métodos
* [acceptChanges()](/Java/CachedRowSet/acceptChanges)
* [columnUpdated()](/Java/CachedRowSet/columnUpdated)
* [commit()](/Java/CachedRowSet/commit)
* [createCopy()](/Java/CachedRowSet/createCopy)
* [createCopyNoConstraints()](/Java/CachedRowSet/createCopyNoConstraints)
* [createCopySchema()](/Java/CachedRowSet/createCopySchema)
* [createShared()](/Java/CachedRowSet/createShared)
* [execute()](/Java/CachedRowSet/execute)
* [getKeyColumns()](/Java/CachedRowSet/getKeyColumns)
* [getOriginal()](/Java/CachedRowSet/getOriginal)
* [getOriginalRow()](/Java/CachedRowSet/getOriginalRow)
* [getPageSize()](/Java/CachedRowSet/getPageSize)
* [getRowSetWarnings()](/Java/CachedRowSet/getRowSetWarnings)
* [getShowDeleted()](/Java/CachedRowSet/getShowDeleted)
* [getSyncProvider()](/Java/CachedRowSet/getSyncProvider)
* [getTableName()](/Java/CachedRowSet/getTableName)
* [nextPage()](/Java/CachedRowSet/nextPage)
* [populate()](/Java/CachedRowSet/populate)
* [previousPage()](/Java/CachedRowSet/previousPage)
* [release()](/Java/CachedRowSet/release)
* [restoreOriginal()](/Java/CachedRowSet/restoreOriginal)
* [rollback()](/Java/CachedRowSet/rollback)
* [rowSetPopulated()](/Java/CachedRowSet/rowSetPopulated)
* [setKeyColumns()](/Java/CachedRowSet/setKeyColumns)
* [setMetaData()](/Java/CachedRowSet/setMetaData)
* [setOriginalRow()](/Java/CachedRowSet/setOriginalRow)
* [setPageSize()](/Java/CachedRowSet/setPageSize)
* [setShowDeleted()](/Java/CachedRowSet/setShowDeleted)
* [setSyncProvider()](/Java/CachedRowSet/setSyncProvider)
* [setTableName()](/Java/CachedRowSet/setTableName)
* [size()](/Java/CachedRowSet/size)
* [toCollection()](/Java/CachedRowSet/toCollection)
* [undoDelete()](/Java/CachedRowSet/undoDelete)
* [undoInsert()](/Java/CachedRowSet/undoInsert)
* [undoUpdate()](/Java/CachedRowSet/undoUpdate)

## Ejemplo
~~~java
{{ site.data.Java.C.CachedRowSet.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CachedRowSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
