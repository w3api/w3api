---
title: SOAPFault.setFaultNode()
permalink: /Java/SOAPFault/setFaultNode/
date: 2021-01-11
key: Java.S.SOAPFault
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPFault.metodos valor="setFaultNode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setFaultNode(String uri) throws SOAPException
~~~

## Parámetros
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}

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
