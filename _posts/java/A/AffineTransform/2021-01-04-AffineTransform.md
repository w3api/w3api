---
title: AffineTransform
permalink: Java/AffineTransform
date: 2021-01-04
key: JavaJava.A.AffineTransform
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AffineTransform.description }}

## Sintaxis
~~~java
public class AffineTransform extends Object implements Cloneable, Serializable
~~~

## Constructores
* [AffineTransform()](/Java/AffineTransform/AffineTransform/)

## Campos
* [TYPE_FLIP](/Java/AffineTransform/TYPE_FLIP)
* [TYPE_GENERAL_ROTATION](/Java/AffineTransform/TYPE_GENERAL_ROTATION)
* [TYPE_GENERAL_SCALE](/Java/AffineTransform/TYPE_GENERAL_SCALE)
* [TYPE_GENERAL_TRANSFORM](/Java/AffineTransform/TYPE_GENERAL_TRANSFORM)
* [TYPE_IDENTITY](/Java/AffineTransform/TYPE_IDENTITY)
* [TYPE_MASK_ROTATION](/Java/AffineTransform/TYPE_MASK_ROTATION)
* [TYPE_MASK_SCALE](/Java/AffineTransform/TYPE_MASK_SCALE)
* [TYPE_QUADRANT_ROTATION](/Java/AffineTransform/TYPE_QUADRANT_ROTATION)
* [TYPE_TRANSLATION](/Java/AffineTransform/TYPE_TRANSLATION)
* [TYPE_UNIFORM_SCALE](/Java/AffineTransform/TYPE_UNIFORM_SCALE)

## Métodos
* [clone()](/Java/AffineTransform/clone)
* [concatenate()](/Java/AffineTransform/concatenate)
* [createInverse()](/Java/AffineTransform/createInverse)
* [createTransformedShape()](/Java/AffineTransform/createTransformedShape)
* [deltaTransform()](/Java/AffineTransform/deltaTransform)
* [equals()](/Java/AffineTransform/equals)
* [getDeterminant()](/Java/AffineTransform/getDeterminant)
* [getMatrix()](/Java/AffineTransform/getMatrix)
* [getQuadrantRotateInstance()](/Java/AffineTransform/getQuadrantRotateInstance)
* [getRotateInstance()](/Java/AffineTransform/getRotateInstance)
* [getScaleInstance()](/Java/AffineTransform/getScaleInstance)
* [getScaleX()](/Java/AffineTransform/getScaleX)
* [getScaleY()](/Java/AffineTransform/getScaleY)
* [getShearInstance()](/Java/AffineTransform/getShearInstance)
* [getShearX()](/Java/AffineTransform/getShearX)
* [getShearY()](/Java/AffineTransform/getShearY)
* [getTranslateInstance()](/Java/AffineTransform/getTranslateInstance)
* [getTranslateX()](/Java/AffineTransform/getTranslateX)
* [getTranslateY()](/Java/AffineTransform/getTranslateY)
* [getType()](/Java/AffineTransform/getType)
* [hashCode()](/Java/AffineTransform/hashCode)
* [inverseTransform()](/Java/AffineTransform/inverseTransform)
* [invert()](/Java/AffineTransform/invert)
* [isIdentity()](/Java/AffineTransform/isIdentity)
* [preConcatenate()](/Java/AffineTransform/preConcatenate)
* [quadrantRotate()](/Java/AffineTransform/quadrantRotate)
* [rotate()](/Java/AffineTransform/rotate)
* [scale()](/Java/AffineTransform/scale)
* [setToIdentity()](/Java/AffineTransform/setToIdentity)
* [setToQuadrantRotation()](/Java/AffineTransform/setToQuadrantRotation)
* [setToRotation()](/Java/AffineTransform/setToRotation)
* [setToScale()](/Java/AffineTransform/setToScale)
* [setToShear()](/Java/AffineTransform/setToShear)
* [setToTranslation()](/Java/AffineTransform/setToTranslation)
* [setTransform()](/Java/AffineTransform/setTransform)
* [shear()](/Java/AffineTransform/shear)
* [toString()](/Java/AffineTransform/toString)
* [transform()](/Java/AffineTransform/transform)
* [translate()](/Java/AffineTransform/translate)

## Ejemplo
~~~java
{{ site.data.Java.A.AffineTransform.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AffineTransform.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
