---
title: DefaultTreeCellEditor
permalink: /Java/DefaultTreeCellEditor/
date: 2021-01-11
key: Java.D.DefaultTreeCellEditor
category: Java
tags: ['java se', 'javax.swing.tree', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DefaultTreeCellEditor.description }}

## Sintaxis
~~~java
public class DefaultTreeCellEditor extends Object implements ActionListener, TreeCellEditor, TreeSelectionListener
~~~

## Constructores
* [DefaultTreeCellEditor()](/Java/DefaultTreeCellEditor/DefaultTreeCellEditor/)

## Campos
* [borderSelectionColor](/Java/DefaultTreeCellEditor/borderSelectionColor)
* [canEdit](/Java/DefaultTreeCellEditor/canEdit)
* [editingComponent](/Java/DefaultTreeCellEditor/editingComponent)
* [editingContainer](/Java/DefaultTreeCellEditor/editingContainer)
* [editingIcon](/Java/DefaultTreeCellEditor/editingIcon)
* [font](/Java/DefaultTreeCellEditor/font)
* [lastPath](/Java/DefaultTreeCellEditor/lastPath)
* [lastRow](/Java/DefaultTreeCellEditor/lastRow)
* [offset](/Java/DefaultTreeCellEditor/offset)
* [realEditor](/Java/DefaultTreeCellEditor/realEditor)
* [renderer](/Java/DefaultTreeCellEditor/renderer)
* [timer](/Java/DefaultTreeCellEditor/timer)
* [tree](/Java/DefaultTreeCellEditor/tree)

## Métodos
* [actionPerformed()](/Java/DefaultTreeCellEditor/actionPerformed)
* [addCellEditorListener()](/Java/DefaultTreeCellEditor/addCellEditorListener)
* [cancelCellEditing()](/Java/DefaultTreeCellEditor/cancelCellEditing)
* [canEditImmediately()](/Java/DefaultTreeCellEditor/canEditImmediately)
* [createContainer()](/Java/DefaultTreeCellEditor/createContainer)
* [createTreeCellEditor()](/Java/DefaultTreeCellEditor/createTreeCellEditor)
* [determineOffset()](/Java/DefaultTreeCellEditor/determineOffset)
* [getBorderSelectionColor()](/Java/DefaultTreeCellEditor/getBorderSelectionColor)
* [getCellEditorListeners()](/Java/DefaultTreeCellEditor/getCellEditorListeners)
* [getCellEditorValue()](/Java/DefaultTreeCellEditor/getCellEditorValue)
* [getFont()](/Java/DefaultTreeCellEditor/getFont)
* [getTreeCellEditorComponent()](/Java/DefaultTreeCellEditor/getTreeCellEditorComponent)
* [inHitRegion()](/Java/DefaultTreeCellEditor/inHitRegion)
* [isCellEditable()](/Java/DefaultTreeCellEditor/isCellEditable)
* [prepareForEditing()](/Java/DefaultTreeCellEditor/prepareForEditing)
* [removeCellEditorListener()](/Java/DefaultTreeCellEditor/removeCellEditorListener)
* [setBorderSelectionColor()](/Java/DefaultTreeCellEditor/setBorderSelectionColor)
* [setFont()](/Java/DefaultTreeCellEditor/setFont)
* [setTree()](/Java/DefaultTreeCellEditor/setTree)
* [shouldSelectCell()](/Java/DefaultTreeCellEditor/shouldSelectCell)
* [shouldStartEditingTimer()](/Java/DefaultTreeCellEditor/shouldStartEditingTimer)
* [startEditingTimer()](/Java/DefaultTreeCellEditor/startEditingTimer)
* [stopCellEditing()](/Java/DefaultTreeCellEditor/stopCellEditing)
* [valueChanged()](/Java/DefaultTreeCellEditor/valueChanged)

## Ejemplo
~~~java
{{ site.data.Java.D.DefaultTreeCellEditor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultTreeCellEditor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
