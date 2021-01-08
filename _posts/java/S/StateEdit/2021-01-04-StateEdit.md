---
title: StateEdit
permalink: Java/StateEdit
date: 2021-01-04
key: JavaJava.S.StateEdit
category: java
tags: ['java se', 'javax.swing.undo', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StateEdit.description }}

## Sintaxis
~~~java
public class StateEdit extends AbstractUndoableEdit
~~~

## Constructores
* [StateEdit()](/Java/StateEdit/StateEdit/)

## Campos
* [object](/Java/StateEdit/object)
* [postState](/Java/StateEdit/postState)
* [preState](/Java/StateEdit/preState)
* [RCSID](/Java/StateEdit/RCSID)
* [undoRedoName](/Java/StateEdit/undoRedoName)

## Métodos
* [end()](/Java/StateEdit/end)
* [getPresentationName()](/Java/StateEdit/getPresentationName)
* [init()](/Java/StateEdit/init)
* [redo()](/Java/StateEdit/redo)
* [removeRedundantState()](/Java/StateEdit/removeRedundantState)
* [undo()](/Java/StateEdit/undo)

## Ejemplo
~~~java
{{ site.data.Java.S.StateEdit.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StateEdit.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
