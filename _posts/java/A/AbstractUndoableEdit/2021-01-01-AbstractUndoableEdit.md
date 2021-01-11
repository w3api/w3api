---
title: AbstractUndoableEdit
permalink: Java/AbstractUndoableEdit
date: 2021-01-11
key: JavaJava.A.AbstractUndoableEdit
category: java
tags: ['java se', 'javax.swing.undo', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AbstractUndoableEdit.description }}

## Sintaxis
~~~java
public class AbstractUndoableEdit extends Object implements UndoableEdit, Serializable
~~~

## Constructores
* [AbstractUndoableEdit()](/Java/AbstractUndoableEdit/AbstractUndoableEdit/)

## Campos
* [RedoName](/Java/AbstractUndoableEdit/RedoName)
* [UndoName](/Java/AbstractUndoableEdit/UndoName)

## Métodos
* [addEdit()](/Java/AbstractUndoableEdit/addEdit)
* [canRedo()](/Java/AbstractUndoableEdit/canRedo)
* [canUndo()](/Java/AbstractUndoableEdit/canUndo)
* [die()](/Java/AbstractUndoableEdit/die)
* [getPresentationName()](/Java/AbstractUndoableEdit/getPresentationName)
* [getRedoPresentationName()](/Java/AbstractUndoableEdit/getRedoPresentationName)
* [getUndoPresentationName()](/Java/AbstractUndoableEdit/getUndoPresentationName)
* [isSignificant()](/Java/AbstractUndoableEdit/isSignificant)
* [redo()](/Java/AbstractUndoableEdit/redo)
* [replaceEdit()](/Java/AbstractUndoableEdit/replaceEdit)
* [toString()](/Java/AbstractUndoableEdit/toString)
* [undo()](/Java/AbstractUndoableEdit/undo)

## Ejemplo
~~~java
{{ site.data.Java.A.AbstractUndoableEdit.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractUndoableEdit.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
