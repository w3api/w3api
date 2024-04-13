---
title: StandardLocation
permalink: /Java/StandardLocation/
date: 2021-01-11
key: Java.S.StandardLocation
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'enumerado java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StandardLocation.description }}

## Sintaxis
~~~java
public enum StandardLocation extends Enum<StandardLocation> implements JavaFileManager.Location
~~~

## Enumerados
* [ANNOTATION_PROCESSOR_MODULE_PATH](/Java/StandardLocation/ANNOTATION_PROCESSOR_MODULE_PATH)
* [ANNOTATION_PROCESSOR_PATH](/Java/StandardLocation/ANNOTATION_PROCESSOR_PATH)
* [CLASS_OUTPUT](/Java/StandardLocation/CLASS_OUTPUT)
* [CLASS_PATH](/Java/StandardLocation/CLASS_PATH)
* [MODULE_PATH](/Java/StandardLocation/MODULE_PATH)
* [MODULE_SOURCE_PATH](/Java/StandardLocation/MODULE_SOURCE_PATH)
* [NATIVE_HEADER_OUTPUT](/Java/StandardLocation/NATIVE_HEADER_OUTPUT)
* [PATCH_MODULE_PATH](/Java/StandardLocation/PATCH_MODULE_PATH)
* [PLATFORM_CLASS_PATH](/Java/StandardLocation/PLATFORM_CLASS_PATH)
* [SOURCE_OUTPUT](/Java/StandardLocation/SOURCE_OUTPUT)
* [SOURCE_PATH](/Java/StandardLocation/SOURCE_PATH)
* [SYSTEM_MODULES](/Java/StandardLocation/SYSTEM_MODULES)
* [UPGRADE_MODULE_PATH](/Java/StandardLocation/UPGRADE_MODULE_PATH)

## Métodos
* [isModuleOrientedLocation()](/Java/StandardLocation/isModuleOrientedLocation)
* [locationFor()](/Java/StandardLocation/locationFor)
* [valueOf()](/Java/StandardLocation/valueOf)
* [values()](/Java/StandardLocation/values)

## Ejemplo
~~~java
{{ site.data.Java.S.StandardLocation.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StandardLocation.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
