---
title: BeanContextSupport
permalink: /Java/BeanContextSupport/
date: 2021-01-11
key: Java.B.BeanContextSupport
category: Java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BeanContextSupport.description }}

## Sintaxis
~~~java
public class BeanContextSupport extends BeanContextChildSupport implements BeanContext, Serializable, PropertyChangeListener, VetoableChangeListener
~~~

## Constructores
* [BeanContextSupport()](/Java/BeanContextSupport/BeanContextSupport/)

## Campos
* [bcmListeners](/Java/BeanContextSupport/bcmListeners)
* [children](/Java/BeanContextSupport/children)
* [designTime](/Java/BeanContextSupport/designTime)
* [locale](/Java/BeanContextSupport/locale)
* [okToUseGui](/Java/BeanContextSupport/okToUseGui)

## Métodos
* [add()](/Java/BeanContextSupport/add)
* [addAll()](/Java/BeanContextSupport/addAll)
* [addBeanContextMembershipListener()](/Java/BeanContextSupport/addBeanContextMembershipListener)
* [avoidingGui()](/Java/BeanContextSupport/avoidingGui)
* [bcsChildren()](/Java/BeanContextSupport/bcsChildren)
* [bcsPreDeserializationHook()](/Java/BeanContextSupport/bcsPreDeserializationHook)
* [bcsPreSerializationHook()](/Java/BeanContextSupport/bcsPreSerializationHook)
* [childDeserializedHook()](/Java/BeanContextSupport/childDeserializedHook)
* [childJustAddedHook()](/Java/BeanContextSupport/childJustAddedHook)
* [childJustRemovedHook()](/Java/BeanContextSupport/childJustRemovedHook)
* [classEquals()](/Java/BeanContextSupport/classEquals)
* [clear()](/Java/BeanContextSupport/clear)
* [contains()](/Java/BeanContextSupport/contains)
* [containsAll()](/Java/BeanContextSupport/containsAll)
* [containsKey()](/Java/BeanContextSupport/containsKey)
* [copyChildren()](/Java/BeanContextSupport/copyChildren)
* [createBCSChild()](/Java/BeanContextSupport/createBCSChild)
* [deserialize()](/Java/BeanContextSupport/deserialize)
* [dontUseGui()](/Java/BeanContextSupport/dontUseGui)
* [fireChildrenAdded()](/Java/BeanContextSupport/fireChildrenAdded)
* [fireChildrenRemoved()](/Java/BeanContextSupport/fireChildrenRemoved)
* [getBeanContextPeer()](/Java/BeanContextSupport/getBeanContextPeer)
* [getChildBeanContextChild()](/Java/BeanContextSupport/getChildBeanContextChild)
* [getChildBeanContextMembershipListener()](/Java/BeanContextSupport/getChildBeanContextMembershipListener)
* [getChildPropertyChangeListener()](/Java/BeanContextSupport/getChildPropertyChangeListener)
* [getChildSerializable()](/Java/BeanContextSupport/getChildSerializable)
* [getChildVetoableChangeListener()](/Java/BeanContextSupport/getChildVetoableChangeListener)
* [getChildVisibility()](/Java/BeanContextSupport/getChildVisibility)
* [getLocale()](/Java/BeanContextSupport/getLocale)
* [getResource()](/Java/BeanContextSupport/getResource)
* [getResourceAsStream()](/Java/BeanContextSupport/getResourceAsStream)
* [initialize()](/Java/BeanContextSupport/initialize)
* [instantiateChild()](/Java/BeanContextSupport/instantiateChild)
* [isDesignTime()](/Java/BeanContextSupport/isDesignTime)
* [isEmpty()](/Java/BeanContextSupport/isEmpty)
* [isSerializing()](/Java/BeanContextSupport/isSerializing)
* [iterator()](/Java/BeanContextSupport/iterator)
* [needsGui()](/Java/BeanContextSupport/needsGui)
* [okToUseGui()](/Java/BeanContextSupport/okToUseGui)
* [propertyChange()](/Java/BeanContextSupport/propertyChange)
* [readChildren()](/Java/BeanContextSupport/readChildren)
* [remove()](/Java/BeanContextSupport/remove)
* [removeAll()](/Java/BeanContextSupport/removeAll)
* [removeBeanContextMembershipListener()](/Java/BeanContextSupport/removeBeanContextMembershipListener)
* [retainAll()](/Java/BeanContextSupport/retainAll)
* [serialize()](/Java/BeanContextSupport/serialize)
* [setDesignTime()](/Java/BeanContextSupport/setDesignTime)
* [setLocale()](/Java/BeanContextSupport/setLocale)
* [size()](/Java/BeanContextSupport/size)
* [toArray()](/Java/BeanContextSupport/toArray)
* [validatePendingAdd()](/Java/BeanContextSupport/validatePendingAdd)
* [validatePendingRemove()](/Java/BeanContextSupport/validatePendingRemove)
* [vetoableChange()](/Java/BeanContextSupport/vetoableChange)
* [writeChildren()](/Java/BeanContextSupport/writeChildren)

## Ejemplo
~~~java
{{ site.data.Java.B.BeanContextSupport.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BeanContextSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
