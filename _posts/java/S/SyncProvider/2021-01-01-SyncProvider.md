---
title: SyncProvider
permalink: Java/SyncProvider
date: 2021-01-11
key: JavaJava.S.SyncProvider
category: java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SyncProvider.description }}

## Sintaxis
~~~java
public abstract class SyncProvider extends Object
~~~

## Constructores
* [SyncProvider()](/Java/SyncProvider/SyncProvider/)

## Campos
* [DATASOURCE_DB_LOCK](/Java/SyncProvider/DATASOURCE_DB_LOCK)
* [DATASOURCE_NO_LOCK](/Java/SyncProvider/DATASOURCE_NO_LOCK)
* [DATASOURCE_ROW_LOCK](/Java/SyncProvider/DATASOURCE_ROW_LOCK)
* [DATASOURCE_TABLE_LOCK](/Java/SyncProvider/DATASOURCE_TABLE_LOCK)
* [GRADE_CHECK_ALL_AT_COMMIT](/Java/SyncProvider/GRADE_CHECK_ALL_AT_COMMIT)
* [GRADE_CHECK_MODIFIED_AT_COMMIT](/Java/SyncProvider/GRADE_CHECK_MODIFIED_AT_COMMIT)
* [GRADE_LOCK_WHEN_LOADED](/Java/SyncProvider/GRADE_LOCK_WHEN_LOADED)
* [GRADE_LOCK_WHEN_MODIFIED](/Java/SyncProvider/GRADE_LOCK_WHEN_MODIFIED)
* [GRADE_NONE](/Java/SyncProvider/GRADE_NONE)
* [NONUPDATABLE_VIEW_SYNC](/Java/SyncProvider/NONUPDATABLE_VIEW_SYNC)
* [UPDATABLE_VIEW_SYNC](/Java/SyncProvider/UPDATABLE_VIEW_SYNC)

## Métodos
* [getDataSourceLock()](/Java/SyncProvider/getDataSourceLock)
* [getProviderGrade()](/Java/SyncProvider/getProviderGrade)
* [getProviderID()](/Java/SyncProvider/getProviderID)
* [getRowSetReader()](/Java/SyncProvider/getRowSetReader)
* [getRowSetWriter()](/Java/SyncProvider/getRowSetWriter)
* [getVendor()](/Java/SyncProvider/getVendor)
* [getVersion()](/Java/SyncProvider/getVersion)
* [setDataSourceLock()](/Java/SyncProvider/setDataSourceLock)
* [supportsUpdatableView()](/Java/SyncProvider/supportsUpdatableView)

## Ejemplo
~~~java
{{ site.data.Java.S.SyncProvider.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SyncProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
