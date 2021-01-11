---
title: TableRowSorter
permalink: Java/TableRowSorter
date: 2021-01-11
key: JavaJava.T.TableRowSorter
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TableRowSorter.description }}

## Sintaxis
~~~java
public class TableRowSorter<M extends TableModel> extends DefaultRowSorter<M,Integer>
~~~

## Constructores
* [TableRowSorter()](/Java/TableRowSorter/TableRowSorter/)

## Métodos
* [getComparator()](/Java/TableRowSorter/getComparator)
* [getStringConverter()](/Java/TableRowSorter/getStringConverter)
* [setModel()](/Java/TableRowSorter/setModel)
* [setStringConverter()](/Java/TableRowSorter/setStringConverter)
* [useToString()](/Java/TableRowSorter/useToString)

## Ejemplo
~~~java
{{ site.data.Java.T.TableRowSorter.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TableRowSorter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
