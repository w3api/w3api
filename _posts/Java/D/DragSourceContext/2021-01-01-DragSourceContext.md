---
title: DragSourceContext
permalink: /Java/DragSourceContext/
date: 2021-01-11
key: Java.D.DragSourceContext
category: Java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DragSourceContext.description }}

## Sintaxis
~~~java
public class DragSourceContext extends Object implements DragSourceListener, DragSourceMotionListener, Serializable
~~~

## Constructores
* [DragSourceContext()](/Java/DragSourceContext/DragSourceContext/)

## Campos
* [CHANGED](/Java/DragSourceContext/CHANGED/)
* [DEFAULT](/Java/DragSourceContext/DEFAULT/)
* [ENTER](/Java/DragSourceContext/ENTER/)
* [OVER](/Java/DragSourceContext/OVER/)

## Métodos
* [addDragSourceListener()](/Java/DragSourceContext/addDragSourceListener/)
* [dragDropEnd()](/Java/DragSourceContext/dragDropEnd/)
* [dragEnter()](/Java/DragSourceContext/dragEnter/)
* [dragExit()](/Java/DragSourceContext/dragExit/)
* [dragMouseMoved()](/Java/DragSourceContext/dragMouseMoved/)
* [dragOver()](/Java/DragSourceContext/dragOver/)
* [dropActionChanged()](/Java/DragSourceContext/dropActionChanged/)
* [getComponent()](/Java/DragSourceContext/getComponent/)
* [getCursor()](/Java/DragSourceContext/getCursor/)
* [getDragSource()](/Java/DragSourceContext/getDragSource/)
* [getSourceActions()](/Java/DragSourceContext/getSourceActions/)
* [getTransferable()](/Java/DragSourceContext/getTransferable/)
* [getTrigger()](/Java/DragSourceContext/getTrigger/)
* [removeDragSourceListener()](/Java/DragSourceContext/removeDragSourceListener/)
* [setCursor()](/Java/DragSourceContext/setCursor/)
* [transferablesFlavorsChanged()](/Java/DragSourceContext/transferablesFlavorsChanged/)
* [updateCurrentCursor()](/Java/DragSourceContext/updateCurrentCursor/)

## Ejemplo
~~~java
{{ site.data.Java.D.DragSourceContext.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DragSourceContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
