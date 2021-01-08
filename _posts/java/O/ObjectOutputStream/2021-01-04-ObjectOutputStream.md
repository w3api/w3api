---
title: ObjectOutputStream
permalink: Java/ObjectOutputStream
date: 2021-01-04
key: JavaJava.O.ObjectOutputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.ObjectOutputStream.description }}

## Sintaxis
~~~java
public class ObjectOutputStream extends OutputStream implements ObjectOutput, ObjectStreamConstants
~~~

## Constructores
* [ObjectOutputStream()](/Java/ObjectOutputStream/ObjectOutputStream/)

## Métodos
* [annotateClass()](/Java/ObjectOutputStream/annotateClass)
* [annotateProxyClass()](/Java/ObjectOutputStream/annotateProxyClass)
* [close()](/Java/ObjectOutputStream/close)
* [defaultWriteObject()](/Java/ObjectOutputStream/defaultWriteObject)
* [drain()](/Java/ObjectOutputStream/drain)
* [enableReplaceObject()](/Java/ObjectOutputStream/enableReplaceObject)
* [flush()](/Java/ObjectOutputStream/flush)
* [putFields()](/Java/ObjectOutputStream/putFields)
* [replaceObject()](/Java/ObjectOutputStream/replaceObject)
* [reset()](/Java/ObjectOutputStream/reset)
* [useProtocolVersion()](/Java/ObjectOutputStream/useProtocolVersion)
* [write()](/Java/ObjectOutputStream/write)
* [writeBoolean()](/Java/ObjectOutputStream/writeBoolean)
* [writeByte()](/Java/ObjectOutputStream/writeByte)
* [writeBytes()](/Java/ObjectOutputStream/writeBytes)
* [writeChar()](/Java/ObjectOutputStream/writeChar)
* [writeChars()](/Java/ObjectOutputStream/writeChars)
* [writeClassDescriptor()](/Java/ObjectOutputStream/writeClassDescriptor)
* [writeDouble()](/Java/ObjectOutputStream/writeDouble)
* [writeFields()](/Java/ObjectOutputStream/writeFields)
* [writeFloat()](/Java/ObjectOutputStream/writeFloat)
* [writeInt()](/Java/ObjectOutputStream/writeInt)
* [writeLong()](/Java/ObjectOutputStream/writeLong)
* [writeObject()](/Java/ObjectOutputStream/writeObject)
* [writeObjectOverride()](/Java/ObjectOutputStream/writeObjectOverride)
* [writeShort()](/Java/ObjectOutputStream/writeShort)
* [writeStreamHeader()](/Java/ObjectOutputStream/writeStreamHeader)
* [writeUnshared()](/Java/ObjectOutputStream/writeUnshared)
* [writeUTF()](/Java/ObjectOutputStream/writeUTF)

## Ejemplo
~~~java
{{ site.data.Java.O.ObjectOutputStream.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
