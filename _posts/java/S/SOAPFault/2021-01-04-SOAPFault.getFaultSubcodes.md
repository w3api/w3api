---
title: SOAPFault.getFaultSubcodes()
permalink: Java/SOAPFault/getFaultSubcodes
date: 2021-01-04
key: JavaJava.S.SOAPFault
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPFault.metodos valor="getFaultSubcodes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Iterator<QName> getFaultSubcodes()
~~~

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[SOAPFault](/Java/SOAPFault/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SOAPFault.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
