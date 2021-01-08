---
title: TransferHandler
permalink: Java/TransferHandler
date: 2021-01-04
key: JavaJava.T.TransferHandler
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TransferHandler.description }}

## Sintaxis
~~~java
public class TransferHandler extends Object implements Serializable
~~~

## Constructores
* [TransferHandler()](/Java/TransferHandler/TransferHandler/)

## Campos
* [COPY](/Java/TransferHandler/COPY)
* [COPY_OR_MOVE](/Java/TransferHandler/COPY_OR_MOVE)
* [LINK](/Java/TransferHandler/LINK)
* [MOVE](/Java/TransferHandler/MOVE)
* [NONE](/Java/TransferHandler/NONE)

## Métodos
* [canImport()](/Java/TransferHandler/canImport)
* [createTransferable()](/Java/TransferHandler/createTransferable)
* [exportAsDrag()](/Java/TransferHandler/exportAsDrag)
* [exportDone()](/Java/TransferHandler/exportDone)
* [exportToClipboard()](/Java/TransferHandler/exportToClipboard)
* [getCopyAction()](/Java/TransferHandler/getCopyAction)
* [getCutAction()](/Java/TransferHandler/getCutAction)
* [getDragImage()](/Java/TransferHandler/getDragImage)
* [getDragImageOffset()](/Java/TransferHandler/getDragImageOffset)
* [getPasteAction()](/Java/TransferHandler/getPasteAction)
* [getSourceActions()](/Java/TransferHandler/getSourceActions)
* [getVisualRepresentation()](/Java/TransferHandler/getVisualRepresentation)
* [importData()](/Java/TransferHandler/importData)
* [setDragImage()](/Java/TransferHandler/setDragImage)
* [setDragImageOffset()](/Java/TransferHandler/setDragImageOffset)

## Ejemplo
~~~java
{{ site.data.Java.T.TransferHandler.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TransferHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
