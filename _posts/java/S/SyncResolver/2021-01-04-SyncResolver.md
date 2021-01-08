---
title: SyncResolver
permalink: Java/SyncResolver
date: 2021-01-04
key: JavaJava.S.SyncResolver
category: java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SyncResolver.description }}

## Sintaxis
~~~java
public interface SyncResolver extends RowSet
~~~

## Campos
* [DELETE_ROW_CONFLICT](/Java/SyncResolver/DELETE_ROW_CONFLICT)
* [INSERT_ROW_CONFLICT](/Java/SyncResolver/INSERT_ROW_CONFLICT)
* [NO_ROW_CONFLICT](/Java/SyncResolver/NO_ROW_CONFLICT)
* [UPDATE_ROW_CONFLICT](/Java/SyncResolver/UPDATE_ROW_CONFLICT)

## Métodos
* [getConflictValue()](/Java/SyncResolver/getConflictValue)
* [getStatus()](/Java/SyncResolver/getStatus)
* [nextConflict()](/Java/SyncResolver/nextConflict)
* [previousConflict()](/Java/SyncResolver/previousConflict)
* [setResolvedValue()](/Java/SyncResolver/setResolvedValue)

## Ejemplo
~~~java
{{ site.data.Java.S.SyncResolver.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SyncResolver.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
