---
title: KeyboardFocusManager
permalink: Java/KeyboardFocusManager
date: 2021-01-11
key: JavaJava.K.KeyboardFocusManager
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.K.KeyboardFocusManager.description }}

## Sintaxis
~~~java
public abstract class KeyboardFocusManager extends Object implements KeyEventDispatcher, KeyEventPostProcessor
~~~

## Constructores
* [KeyboardFocusManager()](/Java/KeyboardFocusManager/KeyboardFocusManager/)

## Campos
* [BACKWARD_TRAVERSAL_KEYS](/Java/KeyboardFocusManager/BACKWARD_TRAVERSAL_KEYS)
* [DOWN_CYCLE_TRAVERSAL_KEYS](/Java/KeyboardFocusManager/DOWN_CYCLE_TRAVERSAL_KEYS)
* [FORWARD_TRAVERSAL_KEYS](/Java/KeyboardFocusManager/FORWARD_TRAVERSAL_KEYS)
* [UP_CYCLE_TRAVERSAL_KEYS](/Java/KeyboardFocusManager/UP_CYCLE_TRAVERSAL_KEYS)

## Métodos
* [addKeyEventDispatcher()](/Java/KeyboardFocusManager/addKeyEventDispatcher)
* [addKeyEventPostProcessor()](/Java/KeyboardFocusManager/addKeyEventPostProcessor)
* [addPropertyChangeListener()](/Java/KeyboardFocusManager/addPropertyChangeListener)
* [addVetoableChangeListener()](/Java/KeyboardFocusManager/addVetoableChangeListener)
* [clearFocusOwner()](/Java/KeyboardFocusManager/clearFocusOwner)
* [clearGlobalFocusOwner()](/Java/KeyboardFocusManager/clearGlobalFocusOwner)
* [dequeueKeyEvents()](/Java/KeyboardFocusManager/dequeueKeyEvents)
* [discardKeyEvents()](/Java/KeyboardFocusManager/discardKeyEvents)
* [dispatchEvent()](/Java/KeyboardFocusManager/dispatchEvent)
* [dispatchKeyEvent()](/Java/KeyboardFocusManager/dispatchKeyEvent)
* [downFocusCycle()](/Java/KeyboardFocusManager/downFocusCycle)
* [enqueueKeyEvents()](/Java/KeyboardFocusManager/enqueueKeyEvents)
* [firePropertyChange()](/Java/KeyboardFocusManager/firePropertyChange)
* [fireVetoableChange()](/Java/KeyboardFocusManager/fireVetoableChange)
* [focusNextComponent()](/Java/KeyboardFocusManager/focusNextComponent)
* [focusPreviousComponent()](/Java/KeyboardFocusManager/focusPreviousComponent)
* [getActiveWindow()](/Java/KeyboardFocusManager/getActiveWindow)
* [getCurrentFocusCycleRoot()](/Java/KeyboardFocusManager/getCurrentFocusCycleRoot)
* [getCurrentKeyboardFocusManager()](/Java/KeyboardFocusManager/getCurrentKeyboardFocusManager)
* [getDefaultFocusTraversalKeys()](/Java/KeyboardFocusManager/getDefaultFocusTraversalKeys)
* [getDefaultFocusTraversalPolicy()](/Java/KeyboardFocusManager/getDefaultFocusTraversalPolicy)
* [getFocusedWindow()](/Java/KeyboardFocusManager/getFocusedWindow)
* [getFocusOwner()](/Java/KeyboardFocusManager/getFocusOwner)
* [getGlobalActiveWindow()](/Java/KeyboardFocusManager/getGlobalActiveWindow)
* [getGlobalCurrentFocusCycleRoot()](/Java/KeyboardFocusManager/getGlobalCurrentFocusCycleRoot)
* [getGlobalFocusedWindow()](/Java/KeyboardFocusManager/getGlobalFocusedWindow)
* [getGlobalFocusOwner()](/Java/KeyboardFocusManager/getGlobalFocusOwner)
* [getGlobalPermanentFocusOwner()](/Java/KeyboardFocusManager/getGlobalPermanentFocusOwner)
* [getKeyEventDispatchers()](/Java/KeyboardFocusManager/getKeyEventDispatchers)
* [getKeyEventPostProcessors()](/Java/KeyboardFocusManager/getKeyEventPostProcessors)
* [getPermanentFocusOwner()](/Java/KeyboardFocusManager/getPermanentFocusOwner)
* [getPropertyChangeListeners()](/Java/KeyboardFocusManager/getPropertyChangeListeners)
* [getVetoableChangeListeners()](/Java/KeyboardFocusManager/getVetoableChangeListeners)
* [postProcessKeyEvent()](/Java/KeyboardFocusManager/postProcessKeyEvent)
* [processKeyEvent()](/Java/KeyboardFocusManager/processKeyEvent)
* [redispatchEvent()](/Java/KeyboardFocusManager/redispatchEvent)
* [removeKeyEventDispatcher()](/Java/KeyboardFocusManager/removeKeyEventDispatcher)
* [removeKeyEventPostProcessor()](/Java/KeyboardFocusManager/removeKeyEventPostProcessor)
* [removePropertyChangeListener()](/Java/KeyboardFocusManager/removePropertyChangeListener)
* [removeVetoableChangeListener()](/Java/KeyboardFocusManager/removeVetoableChangeListener)
* [setCurrentKeyboardFocusManager()](/Java/KeyboardFocusManager/setCurrentKeyboardFocusManager)
* [setDefaultFocusTraversalKeys()](/Java/KeyboardFocusManager/setDefaultFocusTraversalKeys)
* [setDefaultFocusTraversalPolicy()](/Java/KeyboardFocusManager/setDefaultFocusTraversalPolicy)
* [setGlobalActiveWindow()](/Java/KeyboardFocusManager/setGlobalActiveWindow)
* [setGlobalCurrentFocusCycleRoot()](/Java/KeyboardFocusManager/setGlobalCurrentFocusCycleRoot)
* [setGlobalFocusedWindow()](/Java/KeyboardFocusManager/setGlobalFocusedWindow)
* [setGlobalFocusOwner()](/Java/KeyboardFocusManager/setGlobalFocusOwner)
* [setGlobalPermanentFocusOwner()](/Java/KeyboardFocusManager/setGlobalPermanentFocusOwner)
* [upFocusCycle()](/Java/KeyboardFocusManager/upFocusCycle)

## Ejemplo
~~~java
{{ site.data.Java.K.KeyboardFocusManager.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyboardFocusManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
