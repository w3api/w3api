---
title: DropTargetDropEvent
permalink: Java/DropTargetDropEvent
date: 2021-01-04
key: JavaJava.D.DropTargetDropEvent
category: java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DropTargetDropEvent.description }}

## Sintaxis
~~~java
public class DropTargetDropEvent extends DropTargetEvent
~~~

## Constructores
* [DropTargetDropEvent()](/Java/DropTargetDropEvent/DropTargetDropEvent/)

## Métodos
* [acceptDrop()](/Java/DropTargetDropEvent/acceptDrop)
* [dropComplete()](/Java/DropTargetDropEvent/dropComplete)
* [getCurrentDataFlavors()](/Java/DropTargetDropEvent/getCurrentDataFlavors)
* [getCurrentDataFlavorsAsList()](/Java/DropTargetDropEvent/getCurrentDataFlavorsAsList)
* [getDropAction()](/Java/DropTargetDropEvent/getDropAction)
* [getLocation()](/Java/DropTargetDropEvent/getLocation)
* [getSourceActions()](/Java/DropTargetDropEvent/getSourceActions)
* [getTransferable()](/Java/DropTargetDropEvent/getTransferable)
* [isDataFlavorSupported()](/Java/DropTargetDropEvent/isDataFlavorSupported)
* [isLocalTransfer()](/Java/DropTargetDropEvent/isLocalTransfer)
* [rejectDrop()](/Java/DropTargetDropEvent/rejectDrop)

## Ejemplo
~~~java
{{ site.data.Java.D.DropTargetDropEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DropTargetDropEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
