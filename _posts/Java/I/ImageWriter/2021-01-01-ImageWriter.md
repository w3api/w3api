---
title: ImageWriter
permalink: /Java/ImageWriter/
date: 2021-01-11
key: Java.I.ImageWriter
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.ImageWriter.description }}

## Sintaxis
~~~java
public abstract class ImageWriter extends Object implements ImageTranscoder
~~~

## Constructores
* [ImageWriter()](/Java/ImageWriter/ImageWriter/)

## Campos
* [availableLocales](/Java/ImageWriter/availableLocales/)
* [locale](/Java/ImageWriter/locale/)
* [originatingProvider](/Java/ImageWriter/originatingProvider/)
* [output](/Java/ImageWriter/output/)
* [progressListeners](/Java/ImageWriter/progressListeners/)
* [warningListeners](/Java/ImageWriter/warningListeners/)
* [warningLocales](/Java/ImageWriter/warningLocales/)

## Métodos
* [abort()](/Java/ImageWriter/abort/)
* [abortRequested()](/Java/ImageWriter/abortRequested/)
* [addIIOWriteProgressListener()](/Java/ImageWriter/addIIOWriteProgressListener/)
* [addIIOWriteWarningListener()](/Java/ImageWriter/addIIOWriteWarningListener/)
* [canInsertEmpty()](/Java/ImageWriter/canInsertEmpty/)
* [canInsertImage()](/Java/ImageWriter/canInsertImage/)
* [canRemoveImage()](/Java/ImageWriter/canRemoveImage/)
* [canReplaceImageMetadata()](/Java/ImageWriter/canReplaceImageMetadata/)
* [canReplacePixels()](/Java/ImageWriter/canReplacePixels/)
* [canReplaceStreamMetadata()](/Java/ImageWriter/canReplaceStreamMetadata/)
* [canWriteEmpty()](/Java/ImageWriter/canWriteEmpty/)
* [canWriteRasters()](/Java/ImageWriter/canWriteRasters/)
* [canWriteSequence()](/Java/ImageWriter/canWriteSequence/)
* [clearAbortRequest()](/Java/ImageWriter/clearAbortRequest/)
* [dispose()](/Java/ImageWriter/dispose/)
* [endInsertEmpty()](/Java/ImageWriter/endInsertEmpty/)
* [endReplacePixels()](/Java/ImageWriter/endReplacePixels/)
* [endWriteEmpty()](/Java/ImageWriter/endWriteEmpty/)
* [endWriteSequence()](/Java/ImageWriter/endWriteSequence/)
* [getAvailableLocales()](/Java/ImageWriter/getAvailableLocales/)
* [getDefaultImageMetadata()](/Java/ImageWriter/getDefaultImageMetadata/)
* [getDefaultStreamMetadata()](/Java/ImageWriter/getDefaultStreamMetadata/)
* [getDefaultWriteParam()](/Java/ImageWriter/getDefaultWriteParam/)
* [getLocale()](/Java/ImageWriter/getLocale/)
* [getNumThumbnailsSupported()](/Java/ImageWriter/getNumThumbnailsSupported/)
* [getOriginatingProvider()](/Java/ImageWriter/getOriginatingProvider/)
* [getOutput()](/Java/ImageWriter/getOutput/)
* [getPreferredThumbnailSizes()](/Java/ImageWriter/getPreferredThumbnailSizes/)
* [prepareInsertEmpty()](/Java/ImageWriter/prepareInsertEmpty/)
* [prepareReplacePixels()](/Java/ImageWriter/prepareReplacePixels/)
* [prepareWriteEmpty()](/Java/ImageWriter/prepareWriteEmpty/)
* [prepareWriteSequence()](/Java/ImageWriter/prepareWriteSequence/)
* [processImageComplete()](/Java/ImageWriter/processImageComplete/)
* [processImageProgress()](/Java/ImageWriter/processImageProgress/)
* [processImageStarted()](/Java/ImageWriter/processImageStarted/)
* [processThumbnailComplete()](/Java/ImageWriter/processThumbnailComplete/)
* [processThumbnailProgress()](/Java/ImageWriter/processThumbnailProgress/)
* [processThumbnailStarted()](/Java/ImageWriter/processThumbnailStarted/)
* [processWarningOccurred()](/Java/ImageWriter/processWarningOccurred/)
* [processWriteAborted()](/Java/ImageWriter/processWriteAborted/)
* [removeAllIIOWriteProgressListeners()](/Java/ImageWriter/removeAllIIOWriteProgressListeners/)
* [removeAllIIOWriteWarningListeners()](/Java/ImageWriter/removeAllIIOWriteWarningListeners/)
* [removeIIOWriteProgressListener()](/Java/ImageWriter/removeIIOWriteProgressListener/)
* [removeIIOWriteWarningListener()](/Java/ImageWriter/removeIIOWriteWarningListener/)
* [removeImage()](/Java/ImageWriter/removeImage/)
* [replaceImageMetadata()](/Java/ImageWriter/replaceImageMetadata/)
* [replacePixels()](/Java/ImageWriter/replacePixels/)
* [replaceStreamMetadata()](/Java/ImageWriter/replaceStreamMetadata/)
* [reset()](/Java/ImageWriter/reset/)
* [setLocale()](/Java/ImageWriter/setLocale/)
* [setOutput()](/Java/ImageWriter/setOutput/)
* [write()](/Java/ImageWriter/write/)
* [writeInsert()](/Java/ImageWriter/writeInsert/)
* [writeToSequence()](/Java/ImageWriter/writeToSequence/)

## Ejemplo
~~~java
{{ site.data.Java.I.ImageWriter.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.I.ImageWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
