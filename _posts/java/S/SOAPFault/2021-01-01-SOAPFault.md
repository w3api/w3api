---
title: SOAPFault
permalink: /Java/SOAPFault/
date: 2021-01-11
key: Java.S.SOAPFault
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SOAPFault.description }}

## Sintaxis
~~~java
public interface SOAPFault extends SOAPBodyElement
~~~

## Métodos
* [addDetail()](/Java/SOAPFault/addDetail)
* [addFaultReasonText()](/Java/SOAPFault/addFaultReasonText)
* [appendFaultSubcode()](/Java/SOAPFault/appendFaultSubcode)
* [getDetail()](/Java/SOAPFault/getDetail)
* [getFaultActor()](/Java/SOAPFault/getFaultActor)
* [getFaultCode()](/Java/SOAPFault/getFaultCode)
* [getFaultCodeAsName()](/Java/SOAPFault/getFaultCodeAsName)
* [getFaultCodeAsQName()](/Java/SOAPFault/getFaultCodeAsQName)
* [getFaultNode()](/Java/SOAPFault/getFaultNode)
* [getFaultReasonLocales()](/Java/SOAPFault/getFaultReasonLocales)
* [getFaultReasonText()](/Java/SOAPFault/getFaultReasonText)
* [getFaultReasonTexts()](/Java/SOAPFault/getFaultReasonTexts)
* [getFaultRole()](/Java/SOAPFault/getFaultRole)
* [getFaultString()](/Java/SOAPFault/getFaultString)
* [getFaultStringLocale()](/Java/SOAPFault/getFaultStringLocale)
* [getFaultSubcodes()](/Java/SOAPFault/getFaultSubcodes)
* [hasDetail()](/Java/SOAPFault/hasDetail)
* [removeAllFaultSubcodes()](/Java/SOAPFault/removeAllFaultSubcodes)
* [setFaultActor()](/Java/SOAPFault/setFaultActor)
* [setFaultCode()](/Java/SOAPFault/setFaultCode)
* [setFaultNode()](/Java/SOAPFault/setFaultNode)
* [setFaultRole()](/Java/SOAPFault/setFaultRole)
* [setFaultString()](/Java/SOAPFault/setFaultString)

## Ejemplo
~~~java
{{ site.data.Java.S.SOAPFault.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SOAPFault.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
