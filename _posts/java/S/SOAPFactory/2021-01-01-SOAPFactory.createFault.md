---
title: SOAPFactory.createFault()
permalink: Java/SOAPFactory/createFault
date: 2021-01-11
key: JavaJava.S.SOAPFactory
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPFactory.metodos valor="createFault" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SOAPFault createFault() throws SOAPException
public abstract SOAPFault createFault(String reasonText, QName faultCode) throws SOAPException
~~~

## Parámetros
* **String reasonText**,  {% include w3api/param_description.html metodo=_dato parametro="String reasonText" %}
* **QName faultCode**,  {% include w3api/param_description.html metodo=_dato parametro="QName faultCode" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPFactory](/Java/SOAPFactory/)

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
