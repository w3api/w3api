---
title: DragSource
permalink: /Java/DragSource/
date: 2021-01-11
key: Java.D.DragSource
category: Java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DragSource.description }}

## Sintaxis
~~~java
public class DragSource extends Object implements Serializable
~~~

## Constructores
* [DragSource()](/Java/DragSource/DragSource/)

## Campos
* [DefaultCopyDrop](/Java/DragSource/DefaultCopyDrop/)
* [DefaultCopyNoDrop](/Java/DragSource/DefaultCopyNoDrop/)
* [DefaultLinkDrop](/Java/DragSource/DefaultLinkDrop/)
* [DefaultLinkNoDrop](/Java/DragSource/DefaultLinkNoDrop/)
* [DefaultMoveDrop](/Java/DragSource/DefaultMoveDrop/)
* [DefaultMoveNoDrop](/Java/DragSource/DefaultMoveNoDrop/)

## Métodos
* [addDragSourceListener()](/Java/DragSource/addDragSourceListener/)
* [addDragSourceMotionListener()](/Java/DragSource/addDragSourceMotionListener/)
* [createDefaultDragGestureRecognizer()](/Java/DragSource/createDefaultDragGestureRecognizer/)
* [createDragGestureRecognizer()](/Java/DragSource/createDragGestureRecognizer/)
* [createDragSourceContext()](/Java/DragSource/createDragSourceContext/)
* [getDefaultDragSource()](/Java/DragSource/getDefaultDragSource/)
* [getDragSourceListeners()](/Java/DragSource/getDragSourceListeners/)
* [getDragSourceMotionListeners()](/Java/DragSource/getDragSourceMotionListeners/)
* [getDragThreshold()](/Java/DragSource/getDragThreshold/)
* [getFlavorMap()](/Java/DragSource/getFlavorMap/)
* [getListeners()](/Java/DragSource/getListeners/)
* [isDragImageSupported()](/Java/DragSource/isDragImageSupported/)
* [removeDragSourceListener()](/Java/DragSource/removeDragSourceListener/)
* [removeDragSourceMotionListener()](/Java/DragSource/removeDragSourceMotionListener/)
* [startDrag()](/Java/DragSource/startDrag/)

## Ejemplo
~~~java
{{ site.data.Java.D.DragSource.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DragSource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
