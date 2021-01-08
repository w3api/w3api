---
title: JViewport
permalink: Java/JViewport
date: 2021-01-04
key: JavaJava.J.JViewport
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JViewport.description }}

## Sintaxis
~~~java
public class JViewport extends JComponent implements Accessible
~~~

## Constructores
* [JViewport()](/Java/JViewport/JViewport/)

## Campos
* [backingStore](/Java/JViewport/backingStore)
* [BACKINGSTORE_SCROLL_MODE](/Java/JViewport/BACKINGSTORE_SCROLL_MODE)
* [backingStoreImage](/Java/JViewport/backingStoreImage)
* [BLIT_SCROLL_MODE](/Java/JViewport/BLIT_SCROLL_MODE)
* [isViewSizeSet](/Java/JViewport/isViewSizeSet)
* [lastPaintPosition](/Java/JViewport/lastPaintPosition)
* [scrollUnderway](/Java/JViewport/scrollUnderway)
* [SIMPLE_SCROLL_MODE](/Java/JViewport/SIMPLE_SCROLL_MODE)

## Métodos
* [addChangeListener()](/Java/JViewport/addChangeListener)
* [addImpl()](/Java/JViewport/addImpl)
* [computeBlit()](/Java/JViewport/computeBlit)
* [createLayoutManager()](/Java/JViewport/createLayoutManager)
* [createViewListener()](/Java/JViewport/createViewListener)
* [firePropertyChange()](/Java/JViewport/firePropertyChange)
* [fireStateChanged()](/Java/JViewport/fireStateChanged)
* [getAccessibleContext()](/Java/JViewport/getAccessibleContext)
* [getChangeListeners()](/Java/JViewport/getChangeListeners)
* [getExtentSize()](/Java/JViewport/getExtentSize)
* [getInsets()](/Java/JViewport/getInsets)
* [getScrollMode()](/Java/JViewport/getScrollMode)
* [getUI()](/Java/JViewport/getUI)
* [getUIClassID()](/Java/JViewport/getUIClassID)
* [getView()](/Java/JViewport/getView)
* [getViewPosition()](/Java/JViewport/getViewPosition)
* [getViewRect()](/Java/JViewport/getViewRect)
* [getViewSize()](/Java/JViewport/getViewSize)
* [isBackingStoreEnabled()](/Java/JViewport/isBackingStoreEnabled)
* [isOptimizedDrawingEnabled()](/Java/JViewport/isOptimizedDrawingEnabled)
* [isPaintingOrigin()](/Java/JViewport/isPaintingOrigin)
* [paint()](/Java/JViewport/paint)
* [paramString()](/Java/JViewport/paramString)
* [remove()](/Java/JViewport/remove)
* [removeChangeListener()](/Java/JViewport/removeChangeListener)
* [repaint()](/Java/JViewport/repaint)
* [reshape()](/Java/JViewport/reshape)
* [scrollRectToVisible()](/Java/JViewport/scrollRectToVisible)
* [setBackingStoreEnabled()](/Java/JViewport/setBackingStoreEnabled)
* [setBorder()](/Java/JViewport/setBorder)
* [setExtentSize()](/Java/JViewport/setExtentSize)
* [setScrollMode()](/Java/JViewport/setScrollMode)
* [setUI()](/Java/JViewport/setUI)
* [setView()](/Java/JViewport/setView)
* [setViewPosition()](/Java/JViewport/setViewPosition)
* [setViewSize()](/Java/JViewport/setViewSize)
* [toViewCoordinates()](/Java/JViewport/toViewCoordinates)
* [updateUI()](/Java/JViewport/updateUI)

## Ejemplo
~~~java
{{ site.data.Java.J.JViewport.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JViewport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
