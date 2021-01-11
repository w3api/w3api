---
title: AbstractTableModel
permalink: Java/AbstractTableModel
date: 2021-01-10
key: JavaJava.A.AbstractTableModel
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AbstractTableModel.description }}

## Sintaxis
~~~java
public abstract class AbstractTableModel extends Object implements TableModel, Serializable
~~~

## Constructores
* [AbstractTableModel()](/Java/AbstractTableModel/AbstractTableModel/)

## Campos
* [listenerList](/Java/AbstractTableModel/listenerList)

## Métodos
* [addTableModelListener()](/Java/AbstractTableModel/addTableModelListener)
* [findColumn()](/Java/AbstractTableModel/findColumn)
* [fireTableCellUpdated()](/Java/AbstractTableModel/fireTableCellUpdated)
* [fireTableChanged()](/Java/AbstractTableModel/fireTableChanged)
* [fireTableDataChanged()](/Java/AbstractTableModel/fireTableDataChanged)
* [fireTableRowsDeleted()](/Java/AbstractTableModel/fireTableRowsDeleted)
* [fireTableRowsInserted()](/Java/AbstractTableModel/fireTableRowsInserted)
* [fireTableRowsUpdated()](/Java/AbstractTableModel/fireTableRowsUpdated)
* [fireTableStructureChanged()](/Java/AbstractTableModel/fireTableStructureChanged)
* [getColumnClass()](/Java/AbstractTableModel/getColumnClass)
* [getColumnName()](/Java/AbstractTableModel/getColumnName)
* [getListeners()](/Java/AbstractTableModel/getListeners)
* [getTableModelListeners()](/Java/AbstractTableModel/getTableModelListeners)
* [isCellEditable()](/Java/AbstractTableModel/isCellEditable)
* [removeTableModelListener()](/Java/AbstractTableModel/removeTableModelListener)
* [setValueAt()](/Java/AbstractTableModel/setValueAt)

## Ejemplo
~~~java
{{ site.data.Java.A.AbstractTableModel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractTableModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
