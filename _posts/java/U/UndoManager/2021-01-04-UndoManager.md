---
title: UndoManager
permalink: Java/UndoManager
date: 2021-01-04
key: JavaJava.U.UndoManager
category: java
tags: ['java se', 'javax.swing.undo', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.U.UndoManager.description }}

## Sintaxis
~~~java
public class UndoManager extends CompoundEdit implements UndoableEditListener
~~~

## Constructores
* [UndoManager()](/Java/UndoManager/UndoManager/)

## Métodos
* [addEdit()](/Java/UndoManager/addEdit)
* [canRedo()](/Java/UndoManager/canRedo)
* [canUndo()](/Java/UndoManager/canUndo)
* [canUndoOrRedo()](/Java/UndoManager/canUndoOrRedo)
* [discardAllEdits()](/Java/UndoManager/discardAllEdits)
* [editToBeRedone()](/Java/UndoManager/editToBeRedone)
* [editToBeUndone()](/Java/UndoManager/editToBeUndone)
* [end()](/Java/UndoManager/end)
* [getLimit()](/Java/UndoManager/getLimit)
* [getRedoPresentationName()](/Java/UndoManager/getRedoPresentationName)
* [getUndoOrRedoPresentationName()](/Java/UndoManager/getUndoOrRedoPresentationName)
* [getUndoPresentationName()](/Java/UndoManager/getUndoPresentationName)
* [redo()](/Java/UndoManager/redo)
* [redoTo()](/Java/UndoManager/redoTo)
* [setLimit()](/Java/UndoManager/setLimit)
* [toString()](/Java/UndoManager/toString)
* [trimEdits()](/Java/UndoManager/trimEdits)
* [trimForLimit()](/Java/UndoManager/trimForLimit)
* [undo()](/Java/UndoManager/undo)
* [undoableEditHappened()](/Java/UndoManager/undoableEditHappened)
* [undoOrRedo()](/Java/UndoManager/undoOrRedo)
* [undoTo()](/Java/UndoManager/undoTo)

## Ejemplo
~~~java
{{ site.data.Java.U.UndoManager.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UndoManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
