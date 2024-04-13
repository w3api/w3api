---
title: AbstractCellEditor
permalink: /Java/AbstractCellEditor/
date: 2021-01-11
key: Java.A.AbstractCellEditor
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'clase java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AbstractCellEditor.description }}

## Sintaxis
~~~java
public abstract class AbstractCellEditor extends Object implements CellEditor, Serializable
~~~

## Constructores
* [AbstractCellEditor()](/Java/AbstractCellEditor/AbstractCellEditor/)

## Campos
* [changeEvent](/Java/AbstractCellEditor/changeEvent)
* [listenerList](/Java/AbstractCellEditor/listenerList)

## Métodos
* [addCellEditorListener()](/Java/AbstractCellEditor/addCellEditorListener)
* [cancelCellEditing()](/Java/AbstractCellEditor/cancelCellEditing)
* [fireEditingCanceled()](/Java/AbstractCellEditor/fireEditingCanceled)
* [fireEditingStopped()](/Java/AbstractCellEditor/fireEditingStopped)
* [getCellEditorListeners()](/Java/AbstractCellEditor/getCellEditorListeners)
* [isCellEditable()](/Java/AbstractCellEditor/isCellEditable)
* [removeCellEditorListener()](/Java/AbstractCellEditor/removeCellEditorListener)
* [shouldSelectCell()](/Java/AbstractCellEditor/shouldSelectCell)
* [stopCellEditing()](/Java/AbstractCellEditor/stopCellEditing)

## Ejemplo
~~~java
{{ site.data.Java.A.AbstractCellEditor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractCellEditor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
