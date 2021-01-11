---
title: DragGestureRecognizer
permalink: Java/DragGestureRecognizer
date: 2021-01-11
key: JavaJava.D.DragGestureRecognizer
category: java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DragGestureRecognizer.description }}

## Sintaxis
~~~java
public abstract class DragGestureRecognizer extends Object implements Serializable
~~~

## Constructores
* [DragGestureRecognizer()](/Java/DragGestureRecognizer/DragGestureRecognizer/)

## Campos
* [component](/Java/DragGestureRecognizer/component)
* [dragGestureListener](/Java/DragGestureRecognizer/dragGestureListener)
* [dragSource](/Java/DragGestureRecognizer/dragSource)
* [events](/Java/DragGestureRecognizer/events)
* [sourceActions](/Java/DragGestureRecognizer/sourceActions)

## Métodos
* [addDragGestureListener()](/Java/DragGestureRecognizer/addDragGestureListener)
* [appendEvent()](/Java/DragGestureRecognizer/appendEvent)
* [fireDragGestureRecognized()](/Java/DragGestureRecognizer/fireDragGestureRecognized)
* [getComponent()](/Java/DragGestureRecognizer/getComponent)
* [getDragSource()](/Java/DragGestureRecognizer/getDragSource)
* [getSourceActions()](/Java/DragGestureRecognizer/getSourceActions)
* [getTriggerEvent()](/Java/DragGestureRecognizer/getTriggerEvent)
* [registerListeners()](/Java/DragGestureRecognizer/registerListeners)
* [removeDragGestureListener()](/Java/DragGestureRecognizer/removeDragGestureListener)
* [resetRecognizer()](/Java/DragGestureRecognizer/resetRecognizer)
* [setComponent()](/Java/DragGestureRecognizer/setComponent)
* [setSourceActions()](/Java/DragGestureRecognizer/setSourceActions)
* [unregisterListeners()](/Java/DragGestureRecognizer/unregisterListeners)

## Ejemplo
~~~java
{{ site.data.Java.D.DragGestureRecognizer.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DragGestureRecognizer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
