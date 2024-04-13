---
title: JoinRowSet
permalink: /Java/JoinRowSet/
date: 2021-01-11
key: Java.J.JoinRowSet
category: Java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JoinRowSet.description }}

## Sintaxis
~~~java
public interface JoinRowSet extends WebRowSet
~~~

## Campos
* [CROSS_JOIN](/Java/JoinRowSet/CROSS_JOIN)
* [FULL_JOIN](/Java/JoinRowSet/FULL_JOIN)
* [INNER_JOIN](/Java/JoinRowSet/INNER_JOIN)
* [LEFT_OUTER_JOIN](/Java/JoinRowSet/LEFT_OUTER_JOIN)
* [RIGHT_OUTER_JOIN](/Java/JoinRowSet/RIGHT_OUTER_JOIN)

## Métodos
* [addRowSet()](/Java/JoinRowSet/addRowSet)
* [getJoinType()](/Java/JoinRowSet/getJoinType)
* [getRowSetNames()](/Java/JoinRowSet/getRowSetNames)
* [getRowSets()](/Java/JoinRowSet/getRowSets)
* [getWhereClause()](/Java/JoinRowSet/getWhereClause)
* [setJoinType()](/Java/JoinRowSet/setJoinType)
* [supportsCrossJoin()](/Java/JoinRowSet/supportsCrossJoin)
* [supportsFullJoin()](/Java/JoinRowSet/supportsFullJoin)
* [supportsInnerJoin()](/Java/JoinRowSet/supportsInnerJoin)
* [supportsLeftOuterJoin()](/Java/JoinRowSet/supportsLeftOuterJoin)
* [supportsRightOuterJoin()](/Java/JoinRowSet/supportsRightOuterJoin)
* [toCachedRowSet()](/Java/JoinRowSet/toCachedRowSet)

## Ejemplo
~~~java
{{ site.data.Java.J.JoinRowSet.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JoinRowSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
