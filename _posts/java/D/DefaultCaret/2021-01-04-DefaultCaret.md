---
title: DefaultCaret
permalink: Java/DefaultCaret
date: 2021-01-04
key: JavaJava.D.DefaultCaret
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DefaultCaret.description }}

## Sintaxis
~~~java
public class DefaultCaret extends Rectangle implements Caret, FocusListener, MouseListener, MouseMotionListener
~~~

## Constructores
* [DefaultCaret()](/Java/DefaultCaret/DefaultCaret/)

## Campos
* [ALWAYS_UPDATE](/Java/DefaultCaret/ALWAYS_UPDATE)
* [changeEvent](/Java/DefaultCaret/changeEvent)
* [listenerList](/Java/DefaultCaret/listenerList)
* [NEVER_UPDATE](/Java/DefaultCaret/NEVER_UPDATE)
* [UPDATE_WHEN_ON_EDT](/Java/DefaultCaret/UPDATE_WHEN_ON_EDT)

## Métodos
* [addChangeListener()](/Java/DefaultCaret/addChangeListener)
* [adjustVisibility()](/Java/DefaultCaret/adjustVisibility)
* [damage()](/Java/DefaultCaret/damage)
* [deinstall()](/Java/DefaultCaret/deinstall)
* [equals()](/Java/DefaultCaret/equals)
* [fireStateChanged()](/Java/DefaultCaret/fireStateChanged)
* [focusGained()](/Java/DefaultCaret/focusGained)
* [focusLost()](/Java/DefaultCaret/focusLost)
* [getBlinkRate()](/Java/DefaultCaret/getBlinkRate)
* [getChangeListeners()](/Java/DefaultCaret/getChangeListeners)
* [getComponent()](/Java/DefaultCaret/getComponent)
* [getDot()](/Java/DefaultCaret/getDot)
* [getDotBias()](/Java/DefaultCaret/getDotBias)
* [getListeners()](/Java/DefaultCaret/getListeners)
* [getMagicCaretPosition()](/Java/DefaultCaret/getMagicCaretPosition)
* [getMark()](/Java/DefaultCaret/getMark)
* [getMarkBias()](/Java/DefaultCaret/getMarkBias)
* [getSelectionPainter()](/Java/DefaultCaret/getSelectionPainter)
* [getUpdatePolicy()](/Java/DefaultCaret/getUpdatePolicy)
* [install()](/Java/DefaultCaret/install)
* [isActive()](/Java/DefaultCaret/isActive)
* [isSelectionVisible()](/Java/DefaultCaret/isSelectionVisible)
* [isVisible()](/Java/DefaultCaret/isVisible)
* [mouseClicked()](/Java/DefaultCaret/mouseClicked)
* [mouseDragged()](/Java/DefaultCaret/mouseDragged)
* [mouseEntered()](/Java/DefaultCaret/mouseEntered)
* [mouseExited()](/Java/DefaultCaret/mouseExited)
* [mouseMoved()](/Java/DefaultCaret/mouseMoved)
* [mousePressed()](/Java/DefaultCaret/mousePressed)
* [mouseReleased()](/Java/DefaultCaret/mouseReleased)
* [moveCaret()](/Java/DefaultCaret/moveCaret)
* [moveDot()](/Java/DefaultCaret/moveDot)
* [paint()](/Java/DefaultCaret/paint)
* [positionCaret()](/Java/DefaultCaret/positionCaret)
* [removeChangeListener()](/Java/DefaultCaret/removeChangeListener)
* [repaint()](/Java/DefaultCaret/repaint)
* [setBlinkRate()](/Java/DefaultCaret/setBlinkRate)
* [setDot()](/Java/DefaultCaret/setDot)
* [setMagicCaretPosition()](/Java/DefaultCaret/setMagicCaretPosition)
* [setSelectionVisible()](/Java/DefaultCaret/setSelectionVisible)
* [setUpdatePolicy()](/Java/DefaultCaret/setUpdatePolicy)
* [setVisible()](/Java/DefaultCaret/setVisible)

## Ejemplo
~~~java
{{ site.data.Java.D.DefaultCaret.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultCaret.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
