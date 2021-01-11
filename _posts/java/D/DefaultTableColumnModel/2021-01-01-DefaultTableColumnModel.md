---
title: DefaultTableColumnModel
permalink: Java/DefaultTableColumnModel
date: 2021-01-11
key: JavaJava.D.DefaultTableColumnModel
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DefaultTableColumnModel.description }}

## Sintaxis
~~~java
public class DefaultTableColumnModel extends Object implements TableColumnModel, PropertyChangeListener, ListSelectionListener, Serializable
~~~

## Constructores
* [DefaultTableColumnModel()](/Java/DefaultTableColumnModel/DefaultTableColumnModel/)

## Campos
* [changeEvent](/Java/DefaultTableColumnModel/changeEvent)
* [columnMargin](/Java/DefaultTableColumnModel/columnMargin)
* [columnSelectionAllowed](/Java/DefaultTableColumnModel/columnSelectionAllowed)
* [listenerList](/Java/DefaultTableColumnModel/listenerList)
* [selectionModel](/Java/DefaultTableColumnModel/selectionModel)
* [tableColumns](/Java/DefaultTableColumnModel/tableColumns)
* [totalColumnWidth](/Java/DefaultTableColumnModel/totalColumnWidth)

## Métodos
* [addColumn()](/Java/DefaultTableColumnModel/addColumn)
* [addColumnModelListener()](/Java/DefaultTableColumnModel/addColumnModelListener)
* [createSelectionModel()](/Java/DefaultTableColumnModel/createSelectionModel)
* [fireColumnAdded()](/Java/DefaultTableColumnModel/fireColumnAdded)
* [fireColumnMarginChanged()](/Java/DefaultTableColumnModel/fireColumnMarginChanged)
* [fireColumnMoved()](/Java/DefaultTableColumnModel/fireColumnMoved)
* [fireColumnRemoved()](/Java/DefaultTableColumnModel/fireColumnRemoved)
* [fireColumnSelectionChanged()](/Java/DefaultTableColumnModel/fireColumnSelectionChanged)
* [getColumn()](/Java/DefaultTableColumnModel/getColumn)
* [getColumnCount()](/Java/DefaultTableColumnModel/getColumnCount)
* [getColumnIndex()](/Java/DefaultTableColumnModel/getColumnIndex)
* [getColumnIndexAtX()](/Java/DefaultTableColumnModel/getColumnIndexAtX)
* [getColumnMargin()](/Java/DefaultTableColumnModel/getColumnMargin)
* [getColumnModelListeners()](/Java/DefaultTableColumnModel/getColumnModelListeners)
* [getColumns()](/Java/DefaultTableColumnModel/getColumns)
* [getColumnSelectionAllowed()](/Java/DefaultTableColumnModel/getColumnSelectionAllowed)
* [getListeners()](/Java/DefaultTableColumnModel/getListeners)
* [getSelectedColumnCount()](/Java/DefaultTableColumnModel/getSelectedColumnCount)
* [getSelectedColumns()](/Java/DefaultTableColumnModel/getSelectedColumns)
* [getSelectionModel()](/Java/DefaultTableColumnModel/getSelectionModel)
* [getTotalColumnWidth()](/Java/DefaultTableColumnModel/getTotalColumnWidth)
* [moveColumn()](/Java/DefaultTableColumnModel/moveColumn)
* [propertyChange()](/Java/DefaultTableColumnModel/propertyChange)
* [recalcWidthCache()](/Java/DefaultTableColumnModel/recalcWidthCache)
* [removeColumn()](/Java/DefaultTableColumnModel/removeColumn)
* [removeColumnModelListener()](/Java/DefaultTableColumnModel/removeColumnModelListener)
* [setColumnMargin()](/Java/DefaultTableColumnModel/setColumnMargin)
* [setColumnSelectionAllowed()](/Java/DefaultTableColumnModel/setColumnSelectionAllowed)
* [setSelectionModel()](/Java/DefaultTableColumnModel/setSelectionModel)
* [valueChanged()](/Java/DefaultTableColumnModel/valueChanged)

## Ejemplo
~~~java
{{ site.data.Java.D.DefaultTableColumnModel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultTableColumnModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
