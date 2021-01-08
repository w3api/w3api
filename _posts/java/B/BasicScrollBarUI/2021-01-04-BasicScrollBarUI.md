---
title: BasicScrollBarUI
permalink: Java/BasicScrollBarUI
date: 2021-01-04
key: JavaJava.B.BasicScrollBarUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BasicScrollBarUI.description }}

## Sintaxis
~~~java
public class BasicScrollBarUI extends ScrollBarUI implements LayoutManager, SwingConstants
~~~

## Constructores
* [BasicScrollBarUI()](/Java/BasicScrollBarUI/BasicScrollBarUI/)

## Campos
* [buttonListener](/Java/BasicScrollBarUI/buttonListener)
* [decrButton](/Java/BasicScrollBarUI/decrButton)
* [DECREASE_HIGHLIGHT](/Java/BasicScrollBarUI/DECREASE_HIGHLIGHT)
* [decrGap](/Java/BasicScrollBarUI/decrGap)
* [incrButton](/Java/BasicScrollBarUI/incrButton)
* [INCREASE_HIGHLIGHT](/Java/BasicScrollBarUI/INCREASE_HIGHLIGHT)
* [incrGap](/Java/BasicScrollBarUI/incrGap)
* [isDragging](/Java/BasicScrollBarUI/isDragging)
* [maximumThumbSize](/Java/BasicScrollBarUI/maximumThumbSize)
* [minimumThumbSize](/Java/BasicScrollBarUI/minimumThumbSize)
* [modelListener](/Java/BasicScrollBarUI/modelListener)
* [NO_HIGHLIGHT](/Java/BasicScrollBarUI/NO_HIGHLIGHT)
* [propertyChangeListener](/Java/BasicScrollBarUI/propertyChangeListener)
* [scrollbar](/Java/BasicScrollBarUI/scrollbar)
* [scrollBarWidth](/Java/BasicScrollBarUI/scrollBarWidth)
* [scrollListener](/Java/BasicScrollBarUI/scrollListener)
* [scrollTimer](/Java/BasicScrollBarUI/scrollTimer)
* [thumbColor](/Java/BasicScrollBarUI/thumbColor)
* [thumbDarkShadowColor](/Java/BasicScrollBarUI/thumbDarkShadowColor)
* [thumbHighlightColor](/Java/BasicScrollBarUI/thumbHighlightColor)
* [thumbLightShadowColor](/Java/BasicScrollBarUI/thumbLightShadowColor)
* [thumbRect](/Java/BasicScrollBarUI/thumbRect)
* [trackColor](/Java/BasicScrollBarUI/trackColor)
* [trackHighlight](/Java/BasicScrollBarUI/trackHighlight)
* [trackHighlightColor](/Java/BasicScrollBarUI/trackHighlightColor)
* [trackListener](/Java/BasicScrollBarUI/trackListener)
* [trackRect](/Java/BasicScrollBarUI/trackRect)

## Métodos
* [configureScrollBarColors()](/Java/BasicScrollBarUI/configureScrollBarColors)
* [createArrowButtonListener()](/Java/BasicScrollBarUI/createArrowButtonListener)
* [createDecreaseButton()](/Java/BasicScrollBarUI/createDecreaseButton)
* [createIncreaseButton()](/Java/BasicScrollBarUI/createIncreaseButton)
* [createModelListener()](/Java/BasicScrollBarUI/createModelListener)
* [createPropertyChangeListener()](/Java/BasicScrollBarUI/createPropertyChangeListener)
* [createScrollListener()](/Java/BasicScrollBarUI/createScrollListener)
* [createTrackListener()](/Java/BasicScrollBarUI/createTrackListener)
* [createUI()](/Java/BasicScrollBarUI/createUI)
* [getMaximumSize()](/Java/BasicScrollBarUI/getMaximumSize)
* [getMaximumThumbSize()](/Java/BasicScrollBarUI/getMaximumThumbSize)
* [getMinimumThumbSize()](/Java/BasicScrollBarUI/getMinimumThumbSize)
* [getPreferredSize()](/Java/BasicScrollBarUI/getPreferredSize)
* [getSupportsAbsolutePositioning()](/Java/BasicScrollBarUI/getSupportsAbsolutePositioning)
* [getThumbBounds()](/Java/BasicScrollBarUI/getThumbBounds)
* [getTrackBounds()](/Java/BasicScrollBarUI/getTrackBounds)
* [installComponents()](/Java/BasicScrollBarUI/installComponents)
* [installDefaults()](/Java/BasicScrollBarUI/installDefaults)
* [installKeyboardActions()](/Java/BasicScrollBarUI/installKeyboardActions)
* [installListeners()](/Java/BasicScrollBarUI/installListeners)
* [installUI()](/Java/BasicScrollBarUI/installUI)
* [isThumbRollover()](/Java/BasicScrollBarUI/isThumbRollover)
* [layoutHScrollbar()](/Java/BasicScrollBarUI/layoutHScrollbar)
* [layoutVScrollbar()](/Java/BasicScrollBarUI/layoutVScrollbar)
* [paintDecreaseHighlight()](/Java/BasicScrollBarUI/paintDecreaseHighlight)
* [paintIncreaseHighlight()](/Java/BasicScrollBarUI/paintIncreaseHighlight)
* [paintThumb()](/Java/BasicScrollBarUI/paintThumb)
* [paintTrack()](/Java/BasicScrollBarUI/paintTrack)
* [scrollByBlock()](/Java/BasicScrollBarUI/scrollByBlock)
* [scrollByUnit()](/Java/BasicScrollBarUI/scrollByUnit)
* [setThumbBounds()](/Java/BasicScrollBarUI/setThumbBounds)
* [setThumbRollover()](/Java/BasicScrollBarUI/setThumbRollover)
* [uninstallComponents()](/Java/BasicScrollBarUI/uninstallComponents)
* [uninstallDefaults()](/Java/BasicScrollBarUI/uninstallDefaults)
* [uninstallKeyboardActions()](/Java/BasicScrollBarUI/uninstallKeyboardActions)
* [uninstallListeners()](/Java/BasicScrollBarUI/uninstallListeners)
* [uninstallUI()](/Java/BasicScrollBarUI/uninstallUI)

## Ejemplo
~~~java
{{ site.data.Java.B.BasicScrollBarUI.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BasicScrollBarUI.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
