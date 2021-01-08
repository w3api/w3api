---
title: ImageReader
permalink: Java/ImageReader
date: 2021-01-04
key: JavaJava.I.ImageReader
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.ImageReader.description }}

## Sintaxis
~~~java
public abstract class ImageReader extends Object
~~~

## Constructores
* [ImageReader()](/Java/ImageReader/ImageReader/)

## Campos
* [availableLocales](/Java/ImageReader/availableLocales)
* [ignoreMetadata](/Java/ImageReader/ignoreMetadata)
* [input](/Java/ImageReader/input)
* [locale](/Java/ImageReader/locale)
* [minIndex](/Java/ImageReader/minIndex)
* [originatingProvider](/Java/ImageReader/originatingProvider)
* [progressListeners](/Java/ImageReader/progressListeners)
* [seekForwardOnly](/Java/ImageReader/seekForwardOnly)
* [updateListeners](/Java/ImageReader/updateListeners)
* [warningListeners](/Java/ImageReader/warningListeners)
* [warningLocales](/Java/ImageReader/warningLocales)

## Métodos
* [abort()](/Java/ImageReader/abort)
* [abortRequested()](/Java/ImageReader/abortRequested)
* [addIIOReadProgressListener()](/Java/ImageReader/addIIOReadProgressListener)
* [addIIOReadUpdateListener()](/Java/ImageReader/addIIOReadUpdateListener)
* [addIIOReadWarningListener()](/Java/ImageReader/addIIOReadWarningListener)
* [canReadRaster()](/Java/ImageReader/canReadRaster)
* [checkReadParamBandSettings()](/Java/ImageReader/checkReadParamBandSettings)
* [clearAbortRequest()](/Java/ImageReader/clearAbortRequest)
* [computeRegions()](/Java/ImageReader/computeRegions)
* [dispose()](/Java/ImageReader/dispose)
* [getAspectRatio()](/Java/ImageReader/getAspectRatio)
* [getAvailableLocales()](/Java/ImageReader/getAvailableLocales)
* [getDefaultReadParam()](/Java/ImageReader/getDefaultReadParam)
* [getDestination()](/Java/ImageReader/getDestination)
* [getFormatName()](/Java/ImageReader/getFormatName)
* [getHeight()](/Java/ImageReader/getHeight)
* [getImageMetadata()](/Java/ImageReader/getImageMetadata)
* [getImageTypes()](/Java/ImageReader/getImageTypes)
* [getInput()](/Java/ImageReader/getInput)
* [getLocale()](/Java/ImageReader/getLocale)
* [getMinIndex()](/Java/ImageReader/getMinIndex)
* [getNumImages()](/Java/ImageReader/getNumImages)
* [getNumThumbnails()](/Java/ImageReader/getNumThumbnails)
* [getOriginatingProvider()](/Java/ImageReader/getOriginatingProvider)
* [getRawImageType()](/Java/ImageReader/getRawImageType)
* [getSourceRegion()](/Java/ImageReader/getSourceRegion)
* [getStreamMetadata()](/Java/ImageReader/getStreamMetadata)
* [getThumbnailHeight()](/Java/ImageReader/getThumbnailHeight)
* [getThumbnailWidth()](/Java/ImageReader/getThumbnailWidth)
* [getTileGridXOffset()](/Java/ImageReader/getTileGridXOffset)
* [getTileGridYOffset()](/Java/ImageReader/getTileGridYOffset)
* [getTileHeight()](/Java/ImageReader/getTileHeight)
* [getTileWidth()](/Java/ImageReader/getTileWidth)
* [getWidth()](/Java/ImageReader/getWidth)
* [hasThumbnails()](/Java/ImageReader/hasThumbnails)
* [isIgnoringMetadata()](/Java/ImageReader/isIgnoringMetadata)
* [isImageTiled()](/Java/ImageReader/isImageTiled)
* [isRandomAccessEasy()](/Java/ImageReader/isRandomAccessEasy)
* [isSeekForwardOnly()](/Java/ImageReader/isSeekForwardOnly)
* [processImageComplete()](/Java/ImageReader/processImageComplete)
* [processImageProgress()](/Java/ImageReader/processImageProgress)
* [processImageStarted()](/Java/ImageReader/processImageStarted)
* [processImageUpdate()](/Java/ImageReader/processImageUpdate)
* [processPassComplete()](/Java/ImageReader/processPassComplete)
* [processPassStarted()](/Java/ImageReader/processPassStarted)
* [processReadAborted()](/Java/ImageReader/processReadAborted)
* [processSequenceComplete()](/Java/ImageReader/processSequenceComplete)
* [processSequenceStarted()](/Java/ImageReader/processSequenceStarted)
* [processThumbnailComplete()](/Java/ImageReader/processThumbnailComplete)
* [processThumbnailPassComplete()](/Java/ImageReader/processThumbnailPassComplete)
* [processThumbnailPassStarted()](/Java/ImageReader/processThumbnailPassStarted)
* [processThumbnailProgress()](/Java/ImageReader/processThumbnailProgress)
* [processThumbnailStarted()](/Java/ImageReader/processThumbnailStarted)
* [processThumbnailUpdate()](/Java/ImageReader/processThumbnailUpdate)
* [processWarningOccurred()](/Java/ImageReader/processWarningOccurred)
* [read()](/Java/ImageReader/read)
* [readAll()](/Java/ImageReader/readAll)
* [readAsRenderedImage()](/Java/ImageReader/readAsRenderedImage)
* [readerSupportsThumbnails()](/Java/ImageReader/readerSupportsThumbnails)
* [readRaster()](/Java/ImageReader/readRaster)
* [readThumbnail()](/Java/ImageReader/readThumbnail)
* [readTile()](/Java/ImageReader/readTile)
* [readTileRaster()](/Java/ImageReader/readTileRaster)
* [removeAllIIOReadProgressListeners()](/Java/ImageReader/removeAllIIOReadProgressListeners)
* [removeAllIIOReadUpdateListeners()](/Java/ImageReader/removeAllIIOReadUpdateListeners)
* [removeAllIIOReadWarningListeners()](/Java/ImageReader/removeAllIIOReadWarningListeners)
* [removeIIOReadProgressListener()](/Java/ImageReader/removeIIOReadProgressListener)
* [removeIIOReadUpdateListener()](/Java/ImageReader/removeIIOReadUpdateListener)
* [removeIIOReadWarningListener()](/Java/ImageReader/removeIIOReadWarningListener)
* [reset()](/Java/ImageReader/reset)
* [setInput()](/Java/ImageReader/setInput)
* [setLocale()](/Java/ImageReader/setLocale)

## Ejemplo
~~~java
{{ site.data.Java.I.ImageReader.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
