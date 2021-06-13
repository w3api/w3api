---
title: ObjectInputStream
permalink: /Java/ObjectInputStream/
date: 2021-01-11
key: JavaJava.O.ObjectInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.ObjectInputStream.description }}

## Sintaxis
~~~java
public class ObjectInputStream extends InputStream implements ObjectInput, ObjectStreamConstants
~~~

## Constructores
* [ObjectInputStream()](/Java/ObjectInputStream/ObjectInputStream/)

## Métodos
* [available()](/Java/ObjectInputStream/available)
* [close()](/Java/ObjectInputStream/close)
* [defaultReadObject()](/Java/ObjectInputStream/defaultReadObject)
* [enableResolveObject()](/Java/ObjectInputStream/enableResolveObject)
* [getObjectInputFilter()](/Java/ObjectInputStream/getObjectInputFilter)
* [read()](/Java/ObjectInputStream/read)
* [readBoolean()](/Java/ObjectInputStream/readBoolean)
* [readByte()](/Java/ObjectInputStream/readByte)
* [readChar()](/Java/ObjectInputStream/readChar)
* [readClassDescriptor()](/Java/ObjectInputStream/readClassDescriptor)
* [readDouble()](/Java/ObjectInputStream/readDouble)
* [readFields()](/Java/ObjectInputStream/readFields)
* [readFloat()](/Java/ObjectInputStream/readFloat)
* [readFully()](/Java/ObjectInputStream/readFully)
* [readInt()](/Java/ObjectInputStream/readInt)
* [readLine()](/Java/ObjectInputStream/readLine)
* [readLong()](/Java/ObjectInputStream/readLong)
* [readObject()](/Java/ObjectInputStream/readObject)
* [readObjectOverride()](/Java/ObjectInputStream/readObjectOverride)
* [readShort()](/Java/ObjectInputStream/readShort)
* [readStreamHeader()](/Java/ObjectInputStream/readStreamHeader)
* [readUnshared()](/Java/ObjectInputStream/readUnshared)
* [readUnsignedByte()](/Java/ObjectInputStream/readUnsignedByte)
* [readUnsignedShort()](/Java/ObjectInputStream/readUnsignedShort)
* [readUTF()](/Java/ObjectInputStream/readUTF)
* [registerValidation()](/Java/ObjectInputStream/registerValidation)
* [resolveClass()](/Java/ObjectInputStream/resolveClass)
* [resolveObject()](/Java/ObjectInputStream/resolveObject)
* [resolveProxyClass()](/Java/ObjectInputStream/resolveProxyClass)
* [setObjectInputFilter()](/Java/ObjectInputStream/setObjectInputFilter)
* [skipBytes()](/Java/ObjectInputStream/skipBytes)

## Ejemplo
~~~java
{{ site.data.Java.O.ObjectInputStream.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
