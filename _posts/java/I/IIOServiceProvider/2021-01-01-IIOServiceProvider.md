---
title: IIOServiceProvider
permalink: /Java/IIOServiceProvider/
date: 2021-01-11
key: Java.I.IIOServiceProvider
category: Java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.IIOServiceProvider.description }}

## Sintaxis
~~~java
public abstract class IIOServiceProvider extends Object implements RegisterableService
~~~

## Constructores
* [IIOServiceProvider()](/Java/IIOServiceProvider/IIOServiceProvider/)

## Campos
* [vendorName](/Java/IIOServiceProvider/vendorName)
* [version](/Java/IIOServiceProvider/version)

## Métodos
* [getDescription()](/Java/IIOServiceProvider/getDescription)
* [getVendorName()](/Java/IIOServiceProvider/getVendorName)
* [getVersion()](/Java/IIOServiceProvider/getVersion)
* [onDeregistration()](/Java/IIOServiceProvider/onDeregistration)
* [onRegistration()](/Java/IIOServiceProvider/onRegistration)

## Ejemplo
~~~java
{{ site.data.Java.I.IIOServiceProvider.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IIOServiceProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
