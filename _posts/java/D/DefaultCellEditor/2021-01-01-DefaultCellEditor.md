---
title: DefaultCellEditor
permalink: Java/DefaultCellEditor
date: 2021-01-11
key: JavaJava.D.DefaultCellEditor
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DefaultCellEditor.description }}

## Sintaxis
~~~java
public class DefaultCellEditor extends AbstractCellEditor implements TableCellEditor, TreeCellEditor
~~~

## Constructores
* [DefaultCellEditor()](/Java/DefaultCellEditor/DefaultCellEditor/)

## Campos
* [clickCountToStart](/Java/DefaultCellEditor/clickCountToStart)
* [delegate](/Java/DefaultCellEditor/delegate)
* [editorComponent](/Java/DefaultCellEditor/editorComponent)

## Métodos
* [cancelCellEditing()](/Java/DefaultCellEditor/cancelCellEditing)
* [getCellEditorValue()](/Java/DefaultCellEditor/getCellEditorValue)
* [getClickCountToStart()](/Java/DefaultCellEditor/getClickCountToStart)
* [getComponent()](/Java/DefaultCellEditor/getComponent)
* [getTableCellEditorComponent()](/Java/DefaultCellEditor/getTableCellEditorComponent)
* [getTreeCellEditorComponent()](/Java/DefaultCellEditor/getTreeCellEditorComponent)
* [isCellEditable()](/Java/DefaultCellEditor/isCellEditable)
* [setClickCountToStart()](/Java/DefaultCellEditor/setClickCountToStart)
* [shouldSelectCell()](/Java/DefaultCellEditor/shouldSelectCell)
* [stopCellEditing()](/Java/DefaultCellEditor/stopCellEditing)

## Ejemplo
~~~java
{{ site.data.Java.D.DefaultCellEditor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultCellEditor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
