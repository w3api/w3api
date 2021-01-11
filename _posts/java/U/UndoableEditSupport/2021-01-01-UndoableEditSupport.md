---
title: UndoableEditSupport
permalink: Java/UndoableEditSupport
date: 2021-01-11
key: JavaJava.U.UndoableEditSupport
category: java
tags: ['java se', 'javax.swing.undo', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.U.UndoableEditSupport.description }}

## Sintaxis
~~~java
public class UndoableEditSupport extends Object
~~~

## Constructores
* [UndoableEditSupport()](/Java/UndoableEditSupport/UndoableEditSupport/)

## Campos
* [compoundEdit](/Java/UndoableEditSupport/compoundEdit)
* [listeners](/Java/UndoableEditSupport/listeners)
* [realSource](/Java/UndoableEditSupport/realSource)
* [updateLevel](/Java/UndoableEditSupport/updateLevel)

## Métodos
* [_postEdit()](/Java/UndoableEditSupport/_postEdit)
* [addUndoableEditListener()](/Java/UndoableEditSupport/addUndoableEditListener)
* [beginUpdate()](/Java/UndoableEditSupport/beginUpdate)
* [createCompoundEdit()](/Java/UndoableEditSupport/createCompoundEdit)
* [endUpdate()](/Java/UndoableEditSupport/endUpdate)
* [getUndoableEditListeners()](/Java/UndoableEditSupport/getUndoableEditListeners)
* [getUpdateLevel()](/Java/UndoableEditSupport/getUpdateLevel)
* [postEdit()](/Java/UndoableEditSupport/postEdit)
* [removeUndoableEditListener()](/Java/UndoableEditSupport/removeUndoableEditListener)
* [toString()](/Java/UndoableEditSupport/toString)

## Ejemplo
~~~java
{{ site.data.Java.U.UndoableEditSupport.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UndoableEditSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
