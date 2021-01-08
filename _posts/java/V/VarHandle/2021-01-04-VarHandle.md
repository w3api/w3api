---
title: VarHandle
permalink: Java/VarHandle
date: 2021-01-04
key: JavaJava.V.VarHandle
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.V.VarHandle.description }}

## Sintaxis
~~~java
public abstract class VarHandle extends Object
~~~

## Métodos
* [accessModeType()](/Java/VarHandle/accessModeType)
* [acquireFence()](/Java/VarHandle/acquireFence)
* [compareAndExchange()](/Java/VarHandle/compareAndExchange)
* [compareAndExchangeAcquire()](/Java/VarHandle/compareAndExchangeAcquire)
* [compareAndExchangeRelease()](/Java/VarHandle/compareAndExchangeRelease)
* [compareAndSet()](/Java/VarHandle/compareAndSet)
* [coordinateTypes()](/Java/VarHandle/coordinateTypes)
* [fullFence()](/Java/VarHandle/fullFence)
* [get()](/Java/VarHandle/get)
* [getAcquire()](/Java/VarHandle/getAcquire)
* [getAndAdd()](/Java/VarHandle/getAndAdd)
* [getAndAddAcquire()](/Java/VarHandle/getAndAddAcquire)
* [getAndAddRelease()](/Java/VarHandle/getAndAddRelease)
* [getAndBitwiseAnd()](/Java/VarHandle/getAndBitwiseAnd)
* [getAndBitwiseAndAcquire()](/Java/VarHandle/getAndBitwiseAndAcquire)
* [getAndBitwiseAndRelease()](/Java/VarHandle/getAndBitwiseAndRelease)
* [getAndBitwiseOr()](/Java/VarHandle/getAndBitwiseOr)
* [getAndBitwiseOrAcquire()](/Java/VarHandle/getAndBitwiseOrAcquire)
* [getAndBitwiseOrRelease()](/Java/VarHandle/getAndBitwiseOrRelease)
* [getAndBitwiseXor()](/Java/VarHandle/getAndBitwiseXor)
* [getAndBitwiseXorAcquire()](/Java/VarHandle/getAndBitwiseXorAcquire)
* [getAndBitwiseXorRelease()](/Java/VarHandle/getAndBitwiseXorRelease)
* [getAndSet()](/Java/VarHandle/getAndSet)
* [getAndSetAcquire()](/Java/VarHandle/getAndSetAcquire)
* [getAndSetRelease()](/Java/VarHandle/getAndSetRelease)
* [getOpaque()](/Java/VarHandle/getOpaque)
* [getVolatile()](/Java/VarHandle/getVolatile)
* [isAccessModeSupported()](/Java/VarHandle/isAccessModeSupported)
* [loadLoadFence()](/Java/VarHandle/loadLoadFence)
* [releaseFence()](/Java/VarHandle/releaseFence)
* [set()](/Java/VarHandle/set)
* [setOpaque()](/Java/VarHandle/setOpaque)
* [setRelease()](/Java/VarHandle/setRelease)
* [setVolatile()](/Java/VarHandle/setVolatile)
* [storeStoreFence()](/Java/VarHandle/storeStoreFence)
* [toMethodHandle()](/Java/VarHandle/toMethodHandle)
* [varType()](/Java/VarHandle/varType)
* [weakCompareAndSet()](/Java/VarHandle/weakCompareAndSet)
* [weakCompareAndSetAcquire()](/Java/VarHandle/weakCompareAndSetAcquire)
* [weakCompareAndSetPlain()](/Java/VarHandle/weakCompareAndSetPlain)
* [weakCompareAndSetRelease()](/Java/VarHandle/weakCompareAndSetRelease)

## Ejemplo
~~~java
{{ site.data.Java.V.VarHandle.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.VarHandle.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
