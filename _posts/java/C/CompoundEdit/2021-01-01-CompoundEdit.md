---
title: CompoundEdit
permalink: Java/CompoundEdit
date: 2021-01-11
key: JavaJava.C.CompoundEdit
category: java
tags: ['java se', 'javax.swing.undo', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CompoundEdit.description }}

## Sintaxis
~~~java
public class CompoundEdit extends AbstractUndoableEdit
~~~

## Constructores
* [CompoundEdit()](/Java/CompoundEdit/CompoundEdit/)

## Campos
* [edits](/Java/CompoundEdit/edits)

## Métodos
* [addEdit()](/Java/CompoundEdit/addEdit)
* [canRedo()](/Java/CompoundEdit/canRedo)
* [canUndo()](/Java/CompoundEdit/canUndo)
* [die()](/Java/CompoundEdit/die)
* [end()](/Java/CompoundEdit/end)
* [getPresentationName()](/Java/CompoundEdit/getPresentationName)
* [getRedoPresentationName()](/Java/CompoundEdit/getRedoPresentationName)
* [getUndoPresentationName()](/Java/CompoundEdit/getUndoPresentationName)
* [isInProgress()](/Java/CompoundEdit/isInProgress)
* [isSignificant()](/Java/CompoundEdit/isSignificant)
* [lastEdit()](/Java/CompoundEdit/lastEdit)
* [redo()](/Java/CompoundEdit/redo)
* [toString()](/Java/CompoundEdit/toString)
* [undo()](/Java/CompoundEdit/undo)

## Ejemplo
~~~java
{{ site.data.Java.C.CompoundEdit.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompoundEdit.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
