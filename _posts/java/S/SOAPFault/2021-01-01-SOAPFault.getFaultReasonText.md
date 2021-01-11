---
title: SOAPFault.getFaultReasonText()
permalink: Java/SOAPFault/getFaultReasonText
date: 2021-01-11
key: JavaJava.S.SOAPFault
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPFault.metodos valor="getFaultReasonText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String getFaultReasonText(Locale locale) throws SOAPException
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPFault](/Java/SOAPFault/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>