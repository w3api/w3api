---
title: DataFlavor
permalink: /Java/DataFlavor/
date: 2021-01-11
key: Java.D.DataFlavor
category: Java
tags: ['java se', 'java.awt.datatransfer', 'java.datatransfer', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DataFlavor.description }}

## Sintaxis
~~~java
public class DataFlavor extends Object implements Externalizable, Cloneable
~~~

## Constructores
* [DataFlavor()](/Java/DataFlavor/DataFlavor/)

## Campos
* [allHtmlFlavor](/Java/DataFlavor/allHtmlFlavor)
* [fragmentHtmlFlavor](/Java/DataFlavor/fragmentHtmlFlavor)
* [imageFlavor](/Java/DataFlavor/imageFlavor)
* [javaFileListFlavor](/Java/DataFlavor/javaFileListFlavor)
* [javaJVMLocalObjectMimeType](/Java/DataFlavor/javaJVMLocalObjectMimeType)
* [javaRemoteObjectMimeType](/Java/DataFlavor/javaRemoteObjectMimeType)
* [javaSerializedObjectMimeType](/Java/DataFlavor/javaSerializedObjectMimeType)
* [plainTextFlavor](/Java/DataFlavor/plainTextFlavor)
* [selectionHtmlFlavor](/Java/DataFlavor/selectionHtmlFlavor)
* [stringFlavor](/Java/DataFlavor/stringFlavor)

## Métodos
* [clone()](/Java/DataFlavor/clone)
* [equals()](/Java/DataFlavor/equals)
* [getDefaultRepresentationClass()](/Java/DataFlavor/getDefaultRepresentationClass)
* [getDefaultRepresentationClassAsString()](/Java/DataFlavor/getDefaultRepresentationClassAsString)
* [getHumanPresentableName()](/Java/DataFlavor/getHumanPresentableName)
* [getMimeType()](/Java/DataFlavor/getMimeType)
* [getParameter()](/Java/DataFlavor/getParameter)
* [getPrimaryType()](/Java/DataFlavor/getPrimaryType)
* [getReaderForText()](/Java/DataFlavor/getReaderForText)
* [getRepresentationClass()](/Java/DataFlavor/getRepresentationClass)
* [getSubType()](/Java/DataFlavor/getSubType)
* [getTextPlainUnicodeFlavor()](/Java/DataFlavor/getTextPlainUnicodeFlavor)
* [hashCode()](/Java/DataFlavor/hashCode)
* [isFlavorJavaFileListType()](/Java/DataFlavor/isFlavorJavaFileListType)
* [isFlavorRemoteObjectType()](/Java/DataFlavor/isFlavorRemoteObjectType)
* [isFlavorSerializedObjectType()](/Java/DataFlavor/isFlavorSerializedObjectType)
* [isFlavorTextType()](/Java/DataFlavor/isFlavorTextType)
* [isMimeTypeEqual()](/Java/DataFlavor/isMimeTypeEqual)
* [isMimeTypeSerializedObject()](/Java/DataFlavor/isMimeTypeSerializedObject)
* [isRepresentationClassByteBuffer()](/Java/DataFlavor/isRepresentationClassByteBuffer)
* [isRepresentationClassCharBuffer()](/Java/DataFlavor/isRepresentationClassCharBuffer)
* [isRepresentationClassInputStream()](/Java/DataFlavor/isRepresentationClassInputStream)
* [isRepresentationClassReader()](/Java/DataFlavor/isRepresentationClassReader)
* [isRepresentationClassRemote()](/Java/DataFlavor/isRepresentationClassRemote)
* [isRepresentationClassSerializable()](/Java/DataFlavor/isRepresentationClassSerializable)
* [match()](/Java/DataFlavor/match)
* [normalizeMimeType()](/Java/DataFlavor/normalizeMimeType)
* [normalizeMimeTypeParameter()](/Java/DataFlavor/normalizeMimeTypeParameter)
* [readExternal()](/Java/DataFlavor/readExternal)
* [selectBestTextFlavor()](/Java/DataFlavor/selectBestTextFlavor)
* [setHumanPresentableName()](/Java/DataFlavor/setHumanPresentableName)
* [toString()](/Java/DataFlavor/toString)
* [tryToLoadClass()](/Java/DataFlavor/tryToLoadClass)
* [writeExternal()](/Java/DataFlavor/writeExternal)

## Ejemplo
~~~java
{{ site.data.Java.D.DataFlavor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataFlavor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
