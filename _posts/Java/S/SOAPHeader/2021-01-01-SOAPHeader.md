---
title: SOAPHeader
permalink: /Java/SOAPHeader/
date: 2021-01-11
key: Java.S.SOAPHeader
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SOAPHeader.description }}

## Sintaxis
~~~java
public interface SOAPHeader extends SOAPElement
~~~

## Métodos
* [addHeaderElement()](/Java/SOAPHeader/addHeaderElement)
* [addNotUnderstoodHeaderElement()](/Java/SOAPHeader/addNotUnderstoodHeaderElement)
* [addUpgradeHeaderElement()](/Java/SOAPHeader/addUpgradeHeaderElement)
* [examineAllHeaderElements()](/Java/SOAPHeader/examineAllHeaderElements)
* [examineHeaderElements()](/Java/SOAPHeader/examineHeaderElements)
* [examineMustUnderstandHeaderElements()](/Java/SOAPHeader/examineMustUnderstandHeaderElements)
* [extractAllHeaderElements()](/Java/SOAPHeader/extractAllHeaderElements)
* [extractHeaderElements()](/Java/SOAPHeader/extractHeaderElements)

## Ejemplo
~~~java
{{ site.data.Java.S.SOAPHeader.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SOAPHeader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
