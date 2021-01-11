---
title: UndoableEdit
permalink: Java/UndoableEdit
date: 2021-01-11
key: JavaJava.U.UndoableEdit
category: java
tags: ['java se', 'javax.swing.undo', 'java.desktop', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.U.UndoableEdit.description }}

## Sintaxis
~~~java
public interface UndoableEdit
~~~

## Métodos
* [addEdit()](/Java/UndoableEdit/addEdit)
* [canRedo()](/Java/UndoableEdit/canRedo)
* [canUndo()](/Java/UndoableEdit/canUndo)
* [die()](/Java/UndoableEdit/die)
* [getPresentationName()](/Java/UndoableEdit/getPresentationName)
* [getRedoPresentationName()](/Java/UndoableEdit/getRedoPresentationName)
* [getUndoPresentationName()](/Java/UndoableEdit/getUndoPresentationName)
* [isSignificant()](/Java/UndoableEdit/isSignificant)
* [redo()](/Java/UndoableEdit/redo)
* [replaceEdit()](/Java/UndoableEdit/replaceEdit)
* [undo()](/Java/UndoableEdit/undo)

## Ejemplo
~~~java
{{ site.data.Java.U.UndoableEdit.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UndoableEdit.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
