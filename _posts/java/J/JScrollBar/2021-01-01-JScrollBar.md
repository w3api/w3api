---
title: JScrollBar
permalink: Java/JScrollBar
date: 2021-01-11
key: JavaJava.J.JScrollBar
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JScrollBar.description }}

## Sintaxis
~~~java
@JavaBean(defaultProperty="UI", description="A component that helps determine the visible content range of an area.") public class JScrollBar extends JComponent implements Adjustable, Accessible
~~~

## Constructores
* [JScrollBar()](/Java/JScrollBar/JScrollBar/)

## Campos
* [blockIncrement](/Java/JScrollBar/blockIncrement)
* [model](/Java/JScrollBar/model)
* [orientation](/Java/JScrollBar/orientation)
* [unitIncrement](/Java/JScrollBar/unitIncrement)

## Métodos
* [addAdjustmentListener()](/Java/JScrollBar/addAdjustmentListener)
* [fireAdjustmentValueChanged()](/Java/JScrollBar/fireAdjustmentValueChanged)
* [getAccessibleContext()](/Java/JScrollBar/getAccessibleContext)
* [getAdjustmentListeners()](/Java/JScrollBar/getAdjustmentListeners)
* [getBlockIncrement()](/Java/JScrollBar/getBlockIncrement)
* [getMaximum()](/Java/JScrollBar/getMaximum)
* [getMaximumSize()](/Java/JScrollBar/getMaximumSize)
* [getMinimum()](/Java/JScrollBar/getMinimum)
* [getMinimumSize()](/Java/JScrollBar/getMinimumSize)
* [getModel()](/Java/JScrollBar/getModel)
* [getOrientation()](/Java/JScrollBar/getOrientation)
* [getUI()](/Java/JScrollBar/getUI)
* [getUIClassID()](/Java/JScrollBar/getUIClassID)
* [getUnitIncrement()](/Java/JScrollBar/getUnitIncrement)
* [getValue()](/Java/JScrollBar/getValue)
* [getValueIsAdjusting()](/Java/JScrollBar/getValueIsAdjusting)
* [getVisibleAmount()](/Java/JScrollBar/getVisibleAmount)
* [paramString()](/Java/JScrollBar/paramString)
* [removeAdjustmentListener()](/Java/JScrollBar/removeAdjustmentListener)
* [setBlockIncrement()](/Java/JScrollBar/setBlockIncrement)
* [setEnabled()](/Java/JScrollBar/setEnabled)
* [setMaximum()](/Java/JScrollBar/setMaximum)
* [setMinimum()](/Java/JScrollBar/setMinimum)
* [setModel()](/Java/JScrollBar/setModel)
* [setOrientation()](/Java/JScrollBar/setOrientation)
* [setUI()](/Java/JScrollBar/setUI)
* [setUnitIncrement()](/Java/JScrollBar/setUnitIncrement)
* [setValue()](/Java/JScrollBar/setValue)
* [setValueIsAdjusting()](/Java/JScrollBar/setValueIsAdjusting)
* [setValues()](/Java/JScrollBar/setValues)
* [setVisibleAmount()](/Java/JScrollBar/setVisibleAmount)
* [updateUI()](/Java/JScrollBar/updateUI)

## Ejemplo
~~~java
{{ site.data.Java.J.JScrollBar.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JScrollBar.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
